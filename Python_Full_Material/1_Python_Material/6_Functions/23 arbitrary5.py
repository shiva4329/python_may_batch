def display(*p,q,r=20):
    print(p,type(p),len(p))
    print(q,type(q))
    print(r,type(r))
    
display(30,40,50,q=60)
display((10,20,30),q=40,r=50)
