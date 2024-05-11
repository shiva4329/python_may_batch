MODULES :

Every python file by default is a module

ex:  sample.py
     --------
     --------
     -------- ----->module
     --------
     --------
A module consists of
1.Executable statements
2.Global variables
3.functions
4.classes

Main module : If you execute any module, then by default it is called as main module

we can use the properties of one module into another module by using import statement.

sub module:if a module has imported another module,then the imported module is called sub module

ex:   sample.py                 welcome.py    here welcome.py module imported sample.py module
      ---------                 ----------    so,welome.py can access the properties
      ---------    import       ----------    of both welcome.py and sample.py modules
      --------- --------------> ----------    welcome.py is called main module
      ---------                 ----------    sample.py is sub module of welcome.py
      ---------                 ----------

      len(),max(),min()etc are the builtin functions present in __builtins__module,but we can
      access them without importing __builtins__module

1.when i execute the main module(sample.py),then the total code of sample.py will be converted
  into bytecode(sample.pyc)and then it will be converted into machine code, once execution is
  completed,the byte code(sample.pyc) is deleted automatically.

2.when i execute the main module(welcome.py),it has a sub module(sample.py),
  so, 2 pyc files are generated for main module and sub module
  i.e welcome.pyc and sample.pyc
  if sample.pyc is already available,the it wont be generated again unless the source code
  (sample.py) is changed or modified
  once execution is completed,then the the main module.pyc file will be deleted but
  the sub module.pyc file wont be deleted.
  i.e welcome.pyc will be deleted   but sample.pyc remains permanently in hard disk.
3.if the source code(sample.py) is modified and if you execute welcome.py then sample.pyc file
  will be generated again along with welcome.pyc

Summary :
1.when you run the main module, then 2 pyc files will be generated for the main module and submodule
2.when the execution is completed,then mainmodule.pyc file will be deleted automatically and
  submodule.pyc remains
3.when 2nd time if you run the same module,then mainmodule.pyc file will be generated but
  submodule.pyc file wont be generated unless there are some changes or modifications.
4. when a module is imported it's execuable stmts will be executed automatically. 
      

  
  



















