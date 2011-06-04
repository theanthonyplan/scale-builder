#Musical Scale Builder
#anthony gagliardo 6/3/11
#
#lol ok so this is real sloppy still, but heres how to run it:
#import from ui.py, "from ui import *"
#use start() to call the ui handler
#
#to add new scales, add the scale name and step progression to the scaleType dict
#you also need to add values to the scaleMapper dict to update the ui
#
#this is the data representaion of a piano scroll, indexes range [0-11]
fullScale = [ 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
#binds a value to the 12 notes - might be able to replace entirely with fullScale
letter_to_number = { 'a':0, 'a#':1, 'b':2, 'c':3, 'c#':4, 'd':5, 'd#':6, 'e':7,
	'f':8, 'f#':9, 'g':10, 'g#':11}
#converts user input scale-type name as a string
scaleMapper = { '1' : 'Major', '2' : 'Minor', '3' : 'Harmonic Minor', '4' : 'Melodic Minor',
	'5' : 'Diminished', '6' : 'Polytonal', '7' : 'Pentatonic', '8' : 'Blues',
	'9' : 'Gospel',}
#data model for the step patterns from the root note
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

#2 parameters:  root - integer value [0-11]	 
#				sType - name of scale as a string
def buildScale(root, sType):
	
	newScale = []
#append root note	
	newScale.append( fullScale[root] )
#iterate thru the step sequence, apply to root note, append to list	
	for i in scaleType[sType]:
		root = root + i 
		if(root > 11): root -= 12		#allows circular acces of list indexes (0,1...,10,11,12=0,13=1)
		newScale.append( fullScale[root] )
#return scale as a list	
	return newScale
	
	
	
	
	
	
	


