## Alo Raha?

n=input()
A=input().split()
B=[]
for i in range(len(A)):
    zar=1
    for j in range(len(A)):
        if (i!=j):zar=zar*int(A[j])
    B.append(zar%int(A[i]))
print(B.index(max(B))+1)


#############################

# Riazi is simple
A=str(input())
for i in range(len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            a=A[i:j]
            b=A[j:k]
            c=A[k:len(A)+1]

###########################
# Ramz va dast  garmi

AA=input()
BB=input()
AA=AA.replace(".","")
AA=AA.replace("?","")
A=AA.split(" ")
B=BB.split(" ")
output=[]
for j in B:
    k,h=j.split(":")
    output.append(A[int(k)-1][int(h)-1])
print("".join(output).upper())

#############################

# Top bazi !
print("RAHA")


############################

            if int(a)+int(b)==int(c):
                print (j-i,k-j,len(A)-k)
                break

##############################

# Saf mehmani Arian
n, m =input().split()
mehman=[]
for i in range(int(n)):
    mehman.append(input().split())

for kol in range(int(n)):
    abn=[1]*int(m)
    shad=0
    for i in range(int(n)-kol):
        a=mehman[i][0]
        b=mehman[i][1]
        if abn[int(a)-1]:
            shad=shad+1
            abn[int(a)-1]=0
        elif abn[int(b)-1]:
            shad=shad+1
            abn[int(b)-1]=0
    print(shad)
    if len(mehman)>0:del mehman[0]

###################################
# esme sherkat:

A=input()
B=input()
output=[]
AA=list(A)
BB=list(B)
for i in range(int(len(AA)/2+0.5)):
    k='z'
    index=0
    for j in range(len(AA)):
        if AA[j]<k:
            k=AA[j]
            index=j
    AA[index]='z'
    output.append(k)
    if len(output)<len(BB):
        b='a'
        index=0
        for j in range(len(BB)):
            if BB[j]>b:
                b=BB[j]
                index=j
        BB[index]='a'
        output.append(b)
print(''.join(output))

####################################

# prime numbers :
final = [1,2,3,5]
for i in range(0,12):
  tmp2 = [num * 2 for num in final]
  tmp3 = [num * 3 for num in final]
  tmp5 = [num * 5 for num in final]
  final = list(set(tmp2+final))
  final = list(set(tmp3+final))
  final = list(set(tmp5+final))

final.sort()







