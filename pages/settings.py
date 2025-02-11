import flet as ft
from components.appbar import AppBar

class SettingsPage(ft.View):
    def __init__(self, page: ft.Page, app):
        super().__init__(route="/settings", scroll=ft.ScrollMode.AUTO)
        self.page = page
        self.app = app
        self.is_dark_mode = self.page.theme_mode == ft.ThemeMode.DARK

        # self.app.apply_theme(self.page)

        self.appbar = AppBar(self.page)

        self.controls = [
            self.appbar,
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=self.go_home),
                            ft.Text(value="Opções de Configuração", size=20, weight=ft.FontWeight.BOLD),
                        ],
                        spacing=10
                    ),
                    ft.Switch(label="Modo Escuro", on_change=self.change_theme, value=self.is_dark_mode),
                    ft.ElevatedButton(text="Salvar Configurações", on_click=self.save_settings),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START
            )
        ]

        # if self.page:
        #     self.appbar.update_icon()

    def go_home(self, e):
        self.page.go("/")

    def change_theme(self, e):
       self.appbar.switch_theme(e)

    def save_settings(self, e):
        print("Configurações salvas!")