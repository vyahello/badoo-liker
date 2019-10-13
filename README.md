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
  - [Local/remote execution](#localremote-execution)
  - [Docker execution](#docker-execution)
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
#### Local/remote execution
To be able to run script on schedule basis please configure `run-scheduler.sh` shell script with corresponding
`pre-setup` configuration values in it.

```bash
~ ./run-scheduler.sh -h
This script provides badoo executor scheduler. Delay is set to "1800" seconds between run.

Please use next commands:

  - 'counted-executor' to run executor certain amount of time e.g '100'
  - 'infinite-executor' to run executor infinite period of time (it will run until script is crashed)
  - 'infinite-executor-background' to executor infinitely in a background. Logs will be saved in 'logs.txt' file automatically

Please see 'logs.txt' file for additional logs info.
```

#### Docker execution
There are two `docker images` to maintain execution via docker:
1. Base image
Base image contains all `core` required packages/dependencies for fresh code install. 
To build image please use command below:
```bash
~ docker build --no-cache -t vyahello/badoo-liker-base:<new version here> -f Dockerfile.base .
```
Then push it into docker artifactory:
```bash
~  docker push vyahello/badoo-liker-base:<new version here>
```

2. Main image


### Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `pip install -r requirements.txt` to install code dependencies
- `pip install -r requirements-dev.txt` to install code assessment dependencies