import flet as ft
from components.appbar import AppBar
from components.video_info_card import VideoInfoCard
from utils.downloader import VideoDownloader

class HomePage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/", scroll=ft.ScrollMode.AUTO, padding=50)
        self.page = page
        self.page.title = 'YT OpenSave'
        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.video_downloader = VideoDownloader(self.page, self)
        self.video_info_card = VideoInfoCard(self.page, self)

        self.appbar = AppBar(self.page)

        self.title = ft.Text(
            value='Downloader Video YouTube',
            theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
            weight=ft.FontWeight.W_500
        )

        self.urlTextField = ft.CupertinoTextField(
            placeholder_text='Insira o link do video',
            text_size=17,
            padding=ft.padding.symmetric(vertical=13, horizontal=15),
            width=550
        )

        self.searchBtn = ft.CupertinoButton(
            content=ft.Icon(name=ft.Icons.SEARCH, color=ft.Colors.WHITE),
            bgcolor='#8b2c1d',
            on_click=self.show_info,
            tooltip="Buscar vídeo"
        )

        self.progressDownloadLabel = ft.Text(
            value='',
            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
            weight=ft.FontWeight.NORMAL
        )

        self.progressDownload = ft.ProgressBar(
            width=400,
            color=ft.Colors.LIGHT_GREEN_ACCENT_700,
            visible=False
        )

        self.infoDownloadLabel = ft.Text(
            value='',
            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
            weight=ft.FontWeight.NORMAL
        )

        self.controls = [
            self.appbar,
            ft.Column(controls=[
                self.title,
                ft.Row(controls=[
                    self.urlTextField,
                    self.searchBtn,
                ], alignment=ft.MainAxisAlignment.CENTER, wrap=True),
                ft.Divider(),
                self.video_info_card,
                ft.Row(controls=[
                    self.progressDownloadLabel,
                    self.progressDownload,
                    self.infoDownloadLabel,
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=50)
        ]

    def show_info(self, e):
        self.reset_progress()

        url = self.urlTextField.value
        if not url:
            self.reset_progress()
            self.progressDownloadLabel.value = 'Por favor, insira uma URL válida.'
            self.page.update()
            return

        sucess, videoInfo = self.video_downloader.fetch_video_info(url)
        if not sucess:
            self.reset_progress()
            self.progressDownloadLabel.value = 'Erro ao buscar o vídeo.'
            self.page.update()
            return

        self.video_info_card.update_info(videoInfo)
        self.video_info_card.update_formats(videoInfo)

        if self.video_info_card.availableFormats.rows:
            self.video_info_card.visible = True
        else:
            self.reset_progress()
            self.progressDownloadLabel.value = 'Erro, não é possível baixar esse vídeo'

        self.page.update()

    def reset_progress(self):
        self.searchBtn.disabled = False
        self.progressDownload.visible = False
        self.progressDownload.value = 0
        self.video_info_card.visible = False
        self.infoDownloadLabel.value = ''
        self.progressDownloadLabel.value = ''

    # def apply_theme(self, target_page):
    #     target_page.theme_mode = self.page.theme_mode
    #     target_page.update()