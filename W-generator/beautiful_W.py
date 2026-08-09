"""
Description:    This was a more "elegant" approach I really liked when I first made it
Date:           05-03-2026
"""
n = int(input())
w = 3*n - 2

mh = n // 2
mw = w // 2

for i in range(n):
    line = ["." for _ in range(w)]
    
    line[i] = "#"
    line[w-i-1] = "#"
    
    if i >= mh:
        line[mw - (i - mh)] = "#"
        line[mw + (i - mh)] = "#"
    
    print("".join(line))
