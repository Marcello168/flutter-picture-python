# -*- coding: utf-8 -*-
'''
@Author: gongyonghui
@Date: 2019-10-13 09:53:31
@LastEditors: gongyonghui
@LastEditTime: 2019-10-13 16:34:20
@Description: file content
'''
import os
import shutil

rootPath = os.getcwd()  # 获得当前路径 /home/dir1
print('当前路径-> %s' % rootPath)

# 移动文件


def movefile(srcfile, dstfile):
    fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
    if not os.path.exists(fpath):
        os.makedirs(fpath)  # 创建路径
    shutil.move(srcfile, dstfile)  # 移动文件
    print("move %s -> %s" % (srcfile, dstfile))

# 获取图片路径


def getFilePath():
    L1X = []
    L2X = []
    L3X = []
    for root, dirs, files in os.walk(rootPath):  # 遍历该目录下所有文件 包括子目录
        for file in files:
            filePath = os.path.join(root, file)
            fileSuffix = os.path.splitext(filePath)[1]  # 获取文件后缀
            if fileSuffix == '.jpeg' or fileSuffix == '.png':
                pictureName = os.path.split(filePath)[1]
                if pictureName.find('@2x.jpeg') > 0 or pictureName.find('@2x.png') > 0:
                    L2X.append(filePath)
                elif pictureName.find('@3x.jpeg') > 0 or pictureName.find('@3x.png') > 0:
                    L3X.append(filePath)
                else:
                    L1X.append(filePath)
            else:
                L1X.append(filePath)

    return (L1X, L2X, L3X)  # 返回图片路径元组


path2x = rootPath+'/2x'
path3x = rootPath+'/3x'

if os.path.exists(path2x) == False:
    print('2x目录不存在 创建目录')
    os.makedirs(path2x)
else:
    print('2x目录已存在')
if os.path.exists(path3x) == False:
    print('3x目录不存在 创建目录')
    os.makedirs(path3x)
else:
    print('3x目录已存在')
for picture_list in getFilePath():  # 遍历图片元组
    for picturePath in picture_list:  # 拿到图片路径
        old_path, old_pictureName = os.path.split(picturePath)
        new_path = path2x + '/' + old_pictureName
        if old_pictureName.find('@2x.jpeg') > 0 or old_pictureName.find('@2x.png') > 0:
            new_path = path2x + '/' + old_pictureName.replace('@2x', "")
        elif old_pictureName.find('@3x.jpeg') > 0 or old_pictureName.find('@3x.png') > 0:
            new_path = path3x + '/' + old_pictureName.replace('@3x', "")
        else:
            new_path = rootPath + '/' + old_pictureName  # 1x 图片 放在根目录
            pass
        if os.path.exists(new_path):
            # print('%s 文件已存在' % old_pictureName)
            pass
        elif os.path.exists(picturePath) == False:
            print('%s 文件不存在 文件路径 %s' % (old_pictureName, picturePath))
        else:
            movefile(picturePath, new_path)  # 移动图片到指定路径
