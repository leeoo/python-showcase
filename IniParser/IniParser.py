
# -*- coding: utf-8 -*-


from configparser import ConfigParser
import os


def parseIni(filename):
	f = open(filename)
	newFile = open('new.ini', 'w')
	iniParser = ConfigParser()
	l = iniParser.read_file(f)
	sections = iniParser.sections()
	for section in sections:
		print('section -> %s' % section)
		options = iniParser.options(section)
		for option in options:
			print('option -> %s, value -> %s' % (option, iniParser.get(section, option)))
			if option == 'uat-inputdir':
				# print('right............')
				iniParser.set(section, option, 'test dir')
				print('option -> %s, value -> %s' % (option, iniParser.get(section, option)))
		print('')

	iniParser.write(newFile)

	newFile.close()
	f.close()


def main():
	currentPath = os.getcwd()
	filename = '/'.join([currentPath, 'test.ini'])
	print(filename)
	parseIni(filename)




if __name__ == '__main__':
	main()