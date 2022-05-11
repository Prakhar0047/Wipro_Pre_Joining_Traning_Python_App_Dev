def hypen_sort(st):
  temp = st.split("-")
  t = sorted(temp)
  x = "-".join(t)
  return x

s = input()
hypen_sort(s)