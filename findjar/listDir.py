# -*- coding: utf-8 -*-

import os

def listDir(path, fileList=[]):
	files = os.listdir(path)
	for f in files:
		# fileOrDir = os.path.join(path, f)
		fileOrDir = path + os.sep + f
		print(fileOrDir)
		if os.path.isdir(fileOrDir):
			print('dir is %s' % fileOrDir)
			listDir(fileOrDir, fileList)
		else:
			fileList.append(fileOrDir)
	return fileList

def listDirByWalk(path):
	list_dirs = os.walk(path)
	for root, dirs, files in list_dirs:
		for d in dirs:
			print(os.path.join(root, d))
		for f in files:
			print(os.path.join(root, f))


def main():
	print('List dir by os.listdir start.')
	fileList = listDir('.')
	print(fileList)
	print('List dir by os.listdir end.')

	print('List dir by os.walk start.')
	listDirByWalk('.')
	print('List dir by os.walk end.')

if __name__ == '__main__':
	main()