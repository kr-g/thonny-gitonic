from thonny.ui_utils import select_sequence
from thonny import get_workbench
from tkinter import messagebox
import os
import configparser

VERSION = "v0.0.3-develop"

# import subprocess


def open_config():
    cfg = configparser.ConfigParser(allow_no_value=True)
    cfg.read_dict({"DEFAULT": {"path": "."}})

    fnam = os.path.join("~", ".gitonic", "thonnycontrib.cfg")
    fnam = os.path.expanduser(fnam)

    try:
        with open(fnam) as f:
            cfg.read_string(f.read())
    except Exception as ex:
        print("defaulting. file not found.", ex)
        messagebox.showerror("internal error", fnam + " " + str(ex))
    return cfg


def open_gitonic():

    cfg = open_config()
    fp = cfg["DEFAULT"]["path"]

    fp = os.path.join(fp, "gitonic")
    fp = os.path.expanduser(fp)

    fnam = fp + " &"

    try:
        # this will log to the same console like thonny
        # todo
        print("running", fnam)
        os.system(fnam)
        # subprocess.Popen(["gitonic"],creationflags=0)
    except Exception as ex:
        messagebox.showerror(
            "internal error", "could not start gitonic " + str(ex))


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
        messagebox.showerror(
            "internal error", "could not start gitonic plugin")
