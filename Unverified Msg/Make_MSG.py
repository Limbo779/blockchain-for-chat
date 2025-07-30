import json
import rsa
import os
import base64

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

def encrypt(msg,user) :
    global parent_dir
    file_path = os.path.join(parent_dir, 'Users/Userlog', f'{user}.pem')
    with open(file_path,'r') as f :
        pk=rsa.PublicKey.load_pkcs1(f.read())
    
    return rsa.encrypt(msg.encode(),pk)

def sign(msg) :
    global parent_dir
    file_path = os.path.join(parent_dir, 'Users', 'SK.pem')
    with open(file_path,'r') as f :
        sk=rsa.PrivateKey.load_pkcs1(f.read())
    
    return rsa.sign(msg.encode(),sk,"SHA-256")

def verify(message,signature,pk) :
    signature=base64.b64decode(signature)
    pk=rsa.PrivateKey.load_pkcs1(pk)
    try:
        rsa.verify(message.encode('utf-8'),signature,pk)
        return True
    except rsa.verification.VerificationError:
        return False

with open("convo.json","r") as f :
    convo=json.loads(f.read())

convo_no=str(len(convo.keys()))
msg_id=convo[convo_no][0]
pk1=convo[convo_no][1]
pk2=convo[convo_no][2]
sgn1=convo[convo_no][3]
sgn2=convo[convo_no][4]

print(verify(str(msg_id)+pk1+pk2+str(convo_no),sgn1,pk1))