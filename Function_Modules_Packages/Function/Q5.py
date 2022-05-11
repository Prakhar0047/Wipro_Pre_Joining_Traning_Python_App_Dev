def eve(ll):
  r = []
  for x in ll:
    if x%2==0:
      r.append(x)
  return r

l = list(map(int,input().split()))
eve(l)