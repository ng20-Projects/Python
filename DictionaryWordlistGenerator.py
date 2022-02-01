#Dictionary Wordlist Generator

Var_List = []
Var_List = input("Enter the Words with space: ").split()
length = len(Var_List)
#fact=length
l=length
# while(length>1):
#     fact=fact*(length-1)
#     length-=1
print(Var_List)
#print(fact)
for i in range(0,l):
    for j in range(0,l):
        for k in range(0,l):
            if i==j and j==k or i==j or i==k or j==k:
                pass
            else: print(Var_List[i]+Var_List[j]+Var_List[k])