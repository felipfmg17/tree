import bintrees
from bintrees import RBTree

import sortedcontainers
	

tr = RBTree()

tr[3.57] = 1
tr[4.5] = 1
tr[4.05] = 1
del tr[4.05]

print(tr)
print(tr.min_item(),tr.max_item())


ar = [ i for i in range(100) ]

print( 5 in ar, 101 in ar)