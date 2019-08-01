class Graph:

	def __init__(self):
		self.nodes = {}

	def id(self,id):
		return id;

	def node(self, id, convert = false):
		return self.nodes[id] if convert else self.nodes[self.id(id)]

	def data(self, node, content = -1):
		if content != -1:
			node.graph._data = content;
		return node.graph._data;

	def adjacent(self, a, b):
		return if b.id in a.graph

	def neighbors(self, node):
		return list(node.graph.keys());

	def connected(self, a, b):
		return false;

	def connect(self):
		# Initialize and reset connectivity
		nodes = list(self.nodes.values())
		marker = 0;

		for node in nodes:
			node.graph._connectivity = None


		# marks nodes connectivity
		for i in range(len(nodes)):

			if(nodes[i]._connectivity == None):
				continue

			stack = [nodes[i]]
			marker ++;

			while(len(stack) > 0):
				node = stack.pop(0)
				node.graph._connectivity = marker

				for neighbor in self.neighbors(node):
					if(neighbor.graph._connectivity == None and stack.index(neighbor) < 0):
						stack.append(neighbor)
            

    def add(self, node):
    	node.graph = {}
    	self.nodes[node.id] = node
    	return node;

    def delete(self, node):
    	del self.nodes[node.id]

    def edge(self, a, b, a_to_b = 1, b_to_a = 1):
    	if(!(if b.id in a.graph) or !(if a.id in b.graph)):
    		raise Exception('Nodes must be on same graph')

    	if(a_to_b == None):
    		del a.graph[b.id]
    	else:
    		a.graph[b.id] = a_to_b

    	if(b_to_a == None):
    		del b.graph[a.id]
    	else:
    	b.graph[a.id] = b_to_a

    def cost(self, a, b):
    	return 	a.graph[b.id] if self.adjacent(a,b) else None

class Node:
	"""docstring for Node"""
	def __init__(self, id, data):
		self.id = id
		self.graph = {}
		self.data = []

		for d in data:
			self.data.append(d)

class Heuristic:
	
	def manhattan(self, a, b, options = {}):
		dx = abs(b['x'] - a['x'])
		dy = abs(b['y'] - a['y'])
		return (options['multiplier'] or 1) * (dx + dy)

	def manhattanTorus(self, a, b, options = {}):
		dx = min(abs(b['x'] - a['x']), (b['x'] + (options['x'] or 0)) - a['x'], (a['x'] + (options['x'] or 0)) - b['x'])
		dy = min(abs(b['y'] - a['x']), (b['y'] + (options['y'] or 0)) - a['y'], (a['y'] + (options['x'] or 0)) - b['y'])
		return (options['multiplier'] or  1) * (dx + dy)

	def diagonal(a, b, options = {}):
		dx = abs(b['x'] - a['x'])
		dy = abs(b['y'] - a['y'])
		return (options['diagonalmultiplier'] or 1.4) * (dx + dy) + ((options['diagonalmultiplier'] or 1) - 2 * (options['multiplier'] or 1)) * min(dx, dy)

	def diagonalTorus(a, b, options = {}):
		dx = min(abs(b['x'] - a['x']), (b['x'] + (options['x'] or 0) - a['x']), (a['x'] + (options['x'] or 0) - b['x']))
		dy = min(abs(b['y'] - a['y']), (b['y'] + (options['y'] or 0) - a['y']), (a['y'] + (options['y'] or 0) - b['y']))
		return (options['multiplier'] or 1) * (dx + dy) + ((options['diagonalmultiplier'] or 1.4) - 2 * (options.multiplier or 1)) * min(dx, dy)

	def euclidian(a,b,options = {}):
		dx = abs(b['x'] - a['x'])
		dy = abs(b['y'] - a['y'])
		return (options['multiplier'] or 1) * sqrt(dx*dx + dy*dy)

	def euclidianTorus(a, b, options = {}):
		dx = min(abs(b['x'] - a['x']), (b['x'] + (options['x'] or 0)) - a['x'], (a['x'] + (options['x'] or 0)) - b['x'])
		dy = min(abs(b['y'] - a['y']), (b['y'] + (options['y'] or 0)) - a['y'], (a['y'] + (options['y'] or 0)) - b['y'])
		return (options['multiplier'] or 1) * (dx + dy) + ((options['diagonalmultiplier'] || 1.4) - 2 * (options['multiplier'] or 1)) * min(dx, dy);



