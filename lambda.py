def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) # myfunc(2) will return a lambda function, so mydoubler = lambda a : a * 2 

print(mydoubler(11)) # It will print 22 as 11 will be passed to 'lambda a : a * 2' as a. So it will be 22 = 11 * 2