import pygame
from PyCleanUI.Window import Window
from PyCleanUI.Widgets.Text import Text
from PyCleanUI.Widgets.Button import Button

layout = [
    Text("Search Folder:"),
    [Text("'C:/Desktop'"), Button("Browse")],
    Button("Browsee")
]

window = Window("Hello world", layout)

while window.is_running():
    window.loop()
    if window.get_event() is not None:
        print(window.get_event())

window.close()
