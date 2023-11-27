import reflex as rx

class State(rx.State):
    count: int = 50

    def increment(self):
        self.count += 10

    def decrement(self):
        self.count -= 10

def index():
    return rx.vstack(
        rx.button(
            "Decrement",
            font_size="2em",
            bg="#fef2f2",
            color="red",
            border_radius="lg",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="3em"),
        rx.button(
            "Increment",
            font_size="2em",
            bg="#ecfdf5",
            color="green",
            border_radius="lg",
            on_click=State.increment,
        ),
    )


app = rx.App()
app.add_page(index)
app.compile()