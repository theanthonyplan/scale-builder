#Musical Scale Builder
#anthony gagliardo 6/3/11

fullScale = [ 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']

letter_to_number = { 'a':0, 'a#':1, 'b':2, 'c':3, 'c#':4, 'd':5, 'd#':6, 'e':7,
	'f':8, 'f#':9, 'g':10, 'g#':11}

scaleMapper = { '1' : 'Major', '2' : 'Minor', '3' : 'Harmonic Minor', '4' : 'Melodic Minor',
	'5' : 'Diminished', '6' : 'Polytonal', '7' : 'Pentatonic', '8' : 'Blues',
	'9' : 'Gospel',}

scaleType = { 'Major' : [2,2,1,2,2,2,1],
	'Minor' : [2,1,2,2,1,2,2],
	'Harmonic Minor' : [2,1,2,2,1,3,1],
	'Melodic Minor' : [2,1,2,2,2,2,1],
	'Diminished' : [2,1,2,1,2,1,2,1],
	'Polytonal' : [1,2,1,2,1,2,1,2],
	'Pentatonic' : [2,2,3,2,3],
	'Blues'	: [3,2,1,1,3,2],
	'Gospel' : [2,1,1,3,2,3],
	}

	
def buildScale(root, sType):
	
	newScale = []
	
	newScale.append( fullScale[root] )
	
	for i in scaleType[sType]:
		root = root + i 
		if(root > 11): root -= 12
		newScale.append( fullScale[root] )
	
	return newScale
	
	
	
	
	
	
	


