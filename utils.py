import os

def get_absolute_path(relative_path):
    absolute_path_of_program_folder = os.path.dirname(
        os.path.abspath(__file__))
    absolute_path = os.path.join(absolute_path_of_program_folder,
                                 relative_path)
    return absolute_path

