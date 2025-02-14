import flet as ft
from components.appbar import AppBar
from utils.settings_manager import save_settings, load_settings
from components.pick_folder import pick_folder

class SettingsPage(ft.View):
    def __init__(self, page: ft.Page, app):
        super().__init__(route="/settings", scroll=ft.ScrollMode.AUTO)
        self.page = page
        self.app = app

        self.settings = load_settings()

        self.appbar = AppBar(self.page)

        self.theme_switch = ft.Switch(
            label="Modo Escuro",
            value=self.page.theme_mode == ft.ThemeMode.DARK,
            on_change=self.change_theme
        )

        self.download_path_text = ft.Text(f"Diretório para download: {self.settings['download_path']}")

        self.choose_dir_btn = ft.CupertinoButton(
            content=ft.Row([
                ft.Icon(name=ft.Icons.FOLDER_OPEN, color=ft.Colors.WHITE, size=17),
                # ft.Text(value="Escolher Diretório", color=ft.Colors.WHITE, size=12),
            ]),
            bgcolor='#8b2c1d',
            padding=ft.padding.symmetric(vertical=15, horizontal=30),
            tooltip="Escolher Diretório",
            on_click=self.choose_directory
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
                    ft.Row(controls=[self.choose_dir_btn, self.download_path_text]),
                    ft.CupertinoButton(
                        content=ft.Text(value="Salvar Configurações", color=ft.Colors.WHITE),
                        bgcolor='#8b2c1d',
                        padding= ft.padding.symmetric(vertical=15, horizontal=30),
                        on_click=self.save_settings
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START
            )
        ]

    def go_home(self, e):
        self.page.go("/")

    def choose_directory(self, e):
        folder_selected = pick_folder()
        if folder_selected:
            self.settings["download_path"] = folder_selected
            self.download_path_text.value = f"Diretório atual: {folder_selected}"
            self.page.update()

    def change_theme(self, e):
        self.appbar.switch_theme(e)

    def save_settings(self, e):
        self.settings["theme"] = "dark" if self.theme_switch.value else "light"
        save_settings(self.settings)

        self.page.snack_bar = ft.SnackBar(ft.Text("Configurações salvas com sucesso!"))
        self.page.snack_bar.open = True
        self.page.update()