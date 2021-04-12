#!/usr/bin/env python3
# encoding: utf-8
"""
A desktop app written in Python, that unlocks the power of Optimize Images in a
graphical user interface, to help you reduce the file size of images.

© 2021 Victor Domingos, MIT License
"""
import platform
import tkinter as tk
from tkinter import ttk

from optimize_images_x.db.app_settings import AppSettings
from optimize_images_x.db.base import initialize
from optimize_images_x.db.task_settings import TaskSettings
from optimize_images_x.global_setup import APP_NAME, DB_PATH
from optimize_images_x.gui.app_status import AppStatus
from optimize_images_x.gui.main_window import App


def main():
    initialize(DB_PATH, platform.system())
    app_status = AppStatus()
    app_settings = AppSettings(DB_PATH)
    task_settings = TaskSettings(DB_PATH)
    root = tk.Tk()
    app_status.main_window = App(root, app_status, app_settings, task_settings)
    global_style = ttk.Style(root)
    #global_style.theme_use('clam')
    #global_style.theme_use('classic')
    global_style.theme_use(app_settings.app_style)
    root.configure(background='grey95')
    root.title(APP_NAME)
    x = app_settings.main_window_x
    y = app_settings.main_window_y
    width = app_settings.main_window_w
    height = app_settings.main_window_h
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.bind_all("<Mod2-q>", root.quit)
    root.bind("<Configure>", app_status.main_window.update_window_status)
    root.mainloop()


if __name__ == "__main__":
    main()
