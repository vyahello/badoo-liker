# Badoo liker 
![Screenshot](image/badoo.png)

This program allows user to set schedule liker for badoo dating service (https://badoo.com).
It uses **python** and **selenium (pom)** to emulate user bahaviour. 

> Tools
> - `python 3.7+`
> - `selenium-grid`
> - `.yaml` config setup
> - `docker (>=18.0)` and `docker-compose (>= 1.22)`
> - `chromedriver`
> - `pytest`

## Table of contents
- [Usage](#usage)
  - [Launch script](#launch-script)
  - [Schedule runner](#schedule-runner)
    - [Local/remote execution](#localremote-execution)
    - [Docker execution](#docker-execution)
- [Development notes](#development-notes)
  - [Run unittests](#run-unittests)
  - [Meta](#meta)
  - [Contributing](#contributing)

## Usage
### Launch script
Before execution please configure badoo config setup file (`setup.yaml`). 
For local execution you have to [download](https://chromedriver.chromium.org) (as we support `Chrome only` for now) & run `chromedriver` from the cli:
```bash
~ chromedriver
```
We use [selenium-grid](https://www.vinsguru.com/selenium-grid-setup-using-docker) to make it compatible with different OS/browsers (in future)
mostly using `docker-compose.yaml` file.

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
  - 'infinite-executor-background' to run executor infinitely in a background. Logs will be saved in 'logs.txt' file automatically

Please see 'logs.txt' file for additional logs info.
```

#### Docker execution
There are two `docker images` to maintain execution via docker: 
1. Base image
Base image contains all `core` required packages/dependencies for fresh code install. 
To build and push image please use command below:
```bash
~ docker build --no-cache -t vyahello/badoo-liker-base:<new version here> -f Dockerfile.base . && \
  docker push vyahello/badoo-liker-base:<new version here>
```

2. Main image
This image is aimed to run badoo-liker from docker.
To build and push image please use command below (<new version here> may be some `0.1.0` version):
```bash
~ docker build --no-cache -t vyahello/badoo-liker:<new version here> . && \
  docker push vyahello/badoo-liker:<new version here>
```

To run `man` of badoo liker via docker, please start command below ('your version here' may be some `0.1.0` version):
```bash
~ docker run vyahello/badoo-liker:<your version here>
```

To get latest `.yaml` config file, please start command below ('your version here' may be some `0.1.0` version):
```bash
~ docker run vyahello/badoo-liker:<your version here> get-setup > config.yaml
``` 

To run badoo liker help, please follow command below ('your version here' may be some `0.1.0` version):
```bash
~ docker run vyahello/badoo-liker:<your version here> run-liker -h
```

Please use `docker-compose.yaml` file to run badoo liker script in docker with:
```bash
~ docker-compose up <service> # run some service e.g 'help' or 'scheduler'
~ docker compose up -d <service>  # run in background
~ docker logs <service>  # see recent logs
~ docker compose down  # shutdown badoo runner
```
For instance below is a sample of execution via `docker-compose`:
```bash
~ docker-compose up scheduler
Creating network "badoo-liker_default" with the default driver
Creating selenium-hub ... done
Creating badoo-liker_chrome-node_1 ... done
Creating badoo-scheduler           ... done
Attaching to badoo-scheduler
badoo-scheduler | Still waiting for the Grid ...
badoo-scheduler | Still waiting for the Grid ...
badoo-scheduler | [2019-10-13 14:37:06 INFO] Operating 15 badoo like attempts, in progress ...
badoo-scheduler | [2019-10-13 14:38:21 INFO] 15 badoo like attempts were successfully completed, please check your messages!
badoo-scheduler exited with code 0
```
```bash
~ docker-compose down
Stopping badoo-liker_chrome-node_1 ... done
Stopping selenium-hub              ... done
Removing badoo-scheduler           ... done
Removing badoo-liker_chrome-node_1 ... done
Removing selenium-hub              ... done
Removing network badoo-liker_default
```

You can run `infinite scheduler` with command below:
```bash
~ docker-compose up infinite-scheduler
```

Please follow [docker-selenium](https://github.com/SeleniumHQ/docker-selenium) instructions.

## Development notes

### Run unittests
Please execute next command from the root directory of a project
```bash
~ pytest
```

### Meta
Author – Volodymyr Yahello vyahello@gmail.com

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development dependencies