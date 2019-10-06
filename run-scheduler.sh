#!/bin/bash

# pre-setup configuration, please set it to desired values
CONFIG="setup.yaml"
RUNS=10
DELAY_BETWEEN_RUN=3600


function do-executor {
    for (( run=1; run<=${RUNS}; run++ )); do
      python liker.py --config ${CONFIG}
    sleep ${DELAY_BETWEEN_RUN}
    done
}


do-executor