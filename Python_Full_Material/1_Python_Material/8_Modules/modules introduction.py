Modular Programming:

Module: Every python program by default is a module

sample.py
........
........
........
........

A module consists of

1.Executable statements
2.Global variables
3.Functions
4.Classes

main module: if i execute any module , by default it is main module.

we can import the properties of one module into another module using import stmt.

sub-module:if a module imported another module, then the imported module is called as sub-module

sample.py                         Test.py  -------->here Test.py is the main module which  
.........                       ...........         contains sample.py as submodule
.........                       ...........         Test.py can access the properties of both
.........-------import------->  ...........         the modules
.........                       ...........
.........                       ...........


1)If i execute the main module(sample.py) then the code of sample.py will be converted to
  intermediate code called as byte code(.pyc file) and later it is converted to machine code
  and is executed. once execution is complted then the bytecode(sample.pyc) will be deleted
  automatically.

2)If i execute the main module(Test.py) then as it has sub-module(Sample.py),
  so here 2 .pyc files will be generated for main module and sub-module respectively
  i.e Test.pyc and sample.pyc .
  if sub-module.pyc is already existing  then again it wont be generated untill or unless
  the  code of sub-module is modified.
  once the execution is completed then mainmodule .pyc file will be deleted automatically
  but sub-module .pyc file still remains
  i.e Test.pyc will be deleted and sample.pyc still remains.

  If i execute Test.py for the second time then only main module(Test.pyc) will be generated
  but sub-module.pyc wont be generated as it is available already.

3)Before executing main module(Test.py) for the 3rd time , i will modify or change the code
  in sample.py and will execute main module(Test.py) then 2 .pyc files are generated
  for main and sub-module respectively

4)all the executable stmts of the sub-module will be executed automatically within the main module












  







