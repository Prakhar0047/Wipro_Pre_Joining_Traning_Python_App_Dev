def digit_sum(num):
  strr = str(num)
  list_of_number = list(map(int, strr.strip()))
  return sum(list_of_number)

n = int(input())
digit_sum(n)