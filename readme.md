<p align="center">
  <a href="https://github.com/philipempl/ResearchyPi" target="_blank">
    <img height="200" alt="ResearchyPi" src="https://raw.githubusercontent.com/philipempl/researchypi/master/resources/logo.png" />
  </a>
</p>

# Drawing Google Scholar Stats on RPI Waveshare

<p align="center">
  <img src="https://raw.githubusercontent.com/philipempl/Researchypi/master/resources/demo.gif" alt="ResearchyPi in action" width="60%"/>
</p>

## Prerequisites

| Name                       | Link                                                | Price |
|----------------------------|----------------------------------------------------|-------|
| Raspberry Pi Zero WH       | [Get it here](https://www.berrybase.de/raspberry-pi-zero-wh)      | $16   |
| Waveshare 2.13 Display Hat | [Get it here](https://www.waveshare.com/2.13inch-e-paper-hat.htm) | $15   |

## Getting started

### Update and upgrade the RPI
```shell
sudo apt-get update
sudo apt-get upgrade
```

### Install git and clone this repository
```shell
sudo apt-get install git
git clone https://github.com/philipempl/ResearchyPi.git
cd ./ResearchyPi
```

### Install Python and its dependencies
```shell
sudo apt-get install libxslt-dev python3-pip python3-pil
sudo pip3 install RPi.GPIO scholarly
```

### Enable SPI
To enable SPI, follow these steps:

```shell
sudo raspi-config
```

Then, navigate to "Interface Options" (Option 3) and enable SPI (I4).

## Run the app
You can find the scholar identifier in the URL provided by Google Scholar after "user=" and ending with an ampersand.

```shell
python3 src/main.py Lu-BjV4AAAAJ
```

## Update the stats continuously
To update and schedule your stats automatically, create a service file using systemd. For instance:

```shell
sudo nano /etc/systemd/system/update-stats.service
```

The service file itself, updating every 14400 seconds (4-hour interval), looks like this:

```shell
[Unit]
Description=ResearchyPi
After=multi-user.target

[Service]
Type=idle
User=pi
ExecStart=python3 /home/pi/ResearchyPi/main.py SCHOLAR_ID

Restart=always
RestartSec=14400

[Install]
WantedBy=multi-user.target
```

Then, grant rights to the user and enable the systemd file on startup by running the following commands:

```shell
sudo chmod 644 /etc/systemd/system/update-stats.service
sudo systemctl daemon-reload
sudo systemctl enable update-stats.service
sudo systemctl start update-stats.service
```

## Contributing

If you'd like to contribute, have a look through existing [Issues](https://github.com/philipempl/researchypi/issues) and [Pull Requests](https://github.com/philipempl/researchypi/pulls) that you could help with. If you would like to request a feature or report a bug, please [create a GitHub Issue](https://github.com/philipempl/researchypi/issues) using one of the default templates.

## Authors

-   **Philip Empl** - [Department of Information Systems](https://www.uni-regensburg.de/wirtschaftswissenschaften/wi-pernul/team/philip-empl/index.html)  *@ University of Regensburg*

## License

This project is available under the MIT license.
```

Feel free to copy and paste this markdown into your GitHub README.md file, and it should create a visually appealing and well-structured README for your project. Make sure to replace `SCHOLAR_ID` with the actual scholar identifier where needed.
