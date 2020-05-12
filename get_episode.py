import os
import requests
from bs4 import BeautifulSoup

import utils

folder = utils.get_save_folder()


def _download(download_link, episode_number, folder=folder):
    try:
        print(f"Downloading episode {episode_number}")
        raw_episode = requests.get(download_link)
    except KeyboardInterrupt:
        return
    try:
        with open(f"{folder}/p{episode_number}.mp3", "wb") as f:
            print("Writing to mp3")
            f.write(raw_episode.content)
    except KeyboardInterrupt:
        cleanup(episode_number)


def with_episode_number(episode_number, folder=folder):
    url_format = "http://traffic.libsyn.com/joeroganexp/p"

    _download(f"{url_format}{episode_number}.mp3", episode_number, folder=folder)


def latest(folder=folder):
    try:
        homepage = "http://podcasts.joerogan.net/"
        response = requests.get(homepage)
        soup = BeautifulSoup(response.text, "lxml")

        latest_element = soup.find_all("div", attrs={"class": "episode odd"})[0]
        links = latest_element.find_all("li")
        download_link = links[2].a.get("href")

        file_name = download_link.split("/")[4]
        # Stripping with .mp3 is perfect, as the p in front also gets removed.
        episode_number = file_name.strip(".mp3")
    except KeyboardInterrupt:
        return

    _download(download_link, episode_number, folder=folder)


def cleanup(episode_number, folder=folder):
    print("\nKeyboard interrupt detected")
    print("Commencing cleanup")
    os.remove(f"{folder}/p{episode_number}.mp3")
    print("Cleanup complete. Exiting.")
