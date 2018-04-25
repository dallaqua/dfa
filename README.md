# dfa.py
Deterministic Finite Automaton Python implementation 

This code implements a DFA by receiving a file containing transition function, initial and final states and strings to be analyzed as input data.
It opens the file and divides the basic information about the DFA, creating a dictionary of dictionaries for the transition function. 
For each string it is analyzed each symbol, if exists transition function from the actual state to another by reading the current symbol. If it exists, go to next state; else, the execution of the automaton stops and the string is rejected.
Finishing the reading of the symbols it is analyzed if the reached state is a final state or not. If it is, the string is accepted by the automaton; else, the string is rejected.

Some files with examples of automata (.dat extension) are made available in this repository. The file script_dfa.sh executes all the .dat files and gives a description of each automaton. 

