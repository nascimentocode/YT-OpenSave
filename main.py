import flet as ft
from pages.home import HomePage
from pages.settings import SettingsPage
from utils.settings_manager import load_settings

def main(page: ft.Page):
    settings = load_settings()

    page.theme_mode = ft.ThemeMode.DARK if settings.get("theme") == "dark" else ft.ThemeMode.LIGHT

    app = HomePage(page)

    def route_change(route):
        page.views.clear()

        if page.route == "/settings":
            page.views.append(SettingsPage(page, app))
        else:
            page.views.append(app)

        page.update()

        # # hasattr() -> Verificando se appbar ja esta na HomePage
        # if hasattr(app, "appbar") and app.appbar is not None:
        #     app.appbar.update_icon()

    page.on_route_change = route_change
    page.go("/")

if __name__ == '__main__':
    ft.app(target=main)