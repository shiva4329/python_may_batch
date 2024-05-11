#Flow Control Stmts:

-By default Every python stmt executes only once from top to bottom.

-Inorder to execute set of stmts for multiple times , we go for flow control stmts or Control structures

-in order to execute /not to execute set of stmts , we go for flow control stmts

Flow Control stmts are divided into 2 parts:

i.Condition : An  Expression which returns a boolean value

ii.Block/Clause : set of stmts following the same space indentation.

various flow control stmts /control structures are:
    1.if
    2.if-else
    3.elif
    4.while loop
    5.for loop

syntax of if-else:

if(condition):
    stmt1
    stmt2
    stmt3------->Block1/Clause
    stmt4
else:
    stmt5
    stmt6------>Block2/Clause
    stmt7
    stmt8

if condition is true then stmts within if-block (Block1) will be executed
if condition is false then stmts within else block(Block2) will be executed

Nested Blocks: Blocks within a block

if(condition):
    stmt1
    stmt2
    if(condition):
        stmt3
        stmt4
        stmt5
    stmt6
    stmt7
else:
    stmt8
    stmt9
    stmt10


ex:

if(age>=18):
    ........
    ........
    if(state=="local"):
        .........
        .........
        print("Eligible to vote")


























    
