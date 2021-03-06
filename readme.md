<br/>
<a href="https://github.com/philipempl/ResearchyPi" target="blank_">
    <img height="200" alt="ResearchyPi" src="https://raw.githubusercontent.com/philipempl/researchypi/master/resources/logo.png" />
</a>
<br/>

# ResearchyPi: Drawing Google Scholar Stats on the Raspberry

[Short Description]


<img src="https://raw.githubusercontent.com/philipempl/researchypi/master/resources/animation.gif" alt="ResearchyPi in action" width="100%"/>

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
sudo apt-get install libopenjp2-7
sudo apt install python3 idle3
sudo apt-get install python3-pip
sudo pip3 install -r requirements.txt
python3 ./setup.py
```

### Test the app
```
python3 ./main.py
```


## Contributing

Have a look through existing [Issues](https://github.com/philipempl/researchypi/issues) and [Pull Requests](https://github.com/philipempl/researchypi//pulls) that you could help with. If you'd like to request a feature or report a bug, please [create a GitHub Issue](https://github.com/philipempl/researchypi/issues) using one of the default templates.


## Authors

-   **Philip Empl** - [Department of Information Systems](https://www.uni-regensburg.de/wirtschaftswissenschaften/wi-pernul/team/philip-empl/index.html)  *@ University of Regensburg*

## License

This project is available under the MIT license.
