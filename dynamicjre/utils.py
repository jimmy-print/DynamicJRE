import os


def get_absolute_path(relative_path):
    absolute_path_of_root_program_folder = os.path.dirname(
        os.path.abspath(__file__))
    absolute_path = os.path.join(absolute_path_of_root_program_folder,
                                 relative_path)
    return absolute_path


def print_usage_message():
    print("""
Usage:
    jrep <method> [options]

Methods:
    latest                          Download the latest episode
    <episode-number>                Download the specified episode

Options:
    -h, --help                      Show this message
    -p, --pipe                      Use unix pipelines instead of
                                    positional arguments
    --show-save-folder              Print the save folder being used
""")