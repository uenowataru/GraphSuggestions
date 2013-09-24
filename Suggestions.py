def getTopSuggestions(Set order):
	node = rootnode({})
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