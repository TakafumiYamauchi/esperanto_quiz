const APP_VERSION = "2026-05-11-mobile-pwa-3";
const STORAGE_PREFIX = "esperanto-choice-mobile";
const SESSION_KEY = `${STORAGE_PREFIX}:session:v2`;
const SETTINGS_KEY = `${STORAGE_PREFIX}:settings:v2`;
const HISTORY_KEY = `${STORAGE_PREFIX}:history:v2`;

const DATA_URLS = {
  vocab: "./data/vocab.json",
  sentences: "./data/sentences.json",
};

const VOCAB_AUDIO_BASE = "../audio/";
const SENTENCE_AUDIO_BASE = "../Esperanto例文5000文_収録音声/";
const DEFAULT_AUDIO_CONFIG = {
  enabled: !window.location.pathname.includes("/component/"),
  vocabBaseUrl: VOCAB_AUDIO_BASE,
  sentenceBaseUrl: SENTENCE_AUDIO_BASE,
};
const IS_STREAMLIT_COMPONENT = window.location.pathname.includes("/component/");
const BASE_POINTS = 10;
const STREAK_BONUS = 0.5;
const SENTENCE_SCORE_SCALE = 2.0 / 1.5;
const SENTENCE_STREAK_SCALE = 2.0;
const VOCAB_ACCURACY_BONUS = 5.0;
const SENTENCE_ACCURACY_BONUS = 10.0;
const SPARTAN_SCORE_MULTIPLIER = 0.7;

const POS_LABELS = {
  noun: "名詞",
  verb: "動詞",
  adjective: "形容詞",
  adverb: "副詞",
  preposition: "前置詞",
  conjunction: "接続詞",
  prefix: "接頭辞",
  suffix: "接尾辞",
  correlative: "相関詞",
  numeral: "数詞",
  bare_adverb: "原形副詞",
  pronoun: "代名詞",
  personal_pronoun: "代名詞",
  other: "その他",
};

const POS_ORDER = [
  "noun",
  "verb",
  "adjective",
  "adverb",
  "preposition",
  "conjunction",
  "pronoun",
  "correlative",
  "numeral",
  "prefix",
  "suffix",
  "bare_adverb",
  "other",
];

const STAGE_LABELS = {
  beginner: "初級",
  intermediate: "中級",
  advanced: "上級",
};

const DEFAULT_SETTINGS = {
  mode: "vocab",
  userName: "",
  direction: "eo_to_ja",
  seed: 1,
  pos: "noun",
  groupId: "",
  topic: "",
  subtopic: "",
  levels: [],
  length: "all",
  audioMode: "prompt",
  spartanMode: true,
};

const STREAMLIT_API_VERSION = 1;

const streamlitHost = {
  send(type, payload = {}) {
    if (window.parent === window) {
      return;
    }
    window.parent.postMessage({
      isStreamlitMessage: true,
      type,
      ...payload,
    }, "*");
  },
  ready() {
    this.send("streamlit:componentReady", { apiVersion: STREAMLIT_API_VERSION });
  },
  setFrameHeight(height) {
    this.send("streamlit:setFrameHeight", { height });
  },
  setComponentValue(value) {
    this.send("streamlit:setComponentValue", { value });
  },
};

const els = {
  app: document.querySelector("#app"),
  saveStatus: document.querySelector("#saveStatus"),
  resumeButton: document.querySelector("#resumeButton"),
  loadingView: document.querySelector("#loadingView"),
  setupView: document.querySelector("#setupView"),
  quizView: document.querySelector("#quizView"),
  resultView: document.querySelector("#resultView"),
  historyView: document.querySelector("#historyView"),
  errorView: document.querySelector("#errorView"),
  errorMessage: document.querySelector("#errorMessage"),
  reloadButton: document.querySelector("#reloadButton"),
  modeVocab: document.querySelector("#modeVocab"),
  modeSentence: document.querySelector("#modeSentence"),
  resumeNotice: document.querySelector("#resumeNotice"),
  resumeMeta: document.querySelector("#resumeMeta"),
  resumeNoticeButton: document.querySelector("#resumeNoticeButton"),
  setupForm: document.querySelector("#setupForm"),
  userName: document.querySelector("#userName"),
  directionSelect: document.querySelector("#directionSelect"),
  vocabSettings: document.querySelector("#vocabSettings"),
  sentenceSettings: document.querySelector("#sentenceSettings"),
  seedInput: document.querySelector("#seedInput"),
  posSelect: document.querySelector("#posSelect"),
  groupSelect: document.querySelector("#groupSelect"),
  topicSelect: document.querySelector("#topicSelect"),
  subtopicSelect: document.querySelector("#subtopicSelect"),
  levelChips: document.querySelector("#levelChips"),
  lengthSelect: document.querySelector("#lengthSelect"),
  audioMode: document.querySelector("#audioMode"),
  spartanMode: document.querySelector("#spartanMode"),
  phaseLabel: document.querySelector("#phaseLabel"),
  promptText: document.querySelector("#promptText"),
  promptAudioButton: document.querySelector("#promptAudioButton"),
  progressBar: document.querySelector("#progressBar"),
  correctStat: document.querySelector("#correctStat"),
  streakStat: document.querySelector("#streakStat"),
  remainingStat: document.querySelector("#remainingStat"),
  feedbackPanel: document.querySelector("#feedbackPanel"),
  feedbackText: document.querySelector("#feedbackText"),
  nextButton: document.querySelector("#nextButton"),
  choiceGrid: document.querySelector("#choiceGrid"),
  resultTitle: document.querySelector("#resultTitle"),
  accuracyMetric: document.querySelector("#accuracyMetric"),
  pointsMetric: document.querySelector("#pointsMetric"),
  countMetric: document.querySelector("#countMetric"),
  syncScoreButton: document.querySelector("#syncScoreButton"),
  syncScoreStatus: document.querySelector("#syncScoreStatus"),
  retryButton: document.querySelector("#retryButton"),
  newQuizButton: document.querySelector("#newQuizButton"),
  reviewList: document.querySelector("#reviewList"),
  historyList: document.querySelector("#historyList"),
  clearHistoryButton: document.querySelector("#clearHistoryButton"),
  homeNav: document.querySelector("#homeNav"),
  quizNav: document.querySelector("#quizNav"),
  historyNav: document.querySelector("#historyNav"),
  toast: document.querySelector("#toast"),
};

const state = {
  data: {
    vocab: [],
    sentences: [],
  },
  vocabGroups: [],
  settings: { ...DEFAULT_SETTINGS },
  audioConfig: { ...DEFAULT_AUDIO_CONFIG },
  session: null,
  history: [],
  currentView: "loading",
  saveTimer: null,
  frameHeightTimer: null,
  lastFrameHeight: 0,
  latestScoreSyncResult: null,
};

init().catch((error) => {
  showFatalError(error);
});

async function init() {
  installStreamlitMessageHandler();
  streamlitHost.ready();
  installFrameHeightSync();
  bindEvents();
  loadLocalState();
  setView("loading");
  await registerServiceWorker();
  const [vocabPayload, sentencePayload] = await Promise.all([
    fetchJson(DATA_URLS.vocab),
    fetchJson(DATA_URLS.sentences),
  ]);
  state.data.vocab = Array.isArray(vocabPayload.entries) ? vocabPayload.entries : [];
  state.data.sentences = Array.isArray(sentencePayload.entries) ? sentencePayload.entries : [];
  if (state.data.vocab.length < 4 || state.data.sentences.length < 4) {
    throw new Error("クイズデータが不足しています。");
  }
  state.vocabGroups = buildVocabGroups(state.data.vocab, state.settings.seed);
  normalizeSettings();
  renderSetup();
  refreshResumeButton();
  if (isActiveSession(state.session)) {
    setView("quiz");
    renderQuiz();
  } else if (isCompleteSession(state.session)) {
    setView("result");
    renderResult();
  } else {
    setView("setup");
  }
  updateSaveStatus("準備完了");
}

