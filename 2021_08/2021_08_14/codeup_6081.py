inputNum = int(input(),16)

for i in range(1,16):
  print('%X'%inputNum, '*' , '%X'%i , '=' , '%X'%(i*inputNum), sep='')