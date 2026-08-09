"""
Description:    This is a version I thought was faster... But no
Date:           05-03-2026
"""
n = int(input())

mw = (3*n - 2) // 2
mh = n // 2

image = ""

for i in range(n):
    image += "."*i + "#" # Big line
    
    if i < mh or i == n-1:
        image += "."*(mw - i) # Gap
    else:
        image += "."*(mw - 2*i - 1 + mh) # Gap 1
        image += "#" # Small line
        image += "."*(i - mh) # Gap 2
    
    image += image[-mw-1:-1][::-1] # Mirror
    image += "\n"

print(image)
