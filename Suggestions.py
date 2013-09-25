import util

def run():
	getTopSuggestions(setup())

def setup():
	menuitems = ['Fries', 'Rice', 'Burgers', 'Cheeseburgers', 'Coca-cola', 'Fanta']
	
	primes = generatePrime(7919) #generates 1000 primes
	for index in range(len(menuitems)):
		menuitems[index] = [menuitems[index],primes[index]]

	pastorders = generateOrders(menuitems, 10, 3)
	root = Node({})

	#call addOrder

	return root

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
    ordernode = Node(orderlist, menuitems, None)
    while (stack.isEmpty()==0):
        node = stack.pop()
        subset = ordernode.isSubset(node)
        if subset==1:
        	#found the last node to increment
        if subset==0:
        	#found subset, increment and keep goign
        if subset==-1:
        	#not subset, ignore
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

class Node:
	def __init__(self, orderlist, menuitems, parent):
        self.orderlist = orderlist
        self.menuitems = menuitems
        self.parent = parent
        self.successors = []
        self.frequency = 0
        self.product = 1
        for p in menuitems[:,0]:
        	self.product*=p
        __createSuccessors()

    #returns -1 if node not subset
    #returns 0 if node is subset of this
    #returns 1 if node is equal to this
    def isSubset(self, node):
    	if(node.getProduct()==self.product):
    		return 1
    	if(self.product%node.getProduct()==0):
    		return 0
    	return -1

    #slower version
    def isSubset2(self, node):
    	for item in node.getOrders():
    		found = False
    		for item2 in self.orderlist:
    			if item==item2:
    				found = True
    		if not found:
    			return -1
    	if(len(node.getOrders())==len(self.orderlist)):
    		return 1
    	return 0

    def getParent(self):
    	return self.parent

    def getSuccessors(self):
        return self.successors

    def addSuccessor(self, node):
        self.successors.append(node)

    def __createSuccessors(self):
    	for index in range(menuitems):
  		  	temporder = list(orderlist)
  		  	adding = True
  		  	for item in tempmenu:
  		  		finding = True
  		  		for item2 in temporder:
  		  			if(finding and item==item2)
  		  				finding = False
  		  		if(adding and finding):
  		  			temporder.append(item)
  		  			adding = False
  		  	if(not adding):
	  		  	successors.append(Node(temporder,menuitems,self)

    def getCost(self):
        return self.cost

    def getFrequency():
    	return self.frequency

    def incrementFrequency():
    	self.frequency += 1

    def getProduct():
    	return self.product

