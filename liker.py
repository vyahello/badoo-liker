import sys
from argparse import ArgumentParser
from typing import Dict, Any
from badoo.connections.web import Browser
from badoo.services import Liker, BadooLiker
from badoo.setup import Setup
from badoo.yaml import YamlFromPath


def _arguments() -> Dict[str, Any]:
    parser = ArgumentParser(description="This program allows to run badoo liker service.")
    parser.add_argument(
        "--setup",
        "-s",
        help="Setup config file (e.g `config.yaml`)",
        type=str,
        required=True,
        default="data/setup.yaml",
    )
    parser.add_argument(
        "--likes",
        "-l",
        help="Number of likes (e.g `100`)",
        type=int,
        required=True,
    )
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    return vars(args)


def _run_badoo_liker(*, setup: Setup, number_of_likes: int) -> None:
    liker: Liker = BadooLiker(Browser(setup.browser()), setup.badoo().credentials())
    liker.start(number_of_likes, setup.badoo().intro_message())


if __name__ == '__main__':
    _args = _arguments()
    _run_badoo_liker(setup=Setup(YamlFromPath(_args["setup"])), number_of_likes=_args["likes"])
