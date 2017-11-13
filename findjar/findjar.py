# -*- coding: utf-8 -*-

import zipfile, os

LOG4J_CFG_FILENAME = 'log4j.properties'
EXT_NAME = '.jar'
CURRENT_DIR = '.'

# step1: find *.jar files in CLASSPATH or current project root directory.
def listFiles(path='.',name=None,dirlist=[], extName='.jar'):
	files=os.listdir(path)
	for i in files:
		file_path=path+os.sep+i
		if os.path.isdir(file_path):
			listFiles(file_path,name,dirlist)
		else:
			if i.endswith(EXT_NAME):
				dirlist.append(file_path)
	return dirlist

# step2: find log4j.properties configuration file in these jar files.

def findLog4jCfgFile(filenameList=[]):
	if filenameList == []:
		print('You give filenameList is empty!')
		return []

	filenameDict = {}
	for filename in filenameList:
		filenames = []
		# zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'ojdbc6.jar'))
		zipFile = zipfile.ZipFile(filename)
		for filename2 in zipFile.namelist():
			if filename2.find(LOG4J_CFG_FILENAME) >= 0 and filename2.endswith(LOG4J_CFG_FILENAME):
				filenames.append(filename2)
				print(filename2)
			else:
				continue
			filenameDict[filename] = filenames

		# 	print('Not find log4j.properties in these jar files!')
		zipFile.close()

	return filenameDict


def main():
	jarFilenames = listFiles('.', None, [], EXT_NAME)
	print(jarFilenames)
	jarFilenames = findLog4jCfgFile(jarFilenames)
	print(jarFilenames)


if __name__ == '__main__':
	main()