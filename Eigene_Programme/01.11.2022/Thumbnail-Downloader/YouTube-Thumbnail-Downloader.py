from requests import get
from os import remove as rm


def thumbnail_download(url, filename="thumbnail.png"):
    if "youtu.be" in url:
        vid_id = url.split("/")[3]
    else:
        vid_id = url.split("=")[1][:11]
    with open(filename, "wb") as file:
        antwort = get(f"https://img.youtube.com/vi/{vid_id}/maxresdefault.jpg")
        file.write(antwort.content)
        print("Der Download war erfolgreich!")


if __name__ == "__main__":
    loop = "ja"
    while loop == "ja":
        vid_url = input("Gib die URL des YouTube-Videos ein: ")
        thumbnail_name = input("Gib einen Namen für das Thumbnail ein: ")
        thumbnail_download(vid_url, f"{thumbnail_name}.png")
        loop = input("Möchtest du noch ein Thumbnail herunterladen? (Ja|Nein): ").lower()