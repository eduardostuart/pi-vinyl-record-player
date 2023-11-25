<img src="./image.png" width="240" align="right" />

# "Vinyl" Record Player

🎶 Vinyl Record Player is a just-for-fun project I made to play music using RFID tags on my Google Home device. The idea is to simulate a record player; don't take it too seriously.

I'm using a Raspberry Pi 3 B.

## How it works

1. The music catalog is defined on `config.toml` file. See [config.toml.example](./config.toml.example) for an example.
2. When someone places an RFID tag on the reader, the music will play on the Google Home device.

Use the command `python discovery.py` to find your device information.

## Hardware

> This is what I'm using. Use whatever you want.

- [Raspberry Pi 3 B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [MFRC522 RC522](https://www.amazon.nl/-/en/dp/B09H6PLM1C?psc=1&ref=ppx_yo2ov_dt_b_product_details)

## Demo

https://www.youtube.com/watch?v=OBsPoJM-FHk

## How to run

Install dependencies:

```sh
pip install -r requirements.txt
```

Then:

```sh
python main.py my-config.toml
```

### Keep it running

Create a service on `/etc/systemd/system/`. For example:

```sh
# cat /etc/systemd/system/vinyl.service
[Unit]
Description=Vinyl Player Service
After=network.target # Wait for the network to be available

[Service]
User=eduardostuart
WorkingDirectory=/home/eduardostuart/vinyl-record-player/
ExecStart=/usr/bin/python main.py config.toml
Restart=always

[Install]
WantedBy=multi-user.target
```

Then enable & start the service using:

```sh
sudo systemctl enable vinyl.service  # enable
sudo systemctl start vinyl.service   # start
sudo systemctl status vinyl.service  # check if the service is running
sudo systemctl daemon-reload
```

## To-do list (a.k.a.: wishlist)

- [ ] add a button to pause/play the music
- [ ] add a motor to simulate the vinyl record rotation
- [ ] 3d printed vinyl player

## Vinyl builder

If you want to have your own fake vinyl, I created a super simple "vinyl" builder. You can find the app [here](./vinyl-builder). I'm basically printing and using an [A4 laminator](https://www.action.com/nl-nl/p/2554854/fichero-lamineerapparaat/). _(yes, a 3d printed one would look way nicer, but I don't have a 3d printer)_

## References & inspiration

There are a lot of projects out there that are similar to this. The main difference is that I use YouTube Music instead of Spotify and a Google Home device.

<details>
  <summary>Inspiration list</summary>

- [A Modern Day Record Player: RFID Technology & Spotify API by talaexe](https://talaexe.com/moderndayrecordplayer)
- [Automating My Morning Routine - Modern-Day Record Player by Uma Abu](https://www.youtube.com/watch?v=-pfpPQN2Vek&t=454s)
- [DIY RFID Jukebox - by Slopes Tech](https://www.youtube.com/watch?v=wtzMpPbsPb4)
- [TonUINO, DIE DIY Musikbox (nicht nur) für Kinder (Jukebox, Arduino, RFID, DFPlayer, MP3)
  by Thorsten Voß](https://www.youtube.com/watch?v=-WZEMqXRFg4)

</details>

<details>
  <summary>References list</summary>

- [RC522 RFID lezer aansluiten op een Raspberry Pi en uitlezen met Python](https://raspberrytips.nl/rc522-rfid-raspberry-pi-3/)
- [pychromecast from home-assistant](https://github.com/home-assistant-libs/pychromecast)

</details>

## License

Vinyl Record Player is licensed under the MIT license. See [LICENSE](LICENSE) for more information.

[Image](./image.png) created using DALL-E OpenAI.
