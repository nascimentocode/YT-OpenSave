import flet as ft
from components.appbar import AppBar
from utils.settings_manager import save_settings

class SettingsPage(ft.View):
    def __init__(self, page: ft.Page, app):
        super().__init__(route="/settings", scroll=ft.ScrollMode.AUTO)
        self.page = page
        self.app = app

        # self.app.apply_theme(self.page)

        self.appbar = AppBar(self.page)

        self.theme_switch = ft.Switch(
            label="Modo Escuro",
            value=self.page.theme_mode == ft.ThemeMode.DARK,
            on_change=self.change_theme
        )

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
                    self.theme_switch,
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
        print(self.theme_switch)
        save_settings({"theme": "dark" if self.theme_switch.value else "light"})
        self.page.snack_bar = ft.SnackBar(ft.Text("Configurações salvas com sucesso!"))
        self.page.snack_bar.open = True
        self.page.update()