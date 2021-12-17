even_list=[]
for i in range(1,299,1) :
    if ((i % 2)==0) :
      even_list.append(i)
print(even_list)
l=len(even_list)
cpt=0
print("The length of the previous list is :",len(even_list))
print('\nThe squared list values : \n')
for j in range(len(even_list)) :
 print((even_list[j])**2,'',sep=' ')
 cpt=cpt+1
if ((57 % 2 )!=0) :  print("57 is not an element from the list")