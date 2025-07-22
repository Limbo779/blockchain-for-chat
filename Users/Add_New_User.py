import rsa

def make_entry(x):
    pk,sk=rsa.newkeys(1024)
    with open(f"Userlog/{x}.pem","wb") as file :
        file.write(pk.save_pkcs1("PEM"))
    
    with open("Userlog/Userlog.txt","a") as f :
        f.writelines(x+"\n")

    with open("SK.pem","wb") as F :
        F.write(sk.save_pkcs1("PEM"))

username=input("Enter the username you want : ")

with open("Userlog/Userlog.txt","r") as f :
    names=f.readlines()
    l=[]
    for i in names :
        n=len(i)
        l.append(i[0:n-1])
    names=l
    print(names)

if username in names : 
    while True :
        username=input("Enter the name once again , already taken : ")
        if username in names : 
            continue
        else:
            make_entry(username) 
            print("User Added")
            break
else:
    make_entry(username)
    print("User Added")
