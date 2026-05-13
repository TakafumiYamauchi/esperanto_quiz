const { test, expect } = require("@playwright/test");

test.use({
  viewport: { width: 393, height: 851 },
  isMobile: true,
  hasTouch: true,
  deviceScaleFactor: 2.75,
  userAgent: "Mozilla/5.0 (Linux; Android 13; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Mobile Safari/537.36",
});

async function answerRemainingCorrectly(page, scope) {
  for (let guard = 0; guard < 40; guard += 1) {
    const session = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
    if (session.status === "complete") {
      return;
    }
    const question = session.questions[session.inSpartan ? session.spartanCurrent : session.qIndex];
    await scope.locator(`.choice-button[data-index="${question.answerIndex}"]`).click();
    await page.waitForTimeout(80);
  }
  throw new Error("Quiz did not complete within the guard limit");
}

test("Streamlit mobile entry uses the localStorage app and survives reload", async ({ page }) => {
  const appUrl = process.env.STREAMLIT_APP_URL || "http://127.0.0.1:8501/";
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto(appUrl, { waitUntil: "domcontentloaded" });
  const mobileApp = page.frameLocator("iframe[title*='esperanto_mobile_pwa']");
  await expect(mobileApp.locator("#startButton")).toBeEnabled({ timeout: 15000 });
  await mobileApp.locator("#homeNav").click();
  await expect(mobileApp.locator("#setupView")).toHaveClass(/is-active/);
  await expect(mobileApp.locator("#audioMode")).toBeEnabled();
  await expect(mobileApp.locator("#audioMode")).toHaveValue("prompt");

  await mobileApp.locator("#modeSentence").click();
  await expect(mobileApp.locator("#modeSentence")).toHaveAttribute("aria-selected", "true");
  await mobileApp.locator("#modeVocab").click();
  await expect(mobileApp.locator("#modeVocab")).toHaveAttribute("aria-selected", "true");
  await mobileApp.locator("#directionSelect").selectOption("ja_to_eo");
  await expect(mobileApp.locator("#directionSelect")).toHaveValue("ja_to_eo");
  await mobileApp.locator("#directionSelect").selectOption("eo_to_ja");

  const setupMetrics = await mobileApp.locator("body").evaluate(() => {
    const start = document.querySelector("#startButton");
    const nav = document.querySelector(".bottom-nav");
    const startRect = start.getBoundingClientRect();
    const navRect = nav.getBoundingClientRect();
    const navStyle = getComputedStyle(nav);
    return {
      startDisabled: start.disabled,
      navPosition: navStyle.position,
      startBottom: startRect.bottom,
      navTop: navRect.top,
      navBottom: navRect.bottom,
    };
  });
  expect(setupMetrics.startDisabled).toBe(false);
  expect(setupMetrics.navPosition).toBe("static");
  expect(setupMetrics.startBottom).toBeLessThanOrEqual(setupMetrics.navTop);
  const iframeBox = await page.locator("iframe[title*='esperanto_mobile_pwa']").boundingBox();
  expect(iframeBox.height).toBeGreaterThan(setupMetrics.navBottom - 1);

  await mobileApp.locator("#userName").fill("streamlit-mobile-test");
  await mobileApp.locator("#startButton").scrollIntoViewIfNeeded();
  await mobileApp.locator("#startButton").click({ trial: true });
  await mobileApp.locator("#quizNav").click();
  await expect(mobileApp.locator("#quizView")).toHaveClass(/is-active/);
  await expect(mobileApp.locator(".choice-button").first()).toBeVisible();
  await expect(mobileApp.locator("#promptAudioButton")).toBeVisible();
  const audioUrlPattern = /\/component\/mobile_streamlit_bridge\.esperanto_mobile_pwa\/(audio|sentence-audio)\/.+\.wav$/;
  const audioRequestPromise = page.waitForRequest(
    (request) => audioUrlPattern.test(request.url()),
    { timeout: 5000 },
  );
  const audioResponsePromise = page.waitForResponse(
    (response) => audioUrlPattern.test(response.url()),
    { timeout: 5000 },
  );
  const [audioRequest, audioResponse] = await Promise.all([
    audioRequestPromise,
    audioResponsePromise,
    mobileApp.locator("#promptAudioButton").click(),
  ]);
  expect(audioRequest.url()).not.toContain("drive.google");
  expect([200, 206]).toContain(audioResponse.status());
  expect(audioResponse.headers()["content-type"] || "").toMatch(/audio|octet-stream/);

  const quizMetrics = await mobileApp.locator("body").evaluate(() => {
    const grid = document.querySelector("#choiceGrid");
    const nav = document.querySelector(".bottom-nav");
    const gridRect = grid.getBoundingClientRect();
    const navRect = nav.getBoundingClientRect();
    const navStyle = getComputedStyle(nav);
    return {
      navPosition: navStyle.position,
      gridBottom: gridRect.bottom,
      navTop: navRect.top,
      scrollY: window.scrollY,
    };
  });
  expect(quizMetrics.navPosition).toBe("fixed");
  expect(quizMetrics.gridBottom).toBeLessThanOrEqual(quizMetrics.navTop + 1);
  expect(quizMetrics.scrollY).toBe(0);

  const startedSession = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  const answerIndex = startedSession.questions[startedSession.qIndex].answerIndex;
  const wrongIndex = (answerIndex + 1) % startedSession.questions[startedSession.qIndex].options.length;
  await mobileApp.locator(`.choice-button[data-index="${wrongIndex}"]`).click();
  await expect(mobileApp.locator("#feedbackPanel")).toBeVisible();
  await mobileApp.locator("#nextButton").click({ trial: true });
  await page.waitForTimeout(300);
  const storedBeforeReload = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  expect(storedBeforeReload.status).toBe("active");
  expect(storedBeforeReload.answers.length).toBeGreaterThanOrEqual(1);
  expect(storedBeforeReload.answers[0].selectedIndex).not.toBe(storedBeforeReload.answers[0].answerIndex);
  expect(storedBeforeReload.spartanPending.length).toBeGreaterThanOrEqual(1);

  await page.reload({ waitUntil: "domcontentloaded" });
  const restoredMobileApp = page.frameLocator("iframe[title*='esperanto_mobile_pwa']");
  await expect(restoredMobileApp.locator("#quizView, #resultView").first()).toBeVisible();
  const activeView = await restoredMobileApp.locator(".state-view.is-active").first().getAttribute("id");
  expect(["quizView", "resultView"]).toContain(activeView);

  const storedAfterReload = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  expect(storedAfterReload.status).toMatch(/active|complete/);

  let dialogSeen = false;
  page.once("dialog", async (dialog) => {
    dialogSeen = true;
    expect(dialog.message()).toContain("進行中のクイズ");
    await dialog.dismiss();
  });
  await restoredMobileApp.locator("#homeNav").click();
  await restoredMobileApp.locator("#startButton").scrollIntoViewIfNeeded();
  await restoredMobileApp.locator("#startButton").click();
  await expect(restoredMobileApp.locator("#quizView")).toHaveClass(/is-active/);
  const protectedSession = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  expect(protectedSession.id).toBe(storedAfterReload.id);
  expect(dialogSeen).toBe(true);

  expect(errors).toEqual([]);
});

