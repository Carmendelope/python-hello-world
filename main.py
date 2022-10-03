import sys
import time


def main():
    args = sys.argv[1:]
    x = args[0]
    print("Hello " + x + "!")
    time.sleep(5 * 60)

if    __name__    ==     "__main__"      :
   main()