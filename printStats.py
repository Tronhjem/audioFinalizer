import pyloudness
import sys
import os

def stats(file):
    '''Takes a file path and outputs Loudness and Peak to terminal'''
    loudness_stats = pyloudness.get_loudness(file)
    print("File     :  " + os.path.basename(file))
    print("_________________")
    print("Loudness :  " + str(loudness_stats["Integrated Loudness"]["I"]))
    print("Peak     :  " + str(loudness_stats["True Peak"]["Peak"]))
    print("_________________")
    print(" ")


def printStats(folder):
    '''takes a folder and outputs stats for all .wav files in that folder'''
    fileList = os.listdir(folder)
    print("================================================")
    print("STATS:")
    print("================================================")

    for file in fileList:
        filePath = os.path.join(folder, file)
        splitFileName = os.path.basename(file).split('.')
        fileType = splitFileName[len(splitFileName) - 1]
        if fileType == 'wav':
            stats(filePath)

    print("================================================")
    print("STATS DONE")
    print("================================================")


if __name__ == '__main__':
    path = sys.argv[1]
    printStats(path)