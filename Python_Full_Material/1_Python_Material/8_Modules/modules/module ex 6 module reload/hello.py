import hai
import hai
import hai#even though hai module is imported for 3 times,still executed only once
#bcoz when first time hai module is imported,it is loaded into memory and
#.pyc file is generated,when 2nd time it is imported,it wont create the .pyc file
#bcoz already available,so once it is executed
print("hello......")

