import yt_dlp
import flet as ft
import re

from utils.settings_manager import load_settings

class VideoDownloader:
    def __init__(self, page, app):
        self.page = page
        self.app = app
        self.settings = load_settings()

    def is_valid_youtube_url(self, url):
        youtube_regex = re.compile(
            r"^(https?://)?(www\.)?"
            r"(youtube\.com|youtu\.be)/"
        )

        return bool(youtube_regex.match(url))

    def progress_hook(self, d):
        status = d['status']
        if status == 'downloading':
            self.app.progressDownload.visible = True
            self.app.progressDownloadLabel.value = 'Download do video em progresso'
            self.app.progressDownload.value = float(d['_percent_str'].strip('%')) / 100
            self.app.infoDownloadLabel.value = f'{d['_percent_str']}  {d['_speed_str']}  {d['_eta_str']}'
        elif status == 'finished':
            self.app.progressDownloadLabel.value = 'Download do video finalizado, agora pos-processando ...'
            self.app.progressDownload.value = 1
        else:
            self.app.progressDownloadLabel.value = 'Erro no download!'

        self.page.update()

    def fetch_video_info(self, url):
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                return True, info
        except Exception as err:
            return False, None

    def download_video(self, format_id):
        url = self.app.urlTextField.value
        download_path = self.settings["download_path"]
        self.app.searchBtn.disabled = True

        for row in self.app.video_info_card.availableFormats.rows:
            for cell in row.cells:
                if isinstance(cell.content, ft.FilledButton):
                    cell.content.disabled = True
                    cell.content.bgcolor = '#B0B0B0'

        self.page.update()

        ydl_opts = {
            "format": format_id+"+bestaudio",  # Better separate video and audio
            "progress_hooks": [self.progress_hook],  # Call progress_hook at each step
            "merge_output_format": "mp4",  # Merge audio and video in MP4
            "outtmpl": f"{download_path}/%(title)s.%(ext)s",  # File name based on title
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as err:
            self.app.progressDownloadLabel.value = f'Erro ao baixar o vídeo: {str(err)}'
        finally:
            self.app.searchBtn.disabled = False

            for row in self.app.video_info_card.availableFormats.rows:
                for cell in row.cells:
                    if isinstance(cell.content, ft.FilledButton):
                        cell.content.disabled = False
                        cell.content.bgcolor = '#8b2c1d'
                        cell.content.color = ft.Colors.WHITE

            self.page.update()