graph = {
  'P' : ['Q','R','S'],
  'Q' : ['P', 'R'],
  'R' : ['P','Q','T'],
  'S' : ['P'],
  'T' : ['R']
  
}

list1=[]

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


def dfs(visited, graph, node):
    if node not in visited:
        list1.append(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
          



while(True):
	visited = [] 
	queue = []    
	print("\n")
	print('*'*10,"MENU",'*'*10)
	print("\n")
	print("1.BFS\n2.DFS\n3.Exit")
	print("\n")
	ch=int(input("Enter your choice : "))
	if ch==1:
		print("Following is the Breadth-First Search")
		bfs(visited, graph, 'T')  
		
	elif ch==2:
		print("Following is the Depth-First Search")
		dfs(visited, graph, 'T')
		for i in list1:
			print(i,end=' ')
		 
	else:
		break
