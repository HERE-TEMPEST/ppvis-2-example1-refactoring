from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.config import Config


Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class TicTackToe(App):
    def __init__(self, controller):
        super().__init__()
        self.buttons = []
        self.button_restart = None

        self.controller = controller
        self.controller.init_viewer(self)


    def build(self):
        self.title = "Tic Tack Toe"

        root = BoxLayout(orientation="vertical", padding=5)

        grid = GridLayout(cols=3)

        for _ in range(9):
            button = Button(
                color=[0, 0, 0, 1],
                font_size=24,
                disabled=False,
                on_press=self.controller.tic_tac_toe
            )
            self.buttons.append(button)
            grid.add_widget(button)

        root.add_widget(grid)

        self.button_restart = Button(
                text="Restart",
                size_hint=[1, .1],
                on_press=self.controller.restart
        )

        root.add_widget(self.button_restart)

        return root

