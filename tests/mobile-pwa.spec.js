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

test("mobile quiz state survives reload", async ({ page }) => {
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));

  const appUrl = process.env.MOBILE_APP_URL || "http://127.0.0.1:8765/mobile_app/";
  await page.goto(appUrl, { waitUntil: "networkidle" });
  await expect(page.locator("#setupView")).toHaveClass(/is-active/);

  await page.locator("#modeSentence").click();
  await expect(page.locator("#modeSentence")).toHaveAttribute("aria-selected", "true");
  await page.locator("#modeVocab").click();
  await expect(page.locator("#modeVocab")).toHaveAttribute("aria-selected", "true");

  const setupMetrics = await page.evaluate(() => {
    const start = document.querySelector("#startButton");
    const nav = document.querySelector(".bottom-nav");
    const startRect = start.getBoundingClientRect();
    const navRect = nav.getBoundingClientRect();
    return {
      startDisabled: start.disabled,
      navPosition: getComputedStyle(nav).position,
      startBottom: startRect.bottom,
      navTop: navRect.top,
    };
  });
  expect(setupMetrics.startDisabled).toBe(false);
  expect(setupMetrics.navPosition).toBe("static");
  expect(setupMetrics.startBottom).toBeLessThanOrEqual(setupMetrics.navTop);

  await page.fill("#userName", "mobile-test");
  await page.locator("#startButton").scrollIntoViewIfNeeded();
  await page.locator("#startButton").click({ trial: true });
  await page.locator("#quizNav").click();
  await expect(page.locator("#quizView")).toHaveClass(/is-active/);
  await expect(page.locator(".choice-button").first()).toBeVisible();

  const quizMetrics = await page.evaluate(() => {
    const grid = document.querySelector("#choiceGrid");
    const nav = document.querySelector(".bottom-nav");
    const gridRect = grid.getBoundingClientRect();
    const navRect = nav.getBoundingClientRect();
    return {
      navPosition: getComputedStyle(nav).position,
      gridBottom: gridRect.bottom,
      navTop: navRect.top,
    };
  });
  expect(quizMetrics.navPosition).toBe("fixed");
  expect(quizMetrics.gridBottom).toBeLessThanOrEqual(quizMetrics.navTop + 1);

  const firstPrompt = await page.locator("#promptText").textContent();
  expect(firstPrompt && firstPrompt.trim().length).toBeGreaterThan(0);

  const startedSession = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  const answerIndex = startedSession.questions[startedSession.qIndex].answerIndex;
  const wrongIndex = (answerIndex + 1) % startedSession.questions[startedSession.qIndex].options.length;
  await page.locator(`.choice-button[data-index="${wrongIndex}"]`).click();
  await expect(page.locator("#feedbackPanel")).toBeVisible();
  await page.locator("#nextButton").click({ trial: true });
  await page.waitForTimeout(300);
  const storedBeforeReload = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  expect(storedBeforeReload.status).toBe("active");
  expect(storedBeforeReload.answers.length).toBeGreaterThanOrEqual(1);
  expect(storedBeforeReload.answers[0].selectedIndex).not.toBe(storedBeforeReload.answers[0].answerIndex);
  expect(storedBeforeReload.spartanPending.length).toBeGreaterThanOrEqual(1);

  await page.reload({ waitUntil: "networkidle" });
  const activeView = await page.evaluate(() => document.querySelector(".state-view.is-active")?.id);
  expect(["quizView", "resultView"]).toContain(activeView);
  const storedAfterReload = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  expect(storedAfterReload.status).toMatch(/active|complete/);

  let dialogSeen = false;
  page.once("dialog", async (dialog) => {
    dialogSeen = true;
    expect(dialog.message()).toContain("進行中のクイズ");
    await dialog.dismiss();
  });
  await page.locator("#homeNav").click();
  await page.locator("#startButton").scrollIntoViewIfNeeded();
  await page.locator("#startButton").click();
  await expect(page.locator("#quizView")).toHaveClass(/is-active/);
  const protectedSession = await page.evaluate(() => JSON.parse(localStorage.getItem("esperanto-choice-mobile:session:v2")));
  expect(protectedSession.id).toBe(storedAfterReload.id);
  expect(dialogSeen).toBe(true);

  expect(errors).toEqual([]);
});

test("mobile result and history stay readable", async ({ page }) => {
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));

  const appUrl = process.env.MOBILE_APP_URL || "http://127.0.0.1:8765/mobile_app/";
  await page.goto(appUrl, { waitUntil: "networkidle" });
  await page.locator("#lengthSelect").selectOption("10");
  await page.locator("#spartanMode").uncheck();
  await page.locator("#startButton").scrollIntoViewIfNeeded();
  await page.locator("#startButton").click();
  await expect(page.locator("#quizView")).toHaveClass(/is-active/);

  await answerRemainingCorrectly(page, page);
  await expect(page.locator("#resultView")).toHaveClass(/is-active/);
  await expect(page.locator("#accuracyMetric")).toHaveText("100%");
  await expect(page.locator("#syncScoreButton")).toBeDisabled();
  await expect(page.locator("#syncScoreStatus")).toContainText("Streamlit Cloud版");
  await expect(page.locator("#reviewList .review-item").first()).toBeVisible();

  const resultMetrics = await page.evaluate(() => {
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

  await page.locator("#historyNav").click();
  await expect(page.locator("#historyView")).toHaveClass(/is-active/);
  await expect(page.locator("#historyList .history-item").first()).toContainText("単語");
  await expect(errors).toEqual([]);
});

test("mobile setup recovers from malformed localStorage", async ({ page }) => {
  const appUrl = process.env.MOBILE_APP_URL || "http://127.0.0.1:8765/mobile_app/";
  await page.goto(appUrl, { waitUntil: "networkidle" });
  await page.evaluate(() => {
    localStorage.setItem("esperanto-choice-mobile:session:v2", JSON.stringify({ status: "active", questions: "broken" }));
    localStorage.setItem("esperanto-choice-mobile:history:v2", JSON.stringify([{ points: "not-a-number" }]));
  });
  await page.reload({ waitUntil: "networkidle" });
  await expect(page.locator("#setupView")).toHaveClass(/is-active/);
  await expect(page.locator("#startButton")).toBeEnabled();
});
