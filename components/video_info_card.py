import flet as ft
from math import ceil

from utils.downloader import VideoDownloader

class VideoInfoCard(ft.Card):
    def __init__(self, page, app):
        super().__init__(visible=False, width=900)
        self.page = page
        self.app = app
        self.video_downloader = VideoDownloader(self.page, self.app)

        self.thumbnail = ft.Image(src='', width=350, height=200, fit=ft.ImageFit.CONTAIN)
        self.title = ft.Text(value='', size=17, style=ft.TextStyle.baseline)
        self.uploaderSpan = ft.TextSpan(
            text='',
            style=ft.TextStyle(
                color=ft.Colors.BLUE,
                decoration=ft.TextDecoration.UNDERLINE,
                size=17
            ),
            url='',
            url_target=ft.UrlTarget.BLANK
        )

        self.uploader = ft.Text(
            value='Uploader: ',
            weight=ft.FontWeight.W_500,
            spans=[self.uploaderSpan],
            size=17
        )

        self.videoInfo = ft.Container(
            content=ft.Column(
                controls=[self.title, self.uploader],
                width=350
            )
        )

        self.availableFormats = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text('Qualidade')),
                ft.DataColumn(ft.Text('Tamanho')),
                ft.DataColumn(ft.Text('Ação'))
            ],
            rows=[]
        )

        self.content = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[self.thumbnail, self.videoInfo],
                        spacing=5,
                    ),
                    ft.Column(
                        controls=[self.availableFormats],
                    )
                ],
                spacing=35,
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            padding=35
        )

    def update_info(self, videoInfo):
        self.thumbnail.src = videoInfo.get('thumbnail', '')
        self.title.value = videoInfo.get("title", "Título não encontrado")
        self.uploaderSpan.text = videoInfo.get('uploader', 'Não encontrado')
        self.uploaderSpan.url = videoInfo.get('uploader_url', '')
        self.visible = True

        self.page.update()

    def update_formats(self, videoInfo):
        if not videoInfo or 'formats' not in videoInfo:
            print("Erro: Informações de formato não disponíveis.")
            return

        formats = videoInfo.get('formats', [])
        self.availableFormats.rows.clear()

        best_formats = {}

        for format in formats:
            filesize = format.get('filesize', 0)
            quality = format.get('resolution', '')
            ext = format.get('ext', '').upper()

            if filesize and quality != 'audio only' and ext == 'MP4':
                qualityKey = f'{ext} {quality.split("x")[1]}p'

                if qualityKey not in best_formats or filesize > best_formats[qualityKey]['filesize']:
                    best_formats[qualityKey] = {
                        "format_id": format.get('format_id'),
                        "filesize": filesize,
                        "quality": qualityKey
                    }

        for qualityKey, data in best_formats.items():
            filesize_str = f'{ceil(data["filesize"] / 1048576)} MB'

            self.availableFormats.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(qualityKey)),
                        ft.DataCell(ft.Text(filesize_str)),
                        ft.DataCell(ft.FilledButton(
                            text='Download',
                            icon=ft.Icons.DOWNLOAD,
                            bgcolor='#8b2c1d',
                            color=ft.Colors.WHITE,
                            on_click=lambda e, f=data["format_id"]: self.video_downloader.download_video(f),
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), icon_size=16))
                        )
                    ],
                ),
            )

            self.page.update()