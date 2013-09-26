import Node
import Stack
import random

def run():
	#create menu
	menu = ['Fries', 'Rice', 'Burgers', 'Cheeseburgers', 'Coca-cola', 'Fanta']
	order = ['Fries', 'Rice']

	#initialize and obtain root of graph
	root = setup(menu)[0]

	print getTopSuggestions(order, menu, root).getOrderList()

def setup(menu):
	#creates item-prime pair
	menuitems = setMenuItems(menu)
	#create graph of possible orders
	nodelist = createGraph(menuitems)
	#randomly generate pastorders for database
	pastorders = generateOrders(menuitems, 10, 3)
	#add to the graph
	addOrders(pastorders, menuitems, nodelist)

	#for node in nodelist:
		#print node.getOrderList(), node.getFrequency()

	return nodelist

#creates graph of nodes by using bitshifts! (learned in CS2110 yoyoyo)
def createGraph(menuitems):
	#root = Node.Node([],menuitems)
	nodelist = []
	for num2n in range(0,2**len(menuitems)):
		orderlist = []
		index = 0
		product = 1
		num = num2n
		while(num>0):
			if((num & 1) == 1):
				orderlist.append(menuitems[index][0])
				product *= menuitems[index][1]
			index+=1
			num >>= 1
		nodelist.append(Node.Node(orderlist,menuitems))
	for node in nodelist:
		node.createSuccessors(nodelist)
	return nodelist

def getTopSuggestions(orderlist, menu, root):
	#create order node
	order = Node.Node(orderlist, setMenuItems(menu))

	#pseudo-dfs (might be faster using the nodelist and using prime numbers, but this works for now)
	stack = Stack.Stack()
	stack.push(root)
	while(not stack.isEmpty()):
		node = stack.pop()
		if(node.getProduct()==order.getProduct()):
			maxorder = -1
			order = None
			for x in node.getSuccessors():
				if(maxorder < x.getFrequency()):
					maxorder = x.getFrequency()
					order = x
			return order
		else:
			for nextnode in node.getSuccessors():
				stack.push(nextnode)

	

def addOrders(pastorders, menuitems, nodelist):
	for order in pastorders:
		addOrder(order, menuitems, nodelist)

def addOrder(orderlist, menuitems, nodelist):
	order = Node.Node(orderlist, menuitems)
	for node in nodelist:
		if(order.getProduct()%node.getProduct()==0):
			#print order.getProduct()%node.getProduct(), order.getProduct(), node.getProduct()
			node.incrementFrequency()


#probability: 1/probability chance of individual item in menuitems being ordered
def generateOrders(menuitems, numorders, probability):
	pastorders = []
	for orderindex in range(numorders):
		temporder = []
		for menuindex in range(len(menuitems)):
			if random.randint(0,probability-1)<1:
				temporder.append(menuitems[menuindex][0])
		pastorders.append(temporder)
	#print pastorders
	return pastorders

def setMenuItems(menu):
	menuitems = list(menu)
	#create prime numbers to use
	primes = generatePrime(7920) #generates 1000 primes
	for index in range(len(menu)):
		menuitems[index] = [menu[index],primes[index]]
	return menuitems

#generates prime numbers less than n
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

if __name__ == "__main__":
	print 'Runnning with default setting..'
	run()