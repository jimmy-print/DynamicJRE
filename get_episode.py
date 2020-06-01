import os
import requests
from bs4 import BeautifulSoup

import utils

folder = utils.get_save_folder()

REGULAR = "regular"
MMA = "mma"
FIGHT = "fight"
episode_types = (REGULAR, MMA, FIGHT)
url_formats = (
    "http://traffic.libsyn.com/joeroganexp/p{}.mp3",
    "http://traffic.libsyn.com/joeroganexp/mmashow{}.mp3",
)
# Fight episodes aren't supported yet
episode_type_url_format = dict(zip(episode_types, url_formats))


def download(episode_number, episode_type, folder=folder, headers=None):
    try:
        print(f"Downloading episode {episode_type} {episode_number}")
        download_link = (
            episode_type_url_format[episode_type].format(episode_number))
        raw_episode = requests.get(download_link, headers=headers)
        raw_episode.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return
    except KeyboardInterrupt:
        return
    try:
        with open(f"{folder}/p{episode_number}.mp3", "wb") as f:
            print("Writing to mp3")
            f.write(raw_episode.content)
    except KeyboardInterrupt:
        cleanup(episode_number)


def with_episode_number(episode_number, folder=folder, headers=None):
    # with_episode_number only works with regular episodes for now
    download(episode_number, REGULAR, folder=folder, headers=headers)


def get_latest_episode_attributes():
    """Returns latest episode number and type (Regular, MMA, Fight)"""

    homepage = "http://podcasts.joerogan.net/"
    response = requests.get(homepage)
    soup = BeautifulSoup(response.text, "lxml")

    latest_element = soup.find_all("div", attrs={"class": "episode odd"})[0]
    episode_number_element = latest_element.find("span", attrs={"class": "episode-num"})
    episode_number = episode_number_element.text.strip("#")

    title_element = latest_element.find("a", attrs={"class": "ajax-permalink"})
    title_text = title_element.get("data-title")
    if "mma show" in title_text.lower():
        episode_type = MMA
    elif "fight companion" in title_text.lower():
        episode_type = FIGHT
    else:
        episode_type = REGULAR

    return episode_number, episode_type


def latest(folder=folder, headers=None):
    try:
        episode_number, episode_type = get_latest_episode_attributes()
    except KeyboardInterrupt:
        return

    download(episode_number, episode_type, folder=folder, headers=headers)
    return episode_number, episode_type # For testing purposes


def cleanup(episode_number, folder=folder):
    print("Commencing cleanup")
    os.remove(f"{folder}/p{episode_number}.mp3")
    print("Cleanup complete. Exiting.")


if __name__ == "__main__":
    download("0", FIGHT)
