# -*- coding: utf-8 -*-
# 
# @Author  : tyj
# @Time    : 2022/12/9 13:38
# @File: merge.py
import os


def write_filelist(dirs_path= r"D:\my code\course\zhidongxi\video"):
    """
    dirs_path: ts文件所在目录
    @return:
    """
    with open(dirs_path + "filelist.txt",mode="a+",encoding="utf-8") as f:
        for root,dirs,files in os.walk(dirs_path):
            for file_ in files:
                file_path = os.path.join(root,file_)
                row_txt = f"file '{file_path}'\n"
                f.write(row_txt)

if __name__ == '__main__':
    dirpath = os.path.dirname(os.path.abspath(__file__))
    dirpath = dirpath + r"\video"
    os.chdir(dirpath)
    # print(dirpath)
    # write_filelist()
    os.system("D:/ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe -f concat -i filelist.txt -c copy out.mp4")
