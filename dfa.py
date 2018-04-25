#Fernanda Beatriz J. R. Dallaqua
#Deterministic Finite Automaton implementation
#Input data: file containing transition function, initial and final states and strings to be analyzed 

import sys


def automaton(initial_state, final_states, transition_function, string):
#Function that begins in the initial state of the automaton and steps through the string symbol by symbol, updating the state. When the string ends it's analyzed if the actual state is a final state or not. The actual state and if the string is accepted or rejected by the automaton are printed. 
	actual_state = initial_state[0]
	#if string is the empty string (e) the automaton will stay at the initial state.  	
	if string != 'e':
		for s in string:
			#must analyze if exists transition from the actual_state to another by reading the current symbol
			# if it exists, go to next state. Else, the execution of the automaton stops, making impossible to read all the string
			if s in transition_function[actual_state]:
				actual_state = transition_function[actual_state][s]
			else:
				print 'EXECUTION STOPS AT '+actual_state+'. TRANSITION FUNCTION UNDEFINED FOR SYMBOL '+s+':REJECTED.'
				return
	if actual_state in final_states:
		print actual_state+':ACCEPTED'
	else:
		print actual_state+':REJECTED'

if __name__ == "__main__":
	#open the file and divide the information
	m = open(sys.argv[1],'r')
	lm = m.read()
	definitions = lm.split('#')
	transitions = definitions[0].split('\n')
	initial = definitions[1].split('\n')
	finals = definitions[2].split()
	strings = definitions[3].split('\n')
	#get rid of empty elements
	transitions = filter(None, transitions)
	initial = filter(None, initial)
	finals = filter(None, finals)
	strings = filter(None, strings)
	states = []
	alphabet = []
	transitions_dict = {}
	#create a dictionary of dictionaries for the automaton's transition function
	for line in transitions:
		aux = line.split(' ')
		siz = len(aux)
		if aux[0] not in states:
			states.append(aux[0])
		i = 1
		transitions_dict[aux[0]] = {aux[i]:aux[i+1]}
		if aux[i] not in alphabet:
			alphabet.append(aux[i])
		i += 2
		while i < siz:
			transitions_dict[aux[0]].update({aux[i]:aux[i+1]})	 
			if aux[i] not in alphabet:
				alphabet.append(aux[i])				
			i+=2
	#print automaton's information	
	print 'STATES OF THE AUTOMATON'
	print states
	print 'INITIAL STATE'
	print initial
	print 'FINAL STATES'
	print finals
	print 'ALPHABET'
	print alphabet
	#for each string, analyze if it is accepted or rejected by the automaton
	for s in strings:
		print '----------'		
		print 'STRING:'+s
		automaton(initial, finals, transitions_dict, s)	
		

