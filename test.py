import hashlib

name = "www.facebook.com"

text = name.encode('utf-8')
hashed = hashlib.sha256(text).hexdigest()[:8]

print(str(hashed))

local_url = "http://127.0.0.1:5000/"+hashed
print(local_url)