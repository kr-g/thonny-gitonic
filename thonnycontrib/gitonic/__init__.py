try:
    from thonny.ui_utils import select_sequence
    from thonny import get_workbench
except:
    pass

from tkinter import messagebox
import os
import configparser
import shlex

VERSION = "v0.0.3-develop"

# import subprocess


def open_config():
    cfg = configparser.ConfigParser(allow_no_value=True)
    cfg.read_dict(
        {"DEFAULT": {"path": "", "start": "gitonic", "param": ""}})

    fnam = os.path.join("~", ".gitonic", "thonnycontrib.cfg")
    fnam = os.path.expanduser(fnam)

    try:
        with open(fnam) as f:
            cfg.read_string(f.read())
    except Exception as ex:
        print("defaulting. file not found.", ex)
        messagebox.showerror("internal error", fnam + " " + str(ex))
    return cfg


def get_args():

    cfg = open_config()

    proc = cfg["DEFAULT"]["path"].strip()
    proc = os.path.expanduser(proc)
    if (proc == "."):
        proc = ""

    cmd = cfg["DEFAULT"]["start"].strip()
    cmd = os.path.expanduser(cmd)

    if (len(proc) > 0):
        cmd = os.path.join(proc, cmd)

    para = cfg["DEFAULT"]["param"].strip()
    para = os.path.expanduser(para)

    cmdline = " ".join([cmd, para])

    args = shlex.split(cmdline)
    return args


def open_gitonic():

    args = get_args()

    try:
        # this will log to the same console like thonny
        # todo
        print("pwd", os.path.abspath(os.curdir))
        print("running", args)

        # todo
        import subprocess
        rc = subprocess.Popen(args)
        print("started", rc)

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


if __name__ == "__main__":
    args = get_args()
    print(args)
    # open_gitonic()
