#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将电子书从 epub 格式转换为 azw3 格式。

import os
import sys
import glob
import codecs
import subprocess
import tempfile
import shutil
#
import utils
import KindleEBook

cmd_kindlegen = 'kindlegen'

#def norm_path_sep(s):
#    '''将路径分隔符统一为 /。'''
#    return s.replace('\\', '/')

#cwd = norm_path_sep(os.getcwd().decode('mbcs'))
cwd = os.getcwd()

for epub_file in glob.glob('*.epub'):
    print('Processing ' + epub_file + ':')

    # 从 epub 文件的元数据里获取 ASIN
    # <dc:identifier opf:scheme="ASIN">B00ABCDEFG</dc:identifier>
    asin = utils.identifier_asin(epub_file)
    #print('ASIN:', asin)
    #raise SyntaxError

    basename, ext = os.path.splitext(epub_file)
    mobi_file = basename + '.mobi'
    azw3_file = basename + '.azw3'
    # 调用 Kindlegen 将电子书从 epub 格式转换为 MOBI KF6&8 格式
    cmd_epub2mobi = cmd_kindlegen + ' "' + epub_file + '" -o "' + mobi_file + '"'
    try:
        s = subprocess.check_output(cmd_epub2mobi,
                                    stderr=subprocess.STDOUT, # 将进程的 STDERR 输出合并到 STDOUT
                                    shell=True)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8', 'replace').encode('mbcs', 'replace'))
        #
        if os.path.isfile(mobi_file):
            s = raw_input('Kindlegen returned with non-zero exit code. But ' + mobi_file + ' has already been generated. Do you want to continue?(y/n): ')
            if s != 'y' and s != 'Y':
                raise
    else:
        print(s.decode('utf-8', 'replace').encode('mbcs', 'replace'))

    # 在当前目录下，创建临时工作目录，并将 Kindlegen 生成的 MOBI KF6&8
    # 格式电子书移到该临时工作目录下
    workspace_path = tempfile.mkdtemp(dir=cwd) # 临时工作目录绝对路径
    #print('temp:', workspace_path)
    shutil.move(mobi_file, workspace_path)
    os.chdir(workspace_path)
    # 从 MOBI KF6&8 格式电子书里提取 KF8 格式 AZW3 电子书；
    # 添加 EXTH metadata 501/CDEContentType: EBOK；
    # 替换封面缩略图。
    KindleEBook.extract_kf8(mobi_file.decode('mbcs'), asin)
    #
    des = os.path.join(cwd, azw3_file)
    if os.path.isfile(des):
        os.remove(des)
    shutil.move(azw3_file, cwd)
    os.chdir(cwd)
    shutil.rmtree(workspace_path)
