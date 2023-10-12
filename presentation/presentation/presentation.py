# Dependencies
import reflex as rx
from typing import List, Tuple

# Styles
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
)
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow, flex="1"
)
button_style = dict(bg="#CEFFEE", box_shadow=shadow, margin_left="1em")

# State
class State(rx.State):
    username: str = ""
    content: str = ""
    messages: List[Tuple[str, str]] = []

    def post_message(self):
        if self.username and self.content:
            self.messages.append((self.username, self.content))
            self.content = ""
            yield

# Components
def message_display(username: str, content: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(f"{username}: {content}", text_align="left"),
            style=message_style,
        ),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.messages,
            lambda msg: message_display(msg[0], msg[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.username,
            placeholder="Your Name",
            on_change=State.set_username,
            style=input_style,
        ),
        rx.input(
            value=State.content,
            placeholder="Your Message",
            on_change=State.set_content,
            style=input_style,
        ),
        rx.button(
            "Post",
            on_click=State.post_message,
            style=button_style,
        ),
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )

# App Initialization
app = rx.App()
app.add_page(index)
app.compile()

if __name__ == "__main__":
    app.run()
