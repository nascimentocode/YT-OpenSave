import flet as ft
from pages.home import HomePage
from pages.settings import SettingsPage

def main(page: ft.Page):
    app = HomePage(page)

    def route_change(route):
        page.views.clear()
        page.views.append(SettingsPage(page, app) if page.route == "/settings" else app)
        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == '__main__':
    ft.app(target=main)