
import gradio as gr
from backend.ai_chat import MultiAIChat

chat_history = []

def chat_with_ai(prompt, ai_provider):
    chat = MultiAIChat("openai_key", "huggingface_key", "anthropic_key")
    response = ""
    if ai_provider == "OpenAI":
        response = chat.openai_chat(prompt)
    elif ai_provider == "Hugging Face":
        response = chat.huggingface_chat(prompt)
    elif ai_provider == "Anthropic":
        response = chat.anthropic_chat(prompt)
    chat_history.append((prompt, response))
    return chat_history

iface = gr.Interface(
    fn=chat_with_ai,
    inputs=[gr.Textbox(label="Your Prompt"), gr.Radio(["OpenAI", "Hugging Face", "Anthropic"], label="AI Provider")],
    outputs=gr.Chatbot(label="Chat History"),
    live=True
)

iface.launch()
