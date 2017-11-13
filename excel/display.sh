#!/bin/sh

#下面是一个Linux上的bash shell 脚本程序，程序名为 display （5分）
#Shell filename is "display"
CALLER=`basename $0`
TEMP=`getopt lh $*`
if [ $? == 0 ]
then
	echo "$CALLER: Unknown flag(s)"
	exit 1
fi
eval set -- $TEMP
while true
do
case $1 in
	-h) COMMAND=ls\ -lh; shift;;
	-l) COMMAND=ls\ -l; shift;;
	--) shift ; break ;;
	*) echo "Internal error!" ; exit 1 ;;
esac
done
echo $COMMAND
# 问题一、运行display ,结果是什么？
# 问题二、运行display –l, 结果是什么？
# 问题三、运行display –p,结果是什么？