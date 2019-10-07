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
- [Schedule runner](#schedule-runner)
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

You'll get next output:
```bash
[2019-10-07 22:11:39 INFO] Operating 25 badoo like attempts, in progress ...
[2019-10-07 22:13:11 INFO] 25 badoo like attempts were successfully completed, please check your messages!
```

### Schedule runner
To be able to run script on schedule basis please configure `run-scheduler.sh` shell script with corresponding
`pre-setup` configuration values in it.

It will be run on a background and store output into `logs.txt` file:
```bash
~ ./run-scheduler.sh > logs.txt 2>&1 &
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