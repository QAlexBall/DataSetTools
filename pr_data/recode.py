import os
files = os.listdir('./TextFile/')
for file in files:
	f = open(os.path.join('./TextFile/' + file))
	s = f.read()
	s = s.decode('gb2312')
	s = s.encode('utf-8')
	f = open(os.path.join('./TextFile/' + file), "w")
	f.write(str(s))