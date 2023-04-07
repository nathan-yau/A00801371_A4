import tkinter as tk
from GUI import DEFAULT_FONT, DEFAULT_FONT_SIZE, DEFAULT_BUTTON_WIDTH


def create_image_label(frame, widget_name: str, image_path: str):
    """
    Create a tkinter label that contains image represented by the provided path in a tkinter frame.

    :param frame: a tkinter frame that allows for adding label widget in an existed root window
    :param widget_name: a string that represents the name of the creating label
    :param image_path: a string that represents an existing image in the specific directory
    :precondition: tkinter root window must exist and contain at least one frame
    :precondition: frame must be an existing tkinter frame created for containing labels and buttons
                   in a tkinter root window
    :precondition: widget_name must be a string that represents a unique name of the label
    :precondition: image_path must be a string that is a file path
    :precondition: image_path must represent an existing image in the specific directory
    :postcondition: create a tkinter label that contains image represented by the provided path in a tkinter frame
    :raise RuntimeError: if tkinter root window has not been defined
    :raise _tkinter.TclError: if frame is not a tkinter frame or does not exist in the tkinter root window
    :raise KeyError: if widget_name already exists in the specific frame
    :raise TypeError: if widget_name or/and image_path is not a string type
    :raise FileNotFoundError: if the directory represented by image_path does not exist
    """
    if type(widget_name) is not str:
        raise TypeError(f"Label Name & Message must a string.")
    if True in [widget_name == widget.winfo_name() for widget in frame.winfo_children()]:
        raise KeyError(f"The widget name {widget_name} is taken in this {frame} frame. Check for duplication.")
    projected_image = tk.PhotoImage(file=image_path)
    created_image = tk.Label(frame, image=projected_image, name=widget_name)
    created_image.image = projected_image


def update_image_label(frame_object, label_name: str, image_directory: str):
    """
    Update the image of a tkinter label represented by the provided path in a tkinter frame.

    :param frame_object: a tkinter frame that contains the label represented by widget_name
    :param label_name: a string that represents the name of an existing label in frame
    :param image_directory: a string that represents an existing image in the specific directory
    :precondition: frame_object must be an existing tkinter frame that contains the label represented by widget_name
    :precondition: label_name must be a string that represents a unique name of the label
    :precondition: image_directory must be a string that is a file path
    :precondition: image_directory must represent an existing image in the specific directory
    :postcondition: update the image of  a tkinter label represented by the provided path in a tkinter frame.
    :raise RuntimeError: if tkinter root window has not been defined
    :raise _tkinter.TclError: if frame_object is not a tkinter frame or does not exist in the tkinter root window
    :raise KeyError: if label_name does not exist in the specific frame
    :raise TypeError: if label_name or/and image_directory is not a string type
    :raise FileNotFoundError: if the directory represented by image_directory does not exist
    """
    projected_image = tk.PhotoImage(file=image_directory)
    frame_object.children[label_name].config(image=projected_image)
    frame_object.children[label_name].image = projected_image


def create_text_label(frame_obj, text_label_name: str, message: str, font_style: str = DEFAULT_FONT,
                      font_size: int = DEFAULT_FONT_SIZE, **additional_attribute):
    """
    Create a tkinter label that contains image represented by the provided path in a tkinter frame.

    :param frame_obj: a tkinter frame that allows for adding label widget
    :param text_label_name: a string that represents the name of the creating text label
    :param message: a string that represents the desired text to display on the label
    :param font_style: a string that represents a windows built-in font style. Default as DEFAULT_FONT
    :param font_size: an integer that represents a font size. Default as DEFAULT_FONT_SIZE
    :param additional_attribute: an arbitrary KW Args that represents a key-value pair tk.Label function accepts
    :precondition: frame_obj must be an existing tkinter frame object created for containing labels
    :precondition: text_label_name must be a string that represents a unique name of the label
    :precondition: message must be a string
    :precondition: font_style must represent an existing window built-in font style. Default as DEFAULT_FONT
    :precondition: DEFAULT_FONT must exist in the __init__.py in GUI package
    :precondition: font_size must represent an integer that represents a font size. Default as DEFAULT_FONT_SIZE
    :precondition: DEFAULT_FONT_SIZE must exist in the __init__.py in GUI package
    :postcondition: create a tkinter label that contains image represented by the provided path in a tkinter frame
    :raise RuntimeError: if tkinter root window has not been defined
    :raise _tkinter.TclError: if frame is not a tkinter frame or does not exist in the tkinter root window
                              if the key of **additional_attribute is not a valid option for tkinter Label function
                              if font_style is not a string
    :raise TypeError: if font_style, text_label_name and/or message is not a string
    :raise KeyError: if text_label_name already exists in the specific frame
    :raise ValueError: if font_size is not a non-zero positive integer
    """
    if type(font_style) is not str or type(text_label_name) is not str or type(message) is not str:
        raise TypeError(f"Font Style & Label Name & Message must a string.")
    if type(font_size) is not int or font_size <= 0:
        raise ValueError(f"Font Size must be a non-zero positive integer.")
    if True in [text_label_name == widget.winfo_name() for widget in frame_obj.winfo_children()]:
        raise KeyError(f"The widget name {text_label_name} is taken in this {frame_obj} frame. Check for duplication.")
    tk.Label(frame_obj, text=message, font=(font_style, font_size), name=text_label_name, **additional_attribute)


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

