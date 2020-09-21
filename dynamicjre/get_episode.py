import os
import requests
from bs4 import BeautifulSoup

REGULAR = "regular"
MMA = "mma"
FIGHT = "fight"
episode_types = (REGULAR, MMA, FIGHT)
url_formats = (
    "http://traffic.libsyn.com/joeroganexp/p{}.mp3",
    "http://traffic.libsyn.com/joeroganexp/mmashow{}.mp3",
)
# Fight episodes aren't supported yet
alt_regular_url_format = "http://traffic.libsyn.com/joeroganexp/p{}a.mp3"
# Sometimes the url for regular episodes has an 'a' after the
# url number. I have no idea why.

episode_type_url_format = dict(zip(episode_types, url_formats))


def download(episode_number, episode_type, guest, headers=None):
    """Calls requests.get to do the actual downloading"""
    try:
        print(f"Downloading episode {episode_type} {episode_number} {guest}")
        download_link = (
            episode_type_url_format[episode_type].format(episode_number))
        raw_episode = requests.get(download_link, headers=headers)

        if not raw_episode.ok:
            download_link = alt_regular_url_format.format(episode_number)
            print("Trying alternative url format...")
            raw_episode = requests.get(download_link, headers=headers)
            # If the response is the 404 html
            if raw_episode.headers['content-type'] == 'text/html; charset=UTF-8':
                print('Episode {} was not found.'.format(episode_number))
    except KeyboardInterrupt:
        return

    # Use context manager here?
    try:
        with open(f"p{episode_number}.mp3", "wb") as f:
            print("Writing to mp3")
            f.write(raw_episode.content)
    except KeyboardInterrupt:
        cleanup(episode_number)


def with_episode_number(episode_number, headers=None):
    """Downloads the specified regular episode"""
    # guest is an empty string because I haven't implemented searching
    # with ep. numbers
    download(episode_number, REGULAR, guest="", headers=headers)


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

    guest = latest_element.find("a", attrs={"data-section": "podcasts"}).get("data-title")

    return episode_number, episode_type, guest


def latest(headers=None):
    """Downloads the latest episode"""
    try:
        episode_number, episode_type, guest = get_latest_episode_attributes()
    except KeyboardInterrupt:
        return

    download(episode_number, episode_type, guest, headers=headers)
    return episode_number, episode_type, guest # For testing purposes


def cleanup(episode_number):
    """Deletes the downloaded episode"""
    print("Commencing cleanup")
    os.remove(f"p{episode_number}.mp3")
    print("Cleanup complete. Exiting.")
