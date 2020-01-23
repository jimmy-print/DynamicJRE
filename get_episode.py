import subprocess

def with_episode_number(episode_number):
    try:
        int(episode_number)
    except ValueError:
        raise TypeError

    print(f"The episode number is {episode_number}")
    
    url_format = "http://traffic.libsyn.com/joeroganexp/p"

    try:
        subprocess.run(["wget",f"{url_format}{episode_number}.mp3"])
    except KeyboardInterrupt:
        cleanup(episode_number)

def cleanup(episode_number):
    print("Keyboard interrupt detected")
    print("Commencing cleanup")
    subprocess.run(["rm",f"p{episode_number}.mp3"])
    print("Cleanup complete. Exiting.")
