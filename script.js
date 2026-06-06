const sendBtn = document.getElementById("sendBtn");
const messageInput = document.getElementById("messageInput");
const chatContainer = document.getElementById("chatContainer");
const typingIndicator = document.getElementById("typingIndicator");

sendBtn.addEventListener("click", sendMessage);

messageInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    sendMessage();
  }
});

function sendMessage() {

  const message = messageInput.value.trim();

  if (!message) return;

  // User Message
  const userDiv = document.createElement("div");

  userDiv.className = "flex justify-start";

  userDiv.innerHTML = `
    <div class="bg-gray-800 max-w-xl p-5 rounded-2xl">
      <p>${message}</p>
    </div>
  `;

  chatContainer.appendChild(userDiv);

  messageInput.value = "";

  chatContainer.scrollTop = chatContainer.scrollHeight;

  // Show typing indicator
  typingIndicator.classList.remove("hidden");

  // Fake AI response
  setTimeout(() => {

    typingIndicator.classList.add("hidden");

    const aiDiv = document.createElement("div");

    aiDiv.className = "flex justify-end";

    aiDiv.innerHTML = `
      <div class="bg-blue-600 max-w-xl p-5 rounded-2xl">
        <p>
          I remember your previous issue and I’m checking the best solution for you.
        </p>
      </div>
    `;

    chatContainer.appendChild(aiDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;

  }, 1500);
}