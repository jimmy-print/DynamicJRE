import subprocess
import requests
from bs4 import BeautifulSoup


def with_episode_number(episode_number):
    print(f"The episode number is {episode_number}")

    url_format = "http://traffic.libsyn.com/joeroganexp/p"

    try:
        subprocess.run(["wget", f"{url_format}{episode_number}.mp3"])
    except KeyboardInterrupt:
        cleanup(episode_number)


def latest():
    homepage = "http://podcasts.joerogan.net/"
    response = requests.get(homepage)
    soup = BeautifulSoup(response.text, "lxml")

    latest_element = soup.find_all("div", attrs={"class":"episode odd"})[0]
    links = latest_element.find_all("li")
    download_link = links[2].a.get("href")

    file_name = download_link.split("/")[4]
    # Stripping with .mp3 is perfect, as the p in front also gets removed.
    episode_number = file_name.strip(".mp3")

    try:
        subprocess.run(["wget", download_link])
    except KeyboardInterrupt:
        cleanup(episode_number)


def cleanup(episode_number):
    print("\nKeyboard interrupt detected")
    print("Commencing cleanup")
    subprocess.run(["rm", f"p{episode_number}.mp3"])
    print("Cleanup complete. Exiting.")
