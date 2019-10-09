#!/bin/bash

# pre-setup configuration, please set it to desired values
CONFIG="setup.yaml"
RUNS=10
DELAY_BETWEEN_RUN=60
LOGS="logs.txt"


function run-delayed-liker {
   python liker.py --config ${CONFIG}
   sleep ${DELAY_BETWEEN_RUN}
}


function do-executor {
    iteration=0
    while true; do
        echo "Running #$iteration iteration ..."
        run-delayed-liker
        let iteration+=1
    done
    echo "Something went wrong, please see $LOGS for more details!"
}


do-executor