#!/bin/bash

IMAGE_REPO="vyahello/badoo-liker"
IMAGE_VERSION="2.2.3"
CONFIG="template-setup.yaml"
COMPOSE="docker-compose.yaml"
DELAY_BETWEEN_RUN=1800


function helper {
  cat <<HELP
  This script provides badoo liker executor via docker.

  Please use next commands:
    - 'get-setup' to get latest config .yaml setup file
       docker run ${IMAGE_REPO}:${IMAGE_VERSION} get-setup > config.yaml

    - 'get-compose' to get latest docker-compose file
       docker run ${IMAGE_REPO}:${IMAGE_VERSION} get-compose > docker-compose.yaml

    - 'run-liker' to run badoo-liker script
       docker run ${IMAGE_REPO}:${IMAGE_VERSION} run-liker -h
HELP
}


function get-setup {
  echo "Cloning ${CONFIG} file into ./"
  cat ${CONFIG}
}


function get-compose {
  echo "Cloning ${COMPOSE} file into ./"
  cat ${COMPOSE}
}


function run-single-liker {
  python liker.py $@
}


function run-infinite-liker {
  iteration=0
  while true; do
    echo "Running #$iteration badoo iteration ..."
    run-single-liker $@
    echo "Waiting ${DELAY_BETWEEN_RUN} second(s) for next iteration ..."
    sleep ${DELAY_BETWEEN_RUN}
    let iteration+=1
  done
}


function check-grid-is-ready {
  while ! curl -sSL "http://localhost:4444/wd/hub/status" 2>&1 \
  | jq -r '.value.ready' 2>&1 | grep "true" >/dev/null; do
    echo 'Still waiting for the Grid ...'
    sleep 1
  done
}


function run-liker {
  if [[ -z "$@" ]];
    then python liker.py --help
  else
    check-grid-is-ready

    if [[ "$1" == "--infinite" ]] || [[ "$1" == "-i" ]]; then
      shift
      run-infinite-liker $@
    else
      run-single-liker $@
    fi
  fi
}


function main {
  if (
    [[ "$1" == "-h" ]] ||
    [[ "$1" == "--help" ]] ||
    [[ "$1" == "help" ]] ||
    [[ $# -eq 0 ]]
  ); then
    helper
    exit 0
  fi
  local cmd=$1; shift
  eval "${cmd} $@"
}


main $@
