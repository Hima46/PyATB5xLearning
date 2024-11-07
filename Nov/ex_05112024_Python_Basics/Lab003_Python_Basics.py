print('Hello World!')
print('HimaBindu')

#print(*values, sep=" ", end="\n", file=None, flush=False)`
# print(*values, *args, sep=" ", end="\n", file=None);`


# args - unlimited number of comma seperated arguments
print('HimaBindu', 123, 'Hello World', 'Welcome to Python Classes', '9876')
#  print('HimaBindu', 123, 'Hello World', 'Welcome to Python Classes', '9876') - IndentationError: unexpected indent

##sep -
print('HimaBindu', 123, 'Hello World', 'Welcome to Python Classes', '9876',sep='-')

#end="\n"
print('HimaBindu', 123, 'Hello World', 'Welcome to Python Classes', '9876',end='***')
print('HimaBindu', 123, 'Hello World', 'Welcome to Python Classes', '9876',sep='-')