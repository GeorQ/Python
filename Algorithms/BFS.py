from queue import Queue

adj_list = {
		"S" :["A", "B"],
		"A" :["A1", "A2"],
		"B" :["B1", "B2"],
		"A1":["A3", "A4"],
		"B1":["B3", "B4"],
		"A2":["A5", "A6"],
		"B2":["B5", "B6"],
		"A3":["A7", "A8"],
		"B3":["B7", "B8"],
		"A4":[],
		"B4":[],
		"A5":[],
		"B5":[],
		"A6":[],
		"B6":[],
		"A7":[],
		"B7":[],
		"A8":[],
		"B8":[]
	       }	

list123 = {	
			"A":["B", "D"],
			"B":["A", "C"],
			"C":["B"],
			"D":["A", "E", "F"],
			"E":["D", "F", "G"],
			"F":["D", "E", "H"],
			"G":["E", "H"],
			"H":["G", "F"]
		 }

visited = {}
level = {}
parent = {}
bfs_output = []
queue = Queue()

for node in adj_list.keys():
	visited[node] = False
	parent[node] = None
	level[node] = -1

desireNode = "A4"
s = "S"
visited[s] = True
level[s] = 0
queue.put(s)
Found = False


while not queue.empty() and not Found:
	u = queue.get()
	bfs_output.append(u)
	if u == desireNode:
		break
	for v in adj_list[u]:
		if not visited[v]:
			visited[v] = True
			parent[v] = u
			#level[v] = level[u] + 1
			queue.put(v)
print(parent.get(bfs_output[len(bfs_output) - 1]))
print(bfs_output)