test("Streamlit mobile result and history stay readable", async ({ page }) => {
  const appUrl = process.env.STREAMLIT_APP_URL || "http://127.0.0.1:8501/";
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto(appUrl, { waitUntil: "domcontentloaded" });
  const mobileApp = page.frameLocator("iframe[title*='esperanto_mobile_pwa']");
  await expect(mobileApp.locator("#startButton")).toBeEnabled({ timeout: 15000 });
  await mobileApp.locator("#homeNav").click();
  await expect(mobileApp.locator("#setupView")).toHaveClass(/is-active/);
  await mobileApp.locator("#userName").fill("streamlit-score-test");
  await mobileApp.locator("#lengthSelect").selectOption("10");
  await mobileApp.locator("#spartanMode").uncheck();
  await mobileApp.locator("#startButton").scrollIntoViewIfNeeded();
  await mobileApp.locator("#startButton").click();
  await expect(mobileApp.locator("#quizView")).toHaveClass(/is-active/);

  await answerRemainingCorrectly(page, mobileApp);
  await expect(mobileApp.locator("#resultView")).toHaveClass(/is-active/);
  await expect(mobileApp.locator("#accuracyMetric")).toHaveText("100%");
  await expect(mobileApp.locator("#syncScoreButton")).toBeEnabled();
  await expect(mobileApp.locator("#syncScoreStatus")).toContainText("累積得点");
  await expect(mobileApp.locator("#reviewList .review-item").first()).toBeVisible();

  const resultMetrics = await mobileApp.locator("body").evaluate(() => {
    const actions = document.querySelector(".result-actions").getBoundingClientRect();
    const nav = document.querySelector(".bottom-nav").getBoundingClientRect();
    return {
      actionsWidth: actions.width,
      actionsBottom: actions.bottom,
      navTop: nav.top,
      navBottom: nav.bottom,
      viewportHeight: window.innerHeight,
    };
  });
  expect(resultMetrics.actionsWidth).toBeGreaterThan(300);
  expect(resultMetrics.actionsBottom).toBeLessThanOrEqual(resultMetrics.navTop + 1);
  expect(resultMetrics.navBottom).toBeLessThanOrEqual(resultMetrics.viewportHeight + 1);

  await mobileApp.locator("#historyNav").click();
  await expect(mobileApp.locator("#historyView")).toHaveClass(/is-active/);
  await expect(mobileApp.locator("#cloudRankingTitle")).toBeVisible();
  await expect(mobileApp.locator("#rankingStatus")).toHaveText(/ランキング|Google Sheets|取得|更新/, { timeout: 20000 });
  await expect(mobileApp.locator("#historyList .history-item").first()).toContainText("単語");
  expect(errors).toEqual([]);
});

