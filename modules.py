  
import re
from pytube import YouTube
import urllib
import urllib.request
from urllib.request import urlopen
import colorama
from colorama import Fore, Back, Style
import time

colorama.init()

def down_vid():
    print(Fore.RED)
    link = str(input('Link for video from YouTube: '))
    print(Fore.MAGENTA, end="")
    save_link = input('Path for saving: ')
    regxp = '[\w-]+[\w:]'
    result = re.findall(regxp, save_link) #Разбиваем адрес, куда сохраняем видео на составляющие без обратного слеша
    final_link = '\\\\'.join(result) #Добавляем двойной слеш после каждой папки (под формат Python)

    yt = YouTube(link)

    format_video = yt.streams.filter(resolution="720p").first()

    print(Style.RESET_ALL)
    print('Downloading...')
    format_video.download(final_link)
    print('Download successful. Path: ', save_link)

def get_info():
    print(Fore.RED)
    link = str(input('Link for video from YouTube: '))

    yt = YouTube(link)

    fn = yt.title
    author = yt.author
    desc = yt.description
    views = yt.views
    print(Fore.MAGENTA)
    print("Name of video: ", fn)
    time.sleep(2)
    print(Fore.BLUE)
    print("Author of video: ", author)
    time.sleep(2)
    print(Fore.CYAN)
    print("Description of video:")
    print(desc)
    print(Fore.YELLOW)
    print("Views: ", views)

    print(Style.RESET_ALL)
