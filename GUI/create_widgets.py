import tkinter as tk
from GUI import DEFAULT_FONT, DEFAULT_FONT_SIZE, DEFAULT_BUTTON_WIDTH


def create_image_label(frame, widget_name: str, image_path: str):
    """

    :param frame:
    :param widget_name:
    :param image_path:
    :return:
    """
    projected_image = tk.PhotoImage(file=image_path)
    created_image = tk.Label(frame, image=projected_image, name=widget_name)
    created_image.image = projected_image


def update_image_label(frame, widget_name: str, image_path: str):
    """

    :param frame:
    :param widget_name:
    :param image_path:
    :return:
    """
    projected_image = tk.PhotoImage(file=image_path)
    frame.children[widget_name].config(image=projected_image)
    frame.children[widget_name].image = projected_image


def create_text_label(frame, widget_name: str, message: str, font_style: str = DEFAULT_FONT,
                      font_size: int = DEFAULT_FONT_SIZE, **additional_attribute):
    """

    :param frame:
    :param widget_name:
    :param message:
    :param font_style:
    :param font_size:
    :return:
    """
    tk.Label(frame, text=message, font=(font_style, font_size), name=widget_name, **additional_attribute)


def create_user_entry(frame, widget_name: str, box_width: int, font_style: str = DEFAULT_FONT,
                      font_size: int = DEFAULT_FONT_SIZE):
    """

    :param frame:
    :param widget_name:
    :param box_width:
    :param font_style:
    :param font_size:
    :return:
    """
    tk.Entry(frame, font=(font_style, font_size), width=box_width, name=widget_name).focus_set()


def create_click_button(frame, widget_name: str, message: str, button_width: int = DEFAULT_BUTTON_WIDTH,
                        font_style: str = DEFAULT_FONT, font_size: int = DEFAULT_FONT_SIZE,  **extra_setting):
    """

    :param frame:
    :param widget_name:
    :param message:
    :param button_width:
    :param font_style:
    :param font_size:
    :return:
    """
    tk.Button(frame, text=message, font=(font_style, font_size), width=button_width, name=widget_name, **extra_setting)


def attach_button_function_call(button_name, callable_function):
    button_name.config(command=callable_function)

