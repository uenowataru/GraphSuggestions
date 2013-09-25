def run():
	getTopSuggestions(setup())

def setup():
	menuitems = {'Fries', 'Rice', 'Burgers', 'Cheeseburgers', 'Coca-cola', 'Fanta'}
	pastorders = generateOrders(menuitems, 10, 3)
	root = Node({})
	
	return root

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
	def __init__(self, orderlist, menuitems, parent):
        self.orderlist = orderlist
        self.menuitems = menuitems
        self.parent = parent
        self.frequency = 1

    def getParent(self):
    	return self.parent

    def getSuccessors(self):
        return self.parent

    def setSuccessor(self, node):
        return self.state

    def getCost(self):
        return self.cost

    def getFrequency():
    	return self.frequency

    def incrementFrequency():
    	self.frequency += 1
