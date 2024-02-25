n=int(input("Enter the no. of elements : "))
list1=[]
for i in range(n):
	list1.append(int(input("Enter the elements : ")))
	
print("The elements in the list are : ")
for i in range(n):
	print(list1[i],end=" ")
print("\n")
print("Performing Selection sort!!")
for i in range(n):
	minm=i
	for j in range(i+1,n):
		if (list1[minm]>list1[j]):
			temp_index=list1[minm]
			list1[minm]=list1[j]
			list1[j]=temp_index
			
print("Sorted list of elements is : ")
for i in range(n):
	print(list1[i],end=" ")
print("\n")