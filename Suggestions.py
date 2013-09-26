import util
import Node

def run():
	getTopSuggestions(setup())

def setup():
	#create menu
	menuitems = ['Fries', 'Rice', 'Burgers', 'Cheeseburgers', 'Coca-cola', 'Fanta']
	#create prime numbers to use
	primes = generatePrime(7919) #generates 1000 primes
	for index in range(len(menuitems)):
		menuitems[index] = [menuitems[index],primes[index]]
	#create graph of possible orders
	root = createGraph(menuitems)
	#randomly generate pastorders for database
	pastorders = generateOrders(menuitems, 10, 3)
	#add to the graph
	for order in pastorders:
		addOrder(order,menuitems,root)
	return root

#creates graph of nodes by using bitshifts! (learned in CS2110 yoyoyo)
def createGraph(menuitems):
	root = Node({},menuitems)
	nodelist = {root}
	for num in range(1,2**len(menuitems)):
		orderlist = {}
		index = 0
		product = 1
		while(i>0):
			if(num & 1 == 1):
				orderlist.append(menuitems[index])
				product *= menuitems[index][1]
				index+=1
			num >>= 1
		nodelist.append(Node(orderlist,menuitems))
	for node in nodelist:
		node.createSuccessors(nodelist)
	return root

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
               		stack.push(Node())
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

#generates prime numbers less than or equal to n
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
	