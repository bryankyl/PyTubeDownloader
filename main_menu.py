def main_menu() -> int:
    print("YouTube Downloader")
    print()
    print("1. Channel")
    print("2. Playlist")
    print("3. Specific YouTube Video")
    print("4. Audio Track")
    print("0. Exit")

    c = int(input("Please input your selection : "))
    return c