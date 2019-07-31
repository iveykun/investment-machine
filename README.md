# investment-machine
a fun investment machine

How it works:

Exploration phase:
The algorithm loops the first machine 5 times, and checks if the win ratio is over 0.5
If it is, it labels that machine as the most profitable one
Else, it continues for another 5 times on the second machine and then uses whichever machine has a higher win ratio for the Exploitation phase
This permits a saving of 0-5 investment chances, 50% of the time

Exploitation phase:
Things that can be changed: the number of runs, the money invested
For the money invested, I ran the program into another “fake machine learning program” that compiled a list of all SR for many denominators, then I picked the one with the highest SR (total money/u, u being the denominator)
Then the program exploits as usual
