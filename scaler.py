#Musical Scale Builder
#anthony gagliardo 6/3/11
#
#THIS NEEDS TO BE REDESIGNED.  INSTEAD OF THIS UTTER CRAP, THIS MODULES
#FUNCTIONALITY SHOULD BE HANDLED BY A ROBUST MUSIC ENGINE THAT WILL
#INTERACT WITH INDIVIDUAL USER OBJECTS.
#
#PATTERNS NEED TO BE HARDCODED INTO THE DATABASE, WHICH WILL REQUIRE
#AN ABSTRACT SCALE/CHORD/NOTE OBJECT THAT HAS WILL BE SUBCLASSEDS
#
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
#data model for the step patterns from the root_note note
#THIS CODE SHOULD LIVE IN A DATABASE
scaleType = {
	'Major' : [2,2,1,2,2,2,1],
	'Minor' : [2,1,2,2,1,2,2],
	'Harmonic Minor' : [2,1,2,2,1,3,1],
	'Melodic Minor' : [2,1,2,2,2,2,1],
	'Diminished' : [2,1,2,1,2,1,2,1],
	'Polytonal' : [1,2,1,2,1,2,1,2],
	'Pentatonic' : [2,2,3,2,3],
	'Blues'	: [3,2,1,1,3,2],
	'Gospel' : [2,1,1,3,2,3],
	}

#2 parameters:  root_note - integer value [0-11]	 
#				sType - name of scale as a string
def buildScale(root_note, sType):
	
	newScale = []
	#append root_note note	
	newScale.append( fullScale[root_note] )
	#iterate thru the step sequence, apply to root_note note, append to list	
	for i in scaleType[sType]:
		root_note = root_note + i 
		if(root_note > 11): root_note -= 12		
		#allows circular acces of list indexes (0,1...,10,11,12=0,13=1)
		newScale.append( fullScale[root_note] )
	#return scale as a list	
	return newScale
	
	
	
	
	
	
	


