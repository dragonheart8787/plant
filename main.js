async function getSuggestion() {
  const plant = document.getElementById("plant").value.trim();
  const condition = document.getElementById("condition").value.trim();
  const outputBox = document.getElementById("output");

  if (!plant || !condition) {
    outputBox.innerText = "請填入植物與環境條件";
    return;
  }

  const prompt = `我想要種植「${plant}」，但環境是「${condition}」，請給我具體的照顧建議與常見注意事項。`;

  outputBox.innerText = "請稍候，AI 正在生成建議...";

  const res = await fetch("/api/suggest", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt })
  });

  const data = await res.json();
  outputBox.innerText = data.result || "未收到建議。";
}
