import msvcrt

while 1:
    if msvcrt.kbhit():
        print("inside loop")