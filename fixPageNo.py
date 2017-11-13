# -*- encoding: utf-8 -*-

# 将当前目录下一个存放了PDF目录书签的文本文件中的页码进行修正，
# 然后输出到一个新的文件到当前目录。
# 1) 将每行末尾的数字加上页码校正偏移量
# 2）可使用TAB制表符分隔
# 3）将所有的空行删除
# 4）设置缓冲区来写入文件 TODO
# 5）最后将输出文件末尾的那一行空行删除 TODO
### 命令行的使用示例：python fixPageNo.py old.txt 34

import sys
import os
import re


# def calcAndFixPageNo(inFile, offset):
# 	if (not os.path.exists(inFile)) or (not os.path.isfile(inFile)) or (offset <= 0):
# 		print("Please input valid file path and offset!!!")
# 		sys.exit(1)

# 	# create a new file
# 	outFileName = 'pageNoFixed.txt'
# 	outFile = open(outFileName, 'w')

# 	# 写入前先清空已存在的输出文件
# 	outFile.truncate()

# 	lineNumber = 0
# 	with open(inFile) as a_file:
# 		for line in a_file:
# 			lineNumber += 1
# 			# TODO
# 			print('line%d-->%s' % (lineNumber, line))
# 			lst = line.split("\t")
# 			if len(lst) > 1:
# 				pageNoStr = lst[-1] # lst[len(lst) - line]
# 				lst.pop(-1)
# 				# TODO
# 				print('pageNoStr-->' + pageNoStr)
# 				pageNo = int(pageNoStr)
# 				print('pageNo-->%d' % pageNo)
# 				pageNoFix = pageNo + offset
# 				lst.append(pageNoFix)
# 			else: # 忽略空行
# 				continue
# 			newLineStr = list2StrJoinByTab(lst)

# 			# outFile.write(newLineStr + '\n') # 行末需要有换行符
# 			outFile.write(newLineStr) # 行末需要有换行符

# 	outFile.close()

# usage: python fixPageNo.py <in_filename> <offset>
'''
def calcAndFixPageNo(inFile, offset):
	if (not os.path.exists(inFile)) or (not os.path.isfile(inFile)) or (not isinstance(offset, int)):
		print("Please input valid file path and offset!!!")
		sys.exit(1)

	# create a new file
	outFileName = 'pageNoFixed.txt'
	outFile = open(outFileName, 'w')

	# 写入前先清空已存在的输出文件
	outFile.truncate()

	lineNumber = 0
	with open(inFile) as a_file:
		for line in a_file:
			lineNumber += 1
			print('line%d-->%s' % (lineNumber, line))
			lst = line.rpartition("\t")
			if len(lst) > 1:
				pageNoStr = lst[-1]
				frontPartition = lst[0]
				print('pageNoStr-->' + pageNoStr)
				if not pageNoStr.strip().isdigit():
					outFile.write(line) # 行末需要有换行符
					continue
				pageNo = int(pageNoStr.strip())
				print('pageNo-->%d' % pageNo)
				pageNoFix = pageNo + offset
			else: # 忽略空行
				continue
			newLineStr = frontPartition + '\t' + str(pageNoFix) + '\n'

			outFile.write(newLineStr) # 行末需要有换行符

	outFile.close()
'''
def calcAndFixPageNo():
	inFile = input('Please input your inFile path(e.g. old.txt): ')	
	offset = input('Please input your offset(e.g. 3): ')
	offset = int(offset.strip())
	# validate inFile and offset
	if (not os.path.exists(inFile)) or (not os.path.isfile(inFile)) or (not isinstance(offset, int)):
		print("Please input valid file path and offset!!!")
		sys.exit(1)

	# create a new file
	outFileName = 'pageNoFixed.txt'
	outFile = open(outFileName, 'w')

	# 写入前先清空已存在的输出文件
	outFile.truncate()

	lineNumber = 0
	with open(inFile, encoding='utf-8') as a_file:
		for line in a_file:
			lineNumber += 1
			print('line%d-->%s' % (lineNumber, line))
			lst = line.rpartition("\t")
			if len(lst) > 1:
				pageNoStr = lst[-1]
				frontPartition = lst[0]
				print('pageNoStr-->' + pageNoStr)
				if not pageNoStr.strip().isdigit():
					outFile.write(line) # 行末需要有换行符
					continue
				pageNo = int(pageNoStr.strip())
				print('pageNo-->%d' % pageNo)
				pageNoFix = pageNo + offset
			else: # 忽略空行
				continue
			newLineStr = frontPartition + '\t' + str(pageNoFix) + '\n'

			outFile.write(newLineStr) # 行末需要有换行符

	outFile.close()

# 将列表的元素用1个TAB制表相互连接起来，末尾不需要TAB制表符但是需要回车换行符
def list2StrJoinByTab(lst):
	text = ''
	for element in lst:	
		text += str(element)
		# text = text + str(element) + '\t'
		if element != lst[-1]:
			 text += '\t'
		else:
			text += '\n'

	# 删除字符串尾部的空格、TAB制表符、回车符或换行符， 删除头部的可以使用lstrip()函数，删除头尾两端的可以使用strip()函数
	# text = text.rstrip()

	return text


