from urllib.request import urlopen

try:
    with urlopen('http://www.google.co.in/') as webpage:
        print(webpage)
        webpage_words = []
        for line in webpage:
            webpage_words = line.decode('utf-8').split()
            print(webpage_words)
except Exception:
    print("Found Exception")
