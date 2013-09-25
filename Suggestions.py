import util
import Node

def run():
	getTopSuggestions(setup())

def setup():
	menuitems = ['Fries', 'Rice', 'Burgers', 'Cheeseburgers', 'Coca-cola', 'Fanta']
	
	primes = generatePrime(7919) #generates 1000 primes
	for index in range(len(menuitems)):
		menuitems[index] = [menuitems[index],primes[index]]

	root = createGraph(menuitems)
	pastorders = generateOrders(menuitems, 10, 3)

	for order in pastorders:
		addOrder(order,menuitems,root)

	return root

def createGraph(menuitems):
	root = Node({},menuitems,None)
	
	#creates graph

def generatePrime(n):
	primelist = []
	intlist = []
	for num in range(0,n):
		intlist.append([1,num])
	for index in range(2,n):
		if(intlist[index][0]==1):
			primelist.append(index)
			tindex = index
			while(tindex < n):
				intlist[tindex][0] = 0
				tindex += index
	return primelist

def getTopSuggestions(orderlist, root):
	stack = util.Stack()
	while(order.isSubset(node)!=1):

		for x in node.getSuccessors():
			if x is in order:
				node = x
	maxorder = 0
	order = None
	for x in node.getSuccessors():
		if(maxorder < x.getFrequency()):
			maxorder = x.getFrequency()
			order = x
	return order

def addOrder(orderlist, menuitem, root):
	visited = set()
    stack.push(root)
    while (stack.isEmpty()==0):
        node = stack.pop()
        subset = ordernode.isSubset(node)
        if subset==1:
			#found the last node to increment
        	node.incrementFrequency()
        	stack.clear()
        if subset==-1:
        	#not subset, ignore
        if subset==0:
        	#found subset, increment and keep goign
        	node.incrementFrequency()
        	if node not in visited:
            	visited.add(node)
            	successors = node.getSuccessors()
           	 	for index in range(0,len(successors)):
               		stack.push(Node(successors[index][0], node, successors[index][1], node.getCost() + successors[index][2]))
    return 0

#probability: 1/probability chance of individual menu being ordered
def generateOrders(menuitems, numorders, probability):
	pastorders = {}
	for orderindex in range(numorders):
		temporder = {}
		for menuindex in range(menuitems):
			if random.randint(0,probability-1)<1:
				temporder.append(menuitems[menuindex])
		pastorders.append(temporder)
	return pastorders



