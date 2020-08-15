from time import*  
from datetime import datetime as t  

host_path = r"C:\Windows\System32\drivers\etc\hosts"  
redirect = "127.0.0.1"  
web = []
n=int(input("Enter the number of Websites to be blocked:"))
print("Enter the URL of the website:")
for i in range(n):
    x=input()
    web.append(x)  
    
if t(t.now().year,t.now().month,t.now().day,8)<t.now()<t(t.now().year,t.now().month,t.now().day,14):  
    with open(host_path,"r+") as fileptr: 
        print("website blocked") 
        content = fileptr.read()  
        for website in websites:  
            if website in content:  
                pass  
            else:  
                fileptr.write(redirect+"\t"+website+"\n")  
else:  
    with open(host_path,'r+') as file:  
        content = file.readlines();  
        file.seek(0)  
        for line in content:  
            if not any(website in line for website in  websites):  
                file.write(line)  
        file.truncate()  
        print("website unblocked!!")
