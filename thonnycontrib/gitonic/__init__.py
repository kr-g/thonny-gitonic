import os

VERSION = "v0.0.1"

# import subprocess

from tkinter import messagebox

from thonny import get_workbench
from thonny.ui_utils import select_sequence


def open_gitonic():
    try:
        # this will log to the same console like thonny
        # todo
        os.system("gitonic &")
        # subprocess.Popen(["gitonic"],creationflags=0)
    except Exception as ex:
        print(ex)
        messagebox.showerror("internal error", "could not start gitonic")


def load_plugin():
    try:
        get_workbench().add_command(
            command_id="gitonic",
            menu_name="tools",
            command_label="gitonic",
            handler=open_gitonic,
            default_sequence=select_sequence("<Control-G>", "<Command-G>"),
        )
    except Exception as ex:
        print(ex)
        messagebox.showerror("internal error", "could not start gitonic plugin<")
