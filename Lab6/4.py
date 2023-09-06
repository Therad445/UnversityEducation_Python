import urllib.request
from time import time
from threading import Thread

sites = [
    "https://online.sochisirius.ru",
    "https://www.osu.ru",
    "https://orioks.miet.ru",
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    "https://google.ru",
    "https://yandex.ru",
    "https://music.youtube.com",
    "https://vk.com",
    "https://mos.ru",
]


def parse_sites():
    for site in sites:
        urllib.request.urlopen(site)


start = time()
parse_sites()
parse_sites()
print("With 1 thread: " + str(time() - start) + " seconds")
start = time()
t1 = Thread(target=parse_sites)
t1.start()
t2 = Thread(target=parse_sites)
t2.start()
t1.join()
t2.join()
print("With 2 threads: " + str(time() - start) + " seconds")
