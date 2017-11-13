# -*- encoding: utf-8 -*-


import time
# read file

# Read file by chunk size.
def readFileByChunk(filename, chunkSize = 4096):

	fobj = open(filename)

	try:
		while True:
			chunk = fobj.read(chunkSize)
			if not chunk:
				break
			# TODO
			# print(chunk)
			# time.sleep(1)
	finally:	
		fobj.close()

# try:
# 	# lines = fobj.read()
# 	# print(lines)
# 	# lines = fobj.readlines()
# 	# print(lines)
# 	# lines = fobj.read().splitlines()
# 	# print(lines)
# 	# lines = fobj.read().split('\n')
# 	# print(lines)

# 	# lines = [l.rstrip('\n') for l in fobj]
# 	# print(lines)

# 	# in this case: each line will be apped a string '\n'
# 	for line in fobj:
# 		# print(line)
# 		# strip white string at the end
# 		print(line.rstrip('\n'))

# finally:
# 	fobj.close()


# write file

# Write file by chunk size.
def writeFileByChunk(filename, chunkSize = 4096):
	fileObjectWrite = open(filename, 'w')
	try:
		# fileObjectWrite.write('test....')
		fileObjectWrite.writelines([l for l in open('test.txt'])
	finally:
		fileObjectWrite.close()

def main():
	readFileByChunk('test.txt')
	writeFileByChunk('out.txt')



if __name__ == '__main__':
	main()