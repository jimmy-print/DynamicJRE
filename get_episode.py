def with_episode_number(episode_number):
    try:
        int(episode_number)
    except ValueError:
        raise TypeError

    print(f"The episode number is {episode_number}")
