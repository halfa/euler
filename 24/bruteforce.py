#!/usr/bin/python3

def unique(s):
  for c in range(0, len(s)):
    for d in range(c+1, len(s)):
      if s[c] == s[d]:
        return False
  return True

before = [None] * 100
def permut(n,r):
  if n == -1:
    return [""]
  else:
    if before[n-1] == None:
      before[n-1] = permut(n-1, r)


    res = []
    for i in r:
      if n > 4:
        print(i,n)
      for e in before[n-1]:
        candidate = i + e;
        if(unique(candidate)):
          res.append(candidate)

    return res

p = permut(3, ["0", "1", "2", "3"])
print(len(p))
print(p)