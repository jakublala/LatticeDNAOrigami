import numpy as np
#import sys

sequenceLength = input('Enter sequence length:')
length = int(sequenceLength) #int(sys.argv[1])

sequence = ''.join(np.random.choice(['A', 'C', 'G', 'T'], size=length).tolist())
print(sequence)
