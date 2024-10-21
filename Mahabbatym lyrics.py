import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Мойныңда сенің күмістен алқа", 0.14),
        ("Толқынды жаға", 0.15),
        ("Екеуміз ғана ", 0.15),
        ("Сырымыз бітпей. Жалғасты таңға", 0.15),

        ("Жағымды жанға", 0.15),
        ("Менде арман бар ма?", 0.12),

    ]

    delays = [2, 2.1, 5, 2.1,
              2, 3, ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
