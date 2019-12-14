from p1.file1 import func1,a # less time consume and also memory
from p1.file2 import func1
func1() # it is taking file2 func
func1() # it is also taking file2 func as it replace the address
print(a)
