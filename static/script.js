window.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById('message-input');
  const messagesDiv = document.getElementById('messages');
  const sendBtn = document.querySelector('button');

  async function sendMessage() {
    const msg = input.value.trim();
    if (!msg) return;

    messagesDiv.innerHTML += `<div class="msg user-msg fade-in"><span>You:</span> ${msg}</div>`;
    input.value = '';

    try {
      const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
      });

      const data = await response.json();
      messagesDiv.innerHTML += `<div class="msg bot-msg fade-in"><span>Mistral:</span> ${data.response}</div>`;
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    } catch (error) {
      messagesDiv.innerHTML += `<div class="msg bot-msg fade-in"><span>Error:</span> Failed to get response.</div>`;
    }
  }

  input.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') sendMessage();
  });

  sendBtn.addEventListener('click', sendMessage);
});