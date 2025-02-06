const ALLOWED_EXTENSIONS = ['pdf','zip','html','js','java','css','ts','gitignore','env','json','config','txt','rb','py','xml','doc','xls','ppt','7z','rar','db','mhtml','xhtml','pl','pyc'];
let currentFiles = [];
let isRecording = false;
let recognition;

if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById('user-input').value = transcript;
    };

    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
    };
}

function saveSettings() {
    localStorage.setItem('apiEndpoint', document.getElementById('apiEndpoint').value);
    localStorage.setItem('githubToken', document.getElementById('githubToken').value);
    alert('Settings saved');
}

function loadSettings() {
    document.getElementById('apiEndpoint').value = localStorage.getItem('apiEndpoint') || '';
    document.getElementById('githubToken').value = localStorage.getItem('githubToken') || '';
}

function handleFileUpload(e) {
    const files = Array.from(e.target.files);
    const invalidFiles = files.filter(f => {
        const ext = f.name.split('.').pop();
        return !ALLOWED_EXTENSIONS.includes(ext);
    });

    if (invalidFiles.length > 0) {
        showError(`Invalid file types: ${invalidFiles.map(f => f.name).join(', ')}`);
        return;
    }

    currentFiles = [...currentFiles, ...files];
    showError('Files uploaded successfully', 'success');
}

async function exportZip() {
    if (currentFiles.length === 0) {
        showError('No files to export');
        return;
    }

    const formData = new FormData();
    currentFiles.forEach((file, i) => formData.append(`file${i}`, file));

    try {
        const response = await fetch('/api/export-zip', {
            method: 'POST',
            body: formData
        });
        
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'export.zip';
        a.click();
    } catch (error) {
        showError('ZIP export failed');
    }
}

function addMessage(sender, content, isPartial = false) {
    const container = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    messageDiv.innerHTML = `
        <div>${content}</div>
        <div class="message-actions">
            <button onclick="copyToClipboard('${content}')"><i class="fas fa-copy"></i></button>
            <button onclick="shareMessage('${content}')"><i class="fas fa-share"></i></button>
            ${sender === 'ai' ? `<button onclick="downloadCode('${content}')"><i class="fas fa-download"></i></button>` : ''}
        </div>
        ${isPartial ? '<button class="continue-button" onclick="continueResponse()">Continue</button>' : ''}
    `;

    container.appendChild(messageDiv);
    container.scrollTop = container.scrollHeight;
}

async function continueResponse() {
    try {
        const response = await fetch('/continue_response', {
            method: 'POST'
        });
        
        const data = await response.json();
        addMessage('ai', data.response, data.isPartial);
    } catch (error) {
        showError('Error continuing response');
    }
}

function toggleVoice() {
    if (!recognition) {
        showError('Speech recognition not supported');
        return;
    }

    isRecording = !isRecording;
    const micButton = document.querySelector('.fa-microphone');
    
    if (isRecording) {
        recognition.start();
        micButton.classList.add('voice-recording');
    } else {
        recognition.stop();
        micButton.classList.remove('voice-recording');
    }
}

function showError(message, type = 'error') {
    const errorDiv = document.createElement('div');
    errorDiv.className = `error-message ${type}`;
    errorDiv.textContent = message;
    document.body.appendChild(errorDiv);
    
    setTimeout(() => errorDiv.remove(), 5000);
}

document.addEventListener('DOMContentLoaded', () => {
    loadSettings();
});

function copyToClipboard(content) {
    navigator.clipboard.writeText(content).then(() => {
        showError('Copied to clipboard', 'success');
    }).catch(err => {
        showError('Failed to copy', 'error');
    });
}

function shareMessage(content) {
    if (navigator.share) {
        navigator.share({
            title: 'Chat Message',
            text: content
        }).then(() => {
            showError('Message shared', 'success');
        }).catch(err => {
            showError('Failed to share', 'error');
        });
    } else {
        showError('Share not supported', 'error');
    }
}

function downloadCode(content) {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `code-${Date.now()}.txt`;
    a.click();
}

function toggleDarkMode() {
    document.body.classList.toggle('light-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('light-mode') ? 'false' : 'true');
}

function handleImageUpload() {
    const input = document.getElementById('image-upload');
    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            document.getElementById('chat-box').appendChild(img);
        };
        reader.readAsDataURL(file);
    }
}

function handleDocUpload() {
    const input = document.getElementById('doc-upload');
    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const text = e.target.result;
            addMessage('user', text);
        };
        reader.readAsText(file);
    }
}

function switchMode(mode) {
    const modes = ['ai-chat', 'red-team', 'blue-team', 'purple-team', 'developer', 'foia-manager', 'support'];
    modes.forEach(m => document.body.classList.remove(m));
    document.body.classList.add(mode);
    showError(`Switched to ${mode} mode`, 'success');
}

function loadPreviousConversations() {
    const conversations = JSON.parse(localStorage.getItem('conversations')) || [];
    const container = document.getElementById('previous-conversations');
    container.innerHTML = '';
    conversations.forEach((conv, index) => {
        const item = document.createElement('div');
        item.className = 'conversation-item';
        item.textContent = `Conversation ${index + 1}`;
        item.onclick = () => loadConversation(index);
        container.appendChild(item);
    });
}

function loadConversation(index) {
    const conversations = JSON.parse(localStorage.getItem('conversations')) || [];
    const conversation = conversations[index];
    const container = document.getElementById('chat-box');
    container.innerHTML = '';
    conversation.forEach(msg => addMessage(msg.sender, msg.content));
}

function saveConversation() {
    const messages = Array.from(document.querySelectorAll('.message')).map(msg => ({
        sender: msg.classList.contains('user-message') ? 'user' : 'ai',
        content: msg.querySelector('div').textContent
    }));
    const conversations = JSON.parse(localStorage.getItem('conversations')) || [];
    conversations.push(messages);
    localStorage.setItem('conversations', JSON.stringify(conversations));
    showError('Conversation saved', 'success');
}

function deleteConversation(index) {
    const conversations = JSON.parse(localStorage.getItem('conversations')) || [];
    conversations.splice(index, 1);
    localStorage.setItem('conversations', JSON.stringify(conversations));
    loadPreviousConversations();
    showError('Conversation deleted', 'success');
}

document.addEventListener('DOMContentLoaded', () => {
    loadSettings();
    loadPreviousConversations();
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
    }
});
