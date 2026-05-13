import gradio as gr

def chatbot(query):
    return f"Medical AI Response for: {query}"

interface = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="Medical Chatbot using RAG"
)

interface.launch()