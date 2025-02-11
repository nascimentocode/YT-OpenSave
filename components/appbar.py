import flet as ft

class AppBar(ft.AppBar):
    def __init__(self, page):
        self.page = page
        self.is_dark_mode = self.page.theme_mode == ft.ThemeMode.DARK
        # self.theme_icon = ft.Icons.WB_SUNNY_ROUNDED if self.is_dark_mode else ft.Icons.NIGHTLIGHT_ROUNDED

        super().__init__(
            leading=ft.Icon(ft.Icons.MOVIE),
            leading_width=40,
            title=ft.Text("YT OpenSave"),
            bgcolor="#8b2c1d",
            actions=[
                # ft.IconButton(icon=self.theme_icon, on_click=self.switch_theme),
                ft.IconButton(icon=ft.Icons.SETTINGS, on_click = lambda e: self.page.go("/settings"))
            ]
        )

    def switch_theme(self, e):
        self.is_dark_mode = not self.is_dark_mode
        self.page.theme_mode = ft.ThemeMode.DARK if self.is_dark_mode else ft.ThemeMode.LIGHT
        # self.update_icon()
        self.page.update()

    # def update_icon(self):
    #     if not self.page or not hasattr(self.page, "views") or len(self.page.views) == 0:
    #         return
    #
    #     self.is_dark_mode = self.page.theme_mode == ft.ThemeMode.DARK
    #     self.actions[0].icon = ft.Icons.WB_SUNNY_ROUNDED if self.is_dark_mode else ft.Icons.NIGHTLIGHT_ROUNDED
    #
    #     if self in self.page.views[-1].controls:
    #         self.update()