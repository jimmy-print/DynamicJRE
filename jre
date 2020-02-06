#!/usr/local/bin/python3

import sys
import os

import get_episode
import utils

def main():
    arguments = sys.argv
    arguments.pop(0)
    
    if len(arguments) == 0:
        print_usage_message()
        return 1
    
    if "-h" in arguments or "--help" in arguments:
        print_usage_message()
        return 0

    not_using_pipeline = True
    if "-p" in arguments or "--pipe" in arguments:
        not_using_pipeline = False
    
    if not_using_pipeline:
        first_argument = arguments[0]
    else:
        first_argument = "".join(
            sys.stdin.readlines()
        ).rstrip()
        
    episode_number = first_argument
    
    try:
        get_episode.with_episode_number(episode_number)
    except TypeError:
        print("You did not enter a proper episode number")
        return 1

def print_usage_message():
    path = f"{utils.get_absolute_path('usage_message.txt')}"
    with open(path, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    sys.exit(main())
