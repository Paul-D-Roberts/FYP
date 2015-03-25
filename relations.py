# Same structure as Graph files with the exception
# of every element being related to itself, turning
# all graphs into a relation on itself.

R = [{1, 2, 3}, {'A': [1, 2, 'A'],
                 'B': [2, 3, 'B'],
                 1: [1],
                 2: [2],
                 3: [3]}]

subR = [{3}, {3: [3]}]

subR2 = [{2, 3}, {'B': [2, 3, 'B'],
                  2: [2], 3: [3]}]


