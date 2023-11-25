#!/usr/bin/env python3

import sys
from cast import HomeDeviceCast
from config import Config
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

class PlayerException (Exception):
   """Custom player exception"""

class VinylPlayer:

    def __init__(self, config_file: str):
      self.config = Config(config_file)

    @property
    def cast(self):
      return HomeDeviceCast(self.config.cast)

    @property
    def albums(self):
      return self.config.albums

    def get_album_by_id(self, id):
      album = self.albums.get(str(id), None)

      if album is None:
          return None

      media_id = album.get("media_id", None)
      playlist_id = album.get("playlist_id", None)

      if not (media_id or not playlist_id):
          return None

      return (media_id, playlist_id)

    def play_album(self, id):
      album = self.get_album_by_id(id)

      if album is None:
          raise PlayerException(f"Album ({id}) not found or invalid")

      try:
        self.cast.play_media(*album)
      except Exception as e:
        raise PlayerException(f"Error playing album: {e}")

    def run(self):
        print("Starting Vinyl Player")

        while True:
          reader = SimpleMFRC522()
          try:
              id, text = reader.read()
              self.play_album(id)
          except PlayerException as e:
              print("Error: {}", e)
          finally:
            GPIO.cleanup()

          sleep(5)

def main():
  if len(sys.argv) < 2:
    print("Usage: python vinyl-player <config_file>")
    exit(1)

  config_file = sys.argv[1]
  app = VinylPlayer(config_file)
  app.run()

if __name__ == '__main__':
  main()
