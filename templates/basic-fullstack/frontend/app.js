/** 前端逻辑：连接后端 /api/chat，支持普通 + 流式两种模式。 */

const API_BASE = "http://localhost:8000";

const $ = (id) => document.getElementById(id);
const chatArea = $("chatArea");
const input = $("input");
const sendBtn = $("sendBtn");
const streamToggle = $("streamToggle");
const backendSelect = $("backendSelect");
const welcome = $("welcome");

let isStreaming = false;

// ── 发送消息 ──
sendBtn.addEventListener("click", send);
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    send();
  }
});

// 快捷提示
document.querySelectorAll(".quick-prompts button").forEach((btn) => {
  btn.addEventListener("click", () => {
    input.value = btn.dataset.prompt;
    send();
  });
});

async function send() {
  const text = input.value.trim();
  if (!text || isStreaming) return;
  input.value = "";
  input.style.height = "auto";

  // 隐藏欢迎页
  if (welcome) welcome.style.display = "none";

  // 收集当前消息
  const messages = getMessages();
  messages.push({ role: "user", content: text });

  // 渲染用户消息
  appendMessage("user", text);

  // 渲染 AI 占位
  const botEl = appendMessage("bot", "", true);

  if (streamToggle.checked) {
    await streamChat(messages, botEl);
  } else {
    await normalChat(messages, botEl);
  }
}

// ── 从 DOM 中提取已有消息 ──
function getMessages() {
  const msgs = [];
  const items = chatArea.querySelectorAll(".message");
  items.forEach((el) => {
    const role = el.classList.contains("user") ? "user" : "assistant";
    const bubble = el.querySelector(".bubble");
    if (bubble && bubble.textContent.trim()) {
      msgs.push({ role, content: bubble.textContent.trim() });
    }
  });
  return msgs;
}

// ── 非流式 ──
async function normalChat(messages, botEl) {
  const bubble = botEl.querySelector(".bubble");
  try {
    const resp = await fetch(`${API_BASE}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages, stream: false }),
    });
    if (!resp.ok) throw new Error(`${resp.status} ${resp.statusText}`);
    const data = await resp.json();
    bubble.textContent = data.reply;
    bubble.classList.remove("streaming");
    scrollBottom();
  } catch (err) {
    bubble.textContent = `请求失败: ${err.message}`;
    bubble.style.color = "#e53e3e";
    bubble.classList.remove("streaming");
  }
}

// ── 流式（SSE/plain text chunk）──
async function streamChat(messages, botEl) {
  isStreaming = true;
  sendBtn.disabled = true;
  const bubble = botEl.querySelector(".bubble");
  bubble.textContent = "";

  try {
    const resp = await fetch(`${API_BASE}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages, stream: true }),
    });

    if (!resp.ok) throw new Error(`${resp.status} ${resp.statusText}`);

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      bubble.textContent += decoder.decode(value, { stream: true });
      scrollBottom();
    }

    bubble.classList.remove("streaming");
  } catch (err) {
    if (!bubble.textContent) {
      bubble.textContent = `流式请求失败: ${err.message}`;
      bubble.style.color = "#e53e3e";
    }
    bubble.classList.remove("streaming");
  } finally {
    isStreaming = false;
    sendBtn.disabled = false;
    scrollBottom();
  }
}

// ── 渲染消息 ──
function appendMessage(role, text, streaming = false) {
  const el = document.createElement("div");
  el.className = `message ${role}`;

  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = role === "user" ? "U" : "AI";

  const bubble = document.createElement("div");
  bubble.className = "bubble" + (streaming ? " streaming" : "");
  bubble.textContent = text;

  el.appendChild(avatar);
  el.appendChild(bubble);
  chatArea.appendChild(el);
  scrollBottom();
  return el;
}

function scrollBottom() {
  chatArea.scrollTop = chatArea.scrollHeight;
}

// ── 自动调整 textarea 高度 ──
input.addEventListener("input", () => {
  input.style.height = "auto";
  input.style.height = Math.min(input.scrollHeight, 120) + "px";
});
