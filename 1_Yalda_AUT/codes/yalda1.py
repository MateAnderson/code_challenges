AA=input()
BB=input()
A=AA.split(' ')
B=BB.split(' ')
output=[]
for j in B:
    k,h=j.split(':')
    output.append(A[int(k)-1][int(h)-1])
print(''.join(output).upper())
