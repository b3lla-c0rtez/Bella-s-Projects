def foo(astr):
    myD = {}

    for ch in astr:
        if ch in myD:
            myD[ch] += 1
        else:
            myD[ch] = 1
	    
    valL = myD.values()
    ct = min(valL)
	    
    myS = []
	    
    for item in myD:
        if myD[item] == ct: 
            myS.append(item)
	            
    return myS
