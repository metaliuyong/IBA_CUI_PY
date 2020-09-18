# -*- coding: UTF-8 -*-

import os


def convertSpeToTxt_batch(file_name_list):
    for name in file_name_list:
        convertSpeToTxt(name)


def convertSpeToTxt(file_name):
    fr = open(file_name, 'r')
    txt_name = os.path.splitext(file_name)[0] + ".txt"
    fw = open(txt_name, 'w')

    for i in range(11):
        fr.readline()

    start_end = fr.readline().split()
    end = int(start_end[1]) + 1

    for i in range(end):
        channel = i + 1
        count = int(fr.readline())
        fw.write("{}\t{}\n".format(channel, count))

    fw.close()
    fr.close()


def getSpeFileNameList(directory_name):
    file_name = os.listdir(directory_name)
    file_name_list = []
    for name in file_name:
        if (os.path.splitext(name)[1] == ".Spe"):
            file_name_list.append(directory_name + "\\" + name)
    return file_name_list
