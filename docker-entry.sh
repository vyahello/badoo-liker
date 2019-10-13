#!/bin/bash

IMAGE_REPO="vyahello/badoo-liker"
CONFIG="template-setup.yaml"

function helper {
    cat <<HELP
    This script provides badoo liker executor via docker.

    Please use next commands:
      - 'get-setup' to get latest config .yaml setup file
         docker run ${IMAGE_REPO}:<image-version> get-setup > config.yaml

      - 'run-liker' to run badoo-liker script
         docker run ${IMAGE_REPO}:<image-version> run-liker -h

HELP
}


function get-setup {
    cat ${CONFIG}
}


function run-liker {
   if [[ -z "$@" ]];
       then python liker.py --help
   else
       python liker.py $@
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
