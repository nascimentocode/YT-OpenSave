import flet as ft

class AppBar(ft.AppBar):
    def __init__(self, page, app):
        self.page = page
        self.app = app

        super().__init__(
            leading=ft.Icon(ft.Icons.MOVIE),
            leading_width=40,
            title=ft.Text("YT OpenSave"),
            bgcolor="#8b2c1d",
            actions=[
                ft.IconButton(icon=ft.Icons.NIGHTLIGHT_ROUNDED, on_click=self.app.switch_theme),
                ft.IconButton(icon=ft.Icons.SETTINGS, on_click = lambda e: self.page.go("/settings"))
            ]
        )

    def update_icon(self, is_dark_mode):
        self.actions[0].icon = ft.Icons.WB_SUNNY_ROUNDED if is_dark_mode else ft.Icons.NIGHTLIGHT_ROUNDED
        self.update()