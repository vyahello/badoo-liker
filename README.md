# Badoo liker 
![Screenshot](image/like.png)

This program allows user to set schedule liker for badoo dating service (https://badoo.com).
It uses **python** and **selenium (pom)** to emulate user bahaviour. 

> Tools
> - `python 3.7+`
> - `selenium`
> - `.yaml` config setup
> - `chromedriver`
> - `pytest`

## Table of contents
- [Launch script](#launch-script)
- [Contributing](#contributing)

### Launch script
Before execution please configure badoo config setup file (`setup.yaml`). 
For local execution you have to [download](https://chromedriver.chromium.org) & run `chromedriver` from the cli:
```bash
~ chromedriver
```

Then just run script from the root directory of the project:
```bash
~ python liker.py -h
~ python liker.py --config setup.yaml
```

### Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `pip install -r requirements.txt` to install code dependencies
- `pip install -r requirements-dev.txt` to install code assessment dependencies