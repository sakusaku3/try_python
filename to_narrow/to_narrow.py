import sys
import re

import jaconv

s = re.compile(r'[！＂＃＄％＆＇（）＊＋，－．／０-９：；＜＝＞？＠Ａ-Ｚ［＼］＾＿｀>？＠ａ-ｚ｛｜｝～]')

trans_table = str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})

def main():
    text = sys.argv[1]
    print(to_narrow(text))

def to_narrow(text):
    to_up = jaconv.h2z(text,digit=True,ascii=True) 
    return s.sub(to_narrow_core, to_up)

def to_narrow_core(match):
    value = match.group()
    return value.translate(trans_table)

if __name__ == "__main__":
    main()