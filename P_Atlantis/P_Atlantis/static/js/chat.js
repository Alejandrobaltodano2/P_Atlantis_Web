var chatOpen = false;
var chatContainer = document.getElementById('chat-container');
var messageArea = document.getElementById('message-area');

function toggleChat() {
    chatOpen = !chatOpen;
    if (chatOpen) {
        chatContainer.style.display = 'block';
    } else {
        chatContainer.style.display = 'none';
    }
}

function sendMessage(event) {
    if (event.key === 'Enter') {
        var messageText = event.target.value;
        if (messageText.trim() !== '') {
            var messageElement = document.createElement('div');
            messageElement.classList.add('message', 'outgoing');
            messageElement.textContent = messageText;
            messageArea.appendChild(messageElement);
            event.target.value = '';
        }
    }
}