import re
m=raw_input()
n=re.search(r'([A-Za-z0-9])\1+',m)
if n:
    print n.group(1)
else:
    print -1
