import flet as ft

class AppBar(ft.AppBar):
    def __init__(self, page):
        self.page = page
        self.is_dark_mode = self.page.theme_mode == ft.ThemeMode.DARK

        super().__init__(
            leading=ft.Icon(ft.Icons.MOVIE),
            leading_width=40,
            title=ft.Text("YT OpenSave"),
            bgcolor="#8b2c1d",
            actions=[
                ft.IconButton(icon=ft.Icons.SETTINGS, on_click = lambda e: self.page.go("/settings"))
            ]
        )

    def switch_theme(self, e):
        self.is_dark_mode = not self.is_dark_mode
        self.page.theme_mode = ft.ThemeMode.DARK if self.is_dark_mode else ft.ThemeMode.LIGHT
        self.page.update()