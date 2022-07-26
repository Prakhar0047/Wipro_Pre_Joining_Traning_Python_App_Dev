from cgi import test


def isListOfInts(test_list):
  if type(test_list) != list:
    raise TypeError('Not A List')
  else:
    if len(test_list) == 0:
      return True
    elif len(test_list)>0:
      all([isinstance(item, int) for item in test_list])
      # for item in test_list:
      #   isinstance(item,int)
      return True
    else:
      return False

li = list(map(int,input().split()))
ans = isListOfInts(li)
print(ans)