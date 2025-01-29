async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const userMessage = inputField.value;
    inputField.value = '';
    appendMessage("You: " + userMessage);

    let responseMessage = "I'm sorry, I didn't understand that.";
    if (userMessage.toLowerCase().includes("scan networks")) {
        const response = await fetch('/scan_network', { method: 'POST' });
        const vulnerabilities = await response.json();
        responseMessage = "Vulnerabilities found: " + JSON.stringify(vulnerabilities);
    } else if (userMessage.toLowerCase().includes("deploy exploit")) {
        const target = prompt("Enter target for exploit deployment:");
        const response = await fetch('/deploy_exploit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ target })
        });
        const result = await response.json();
        responseMessage = "Exploit deployment result: " + result.result;
    }
    appendMessage("Chatbot: " + responseMessage);
}

async function uploadImage() {
    const fileInput = document.getElementById("image-input");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('image', file);

    const response = await fetch('/extract_text_from_image', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    appendMessage("Extracted Text: " + data.extracted_text);
}

async function uploadDocument() {
    const fileInput = document.getElementById("document-input");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('document', file);

    const response = await fetch('/parse_document', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    appendMessage("Parsed Text: " + data.parsed_text);
}

function appendMessage(message) {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += "<div>" + message + "</div>";
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
}
