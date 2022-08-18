
<br/>
<a href="https://github.com/philipempl/ResearchyPi" target="blank_">
    <img height="200" alt="ResearchyPi" src="https://raw.githubusercontent.com/philipempl/researchypi/master/resources/logo.png" />
</a>
<br/>

# Drawing Google Scholar Stats on the Raspberry

<img src="https://raw.githubusercontent.com/philipempl/researchypi/master/resources/demo.gif" alt="ResearchyPi in action" width="60%"/>

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
cd ./ ResearchyPi
```
### Install python, pip and all dependencies
```shell
sudo apt-get install libxslt-dev
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo pip3 install RPi.GPIO
sudo pip3 install scholarly
```

### Enable SPI
Get into the menu using:
```shell
sudo raspi-config
```
Then enable SPI (I4) under interface options (3).


## Run the app
You can find the scholar identifier in the URL provided by Google scholar after user= and ending with an ampersand.
```shell
python3 src/main.py Lu-BjV4AAAAJ
```

## Update the stats continuously
For updating and scheduling your stats automatically, you can define service files using systemd. For instance:
```shell
sudo nano /etc/systemd/system/update-stats.service
```
The service file itself updating every 14400 second (4 hour interval) looks the following:

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
Then you need to grant rights to the user and enable the systemd file on startup by running the following commands:
```shell
sudo chmod 644 /etc/systemd/system/update-stats.service
sudo systemctl daemon-reload
sudo systemctl enable update-stats.service
sudo systemctl start update-stats.service
```
## Contributing

Have a look through existing [Issues](https://github.com/philipempl/researchypi/issues) and [Pull Requests](https://github.com/philipempl/researchypi//pulls) that you could help with. If you'd like to request a feature or report a bug, please [create a GitHub Issue](https://github.com/philipempl/researchypi/issues) using one of the default templates.


## Authors

-   **Philip Empl** - [Department of Information Systems](https://www.uni-regensburg.de/wirtschaftswissenschaften/wi-pernul/team/philip-empl/index.html)  *@ University of Regensburg*

## License

This project is available under the MIT license.
