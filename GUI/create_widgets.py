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
    :raise AttributeError: if frame is not a tkinter frame
    :raise KeyError: if widget_name already exists in the specific frame
    :raise TypeError: if widget_name or/and image_path is not a string type
    :raise _tkinter.TclError: if the directory represented by image_path does not exist
    """
    if type(widget_name) is not str or type(image_path) is not str:
        raise TypeError(f"Label Name & Image Path must a string.")
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
    :precondition: tkinter root window must exist and contain at least one frame
    :precondition: frame_object must be an existing tkinter frame that contains the label represented by widget_name
    :precondition: label_name must be a string that represents a unique name of the label
    :precondition: image_directory must be a string that is a file path
    :precondition: image_directory must represent an existing image in the specific directory
    :postcondition: update the image of  a tkinter label represented by the provided path in a tkinter frame.
    :raise AttributeError: if frame_object is not a tkinter frame
    :raise KeyError: if label_name does not exist in the specific frame
    :raise TypeError: if label_name or/and image_directory is not a string type
    :raise _tkinter.TclError: if the directory represented by image_directory does not exist
    """
    if type(label_name) is not str:
        raise TypeError(f"Label Name must a string.")
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
    :precondition: DEFAULT_FONT must exist be defined
    :precondition: font_size must represent an integer that represents a font size. Default as DEFAULT_FONT_SIZE
    :precondition: DEFAULT_FONT_SIZE must be defined
    :postcondition: create a tkinter label that contains image represented by the provided path in a tkinter frame
    :raise NameError: if DEFAULT_FONT and/or DEFAULT_FONT_SIZE is not defined
    :raise _tkinter.TclError: if the key of **additional_attribute is not a valid option for tkinter Label function
    :raise AttributeError: if frame_obj is not a tkinter frame
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


def create_user_entry(upper_frame, widget_id: str, box_width: int, entry_font_style: str = DEFAULT_FONT,
                      entry_font_size: int = DEFAULT_FONT_SIZE):
    """
    Create a tkinter entry for player's input in a tkinter frame.

    :param upper_frame: a tkinter frame that allows for adding entry widget in an existed root window
    :param widget_id: a string that represents the name of the creating entry box
    :param box_width: an integer that indicates the width of the entry box
    :param entry_font_style: a string that represents a windows built-in font style. Default as DEFAULT_FONT
    :param entry_font_size: an integer that represents a font size. Default as DEFAULT_FONT_SIZE
    :precondition: tkinter root window must exist and contain at least one frame
    :precondition: upper_frame must be an existing tkinter frame created for containing entry box
                   in a tkinter root window
    :precondition: widget_id must be a string that represents a unique name of the label
    :precondition: entry_font_style must represent an existing window built-in font style. Default as DEFAULT_FONT
    :precondition: DEFAULT_FONT must exist in the __init__.py in GUI package
    :precondition: entry_font_size must represent an integer that represents a font size. Default as DEFAULT_FONT_SIZE
    :precondition: DEFAULT_FONT_SIZE must exist in the __init__.py in GUI package
    :postcondition: create a tkinter entry for player's input in a tkinter frame
    :raise RuntimeError: if tkinter root window has not been defined
    :raise KeyError: if widget_id already exists in the specific frame
    :raise TypeError: if widget_id and/or entry_font_style is not a string type
    :raise _tkinter.TclError: if the key of **additional_attribute is not a valid option for tkinter Label function
    :raise ValueError: if box_width and/or entry_font_size is not a non-zero positive integer
    :raise AttributeError: if upper_frame is not a tkinter frame
    """
    if type(box_width) is not int or box_width <= 0 or type(entry_font_size) is not int or entry_font_size <= 0:
        raise ValueError(f"Box Width & Font Size must be a non-zero positive integer")
    if type(entry_font_style) is not str or type(widget_id) is not str:
        raise TypeError(f"Font Style & Label Name must a string.")
    if True in [widget_id == widget.winfo_name() for widget in upper_frame.winfo_children()]:
        raise KeyError(f"The widget name {widget_id} is taken in this {upper_frame} frame. Check for duplication.")
    tk.Entry(upper_frame, font=(entry_font_style, entry_font_size), width=box_width, name=widget_id).focus_set()


def create_click_button(belonging_frame, widget_name_id: str, message: str, button_width: int = DEFAULT_BUTTON_WIDTH,
                        button_font_style: str = DEFAULT_FONT, button_font_size: int = DEFAULT_FONT_SIZE,
                        **extra_setting):
    """
    Create a tkinter button for player to click in a tkinter frame.

    :param belonging_frame: a tkinter frame that allows for adding entry widget in an existed root window
    :param widget_name_id: a string that represents the name of the creating entry box
    :param message: a string that represents the desired text to display on the click button
    :param button_width: an integer that indicates the width of the button
    :param button_font_style: a string that represents a windows built-in font style. Default as DEFAULT_FONT
    :param button_font_size: an integer that represents a font size. Default as DEFAULT_FONT_SIZE
    :precondition: tkinter root window must exist and contain at least one frame
    :precondition: belonging_frame must be an existing tkinter frame created for containing entry box
                   in a tkinter root window
    :precondition: widget_name_id must be a string that represents a unique name of the label
    :precondition: button_font_style must represent an existing window built-in font style. Default as DEFAULT_FONT
    :precondition: DEFAULT_FONT must exist in the __init__.py in GUI package
    :precondition: button_font_size must represent an integer that represents a font size. Default as DEFAULT_FONT_SIZE
    :precondition: DEFAULT_FONT_SIZE must exist in the __init__.py in GUI package
    :postcondition: create a tkinter button for player to click in a tkinter frame
    :raise RuntimeError: if tkinter root window has not been defined
    :raise KeyError: if widget_name_id already exists in the specific frame
    :raise TypeError: if widget_name_id, button_font_style and/or message is not a string type
    :raise _tkinter.TclError: if the key of **extra_setting is not a valid option for tkinter click function
    :raise ValueError: if button_width and/or button_font_size is not a non-zero positive integer
    :raise AttributeError: if belonging_frame is not a tkinter frame
    """
    if type(button_font_size) is not int or button_font_size <= 0 or type(button_width) is not int or button_width <= 0:
        raise ValueError(f"Font Size & Button Width must be a non-zero positive integer.")
    if type(button_font_style) is not str or type(widget_name_id) is not str or type(message) is not str:
        raise TypeError(f"Font Style, Widget Name & Message must a string.")
    if True in [widget_name_id == widget.winfo_name() for widget in belonging_frame.winfo_children()]:
        raise KeyError(f"The widget name {widget_name_id} is taken in {belonging_frame} frame. Check for duplication.")
    tk.Button(belonging_frame, text=message, font=(button_font_style, button_font_size),
              width=button_width, name=widget_name_id, **extra_setting)


def attach_button_function_call(button_name, callable_function):
    """
    Attach a function to a button.

    :param button_name: an existing tkinter button object
    :param callable_function: a callable function that exists
    :precondition: button_name must be an existing tkinter button object
    :precondition: callable_function must be a callable function or None type
    :postcondition: attach callable function to a button
    :raise TypeError: if callable_function is not a callable function or None type
    :raise AttributeError: if button_name is not a tkinter button
    """
    if not callable(callable_function) and None:
        raise TypeError("callable_function must be a callable function!")
    button_name.config(command=callable_function)
