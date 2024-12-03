import gradio as gr
import openai_gradio

gr.load(
    name='Qwen/Qwen2.5-Coder-7B-Instruct',
    url='http://192.168.55.14:8001/v1/',
    token='EMPTY',
    src=openai_gradio.registry,
).launch()