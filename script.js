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

async function sendMessage() {

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

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/v1/chat/",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    customer_id: "test-user",
                    message: message
                })
            }
        );

        const data = await response.json();

        typingIndicator.classList.add("hidden");

        const aiDiv = document.createElement("div");

        aiDiv.className = "flex justify-end";

        aiDiv.innerHTML = `
            <div class="bg-blue-600 max-w-xl p-5 rounded-2xl">
                <p>${data.reply}</p>
            </div>
        `;

        chatContainer.appendChild(aiDiv);

        chatContainer.scrollTop = chatContainer.scrollHeight;

    } catch (error) {

        typingIndicator.classList.add("hidden");

        console.error("Backend Error:", error);

        const errorDiv = document.createElement("div");

        errorDiv.className = "flex justify-end";

        errorDiv.innerHTML = `
            <div class="bg-red-600 max-w-xl p-5 rounded-2xl">
                <p>Backend connection failed</p>
            </div>
        `;

        chatContainer.appendChild(errorDiv);
    }
}