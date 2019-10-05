# Badoo liker
This program allows user to set schedule liker for badoo dating service (https://badoo.com).
It uses **python** and **selenium (pom)** to emulate user bahaviour. 

## Table of contents
- [Launch script](#launch-script)
- [Contributing](#contributing)

### Launch script
Before execution please configure badoo data setup file (`data/setup.yaml`). 
For local execution you have to [download](https://chromedriver.chromium.org) & run `chromedriver` from the cli:
```bash
~ chromedriver
```

Then just run script from the root directory of the project:
```bash
~ python liker.py -h
~ python liker.py --setup data/setup.yaml --likes 5
```

### Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.7+` is required to run the code