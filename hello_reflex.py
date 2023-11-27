# chatapp.py

import reflex as rx
from hello_reflex import style
from hello_reflex.state import State


def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style),text_align="right",),
        rx.box(rx.text(answer, style=style.answer_style),text_align="left",),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question here: ",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
        )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()