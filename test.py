import pygame
from PyCleanUI.Window import Window
from PyCleanUI.Widgets.Text import Text
from PyCleanUI.Widgets.Button import Button

layout = [
    Text("Search Folder:"),
    [Text("'C:/Desktop'"), Button("Browse")]
]

window = Window("Hello world", layout)

window.close()
