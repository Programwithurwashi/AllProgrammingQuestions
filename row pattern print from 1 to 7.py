#WAP to print this pattern
#1
#12
#123
#1234
#12345
#123456
#1234567

for i in range(1,9):
    for j in range(1,i):
        print(j,end=' ')
    print('')
        