


#if file exists then remove else say file doesnt exist


import os

if(os.path.exists("C:/digitalnest930am/list3.py")):
    os.remove("C:/digitalnest930am/list3.py")
else:
    print("file doesnt exist")

print(os.listdir("C:/digitalnest930am"))
