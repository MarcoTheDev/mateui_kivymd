"""
Mate UI

Usage: python -m app
"""

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (700, 900)

class MateUI(MDApp):
    """Main App"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu = None

    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "800"
        self.create_app_menu()
        return Builder.load_file(filename="app_design.kv")

    def create_app_menu(self):
        """_summary_"""

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Switch App Theme",
                "height": dp(42),
                "on_release": lambda x=f"Item {i}": self.menu_callback(),
            } for i in range(1)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
        )

    def switch_app_menu_color(self):
        """_summary_"""

        if self.theme_cls.theme_style == "Dark":
            for item in self.menu.items:
                item.update({"theme_text_color": "Custom"})
                item.update({"text_color": "white"})
        else:
            for item in self.menu.items:
                item.update({"theme_text_color": "Secondary"})
                item.update({"text_color": "black"})

    def callback(self, button):
        """_summary_
        Args:
            button (_type_): _description_
        """

        self.menu.caller = button
        self.menu.open()

    def menu_callback(self):
        """_summary_

        Args:
            text_item (_type_): _description_

        Returns:
            _type_: _description_
        """

        self.menu.dismiss()
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.root.ids.mate_label.theme_text_color = "Secondary"
            self.root.ids.notice.theme_text_color = "Secondary"
            self.root.ids.root_card.md_bg_color = self.theme_cls.bg_light
            self.switch_app_menu_color()
        else:
            self.theme_cls.theme_style = "Dark"
            self.root.ids.mate_label.theme_text_color = "Custom"
            self.root.ids.mate_label.text_color = "white"
            self.root.ids.notice.theme_text_color = "Custom"
            self.root.ids.notice.text_color = "white"
            self.root.ids.root_card.md_bg_color = self.theme_cls.bg_dark
            self.switch_app_menu_color()

MateUI().run()
