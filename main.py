import flet as ft
from pages.home import HomePage
from pages.settings import SettingsPage

def main(page: ft.Page):
    app = HomePage(page)

    def route_change(route):
        page.views.clear()

        if page.route == "/settings":
            settings_page = SettingsPage(page, app)
            page.views.append(settings_page)
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