function bindEvents() {
  els.reloadButton.addEventListener("click", () => window.location.reload());
  els.resumeButton.addEventListener("click", resumeStoredSession);
  els.resumeNoticeButton.addEventListener("click", resumeStoredSession);

  els.modeVocab.addEventListener("click", () => switchMode("vocab"));
  els.modeSentence.addEventListener("click", () => switchMode("sentence"));
  els.setupForm.addEventListener("submit", (event) => {
    event.preventDefault();
    startQuiz();
  });

  els.userName.addEventListener("input", persistSettingsFromForm);
  els.directionSelect.addEventListener("change", persistSettingsFromForm);
  els.seedInput.addEventListener("change", () => {
    persistSettingsFromForm();
    state.vocabGroups = buildVocabGroups(state.data.vocab, state.settings.seed);
    ensureVocabSelection();
    renderVocabControls();
    saveSettings();
  });
  els.posSelect.addEventListener("change", () => {
    state.settings.pos = els.posSelect.value;
    ensureVocabSelection(true);
    renderVocabControls();
    saveSettings();
  });
  els.groupSelect.addEventListener("change", persistSettingsFromForm);
  els.topicSelect.addEventListener("change", () => {
    state.settings.topic = els.topicSelect.value;
    ensureSentenceSelection(true);
    renderSentenceControls();
    saveSettings();
  });
  els.subtopicSelect.addEventListener("change", () => {
    state.settings.subtopic = els.subtopicSelect.value;
    ensureSentenceLevels(true);
    renderSentenceControls();
    saveSettings();
  });
  els.lengthSelect.addEventListener("change", persistSettingsFromForm);
  els.audioMode.addEventListener("change", persistSettingsFromForm);
  els.spartanMode.addEventListener("change", persistSettingsFromForm);

  els.promptAudioButton.addEventListener("click", () => {
    const current = getCurrentQuestion();
    if (current) {
      playAudio(current.mode, current.options[current.answerIndex]);
    }
  });
  els.nextButton.addEventListener("click", advanceAfterFeedback);
  els.syncScoreButton.addEventListener("click", syncScoreToSheets);
  els.retryButton.addEventListener("click", retrySession);
  els.newQuizButton.addEventListener("click", () => {
    state.session = null;
    saveSession();
    refreshResumeButton();
    setView("setup");
  });
  els.clearHistoryButton.addEventListener("click", () => {
    if (!state.history.length) {
      return;
    }
    if (window.confirm("保存された成績を消去しますか？")) {
      state.history = [];
      saveHistory();
      renderHistory();
    }
  });

  els.homeNav.addEventListener("click", () => setView("setup"));
  els.quizNav.addEventListener("click", () => {
    if (isActiveSession(state.session)) {
      setView("quiz");
      renderQuiz();
    } else if (isCompleteSession(state.session)) {
      setView("result");
      renderResult();
    } else {
      setView("setup");
      startQuiz();
    }
  });
  els.historyNav.addEventListener("click", () => {
    renderHistory();
    setView("history");
  });

  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "hidden") {
      saveSession();
      saveSettings();
    }
  });
  window.addEventListener("beforeunload", () => {
    saveSession();
    saveSettings();
  });
}

function resumeStoredSession() {
  if (isActiveSession(state.session)) {
    setView("quiz");
    renderQuiz();
  } else if (isCompleteSession(state.session)) {
    setView("result");
    renderResult();
  }
}

function installStreamlitMessageHandler() {
  if (!IS_STREAMLIT_COMPONENT) {
    return;
  }
  window.addEventListener("message", (event) => {
    const message = event.data;
    if (!message || message.type !== "streamlit:render") {
      return;
    }
    if (message.args?.audioConfig) {
      applyAudioConfig(message.args.audioConfig);
    }
    const result = message.args?.scoreSyncResult;
    if (result) {
      handleScoreSyncResult(result);
    }
  });
}

function applyAudioConfig(config) {
  const previous = JSON.stringify(state.audioConfig);
  state.audioConfig = normalizeAudioConfig(config);
  if (previous === JSON.stringify(state.audioConfig)) {
    return;
  }
  normalizeSettings();
  if (state.currentView === "setup") {
    renderSetup();
  } else if (state.currentView === "quiz") {
    renderQuiz();
  }
}

function normalizeAudioConfig(config) {
  const candidate = isPlainObject(config) ? config : {};
  const vocabBaseUrl = String(candidate.vocabBaseUrl || "").trim();
  const sentenceBaseUrl = String(candidate.sentenceBaseUrl || "").trim();
  if (!IS_STREAMLIT_COMPONENT) {
    return { ...DEFAULT_AUDIO_CONFIG };
  }
  return {
    enabled: Boolean(candidate.enabled && (vocabBaseUrl || sentenceBaseUrl)),
    vocabBaseUrl: ensureTrailingSlash(vocabBaseUrl),
    sentenceBaseUrl: ensureTrailingSlash(sentenceBaseUrl),
  };
}

function handleScoreSyncResult(result) {
  const session = state.session;
  if (!isCompleteSession(session) || result.type !== "score_save_result") {
    return;
  }
  const resultSaveId = String(result.saveId || "");
  const resultRequestId = String(result.requestId || "");
  const matchesSave = Boolean(resultSaveId && session.scoreSaveId && resultSaveId === session.scoreSaveId);
  const matchesRequest = Boolean(resultRequestId && session.scoreSyncRequestId && resultRequestId === session.scoreSyncRequestId);
  if (!matchesSave && !matchesRequest) {
    return;
  }
  session.scoreSyncStatus = result.ok ? "saved" : "error";
  session.scoreSyncMessage = String(result.message || (result.ok ? "ランキングに保存しました。" : "保存に失敗しました。"));
  state.latestScoreSyncResult = result;
  saveSession();
  if (state.currentView === "result") {
    renderResult();
  }
}

function installFrameHeightSync() {
  if (!IS_STREAMLIT_COMPONENT) {
    return;
  }
  const observer = new ResizeObserver(() => requestFrameHeightSync());
  observer.observe(document.documentElement);
  observer.observe(document.body);
  if (els.app) {
    observer.observe(els.app);
  }
  window.addEventListener("resize", requestFrameHeightSync);
  window.visualViewport?.addEventListener("resize", requestFrameHeightSync);
  requestFrameHeightSync();
}

function requestFrameHeightSync() {
  if (!IS_STREAMLIT_COMPONENT) {
    return;
  }
  window.clearTimeout(state.frameHeightTimer);
  state.frameHeightTimer = window.setTimeout(syncFrameHeight, 40);
}

function syncFrameHeight() {
  if (!IS_STREAMLIT_COMPONENT) {
    return;
  }
  const viewportHeight = Math.ceil(window.visualViewport?.height || window.innerHeight || 720);
  const screenHeight = Math.ceil(window.screen?.height || viewportHeight);
  const interactiveHeight = Math.max(640, Math.min(viewportHeight, screenHeight, 900));
  const minHeight = Math.max(640, Math.min(viewportHeight, screenHeight));
  const contentHeight = Math.ceil(Math.max(
    document.documentElement.scrollHeight,
    document.body.scrollHeight,
    els.app?.scrollHeight || 0,
  ));
  const fixedNavView = ["quiz", "result", "history", "error"].includes(state.currentView);
  const desiredHeight = fixedNavView
    ? interactiveHeight
    : Math.max(minHeight, contentHeight + 8);
  if (Math.abs(desiredHeight - state.lastFrameHeight) >= 4) {
    state.lastFrameHeight = desiredHeight;
    streamlitHost.setFrameHeight(desiredHeight);
  }
}

