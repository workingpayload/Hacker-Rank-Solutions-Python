# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

in_css = False

for _ in range(N):
    s = input()

    if '{' in s:
        in_css = True

    elif '}' in s:
        in_css = False

    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)
