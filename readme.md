<br/>
<a href="https://github.com/philipempl/ResearchyPi" target="blank_">
    <img height="200" alt="ResearchyPi" src="https://raw.githubusercontent.com/philipempl/researchypi/master/resources/logo.png" />
</a>
<br/>

# ResearchyPi: Drawing Google Scholar Stats on the Raspberry

[Short Description]


<img src="https://raw.githubusercontent.com/philipempl/researchypi/master/resources/demo.gif" alt="ResearchyPi in action" width="100%"/>

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


### Test the app
You can find the scholar identifier in the URL provided by Google scholar after user= and ending with an ampersand.
```shell
python3 src/main.py Lu-BjV4AAAAJ
```


## Contributing

Have a look through existing [Issues](https://github.com/philipempl/researchypi/issues) and [Pull Requests](https://github.com/philipempl/researchypi//pulls) that you could help with. If you'd like to request a feature or report a bug, please [create a GitHub Issue](https://github.com/philipempl/researchypi/issues) using one of the default templates.


## Authors

-   **Philip Empl** - [Department of Information Systems](https://www.uni-regensburg.de/wirtschaftswissenschaften/wi-pernul/team/philip-empl/index.html)  *@ University of Regensburg*

## License

This project is available under the MIT license.
