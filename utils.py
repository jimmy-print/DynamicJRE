import os

def get_absolute_path(relative_path):
    return f"{os.path.dirname(os.path.abspath(relative_path))}/{relative_path}"

if __name__ == "__main__":
    print(get_absolute_path("example_file.txt"))