function scrollHostToTop() {
  window.scrollTo({ top: 0, left: 0, behavior: "auto" });
  if (!IS_STREAMLIT_COMPONENT) {
    return;
  }
  try {
    window.parent?.scrollTo({ top: 0, left: 0, behavior: "auto" });
    const parentDoc = window.parent?.document;
    parentDoc?.querySelectorAll?.(
      "section[data-testid='stMain'], [data-testid='stMain'], [data-testid='stAppViewContainer']",
    ).forEach((node) => {
      node.scrollTop = 0;
    });
    if (parentDoc?.scrollingElement) {
      parentDoc.scrollingElement.scrollTop = 0;
    }
  } catch (error) {
    window.parent?.scrollTo?.(0, 0);
  }
  try {
    window.top?.scrollTo({ top: 0, left: 0, behavior: "auto" });
  } catch (error) {
    window.top?.scrollTo?.(0, 0);
  }
}

async function registerServiceWorker() {
  if (
    !("serviceWorker" in navigator)
    || window.location.protocol === "file:"
    || window.location.pathname.includes("/component/")
  ) {
    return;
  }
  try {
    await navigator.serviceWorker.register("../mobile-sw.js", { scope: "../" });
  } catch (error) {
    console.warn("Service worker registration failed", error);
  }
}

async function fetchJson(url) {
  const controller = new AbortController();
  const timeoutId = window.setTimeout(() => controller.abort(), 15000);
  try {
    const response = await fetch(url, { signal: controller.signal });
    if (!response.ok) {
      throw new Error(`${url}: HTTP ${response.status}`);
    }
    return await response.json();
  } finally {
    window.clearTimeout(timeoutId);
  }
}

function loadLocalState() {
  state.settings = sanitizeSettings(readJson(SETTINGS_KEY, {}));
  state.session = sanitizeSession(readJson(SESSION_KEY, null));
  state.history = sanitizeHistory(readJson(HISTORY_KEY, []));
}

