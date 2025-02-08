import flet as ft
from components.appbar import AppBar

class SettingsPage(ft.View):
    def __init__(self, page: ft.Page, app):
        super().__init__(route="/settings", scroll=ft.ScrollMode.AUTO)
        self.page = page
        self.app = app

        self.appbar = AppBar(self.page, self.app)

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
                    ft.Switch(label="Modo Escuro", on_change=self.switch_theme),
                    ft.ElevatedButton(text="Salvar Configurações", on_click=self.save_settings),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START
            )
        ]

    def switch_theme(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )

        self.page.update()

    def go_home(self, e):
        self.page.go("/")

    def save_settings(self, e):
        print("Configurações salvas!")