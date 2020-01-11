import os

def with_episode_number(episode_number):
    try:
        int(episode_number)
    except ValueError:
        raise TypeError

    print(f"The episode number is {episode_number}")
    
    url_format = "http://traffic.libsyn.com/joeroganexp/p"

    os.system(f"wget {url_format}{episode_number}.mp3")
