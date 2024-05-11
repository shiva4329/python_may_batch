#If i want to execute a module more than once then i have a function called
#reload() present in imp module

import hai
import imp  #pre-defined module  
print("welcome")
imp.reload(hai)
imp.reload(hai)
imp.reload(hai)
