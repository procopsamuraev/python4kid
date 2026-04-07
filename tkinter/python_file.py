import time

file = open('text_sample.txt', 'r+')
while True:
    line = file.readline().strip()
    if line:
        print(line)
    else:
        time.sleep(1)

