import json
import rsa
import base64

pk1,sk1=rsa.newkeys(1024)
pk2,sk2=rsa.newkeys(1024)

msg_id=569
pk1=pk1.save_pkcs1().decode('ascii')
pk2=pk2.save_pkcs1().decode('ascii')
convo_no=5
msg=str(msg_id)+pk1+pk2+f"{convo_no}"

sgn1=rsa.sign(msg.encode(),sk1,"SHA-256")
sgn2=rsa.sign(msg.encode(),sk2,"SHA-256")
sgn1=base64.b64encode(sgn1).decode('ascii')
sgn2=base64.b64encode(sgn2).decode('ascii')

with open('convo.json','r') as f :
    data=json.loads(f.read())

data[convo_no]=[msg_id,pk1,pk2,sgn1,sgn2]

data=json.dumps(data,indent=2)

with open('convo.json','w') as file :
    file.write(data)