# 找到每行末尾的数字，如有，则将其与前面的字符串用TAB制表符分开，否则该行不变.
# 使用正则来做这个事！！！
def fixPageNoPosition():
	inFile = input('Please input your inFile path: ')
	if (not os.path.exists(inFile)) or (not os.path.isfile(inFile)):
		print("Please input valid file path!!!")
		sys.exit(1)

	# create a new file
	outFileName = 'pageNoFixed.txt'
	outFile = open(outFileName, 'w')

	# 写入前先清空已存在的输出文件
	outFile.truncate()

	pattern = '\D'
	lineNumber = 0
	with open(inFile) as a_file:
		for line in a_file:
			lineNumber += 1
			# TODO
			print('line%d-->%s' % (lineNumber, line))
			hasNumOnTail = False # 尾部有数字为假

			lst = re.split(pattern, line)
			lastNumOfThisLine = lst[-2]
			if lastNumOfThisLine is '':
				outFile.write(line)
				continue

			print('lastNumOfThisLine-->%s' % lastNumOfThisLine)

			lst = line.split(lastNumOfThisLine)
			front_ = line.sub
			lastNumOfThisLineFixed = '\t' + lastNumOfThisLine
			newLineStr = front_ + lastNumOfThisLineFixed + '\n'

			# outFile.write(newLineStr + '\n') # 行末需要有换行符
			outFile.write(newLineStr) # 行末需要有换行符

	outFile.close()


# 找到每行末尾的数字，如有，则将其前面的1个空格转换成TAB制表符，否则该行不变.
# 使用正则来做这个事！！！
def changeSpace2TabOfPageNo():
	inFile = input('Please input your inFile path: ')
	if (not os.path.exists(inFile)) or (not os.path.isfile(inFile)):
		print("Please input valid file path!!!")
		sys.exit(1)

	# create a new file
	outFileName = 'pageNoFixed.txt'
	outFile = open(outFileName, 'w')

	# 写入前先清空已存在的输出文件
	outFile.truncate()

	pattern = ' '
	lineNumber = 0
	with open(inFile) as a_file:
		for line in a_file:
			lineNumber += 1
			# TODO
			print('line%d-->%s' % (lineNumber, line))

			lst = line.rpartition(pattern)
			lastNumOfThisLine = lst[-1]
			print('lastNumOfThisLine-->%s' % lastNumOfThisLine)
			frontPartition = lst[0]
			if not lastNumOfThisLine.strip().isdigit():
				outFile.write(line)
				continue

			print('lastNumOfThisLine-->%s' % lastNumOfThisLine)

			lastNumOfThisLineFixed = '\t' + lastNumOfThisLine
			newLineStr = frontPartition + lastNumOfThisLineFixed

			# outFile.write(newLineStr + '\n') # 行末需要有换行符
			outFile.write(newLineStr) # 行末需要有换行符

	outFile.close()


# 将列表的元素用1个TAB制表相互连接起来，末尾不需要TAB制表符但是需要回车换行符
def list2StrJoinByTab(lst):
	text = ''
	for element in lst:	
		text += str(element)
		# text = text + str(element) + '\t'
		if element != lst[-1]:
			 text += '\t'
		else:
			text += '\n'

	# 删除字符串尾部的空格、TAB制表符、回车符或换行符， 删除头部的可以使用lstrip()函数，删除头尾两端的可以使用strip()函数
	# text = text.rstrip()

	return text

# Beacuse python has no switch..case structure, i can use dict to do same thing.
actionDict = {
	0: calcAndFixPageNo,
	1: fixPageNoPosition,
	2: changeSpace2TabOfPageNo
}


def selectCommand():
	print('\n# ***************************************************************\n')
	print('# Below are the functions you can use!\n')
	print('# 0: calcAndFixPageNo, Usage: python fixPageNo.py <inFile> <offset>\n')
	print('# 1: fixPageNoPosition, Usage: python fixPageNo.py <inFile>\n')
	print('# 2: changeSpace2TabOfPageNo, Usage: python fixPageNo.py <inFile>\n')
	print('# ***************************************************************\n')

	while(True):
		print('Please input your right number to select a function!')
		functionId = input()
		functionId = functionId.strip()
		if functionId.isdigit():
			functionId = int(functionId)
			if 0 <= functionId < 3:
				print('functionId=%d, functionName=%s' % (functionId, actionDict.get(functionId).__name__))
				actionDict.get(functionId)()
				break


def main():
	# TODO first call a function to show functions of this program
	selectCommand()
	print(sys.argv)
	# inFile = sys.argv[1]
	# offset = int(sys.argv[2])
	# calcAndFixPageNo(inFile, offset)
	# fixPageNoPosition(inFile)
	# changeSpace2TabOfPageNo(inFile)


if __name__ == '__main__':
	main()