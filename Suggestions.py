def run():
	getTopSuggestions(setup())

def setup():
	menuitems = ['Fries', 'Rice', 'Burgers', 'Cheeseburgers', 'Coca-cola', 'Fanta']
	
	primes = generatePrime(7919) #generates 1000 primes
	for index in range(len(menuitems):
		menuitems[index] = [menuitems[index],primes[index]]

	pastorders = generateOrders(menuitems, 10, 3)
	root = Node({})

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
				print index, tindex
				intlist[tindex][0] = 0
				tindex += index
	return primelist

def getTopSuggestions(orderlist, root):
	while(node not order):
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
	def __init__(self, orderlist, menuitems, parent, product):
        self.orderlist = orderlist
        self.menuitems = menuitems
        self.parent = parent
        self.successors = {}
        self.frequency = 0
        self.product = product 

    #returns -1 if not subset
    #returns 0 if subset
    #returns 1 if equal
    def isSubset(self, node):
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

    def getCost(self):
        return self.cost

    def getFrequency():
    	return self.frequency

    def incrementFrequency():
    	self.frequency += 1
