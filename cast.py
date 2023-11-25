from pychromecast import get_listed_chromecasts
from pychromecast.controllers.youtube import YouTubeController

class HomeDeviceCast:

    def __init__(self, config):
        self.config = config
        if self.device_friendly_name is None:
            raise ValueError("Missing device friendly name in cast config")

    @property
    def device_friendly_name(self):
        return self.config.get("device_friendly_name", None)

    def register_cast(self):
        chromecasts, browser = get_listed_chromecasts(friendly_names=[
          self.device_friendly_name
        ])

        if len(chromecasts) == 0:
            raise ValueError(f"Could not find chromecast with friendly name {self.device_friendly_name}")

        self.yt = YouTubeController()
        self.cast = chromecasts[0]
        self.cast.wait()
        self.cast.register_handler(self.yt)
        browser.stop_discovery()


    def play_media(self, media_id, playlist_id):
        self.register_cast()

        self.cast.volume_mute = False
        self.yt.quick_play(media_id, playlist_id)

        print(f"Playing album: {media_id} {playlist_id} on {self.device_friendly_name}")
        print("Cast status: {}", self.cast.status)
