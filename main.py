import modules
import colorama
from colorama import Fore, Back, Style
colorama.init()

keep = True

print(Fore.RED, end="")
print("█████████████████████████████████████████████████████████████████")
print("█─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▀█▀─▄█▄─██─▄█▄─▀─▄█─▄─▄─█▄─██─▄█▄─▄─▀█▄─▄▄─█")
print("███─████─▄█▀██─▄─▄██─█▄█─███─██─███▀─▀████─████─██─███─▄─▀██─▄█▀█")
print("▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄█▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀")
print("                                  by Konstantinov Vladimir Studio")

while keep:
    print(Fore.MAGENTA)
    print("-----------------------------------------------------------------")
    print("Menu. To select a function, enter its number: \n")
    print("[1] Download a video from Youtube")
    print("[2] Info of video from Youtube")
    print("[99] Exit")
    print(Style.RESET_ALL)
    op = input("Function: ")
    if op == "1":
        modules.down_vid()
    elif op == "2":
        modules.get_info()
    elif op == "99":
        keep = False
    else:
        print(Fore.RED + "[ERROR] Wrong number" + Style.RESET_ALL)
print("-----------------------------------------------------------------")
print("Thanks for using! Bye!")