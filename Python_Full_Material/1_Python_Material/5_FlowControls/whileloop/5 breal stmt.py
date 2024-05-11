

#break stmt: whenever break stmt is used then ctrl comes out of that loop and stmts after
#            break are not executed.


x=1

while(True):
    print("hello")
    if(x==5):
        break
        print("hi")
    x=x+1
print("end")
