def ruler(num):
  q, mod = divmod(num, 10)
  l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  a = l*q+l[:mod]
  answer = "".join(a)
  return answer


x = int(input())
ans = ruler(x)
print(ans)
