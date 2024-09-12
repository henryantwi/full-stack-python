import reflex as rx

from .nav import navbar


def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    # print([type(x) for x in args])
    if not isinstance(child, rx.Component):
        child = rx.heading("this is not a valid child element")
    if hide_navbar:
        return rx.container(
            # navbar(), # Navbar removed!
            child,
            rx.color_mode.button(position="bottom-left"),
            rx.logo(),
        )
    return rx.container(
        navbar(),
        child,
        rx.color_mode.button(position="bottom-left", id="my-light-mode-btn"),
        rx.logo(),
        id="my-base-container",
    )
