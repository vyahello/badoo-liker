#!/bin/bash

# pre-setup configuration, please set it to desired values
CONFIG="template-setup.yaml"
DELAY_BETWEEN_RUN=3600
LOGS="logs.txt"


function helper {
  cat <<HELP
  This script provides badoo executor scheduler. Delay is set to "${DELAY_BETWEEN_RUN}" seconds between run.

  Please use next commands:
    - 'counted-executor' to run executor certain amount of time e.g '100'
    - 'infinite-executor' to run executor infinite period of time (it will run until script is crashed)
    - 'infinite-executor-background' to run executor infinitely in a background.
       Logs will be saved in '${LOGS}' file automatically

  Please see '${LOGS}' file for additional logs info.
HELP
}


function run-delayed-liker {
  python liker.py --config ${CONFIG}
  echo "Waiting ${DELAY_BETWEEN_RUN} second(s) for next iteration ..."
  sleep ${DELAY_BETWEEN_RUN}
}


function counted-executor {
  runs=$1
  if [[ -z "$runs" ]]; then
    echo "Please specify run command parameter e.g '5'!"
    exit 1
  fi
  echo "Running badoo-liker with $1 run attempts (delayed with "${DELAY_BETWEEN_RUN}" seconds)"
  for (( run=0; run<=$1; run++ )) do
    echo "$runs attempts are left to run!"
    run-delayed-liker
    let runs-=1
  done
}


function infinite-executor {
  iteration=0
  while true; do
    echo "Running #$iteration badoo iteration ..."
    run-delayed-liker
    let iteration+=1
  done
  echo "Something went wrong, please see '${LOGS}' for more details!"
}


function infinite-executor-background {
  infinite-executor > ${LOGS} 2>&1 &
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
