even_list=[]
for i in range(1,299) :
    if ((i % 2)==0) :
      even_list.append(i)
print(even_list)
print("The length of the previous list is :",len(even_list))
print('\nThe squared list values : \n')
for j in range(len(even_list)) :
 print((even_list[j])**2,'',sep=' ')
print(57 in even_list)
