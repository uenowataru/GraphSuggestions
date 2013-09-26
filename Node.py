class Node:
    def __init__(self, orderlist, menuitems):
        self.orderlist = orderlist
        self.menuitems = menuitems
        self.successors = []
        self.frequency = 0
        self.product = self.createProduct()

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

    #def getParent(self):
    	#return self.parent
    def createProduct(self):
        product = 1
        for item in self.orderlist:
            for item2 in self.menuitems:
                #print item, item2[0]
                if(item==item2[0]):
                    product*=item2[1]
        return product

    def getSuccessors(self):
        return self.successors

    def addSuccessor(self, node):
        self.successors.append(node)

    def createSuccessors(self, nodelist):
        for index in range(len(self.menuitems)):
            for node in nodelist:
                if(self.menuitems[index][1]*self.product==node.getProduct()):
                    self.successors.append(node)

    def setSuccessors(self, successors):
        self.successors = successors

    def getFrequency(self):
    	return self.frequency

    def incrementFrequency(self):
    	self.frequency += 1

    def getProduct(self):
    	return self.product

    def getOrderList(self):
        return self.orderlist