test("Streamlit mobile review can replay the Esperanto correct answer", async ({ page }) => {
  const appUrl = process.env.STREAMLIT_APP_URL || "http://127.0.0.1:8501/";
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto(appUrl, { waitUntil: "domcontentloaded" });
  const mobileApp = page.frameLocator("iframe[title*='esperanto_mobile_pwa']");
  await expect(mobileApp.locator("#startButton")).toBeEnabled({ timeout: 15000 });
  await mobileApp.locator("#homeNav").click();
  await mobileApp.locator("#lengthSelect").selectOption("10");
  await mobileApp.locator("#spartanMode").uncheck();
  await mobileApp.locator("#startButton").scrollIntoViewIfNeeded();
  await mobileApp.locator("#startButton").click();
  await expect(mobileApp.locator("#quizView")).toHaveClass(/is-active/);

  const startedSession = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  const answerIndex = startedSession.questions[startedSession.qIndex].answerIndex;
  const wrongIndex = (answerIndex + 1) % startedSession.questions[startedSession.qIndex].options.length;
  await mobileApp.locator(`.choice-button[data-index="${wrongIndex}"]`).click();
  await expect(mobileApp.locator("#feedbackPanel")).toBeVisible();
  await mobileApp.locator("#nextButton").click();

  await answerRemainingCorrectly(page, mobileApp);
  await expect(mobileApp.locator("#resultView")).toHaveClass(/is-active/);
  await expect(mobileApp.locator(".review-audio-button").first()).toBeVisible();

  const audioUrlPattern = /\/component\/mobile_streamlit_bridge\.esperanto_mobile_pwa\/audio\/.+\.wav$/;
  const audioResponsePromise = page.waitForResponse(
    (response) => audioUrlPattern.test(response.url()),
    { timeout: 5000 },
  );
  await mobileApp.locator(".review-audio-button").first().click();
  const audioResponse = await audioResponsePromise;
  expect([200, 206]).toContain(audioResponse.status());
  expect(audioResponse.headers()["content-type"] || "").toMatch(/audio|octet-stream/);

  expect(errors).toEqual([]);
});

