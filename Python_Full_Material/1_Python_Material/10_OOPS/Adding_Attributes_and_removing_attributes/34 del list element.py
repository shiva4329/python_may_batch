x=[10,2.5,True,10,"python"] #list
print(x)     #Rc=1
del x[1]     #RC of float object becomes 0,so  float object removed, destructor called
print(x)
del x[0]     #RC was 2,becomes 1,destructor not called,
print(x)
del x[1]     #RC was 1,becomes 0,destructor called,int object removed
print(x)



