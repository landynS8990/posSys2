from datetime import datetime
from pytz import timezone

def getDate():
	#Define getDate() function
	e = datetime.today().strftime('%Y-%m-%d')
	return e

class handleFile:
	def addLine(line):
		e = getDate()
		with open('inventory.txt', 'a') as the_file:
			newStr = f"{e}:{line[0]} {line[1]} {line[2]} {line[3]} {line[4]} {line[5]} {line[6]} {line[7]}"
			newStr += '\n'
			the_file.write(newStr)

	def addSpecLine(line, fil):
		e = getDate()
		with open(fil, 'a') as the_file:
			newStr = f"{e}:{line[0]} {line[1]} {line[2]} {line[3]} {line[4]} {line[5]} {line[6]} {line[7]}"
			newStr += '\n'
			the_file.write(newStr)

	def returnAll(self):
		e = getDate()
		with open ("inventory.txt", "r") as myfile:
			mainList = []
			data=myfile.readlines()
			for i in data:
				dat = i.replace('\n', '')
				mainList += [dat.split(" ")]
			return mainList

	def replace_line(self, line_num, text):
		e = getDate()
		lines = open("inventory.txt", 'r').readlines()
		y = 0
		o = 0
		tex = ""
		for i in lines:
			if o < 1:
				if line_num.lower() in i.lower():
					o += 1
				y += 1
		if ":" in lines[y - 1]:
			tex = f"{text}"
		else:
			tex = f"{e}:{text}"
		lines[y - 1] = tex
		out = open("inventory.txt", 'w')
		out.writelines(lines)
		out.close()

	def delete_line(self, line_num):
		e = getDate()
		text = ""
		lines = open("inventory.txt", 'r').readlines()
		y = 0
		o = 0
		for i in lines:
			if o < 1:
				if line_num.lower() in i.lower():
					o += 1
				y += 1
		lines[y - 1] = text
		out = open("inventory.txt", 'w')
		out.writelines(lines)
		out.close()
