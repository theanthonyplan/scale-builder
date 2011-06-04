from scaler import *

def start():	
	print "This program builds scales based on user input"
	
	print "Select a root note:\n"
	print fullScale
	print
	print
		
	note_by_letter = raw_input()
	note_by_number = (letter_to_number[note_by_letter])
	
	print
	print
	
	print "Which type of scale?\n"

	for q in range(1, len(scaleType)+1) :
		print q, '-', scaleMapper[str(q)]
		
	print	
	scale_input = raw_input()
	scale_type = scaleMapper[scale_input]
	
	print
	print
	print "Building ", fullScale[note_by_number], "scale..."
	
	print buildScale(note_by_number,scale_type)