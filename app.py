import gradio as gr
import openai_gradio

gr.load(
    name='',
#    url='http://127.0.0.1:8000/v1/',
    token='',
    src=openai_gradio.registry,
).launch()