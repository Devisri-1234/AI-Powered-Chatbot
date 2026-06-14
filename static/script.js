function sendMessage() {

    let input = document.getElementById("message");
    let message = input.value.trim();

    if(message === ""){
        return;
    }

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML +=
        `<div class="user-message">${message}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })

    .then(response => response.json())

    .then(data => {

        chatBox.innerHTML +=
            `<div class="bot-message">${data.response}</div>`;

        chatBox.scrollTop = chatBox.scrollHeight;
    })

    .catch(error => {

        chatBox.innerHTML +=
            `<div class="bot-message">Error connecting to chatbot.</div>`;
    });

    input.value = "";
}

function handleEnter(event){

    if(event.key === "Enter"){
        sendMessage();
    }
}