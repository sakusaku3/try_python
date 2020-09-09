import os
import sys

def files(path):
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(pathname, filename)

def main():
    print('ディレクトリを指定してね!')
    dir = input()

    for file in files(dir):
        print(file)

if __name__ == '__main__':
    main()