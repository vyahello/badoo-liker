![Screenshot](logo.png)

# Badoo liker

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Docker pulls](https://img.shields.io/docker/pulls/vyahello/badoo-liker.svg)](https://hub.docker.com/repository/docker/vyahello/badoo-liker)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

> This program allows user to set schedule liker for badoo dating service (https://badoo.com).
>
> It uses **python** and **selenium (pom)** to emulate user behaviour. 

## Tools

### Production
- python 3.7+
- selenium-grid
- docker (>=18.0)
- docker-compose (>= 1.22)
- zalenium
- chromedriver
- yaml config setup

### Development
- pytest

## Table of contents
- [Usage](#usage)
  - [Docker](#docker)
  - [Source code](#source-code)
- [Development notes](#development-notes)
  - [Docker build](#docker-build)
  - [Testing](#testing)
  - [Contributing](#contributing)

## Usage

![Demo](demo.gif)

### Docker

Please use official docker `vyahello/badoo-like` image and docker-compose setup for common usage.
```bash
docker run --rm vyahello/badoo-liker:2.2.3
```

It uses [zalenium](https://github.com/zalando/zalenium) so you can check what's going on in the browser via http://localhost:4444/grid/admin/live endpoint.

To get latest `setup.yaml` config file, please start the command below:
```bash
docker run --rm vyahello/badoo-liker:2.2.3 get-setup > setup.yaml
``` 

> Please make sure `grid-url` is set to `http://localhost:4444/wd/hub`

To get latest `docker-compose.yaml` config file, please start command below:
```bash
docker run --rm vyahello/badoo-liker:2.2.3 get-compose > docker-compose.yaml
``` 

Please use [docker-compose.yaml](docker-compose.yaml) file to run badoo liker script in docker with:
```bash
docker-compose up <service> # run some service e.g 'help' or 'single-scheduler'
docker compose up -d <service>  # run in background
docker logs <service>  # see recent logs
docker compose down  # shutdown badoo runner
```

For instance, below is a sample of execution via `docker-compose`:
```bash
docker-compose up single-scheduler

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

You can run `infinite scheduler` with command below:
```bash
docker-compose up infinite-scheduler
```

Please follow [docker-selenium](https://github.com/SeleniumHQ/docker-selenium) instructions.

### Source code
Before execution please configure badoo config setup file [template-setup.yaml](template-setup.yaml). 

> Please make sure `grid-url` is set to `http://localhost:9515`

For local execution you have to download [chromedriver](https://chromedriver.chromium.org) (as we support `Chrome only` for now) & run it from the cli:
```bash
chromedriver
```

We use [selenium-grid](https://www.vinsguru.com/selenium-grid-setup-using-docker) to make it compatible with different OS/browsers (in future).

Then just run script from the root directory of the project:
```bash
python liker.py --help
usage: liker.py [-h] [--config CONFIG]

This program allows to run badoo liker service.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG
                        Setup badoo config file (e.g `setup.yaml`)
```

You'll get next output:
```bash
[2019-10-07 22:11:39 INFO] Operating 25 badoo like attempts, in progress ...
[2019-10-07 22:13:11 INFO] 25 badoo like attempts were successfully completed, please check your messages!
```
**[⬆ back to top](#table-of-contents)**

**Scheduler**

To be able to run script on schedule basis please configure [run-scheduler.sh](run-scheduler.sh) shell script with corresponding
`pre-setup` configuration values in it.

```bash
./run-scheduler.sh -h

This script provides badoo executor scheduler. Delay is set to "1800" seconds between run.

Please use next commands:

  - 'counted-executor' to run executor certain amount of time e.g '100'
  - 'infinite-executor' to run executor infinite period of time (it will run until script is crashed)
  - 'infinite-executor-background' to run executor infinitely in a background. 
     Logs will be saved in 'logs.txt' file automatically

Please see 'logs.txt' file for additional logs info.
```

**[⬆ back to top](#table-of-contents)**

## Development notes

### Docker build
There are two `docker images` to maintain execution via docker: 
1. **Base image**

Base image contains all `core` required packages/dependencies for fresh code install. 
To build and push image please use command below:
```bash
docker build --no-cache -t vyahello/badoo-liker-base:<new version here> -f Dockerfile.base . && \
docker push vyahello/badoo-liker-base:<new version here>
```

2. **Main image**

This image is aimed to run badoo-liker from docker.
To build and push image please use the command below (<new version here> may be some `0.1.0` version):
```bash
docker build --no-cache -t vyahello/badoo-liker:<new version here> . && \
docker push vyahello/badoo-liker:<new version here>
```

### Testing
Please execute the next command from the root directory of a project:
```bash
pytest
```

### Contributing
1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request