function readJson(key, fallback) {
  try {
    const raw = window.localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch (error) {
    console.warn(`Failed to read ${key}`, error);
    return fallback;
  }
}

function sanitizeSettings(value) {
  const candidate = isPlainObject(value) ? value : {};
  const settings = {
    ...DEFAULT_SETTINGS,
    ...candidate,
  };
  settings.userName = String(settings.userName || "").trim().slice(0, 32);
  settings.seed = clampInteger(settings.seed, 1, 8192, DEFAULT_SETTINGS.seed);
  if (!["vocab", "sentence"].includes(settings.mode)) {
    settings.mode = DEFAULT_SETTINGS.mode;
  }
  if (!["eo_to_ja", "ja_to_eo"].includes(settings.direction)) {
    settings.direction = DEFAULT_SETTINGS.direction;
  }
  if (!["10", "20", "all"].includes(settings.length)) {
    settings.length = DEFAULT_SETTINGS.length;
  }
  if (!["prompt", "all", "off"].includes(settings.audioMode)) {
    settings.audioMode = DEFAULT_SETTINGS.audioMode;
  }
  settings.pos = String(settings.pos || DEFAULT_SETTINGS.pos);
  settings.groupId = String(settings.groupId || "");
  settings.topic = String(settings.topic || "");
  settings.subtopic = String(settings.subtopic || "");
  settings.levels = Array.isArray(settings.levels)
    ? unique(settings.levels.map((level) => Number(level)).filter(Number.isFinite))
    : [];
  settings.spartanMode = Boolean(settings.spartanMode);
  return settings;
}

function sanitizeSession(value) {
  if (!isPlainObject(value) || !["active", "complete"].includes(value.status)) {
    return null;
  }
  if (!Array.isArray(value.questions) || !value.questions.length || !value.questions.every(isValidQuestion)) {
    return null;
  }
  const questionCount = value.questions.length;
  const answers = Array.isArray(value.answers)
    ? value.answers.filter((answer) => isValidAnswer(answer, questionCount))
    : [];
  const spartanPending = unique(
    (Array.isArray(value.spartanPending) ? value.spartanPending : [])
      .map((index) => Number(index))
      .filter((index) => Number.isInteger(index) && index >= 0 && index < questionCount),
  );
  const scoreSyncStatus = ["pending", "saved", "error"].includes(value.scoreSyncStatus)
    ? value.scoreSyncStatus
    : "idle";
  const session = {
    ...value,
    settings: sanitizeSettings(value.settings),
    qIndex: clampInteger(value.qIndex, 0, questionCount, 0),
    correct: clampInteger(value.correct, 0, questionCount, 0),
    streak: clampInteger(value.streak, 0, questionCount, 0),
    answers,
    showingFeedback: Boolean(value.showingFeedback && isPlainObject(value.feedback)),
    feedback: isPlainObject(value.feedback) ? value.feedback : null,
    mainPoints: finiteNumber(value.mainPoints, 0),
    spartanRawPoints: finiteNumber(value.spartanRawPoints, 0),
    spartanScaledPoints: finiteNumber(value.spartanScaledPoints, 0),
    spartanPending,
    inSpartan: Boolean(value.inSpartan && spartanPending.length),
    spartanAttempts: clampInteger(value.spartanAttempts, 0, 99999, 0),
    spartanCorrect: clampInteger(value.spartanCorrect, 0, 99999, 0),
    savedToHistory: Boolean(value.savedToHistory),
    scoreSaveId: String(value.scoreSaveId || ""),
    scoreSyncRequestId: String(value.scoreSyncRequestId || ""),
    scoreSyncStatus: scoreSyncStatus === "pending" ? "error" : scoreSyncStatus,
    scoreSyncMessage: scoreSyncStatus === "pending"
      ? "前回の保存結果を確認できませんでした。重複は防止されるため、もう一度保存を押してください。"
      : String(value.scoreSyncMessage || ""),
    startedAt: String(value.startedAt || new Date().toISOString()),
    updatedAt: String(value.updatedAt || new Date().toISOString()),
  };
  session.spartanCurrent = Number.isInteger(value.spartanCurrent) && spartanPending.includes(value.spartanCurrent)
    ? value.spartanCurrent
    : null;
  if (session.status === "complete") {
    session.completedAt = String(value.completedAt || session.updatedAt);
  }
  return session;
}

function sanitizeHistory(value) {
  if (!Array.isArray(value)) {
    return [];
  }
  return value
    .filter(isPlainObject)
    .map((record) => ({
      id: String(record.id || createId()),
      userName: String(record.userName || "").slice(0, 32),
      mode: record.mode === "sentence" ? "sentence" : "vocab",
      direction: record.direction === "ja_to_eo" ? "ja_to_eo" : "eo_to_ja",
      correct: clampInteger(record.correct, 0, 99999, 0),
      total: clampInteger(record.total, 1, 99999, 1),
      accuracy: Math.min(1, Math.max(0, finiteNumber(record.accuracy, 0))),
      points: finiteNumber(record.points, 0),
      completedAt: String(record.completedAt || ""),
    }))
    .slice(0, 100);
}

function isValidQuestion(question) {
  return Boolean(
    isPlainObject(question)
    && Array.isArray(question.options)
    && question.options.length >= 4
    && Number.isInteger(question.answerIndex)
    && question.answerIndex >= 0
    && question.answerIndex < question.options.length
    && question.options.every((option) => isPlainObject(option) && "eo" in option && "ja" in option),
  );
}

function isValidAnswer(answer, questionCount) {
  return Boolean(
    isPlainObject(answer)
    && Number.isInteger(answer.qIndex)
    && answer.qIndex >= 0
    && answer.qIndex < questionCount
    && Number.isInteger(answer.selectedIndex)
    && Number.isInteger(answer.answerIndex),
  );
}

function writeJson(key, value) {
  try {
    window.localStorage.setItem(key, JSON.stringify(value));
    return true;
  } catch (error) {
    console.warn(`Failed to write ${key}`, error);
    updateSaveStatus("保存できません");
    return false;
  }
}

function saveSettings() {
  writeJson(SETTINGS_KEY, state.settings);
}

function saveSession() {
  if (state.session) {
    state.session.updatedAt = new Date().toISOString();
  }
  if (writeJson(SESSION_KEY, state.session)) {
    updateSaveStatus("自動保存済み");
  }
}

function queueSessionSave() {
  window.clearTimeout(state.saveTimer);
  state.saveTimer = window.setTimeout(() => {
    saveSession();
    refreshResumeButton();
  }, 80);
}

function saveHistory() {
  writeJson(HISTORY_KEY, state.history.slice(0, 100));
}

function normalizeSettings() {
  state.settings.seed = clampInteger(state.settings.seed, 1, 8192, 1);
  if (!["vocab", "sentence"].includes(state.settings.mode)) {
    state.settings.mode = "vocab";
  }
  if (!["eo_to_ja", "ja_to_eo"].includes(state.settings.direction)) {
    state.settings.direction = "eo_to_ja";
  }
  if (!["10", "20", "all"].includes(state.settings.length)) {
    state.settings.length = state.settings.mode === "sentence" ? "10" : "all";
  }
  if (!["prompt", "all", "off"].includes(state.settings.audioMode)) {
    state.settings.audioMode = "prompt";
  }
  if (!hasAudioForMode(state.settings.mode)) {
    state.settings.audioMode = "off";
  }
  ensureVocabSelection();
  ensureSentenceSelection();
  saveSettings();
}

function persistSettingsFromForm() {
  state.settings.userName = els.userName.value.trim();
  state.settings.direction = els.directionSelect.value;
  state.settings.seed = clampInteger(els.seedInput.value, 1, 8192, 1);
  state.settings.pos = els.posSelect.value || state.settings.pos;
  state.settings.groupId = els.groupSelect.value || state.settings.groupId;
  state.settings.topic = els.topicSelect.value || state.settings.topic;
  state.settings.subtopic = els.subtopicSelect.value || state.settings.subtopic;
  state.settings.levels = getCheckedLevels();
  state.settings.length = els.lengthSelect.value;
  state.settings.audioMode = els.audioMode.value;
  if (!hasAudioForMode(state.settings.mode)) {
    state.settings.audioMode = "off";
  }
  state.settings.spartanMode = els.spartanMode.checked;
  saveSettings();
}

function switchMode(mode) {
  if (state.settings.mode === mode) {
    return;
  }
  state.settings.mode = mode;
  if (mode === "sentence" && state.settings.length === "all") {
    state.settings.length = "10";
  }
  if (mode === "vocab" && state.settings.length === "10") {
    state.settings.length = "all";
  }
  normalizeSettings();
  renderSetup();
  requestFrameHeightSync();
}

function renderSetup() {
  const mode = state.settings.mode;
  els.modeVocab.classList.toggle("is-selected", mode === "vocab");
  els.modeSentence.classList.toggle("is-selected", mode === "sentence");
  els.modeVocab.setAttribute("aria-selected", String(mode === "vocab"));
  els.modeSentence.setAttribute("aria-selected", String(mode === "sentence"));
  els.vocabSettings.hidden = mode !== "vocab";
  els.sentenceSettings.hidden = mode !== "sentence";

  els.userName.value = state.settings.userName || "";
  els.directionSelect.value = state.settings.direction;
  els.seedInput.value = state.settings.seed;
  els.lengthSelect.value = state.settings.length;
  els.audioMode.value = state.settings.audioMode;
  els.audioMode.disabled = !hasAudioForMode(mode);
  els.spartanMode.checked = Boolean(state.settings.spartanMode);

  renderVocabControls();
  renderSentenceControls();
  refreshResumeButton();
  requestFrameHeightSync();
}

function renderVocabControls() {
  const posValues = unique(state.vocabGroups.map((group) => group.pos))
    .sort((a, b) => posSortIndex(a) - posSortIndex(b) || labelForPos(a).localeCompare(labelForPos(b), "ja"));
  replaceOptions(
    els.posSelect,
    posValues.map((pos) => ({ value: pos, label: labelForPos(pos) })),
  );
  els.posSelect.value = state.settings.pos;

  const groups = state.vocabGroups.filter((group) => group.pos === state.settings.pos);
  replaceOptions(
    els.groupSelect,
    groups.map((group) => ({
      value: group.id,
      label: `${formatStageLabel(group.stages)} ${group.indexLabel} (${group.entries.length}語)`,
    })),
  );
  els.groupSelect.value = state.settings.groupId;
}

function renderSentenceControls() {
  const topics = unique(state.data.sentences.map((entry) => entry.topic)).sort((a, b) => a.localeCompare(b));
  replaceOptions(els.topicSelect, topics.map((topic) => ({ value: topic, label: topic })));
  els.topicSelect.value = state.settings.topic;

  const subtopics = unique(
    state.data.sentences
      .filter((entry) => entry.topic === state.settings.topic)
      .map((entry) => entry.subtopic),
  ).sort((a, b) => a.localeCompare(b));
  replaceOptions(els.subtopicSelect, subtopics.map((subtopic) => ({ value: subtopic, label: subtopic })));
  els.subtopicSelect.value = state.settings.subtopic;

  const availableLevels = getAvailableSentenceLevels();
  els.levelChips.replaceChildren(
    ...availableLevels.map((level) => {
      const label = document.createElement("label");
      label.className = "chip";
      const input = document.createElement("input");
      input.type = "checkbox";
      input.value = String(level);
      input.checked = state.settings.levels.includes(level);
      input.addEventListener("change", persistSettingsFromForm);
      const span = document.createElement("span");
      span.textContent = `Lv ${level}`;
      label.append(input, span);
      return label;
    }),
  );
}

function replaceOptions(select, options) {
  select.replaceChildren(
    ...options.map((option) => {
      const node = document.createElement("option");
      node.value = option.value;
      node.textContent = option.label;
      return node;
    }),
  );
}

function ensureVocabSelection(resetGroup = false) {
  const posValues = unique(state.vocabGroups.map((group) => group.pos));
  if (!posValues.includes(state.settings.pos)) {
    state.settings.pos = posValues.includes("noun") ? "noun" : posValues[0] || "";
    resetGroup = true;
  }
  const groups = state.vocabGroups.filter((group) => group.pos === state.settings.pos);
  if (resetGroup || !groups.some((group) => group.id === state.settings.groupId)) {
    state.settings.groupId = groups[0]?.id || "";
  }
}

function ensureSentenceSelection(resetSubtopic = false) {
  const topics = unique(state.data.sentences.map((entry) => entry.topic)).sort((a, b) => a.localeCompare(b));
  if (!topics.includes(state.settings.topic)) {
    state.settings.topic = topics[0] || "";
    resetSubtopic = true;
  }
  const subtopics = unique(
    state.data.sentences
      .filter((entry) => entry.topic === state.settings.topic)
      .map((entry) => entry.subtopic),
  ).sort((a, b) => a.localeCompare(b));
  if (resetSubtopic || !subtopics.includes(state.settings.subtopic)) {
    state.settings.subtopic = subtopics[0] || "";
  }
  ensureSentenceLevels(resetSubtopic);
}

function ensureSentenceLevels(resetLevels = false) {
  const availableLevels = getAvailableSentenceLevels();
  const valid = state.settings.levels.filter((level) => availableLevels.includes(level));
  state.settings.levels = resetLevels || valid.length === 0 ? availableLevels : valid;
}

function getAvailableSentenceLevels() {
  return unique(
    state.data.sentences
      .filter((entry) => entry.topic === state.settings.topic && entry.subtopic === state.settings.subtopic)
      .map((entry) => Number(entry.level))
      .filter(Number.isFinite),
  ).sort((a, b) => a - b);
}

function getCheckedLevels() {
  return [...els.levelChips.querySelectorAll("input:checked")]
    .map((input) => Number(input.value))
    .filter(Number.isFinite);
}

function startQuiz({ replaceActive = false } = {}) {
  if (isActiveSession(state.session) && !replaceActive) {
    const replace = window.confirm("進行中のクイズがあります。現在の進行を終了して、新しいクイズを開始しますか？");
    if (!replace) {
      showToast("進行中のクイズを保持しました。");
      resumeStoredSession();
      return false;
    }
  }
  persistSettingsFromForm();
  const settings = { ...state.settings, levels: [...state.settings.levels] };
  const seed = settings.seed + Date.now();
  const rng = mulberry32(seed);
  const questions = settings.mode === "vocab"
    ? buildVocabQuestions(settings, rng)
    : buildSentenceQuestions(settings, rng);
  if (questions.length < 1) {
    showToast("選択した条件では問題を作成できません。");
    return;
  }
  state.session = {
    id: createId(),
    appVersion: APP_VERSION,
    status: "active",
    settings,
    questions,
    qIndex: 0,
    correct: 0,
    streak: 0,
    answers: [],
    showingFeedback: false,
    feedback: null,
    mainPoints: 0,
    spartanRawPoints: 0,
    spartanScaledPoints: 0,
    spartanPending: [],
    inSpartan: false,
    spartanCurrent: null,
    spartanAttempts: 0,
    spartanCorrect: 0,
    savedToHistory: false,
    scoreSaveId: "",
    scoreSyncRequestId: "",
    scoreSyncStatus: "idle",
    scoreSyncMessage: "",
    startedAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
  saveSession();
  refreshResumeButton();
  setView("quiz");
  renderQuiz();
  return true;
}

function retrySession() {
  if (!state.session) {
    setView("setup");
    return;
  }
  state.settings = {
    ...DEFAULT_SETTINGS,
    ...state.session.settings,
    levels: [...(state.session.settings.levels || [])],
  };
  renderSetup();
  startQuiz();
}

function buildVocabQuestions(settings, rng) {
  const group = state.vocabGroups.find((candidate) => candidate.id === settings.groupId);
  if (!group || group.entries.length < 4) {
    return [];
  }
  const selectedEntries = limitEntries(group.entries, settings.length, rng);
  return selectedEntries.map((entry) => buildQuestionFromEntry({
    mode: "vocab",
    correct: entry,
    pool: group.entries,
    stages: group.stages,
    rng,
  })).filter(Boolean);
}

function buildSentenceQuestions(settings, rng) {
  const pool = state.data.sentences.filter((entry) => (
    entry.topic === settings.topic
    && entry.subtopic === settings.subtopic
    && settings.levels.includes(Number(entry.level))
  ));
  if (pool.length < 4) {
    return [];
  }
  const selectedEntries = limitEntries(pool, settings.length, rng);
  return selectedEntries.map((entry) => buildQuestionFromEntry({
    mode: "sentence",
    correct: entry,
    pool,
    stages: [],
    rng,
  })).filter(Boolean);
}

function buildQuestionFromEntry({ mode, correct, pool, stages, rng }) {
  const wrongPool = pool.filter((entry) => entry !== correct);
  if (wrongPool.length < 3) {
    return null;
  }
  const options = shuffle([...sample(wrongPool, 3, rng), correct], rng).map((entry) => ({
    id: entry.id,
    eo: entry.eo,
    ja: entry.ja,
    level: Number(entry.level),
    audioKey: entry.audioKey,
    hasAudio: Boolean(entry.hasAudio),
  }));
  const answerIndex = options.findIndex((option) => option.id === correct.id && option.eo === correct.eo);
  return {
    mode,
    promptEo: correct.eo,
    promptJa: correct.ja,
    stages: [...stages],
    level: Number(correct.level),
    answerIndex,
    options,
  };
}

function limitEntries(entries, length, rng) {
  const shuffled = shuffle([...entries], rng);
  if (length === "all") {
    return shuffled;
  }
  const limit = Number(length);
  if (!Number.isFinite(limit) || limit <= 0) {
    return shuffled;
  }
  return shuffled.slice(0, Math.min(limit, shuffled.length));
}

function renderQuiz() {
  if (!state.session || !state.session.questions.length) {
    setView("setup");
    return;
  }
  normalizeSessionPhase();
  if (state.session.status === "complete") {
    renderResult();
    setView("result");
    return;
  }

  const session = state.session;
  const question = getCurrentQuestion();
  if (!question) {
    finishSession();
    return;
  }

  const currentNumber = Math.min(session.qIndex + 1, session.questions.length);
  const phaseText = session.inSpartan
    ? `復習 ${session.spartanPending.length}問`
    : `Q${currentNumber}/${session.questions.length}`;
  const prompt = displayPrompt(question, session.settings.direction);
  els.phaseLabel.textContent = phaseText;
  els.promptText.textContent = prompt;

  const answerOption = question.options[question.answerIndex];
  const canPromptAudio = session.settings.audioMode !== "off" && hasPlayableAudio(answerOption);
  els.promptAudioButton.hidden = !canPromptAudio;

  const answeredMain = Math.min(session.qIndex, session.questions.length);
  const progress = session.inSpartan
    ? 1
    : answeredMain / Math.max(session.questions.length, 1);
  els.progressBar.style.width = `${Math.round(progress * 100)}%`;
  els.correctStat.textContent = `正解 ${session.correct}/${session.questions.length}`;
  els.streakStat.textContent = `連続 ${session.streak}`;
  els.remainingStat.textContent = `残り ${remainingCount(session)}`;

  renderFeedback();
  renderChoices(question);
  queueSessionSave();
}

function renderFeedback() {
  const session = state.session;
  if (!session?.showingFeedback || !session.feedback) {
    els.feedbackPanel.hidden = true;
    els.feedbackPanel.classList.remove("is-correct");
    return;
  }
  els.feedbackPanel.hidden = false;
  els.feedbackPanel.classList.toggle("is-correct", Boolean(session.feedback.correct));
  els.feedbackText.textContent = session.feedback.message;
}

function renderChoices(question) {
  const session = state.session;
  const labels = question.options.map((option) => displayOption(option, session.settings.direction));
  const longLabels = question.mode === "sentence" || labels.some((label) => label.length > 24);
  els.choiceGrid.classList.toggle("is-long", longLabels);
  els.choiceGrid.replaceChildren(
    ...question.options.map((option, index) => {
      const card = document.createElement("div");
      card.className = "choice-card";

      const button = document.createElement("button");
      button.type = "button";
      button.className = "choice-button";
      button.disabled = Boolean(session.showingFeedback);
      button.dataset.index = String(index);
      const label = document.createElement("span");
      label.className = "choice-label";
      label.textContent = labels[index];
      button.append(label);

      if (session.showingFeedback) {
        button.classList.toggle("is-correct", index === question.answerIndex);
        button.classList.toggle("is-wrong", index === session.feedback?.selectedIndex);
      } else {
        button.addEventListener("click", () => answerCurrentQuestion(index));
      }
      card.append(button);

      if (session.settings.audioMode === "all" && hasPlayableAudio(option)) {
        const audioButton = document.createElement("button");
        audioButton.type = "button";
        audioButton.className = "choice-audio-button";
        audioButton.textContent = "♪";
        audioButton.setAttribute("aria-label", "選択肢の音声を再生");
        audioButton.addEventListener("click", () => playAudio(question.mode, option));
        card.append(audioButton);
      }
      return card;
    }),
  );
}

function answerCurrentQuestion(selectedIndex) {
  const session = state.session;
  const question = getCurrentQuestion();
  if (!session || !question || session.showingFeedback) {
    return;
  }
  const isCorrect = selectedIndex === question.answerIndex;
  const phase = session.inSpartan ? "spartan" : "main";
  const currentIndex = getCurrentQuestionIndex();
  if (session.inSpartan) {
    session.spartanAttempts += 1;
  }
  session.answers.push({
    qIndex: currentIndex,
    selectedIndex,
    answerIndex: question.answerIndex,
    phase,
    at: new Date().toISOString(),
  });

  if (isCorrect) {
    applyCorrectAnswer(question);
    normalizeSessionPhase();
    saveSession();
    renderQuiz();
    return;
  }

  session.streak = 0;
  if (session.settings.spartanMode && !session.inSpartan && !session.spartanPending.includes(currentIndex)) {
    session.spartanPending.push(currentIndex);
  }
  const correctText = displayOption(question.options[question.answerIndex], session.settings.direction);
  session.showingFeedback = true;
  session.feedback = {
    correct: false,
    selectedIndex,
    message: `不正解。正解: ${correctText}`,
  };
  saveSession();
  renderQuiz();
}

function applyCorrectAnswer(question) {
  const session = state.session;
  session.streak += 1;
  const earned = scoreForCorrect(question, session.streak);
  if (session.inSpartan) {
    session.spartanRawPoints += earned;
    session.spartanScaledPoints += earned * SPARTAN_SCORE_MULTIPLIER;
    session.spartanCorrect += 1;
    session.spartanPending = session.spartanPending.filter((index) => index !== session.spartanCurrent);
    session.spartanCurrent = null;
    if (!session.spartanPending.length) {
      session.inSpartan = false;
    }
  } else {
    session.mainPoints += earned;
    session.correct += 1;
    session.qIndex += 1;
  }
  session.showingFeedback = false;
  session.feedback = null;
}

function advanceAfterFeedback() {
  const session = state.session;
  if (!session?.showingFeedback) {
    return;
  }
  if (session.inSpartan) {
    session.spartanCurrent = null;
  } else {
    session.qIndex += 1;
  }
  session.showingFeedback = false;
  session.feedback = null;
  normalizeSessionPhase();
  saveSession();
  renderQuiz();
}

function normalizeSessionPhase() {
  const session = state.session;
  if (!session || session.status !== "active") {
    return;
  }
  if (session.inSpartan && !session.spartanPending.length) {
    session.inSpartan = false;
    session.spartanCurrent = null;
  }
  if (session.qIndex >= session.questions.length) {
    if (session.settings.spartanMode && session.spartanPending.length) {
      session.inSpartan = true;
      if (session.spartanCurrent === null || session.spartanCurrent === undefined || !session.spartanPending.includes(session.spartanCurrent)) {
        session.spartanCurrent = randomItem(session.spartanPending);
      }
      return;
    }
    finishSession();
  } else if (!session.inSpartan) {
    session.spartanCurrent = null;
  }
}

function finishSession() {
  const session = state.session;
  if (!session) {
    return;
  }
  session.status = "complete";
  session.completedAt = session.completedAt || new Date().toISOString();
  const summary = computeResultSummary(session);
  session.finalPoints = summary.points;
  if (!session.savedToHistory) {
    state.history.unshift({
      id: session.id,
      userName: session.settings.userName,
      mode: session.settings.mode,
      direction: session.settings.direction,
      correct: summary.correct,
      total: summary.total,
      accuracy: summary.accuracy,
      points: summary.points,
      completedAt: session.completedAt,
    });
    state.history = state.history.slice(0, 100);
    session.savedToHistory = true;
    saveHistory();
  }
  saveSession();
  refreshResumeButton();
}

function renderResult() {
  const session = state.session;
  if (!isCompleteSession(session)) {
    setView("setup");
    return;
  }
  const summary = computeResultSummary(session);
  els.resultTitle.textContent = summary.accuracy >= 1 ? "全問正解" : "クイズ完了";
  els.accuracyMetric.textContent = `${Math.round(summary.accuracy * 100)}%`;
  els.pointsMetric.textContent = summary.points.toFixed(1);
  els.countMetric.textContent = `${summary.correct}/${summary.total}`;
  renderScoreSyncControls(summary);
  renderReview();
}

function renderScoreSyncControls(summary) {
  const session = state.session;
  const userName = String(session.settings.userName || "").trim();
  els.syncScoreStatus.classList.remove("is-success", "is-error");

  if (!IS_STREAMLIT_COMPONENT) {
    els.syncScoreButton.disabled = true;
    els.syncScoreButton.textContent = "ランキングに保存";
    els.syncScoreStatus.textContent = "ランキング保存はStreamlit Cloud版で利用できます。";
    return;
  }
  if (!userName) {
    els.syncScoreButton.disabled = true;
    els.syncScoreButton.textContent = "ランキングに保存";
    els.syncScoreStatus.textContent = "ユーザー名を入力して開始するとランキングに保存できます。";
    return;
  }
  if (session.scoreSyncStatus === "pending") {
    els.syncScoreButton.disabled = true;
    els.syncScoreButton.textContent = "保存中...";
    els.syncScoreStatus.textContent = "Google Sheetsへ保存しています。";
    return;
  }
  if (session.scoreSyncStatus === "saved") {
    els.syncScoreButton.disabled = true;
    els.syncScoreButton.textContent = "ランキング保存済み";
    els.syncScoreStatus.classList.add("is-success");
    els.syncScoreStatus.textContent = session.scoreSyncMessage || `今回の${summary.points.toFixed(1)}点を加算しました。`;
    return;
  }
  els.syncScoreButton.disabled = false;
  els.syncScoreButton.textContent = "ランキングに保存";
  if (session.scoreSyncStatus === "error") {
    els.syncScoreStatus.classList.add("is-error");
    els.syncScoreStatus.textContent = session.scoreSyncMessage || "保存に失敗しました。もう一度お試しください。";
  } else {
    els.syncScoreStatus.textContent = `Google Sheetsの累積得点へ${summary.points.toFixed(1)}点を加算します。`;
  }
}

function syncScoreToSheets() {
  const session = state.session;
  if (!isCompleteSession(session)) {
    return;
  }
  const summary = computeResultSummary(session);
  const userName = String(session.settings.userName || "").trim();
  if (!IS_STREAMLIT_COMPONENT) {
    session.scoreSyncStatus = "error";
    session.scoreSyncMessage = "ランキング保存はStreamlit Cloud版で利用できます。";
    saveSession();
    renderResult();
    return;
  }
  if (!userName) {
    session.scoreSyncStatus = "error";
    session.scoreSyncMessage = "保存するにはユーザー名が必要です。";
    saveSession();
    renderResult();
    return;
  }
  if (session.scoreSyncStatus === "saved" || session.scoreSyncStatus === "pending") {
    return;
  }
  if (!session.scoreSaveId) {
    session.scoreSaveId = `mobile-${session.id}`;
  }
  session.scoreSyncRequestId = createId();
  session.scoreSyncStatus = "pending";
  session.scoreSyncMessage = "Google Sheetsへ保存しています。";
  saveSession();
  renderResult();
  streamlitHost.setComponentValue(buildScoreSyncPayload(session, summary));
}

function buildScoreSyncPayload(session, summary) {
  const settings = session.settings || {};
  const spartanAccuracy = session.spartanAttempts ? session.spartanCorrect / session.spartanAttempts : 0;
  return {
    type: "save_score",
    requestId: session.scoreSyncRequestId,
    saveId: session.scoreSaveId,
    sessionId: session.id,
    appVersion: APP_VERSION,
    user: String(settings.userName || "").trim(),
    mode: settings.mode === "sentence" ? "sentence" : "vocab",
    direction: settings.direction,
    correct: summary.correct,
    total: summary.total,
    accuracy: summary.accuracy,
    points: summary.points,
    accuracyBonus: summary.accuracyBonus,
    rawPointsTotal: session.mainPoints + session.spartanRawPoints,
    rawPointsMain: session.mainPoints,
    rawPointsSpartan: session.spartanRawPoints,
    spartanScaledPoints: session.spartanScaledPoints,
    spartanAttempts: session.spartanAttempts,
    spartanCorrect: session.spartanCorrect,
    spartanAccuracy,
    spartanMode: Boolean(settings.spartanMode),
    groupId: settings.groupId || "",
    seed: settings.seed,
    pos: settings.pos || "",
    topic: settings.topic || "",
    subtopic: settings.subtopic || "",
    levels: Array.isArray(settings.levels) ? settings.levels : [],
    length: settings.length,
    startedAt: session.startedAt,
    completedAt: session.completedAt,
    ts: new Date().toISOString(),
  };
}

function renderReview() {
  const session = state.session;
  const wrongAnswers = session.answers.filter((answer) => answer.selectedIndex !== answer.answerIndex);
  if (!wrongAnswers.length) {
    const empty = document.createElement("div");
    empty.className = "review-item";
    empty.innerHTML = "<strong>間違えた問題はありません</strong><p>この結果は端末内の成績に保存されています。</p>";
    els.reviewList.replaceChildren(empty);
    return;
  }
  els.reviewList.replaceChildren(
    ...wrongAnswers.map((answer) => {
      const question = session.questions[answer.qIndex];
      const selected = question?.options[answer.selectedIndex];
      const correct = question?.options[answer.answerIndex];
      const item = document.createElement("article");
      item.className = "review-item";
      const prompt = question ? displayPrompt(question, session.settings.direction) : "";
      const selectedText = selected ? displayOption(selected, session.settings.direction) : "";
      const correctText = correct ? displayOption(correct, session.settings.direction) : "";
      item.innerHTML = `
        <strong>${escapeHtml(prompt)}</strong>
        <p>正解: ${escapeHtml(correctText)}</p>
        <p>回答: ${escapeHtml(selectedText || "-")}</p>
      `;
      return item;
    }),
  );
}

function renderHistory() {
  if (!state.history.length) {
    const empty = document.createElement("div");
    empty.className = "history-item";
    empty.innerHTML = "<strong>成績はまだありません</strong><p>クイズを完了するとここに残ります。</p>";
    els.historyList.replaceChildren(empty);
    return;
  }
  els.historyList.replaceChildren(
    ...state.history.map((record) => {
      const item = document.createElement("article");
      item.className = "history-item";
      const mode = record.mode === "sentence" ? "例文" : "単語";
      const date = formatDate(record.completedAt);
      item.innerHTML = `
        <strong>${escapeHtml(mode)} ${escapeHtml(record.points.toFixed(1))}点</strong>
        <p>${escapeHtml(date)} / ${escapeHtml(record.correct)}/${escapeHtml(record.total)} 正解 / ${escapeHtml(Math.round(record.accuracy * 100))}%</p>
      `;
      return item;
    }),
  );
}

function computeResultSummary(session) {
  const total = session.questions.length;
  const correct = session.correct;
  const accuracy = total ? correct / total : 0;
  const accuracyBonus = accuracy * total * (
    session.settings.mode === "sentence" ? SENTENCE_ACCURACY_BONUS : VOCAB_ACCURACY_BONUS
  );
  const points = session.mainPoints + session.spartanScaledPoints + accuracyBonus;
  return {
    total,
    correct,
    accuracy,
    accuracyBonus,
    points,
  };
}

function scoreForCorrect(question, streak) {
  const streakCount = Math.max(0, streak - 1);
  if (question.mode === "sentence") {
    const base = (Number(question.level) + 11.5) * SENTENCE_SCORE_SCALE;
    return base + streakCount * STREAK_BONUS * SENTENCE_STREAK_SCALE;
  }
  return BASE_POINTS * getStageFactor(question.stages) + streakCount * STREAK_BONUS;
}

function getStageFactor(stages) {
  if (stages.some((stage) => stage.includes("advanced"))) {
    return 1.6;
  }
  if (stages.some((stage) => stage.includes("intermediate"))) {
    return 1.3;
  }
  return 1.0;
}

function getCurrentQuestion() {
  const session = state.session;
  if (!session) {
    return null;
  }
  return session.questions[getCurrentQuestionIndex()] || null;
}

function getCurrentQuestionIndex() {
  const session = state.session;
  if (!session) {
    return -1;
  }
  if (session.inSpartan) {
    if (session.spartanCurrent === null || session.spartanCurrent === undefined || !session.spartanPending.includes(session.spartanCurrent)) {
      session.spartanCurrent = randomItem(session.spartanPending);
    }
    return session.spartanCurrent;
  }
  return session.qIndex;
}

function remainingCount(session) {
  if (session.inSpartan) {
    return session.spartanPending.length;
  }
  return Math.max(session.questions.length - session.qIndex, 0);
}

function displayPrompt(question, direction) {
  return direction === "ja_to_eo" ? question.promptJa : question.promptEo;
}

function displayOption(option, direction) {
  return direction === "ja_to_eo" ? option.eo : option.ja;
}

function playAudio(mode, option) {
  const base = getAudioBaseUrl(mode);
  if (!base || !option?.audioKey) {
    showToast("音声ファイルがありません。");
    return;
  }
  const audio = new Audio(encodeURI(`${base}${option.audioKey}.wav`));
  audio.play().catch(() => {
    showToast("音声を再生できませんでした。");
  });
}

function hasPlayableAudio(option) {
  const mode = getCurrentQuestion()?.mode || state.settings.mode;
  return hasAudioForMode(mode) && Boolean(option?.hasAudio);
}

function hasAudioForMode(mode) {
  return Boolean(state.audioConfig.enabled && getAudioBaseUrl(mode));
}

function getAudioBaseUrl(mode) {
  if (mode === "sentence") {
    return state.audioConfig.sentenceBaseUrl;
  }
  return state.audioConfig.vocabBaseUrl;
}

function ensureTrailingSlash(value) {
  const text = String(value || "").trim();
  if (!text) {
    return "";
  }
  return text.endsWith("/") ? text : `${text}/`;
}

function setView(view) {
  state.currentView = view;
  els.app?.classList.remove("view-loading", "view-setup", "view-quiz", "view-result", "view-history", "view-error");
  els.app?.classList.add(`view-${view}`);
  const viewMap = {
    loading: els.loadingView,
    setup: els.setupView,
    quiz: els.quizView,
    result: els.resultView,
    history: els.historyView,
    error: els.errorView,
  };
  Object.entries(viewMap).forEach(([name, element]) => {
    element.classList.toggle("is-active", name === view);
  });
  els.homeNav.classList.toggle("is-selected", view === "setup");
  els.quizNav.classList.toggle("is-selected", view === "quiz" || view === "result");
  els.historyNav.classList.toggle("is-selected", view === "history");
  if (view === "setup") {
    renderSetup();
  }
  if (view === "result") {
    renderResult();
  }
  if (view === "quiz") {
    window.requestAnimationFrame(scrollHostToTop);
    window.setTimeout(scrollHostToTop, 120);
    window.setTimeout(scrollHostToTop, 350);
  }
  requestFrameHeightSync();
}

function refreshResumeButton() {
  const canResume = isActiveSession(state.session) || isCompleteSession(state.session);
  els.resumeButton.hidden = !canResume;
  els.resumeNotice.hidden = !canResume;
  if (canResume) {
    els.resumeMeta.textContent = describeStoredSession(state.session);
  } else {
    els.resumeMeta.textContent = "";
  }
  requestFrameHeightSync();
}

function describeStoredSession(session) {
  const mode = session.settings?.mode === "sentence" ? "例文" : "単語";
  if (isCompleteSession(session)) {
    const summary = computeResultSummary(session);
    return `${mode} / 完了 / ${summary.correct}/${summary.total} 正解`;
  }
  const current = Math.min(Number(session.qIndex || 0) + 1, session.questions.length);
  const review = Array.isArray(session.spartanPending) && session.spartanPending.length
    ? ` / 復習 ${session.spartanPending.length}問`
    : "";
  return `${mode} / Q${current}/${session.questions.length}${review}`;
}

function updateSaveStatus(text) {
  els.saveStatus.textContent = text;
}

function showToast(message) {
  els.toast.textContent = message;
  els.toast.hidden = false;
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => {
    els.toast.hidden = true;
  }, 2600);
}

function showFatalError(error) {
  console.error(error);
  els.errorMessage.textContent = error?.message || String(error);
  setView("error");
  updateSaveStatus("エラー");
}

function isActiveSession(session) {
  return Boolean(session && session.status === "active" && Array.isArray(session.questions) && session.questions.length);
}

function isCompleteSession(session) {
  return Boolean(session && session.status === "complete" && Array.isArray(session.questions) && session.questions.length);
}

function buildVocabGroups(entries, seed) {
  const rng = mulberry32(clampInteger(seed, 1, 8192, 1));
  const byPos = new Map();
  entries.forEach((entry) => {
    const pos = entry.pos === "personal_pronoun" ? "pronoun" : entry.pos;
    const normalized = { ...entry, pos };
    if (!byPos.has(pos)) {
      byPos.set(pos, []);
    }
    byPos.get(pos).push(normalized);
  });

  const groups = [];
  [...byPos.entries()].forEach(([pos, items]) => {
    const buckets = splitByLevel(items);
    const sublevels = mergeSmallSublevels(buildSublevels(buckets));
    sublevels.forEach(({ labels, words }) => {
      groups.push(...splitIntoGroups(labels, words, pos, rng));
    });
  });
  return groups;
}

function splitByLevel(entries) {
  const sorted = [...entries].sort((a, b) => Number(a.level) - Number(b.level));
  const [beginner, intermediate] = allocateByRatio(sorted.length, [55, 65, 120]);
  return {
    beginner: sorted.slice(0, beginner),
    intermediate: sorted.slice(beginner, beginner + intermediate),
    advanced: sorted.slice(beginner + intermediate),
  };
}

function buildSublevels(buckets) {
  const ordered = [];
  [
    ["beginner", 3],
    ["intermediate", 3],
    ["advanced", 6],
  ].forEach(([stage, parts]) => {
    evenChunks(buckets[stage] || [], parts).forEach((chunk, index) => {
      if (chunk.length) {
        ordered.push({ labels: [`${stage}_${index + 1}`], words: [...chunk] });
      }
    });
  });
  return ordered;
}

function mergeSmallSublevels(sublevels) {
  if (!sublevels.length) {
    return [];
  }
  const merged = [];
  let current = {
    labels: [...sublevels[0].labels],
    words: [...sublevels[0].words],
  };
  sublevels.slice(1).forEach((sublevel) => {
    if (current.words.length < 20) {
      current.labels.push(...sublevel.labels);
      current.words.push(...sublevel.words);
    } else {
      merged.push(current);
      current = {
        labels: [...sublevel.labels],
        words: [...sublevel.words],
      };
    }
  });
  if (current.words.length < 20 && merged.length) {
    const previous = merged.pop();
    previous.labels.push(...current.labels);
    previous.words.push(...current.words);
    merged.push(previous);
  } else {
    merged.push(current);
  }
  return merged;
}

function splitIntoGroups(labels, words, pos, rng) {
  const shuffled = shuffle([...words], rng);
  const total = shuffled.length;
  const sizes = groupSizes(total);
  let cursor = 0;
  return sizes.map((size, index) => {
    const entries = shuffled.slice(cursor, cursor + size);
    cursor += size;
    return {
      id: `${pos}:${labels.join("+")}:g${index + 1}`,
      pos,
      stages: [...labels],
      indexLabel: `G${index + 1}`,
      entries,
    };
  });
}

function groupSizes(total) {
  if (total <= 30) {
    return [total];
  }
  if (total <= 39) {
    const half = Math.floor(total / 2);
    return [half, total - half];
  }
  const count = chooseGroupCount(total);
  const base = Math.floor(total / count);
  const extra = total % count;
  return Array.from({ length: count }, (_, index) => base + (index < extra ? 1 : 0));
}

function chooseGroupCount(total) {
  const lower = Math.ceil(total / 30);
  const upper = Math.max(lower, Math.floor(total / 20));
  let best = lower;
  let bestDistance = Number.POSITIVE_INFINITY;
  for (let count = lower; count <= upper; count += 1) {
    const distance = Math.abs(total / count - 25);
    if (distance < bestDistance) {
      best = count;
      bestDistance = distance;
    }
  }
  return best;
}

function allocateByRatio(total, weights) {
  if (total <= 0) {
    return weights.map(() => 0);
  }
  const sum = weights.reduce((acc, value) => acc + value, 0);
  const raw = weights.map((weight) => total * weight / sum);
  const floors = raw.map(Math.floor);
  let remainder = total - floors.reduce((acc, value) => acc + value, 0);
  const order = raw
    .map((value, index) => ({ index, fraction: value - floors[index] }))
    .sort((a, b) => b.fraction - a.fraction);
  let cursor = 0;
  while (remainder > 0) {
    floors[order[cursor % order.length].index] += 1;
    remainder -= 1;
    cursor += 1;
  }
  return floors;
}

function evenChunks(items, parts) {
  const base = Math.floor(items.length / parts);
  const extra = items.length % parts;
  let cursor = 0;
  return Array.from({ length: parts }, (_, index) => {
    const size = base + (index < extra ? 1 : 0);
    const chunk = items.slice(cursor, cursor + size);
    cursor += size;
    return chunk;
  });
}

function formatStageLabel(stages) {
  return stages.map((stage) => {
    const [name, number] = stage.split("_");
    return `${STAGE_LABELS[name] || name}${number || ""}`;
  }).join("+");
}

function labelForPos(pos) {
  return POS_LABELS[pos] || pos;
}

function posSortIndex(pos) {
  const index = POS_ORDER.indexOf(pos);
  return index === -1 ? 999 : index;
}

function sample(items, count, rng) {
  return shuffle([...items], rng).slice(0, count);
}

function shuffle(items, rng) {
  for (let index = items.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(rng() * (index + 1));
    [items[index], items[swapIndex]] = [items[swapIndex], items[index]];
  }
  return items;
}

function mulberry32(seed) {
  let value = seed >>> 0;
  return function next() {
    value += 0x6D2B79F5;
    let mixed = value;
    mixed = Math.imul(mixed ^ mixed >>> 15, mixed | 1);
    mixed ^= mixed + Math.imul(mixed ^ mixed >>> 7, mixed | 61);
    return ((mixed ^ mixed >>> 14) >>> 0) / 4294967296;
  };
}

function randomItem(items) {
  if (!items.length) {
    return null;
  }
  return items[Math.floor(Math.random() * items.length)];
}

function unique(items) {
  return [...new Set(items.filter((item) => item !== undefined && item !== null && item !== ""))];
}

function isPlainObject(value) {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

function finiteNumber(value, fallback) {
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : fallback;
}

function clampInteger(value, min, max, fallback) {
  const parsed = Number.parseInt(value, 10);
  if (!Number.isFinite(parsed)) {
    return fallback;
  }
  return Math.min(max, Math.max(min, parsed));
}

function createId() {
  if (window.crypto?.randomUUID) {
    return window.crypto.randomUUID();
  }
  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function formatDate(value) {
  try {
    return new Intl.DateTimeFormat("ja-JP", {
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
    }).format(new Date(value));
  } catch {
    return "";
  }
}
