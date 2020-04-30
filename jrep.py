#!/usr/local/bin/python3

import sys

import get_episode
import utils


def main():
    arguments = sys.argv
    arguments.pop(0)

    if len(arguments) == 0:
        utils.print_usage_message()
        return 1

    if "-h" in arguments or "--help" in arguments:
        utils.print_usage_message()
        return 0

    not_using_pipeline = True
    if "-p" in arguments or "--pipe" in arguments:
        not_using_pipeline = False

    if not_using_pipeline:
        method = arguments[0]
    else:
        method = "".join(
            sys.stdin.readlines()
        ).rstrip()

    try:
        int(method)
        internal_method = "number"
    except ValueError:
        if method == "latest":
            internal_method = "latest"
        else:
            print("Your argument should either be "
                  "\"latest\" or an episode number.")
            return 1

    if internal_method == "number":
        episode_number = method
        get_episode.with_episode_number(episode_number)
    elif internal_method == "latest":
        get_episode.latest()


if __name__ == "__main__":
    main()
