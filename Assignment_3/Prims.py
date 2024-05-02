class Tree:
    def __init__(self):
        self.arr = []
        self.v = 0
        self.e = 0
        self.weight = 0
        self.v_array = []
        self.up_vertex = 0
        self.low_vertex = 0
        self.vertex_map = {}  # Map string vertices to integer indices

    def tree_create(self):
        print("Enter the no. of vertices: ")
        self.v = int(input())
        
        print("Enter the no. of edges: ")
        self.e = int(input())

        self.v_array = [0] * self.v

        print("Contents of visited array before traversal are : ")
        print(self.v_array)

        self.arr = [[999] * self.v for _ in range(self.v)]

        print("Adjacency Matrix initialization : ")
        for row in self.arr:
            print(row)

        # Clear existing vertex map
        self.vertex_map.clear()

        # Accept string vertices and map them to indices
        for i in range(self.v):
            vertex = input(f"Enter vertex {i + 1}: ")
            self.vertex_map[vertex] = i

        for _ in range(self.e):
            print("Enter the vertices present at end point of edges :")
            up_vertex, low_vertex = input().split()
            self.up_vertex = self.vertex_map[up_vertex]
            self.low_vertex = self.vertex_map[low_vertex]

            print(f"Enter the weight present between {up_vertex} and {low_vertex}: ")
            self.weight = int(input())

            # now we update the adjacency matrix by weight between the vertices
            self.arr[self.low_vertex][self.up_vertex] = self.arr[self.up_vertex][self.low_vertex] = self.weight

        print("Adjacency Matrix after updation is : ")
        for row in self.arr:
            print("\t".join(map(str, row)))

    def min_path(self):
        if not hasattr(self, 'v_array'):
            print("Please create the tree first.")
            return

        p = q = total = count = 0
        min_val = 0
        
        self.v_array[0] = 1
        
        while count < self.v - 1:
            min_val = 999
            for i in range(self.v):
                if self.v_array[i] == 1:
                    for j in range(self.v):
                        if self.v_array[j] != 1:
                            if min_val > self.arr[i][j]:
                                min_val = self.arr[i][j]
                                p = i
                                q = j
            self.v_array[p] = 1
            self.v_array[q] = 1
            total += min_val

            # Convert indices to string vertices using the vertex_map
            vertex_p = list(self.vertex_map.keys())[list(self.vertex_map.values()).index(p)]
            vertex_q = list(self.vertex_map.keys())[list(self.vertex_map.values()).index(q)]

            print(f"The minimum path found is {vertex_p} -> {vertex_q} with cost: {min_val}")
            count += 1

        print("The minimum cost after traversal using Prim's algorithm is:", total)


if __name__ == "__main__":
    t = Tree()
    ans = 0

    while ans != 2:
        print("**********MENU**********")
        print("1. Create the tree of Phone lines")
        print("2. Find the Minimum Spanning Tree (MST)")
        print("3. Exit")
        print("Enter your choice: ")

        ch = int(input())
        if ch == 1:
            t.tree_create()
        elif ch == 2:
            t.min_path()
        elif ch == 3:
            print("Exited successfully from the program!!")
            break
        else:
            print("You have entered a wrong choice. Please try again!!")

        print("\nDo you want to continue?\n1. Yes\n2. No")
        ans = int(input())

    if ans == 2:
        print("Exited successfully!!")
        
'''
Output : 
PS D:\Ayush\College\Sem VI\Lab\AI> python -u "d:\Ayush\College\Sem VI\Lab\AI\Prims.py"
**********MENU**********
1. Create the tree of Phone lines
2. Find the Minimum Spanning Tree (MST)
3. Exit
Enter your choice:
1
Enter the no. of vertices:
4
Enter the no. of edges:
5
Contents of visited array before traversal are :
[0, 0, 0, 0]
Adjacency Matrix initialization :
[999, 999, 999, 999]
[999, 999, 999, 999]
[999, 999, 999, 999]
[999, 999, 999, 999]
Enter vertex 1: 0
Enter vertex 2: 1
Enter vertex 3: 2
Enter vertex 4: 3
Enter the vertices present at end point of edges :
0 1
Enter the weight present between 0 and 1:
5
Enter the vertices present at end point of edges :
0 2
Enter the weight present between 0 and 2:
8
Enter the vertices present at end point of edges :
1 2
Enter the weight present between 1 and 2:
10
Enter the vertices present at end point of edges :
1 3
Enter the weight present between 1 and 3:
15
Enter the vertices present at end point of edges :
2 3
Enter the weight present between 2 and 3:
20
Adjacency Matrix after updation is :
999     5       8       999
5       999     10      15
8       10      999     20
999     15      20      999

Do you want to continue?
1. Yes
2. No
1
**********MENU**********
1. Create the tree of Phone lines
2. Find the Minimum Spanning Tree (MST)
3. Exit
Enter your choice:
2
The minimum path found is 0 -> 1 with cost: 5
The minimum path found is 0 -> 2 with cost: 8
The minimum path found is 1 -> 3 with cost: 15
The minimum cost after traversal using Prim's algorithm is: 28

Do you want to continue?
1. Yes
2. No
2
Exited successfully!!
PS D:\Ayush\College\Sem VI\Lab\AI> 
'''
