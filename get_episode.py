import os
import requests
from bs4 import BeautifulSoup

import utils

settings = utils.Settings()
settings.load("settings.txt")
folder = os.path.expanduser(settings.retrieve("Save-folder"))


def _download(download_link, episode_number, folder):
    print(f"Downloading episode {episode_number}")
    raw_episode = requests.get(download_link)
    with open(f"{folder}/p{episode_number}.mp3", "wb") as f:
        print("Writing to mp3")
        f.write(raw_episode.content)


def with_episode_number(episode_number, folder=folder):
    url_format = "http://traffic.libsyn.com/joeroganexp/p"

    try:
        _download(f"{url_format}{episode_number}.mp3", episode_number, folder)
    except KeyboardInterrupt:
        cleanup(episode_number)


def latest(folder=folder):
    homepage = "http://podcasts.joerogan.net/"
    response = requests.get(homepage)
    soup = BeautifulSoup(response.text, "lxml")

    latest_element = soup.find_all("div", attrs={"class": "episode odd"})[0]
    links = latest_element.find_all("li")
    download_link = links[2].a.get("href")

    file_name = download_link.split("/")[4]
    # Stripping with .mp3 is perfect, as the p in front also gets removed.
    episode_number = file_name.strip(".mp3")

    try:
        _download(download_link, episode_number, folder)
    except KeyboardInterrupt:
        cleanup(episode_number)


def cleanup(episode_number):
    print("\nKeyboard interrupt detected")
    print("Commencing cleanup")
    try:
        os.remove(f"p{episode_number}.mp3")
    except FileNotFoundError:
        pass
    print("Cleanup complete. Exiting.")
