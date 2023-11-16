import googlesearch
from googlesearch import search
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Odin")
print(ascii_banner)
print("Created by @Yugi")
print("example: example.com")
url = input(f"Target Domain: ")
file = input(f"What files u want: ")
list = file.split()
y = list
for i in y:
    print(f"Searching info in {url} file {i}.. ")
    for results in search(f"site: {url} filetype: {i}", num=int(1), start=0, stop=None, pause=2):
        print(results)