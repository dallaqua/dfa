#Examples
echo '*****s terminates with aaa*****'
python dfa.py afd.dat
echo '*****s contains aa or bb as substring*****'
python dfa.py afd2.dat
echo '*****s terminates with symbol 1 or has even number of 0s after the last 1*****'
python dfa.py afd3.dat
echo '*****s has (odd number of as and even number of bs) or (even number of as and odd number of bs)*****'
python dfa.py afd4.dat
echo '*****s has even number of as and even number of bs*****'
python dfa.py afd5.dat
echo '*****s represents numbers that can start with minus sign, followed by one or more decimal digits, and with an optional decimal point, that is followed by one or more decimal digits*****'
python dfa.py afd6.dat