test("Streamlit mobile sentence prompt audio is served only for Esperanto prompts", async ({ page }) => {
  const appUrl = process.env.STREAMLIT_APP_URL || "http://127.0.0.1:8501/";
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto(appUrl, { waitUntil: "domcontentloaded" });
  const mobileApp = page.frameLocator("iframe[title*='esperanto_mobile_pwa']");
  await expect(mobileApp.locator("#startButton")).toBeEnabled({ timeout: 15000 });
  await mobileApp.locator("#homeNav").click();
  await mobileApp.locator("#modeSentence").click();
  await expect(mobileApp.locator("#modeSentence")).toHaveAttribute("aria-selected", "true");
  await mobileApp.locator("#audioMode").selectOption("all");
  await mobileApp.locator("#lengthSelect").selectOption("10");
  await mobileApp.locator("#spartanMode").uncheck();
  const sentenceAudioUrlPattern = /\/component\/mobile_streamlit_bridge\.esperanto_mobile_pwa\/sentence-audio\/.+\.wav$/;
  const promptAudioResponsePromise = page.waitForResponse(
    (response) => sentenceAudioUrlPattern.test(response.url()),
    { timeout: 5000 },
  );
  await mobileApp.locator("#startButton").scrollIntoViewIfNeeded();
  await mobileApp.locator("#startButton").click();
  await expect(mobileApp.locator("#quizView")).toHaveClass(/is-active/);
  await expect(mobileApp.locator("#promptAudioButton")).toBeVisible();
  await expect(mobileApp.locator(".choice-audio-button")).toHaveCount(0);

  const promptAudioResponse = await promptAudioResponsePromise;
  expect([200, 206]).toContain(promptAudioResponse.status());
  expect(promptAudioResponse.headers()["content-type"] || "").toMatch(/audio|octet-stream/);

  const session = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  const answerIndex = session.questions[session.qIndex].answerIndex;
  const nextPromptAudioResponsePromise = page.waitForResponse(
    (response) => sentenceAudioUrlPattern.test(response.url()),
    { timeout: 5000 },
  );
  await mobileApp.locator(`.choice-button[data-index="${answerIndex}"]`).click();
  const nextPromptAudioResponse = await nextPromptAudioResponsePromise;
  expect([200, 206]).toContain(nextPromptAudioResponse.status());

  expect(errors).toEqual([]);
});

test("Streamlit mobile sentence choice audio is served only for Esperanto choices", async ({ page }) => {
  const appUrl = process.env.STREAMLIT_APP_URL || "http://127.0.0.1:8501/";
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto(appUrl, { waitUntil: "domcontentloaded" });
  const mobileApp = page.frameLocator("iframe[title*='esperanto_mobile_pwa']");
  await expect(mobileApp.locator("#startButton")).toBeEnabled({ timeout: 15000 });
  await mobileApp.locator("#homeNav").click();
  await mobileApp.locator("#modeSentence").click();
  await expect(mobileApp.locator("#modeSentence")).toHaveAttribute("aria-selected", "true");
  await mobileApp.locator("#directionSelect").selectOption("ja_to_eo");
  await mobileApp.locator("#audioMode").selectOption("all");
  await mobileApp.locator("#lengthSelect").selectOption("10");
  await mobileApp.locator("#spartanMode").uncheck();
  const earlyAudioRequests = [];
  const sentenceAudioUrlPattern = /\/component\/mobile_streamlit_bridge\.esperanto_mobile_pwa\/sentence-audio\/.+\.wav$/;
  page.on("request", (request) => {
    if (sentenceAudioUrlPattern.test(request.url())) {
      earlyAudioRequests.push(request.url());
    }
  });
  await mobileApp.locator("#startButton").scrollIntoViewIfNeeded();
  await mobileApp.locator("#startButton").click();
  await expect(mobileApp.locator("#quizView")).toHaveClass(/is-active/);
  await expect(mobileApp.locator("#promptAudioButton")).toBeHidden();
  await expect(mobileApp.locator(".choice-audio-button").first()).toBeVisible();
  await page.waitForTimeout(500);
  expect(earlyAudioRequests).toHaveLength(0);

  const choiceAudioResponsePromise = page.waitForResponse(
    (response) => sentenceAudioUrlPattern.test(response.url()),
    { timeout: 5000 },
  );
  await mobileApp.locator(".choice-audio-button").first().click();
  const choiceAudioResponse = await choiceAudioResponsePromise;
  expect([200, 206]).toContain(choiceAudioResponse.status());
  expect(choiceAudioResponse.headers()["content-type"] || "").toMatch(/audio|octet-stream/);

  expect(errors).toEqual([]);
});
