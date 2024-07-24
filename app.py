import gradio as gr
from huggingface_hub import InferenceClient

"""
For more information on `huggingface_hub` Inference API support, please check the docs: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
"""
client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")


def respond(
    message,
    history: list[tuple[str, str]],
    system_message,
    max_tokens,
    temperature,
    top_p,
):
    system_message = "You are a knowledgeable DBT coach. You always talk about one options at at a time. you add greetings and you ask questions like real counsellor. Remember you are helpful and a good listener. You are concise and never ask multiple questions, or give long response. You response like a human counsellor accurately and correctly. consider the users as your client. and practice verbal cues only where needed. Remember you must be respectful and consider that the user may not be in a situation to deal with a wordy chatbot.  You Use DBT book to guide users through DBT exercises and provide helpful information. When needed only then you ask one follow up question at a time to guide the user to ask appropiate question. You avoid giving suggestion if any dangerous act is mentioned by the user and refer to call someone or emergency."
    messages = [{"role": "system", "content": system_message}]

    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})

    messages.append({"role": "user", "content": message})

    response = ""

    for message in client.chat_completion(
        messages,
        max_tokens=max_tokens,
        stream=True,
        temperature=temperature,
        top_p=top_p,
    ):
        token = message.choices[0].delta.content

        response += token
        yield response

"""
For information on how to customize the ChatInterface, peruse the gradio docs: https://www.gradio.app/docs/chatinterface
"""
demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value = "You are a good listener. You advise relaxation exercises, suggest avoiding negative thoughts, and guide through steps to manage stress. Discuss what's on your mind, or ask me for a quick relaxation exercise.", label="System message"),
        gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p (nucleus sampling)",
        ),
    ],

        examples=[
            ["What is the purpose of Eating Well with Canada's Food Guide?"],
            ["Why are foods categorized into food groups?"],
            ["What are the recommended daily servings for vegetables and fruits? Provide examples of serving sizes."],
            ["How many servings of grain products are recommended daily for men and women, and what constitutes one serving?"],
            ["How many servings of milk and alternatives are recommended daily, and what are examples of one serving from this group?"],
            ["How many servings of meat and alternatives are recommended daily for men and women, and what are examples of one serving from this group?"],
            ["How much unsaturated fat per day is recommended for consumption, and what are examples of sources?"]
        ],
        title='Diet Expert Assistant'
    )


if __name__ == "__main__":
    demo.launch()
