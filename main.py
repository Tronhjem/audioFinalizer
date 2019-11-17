from ffmpeg_normalize import FFmpegNormalize
import printStats as ps
import os
import sys

input_file = "/Users/christian/Desktop/file_test.wav"



def normaliseFile(path, file):
    print("analysing audio for " + file)
    ffmpeg_normalize = FFmpegNormalize(
        target_level=-21, true_peak=-3.3, sample_rate=44100
    )
    ffmpeg_normalize.add_media_file(file, path+'/normalised/'+os.path.basename(file))
    ffmpeg_normalize.run_normalization()
    print("done for " + file)
    print("_")


def normaliseAudioFolder(path):
    fileList = os.listdir(path)
    print("================================================")
    print("NORMALISING...")
    print("================================================")
    for file in fileList:
        filePath = os.path.join(path, file)
        splitFileName = os.path.basename(file).split('.')
        fileType = splitFileName[len(splitFileName) - 1]

        if fileType == 'wav':
            normaliseFile(path, filePath)
    print("================================================")
    print("DONE NORMALISING")
    print("================================================")

if __name__ == "__main__":
    path = sys.argv[1]
    pathToNorm = path + '/normalised/'
    if not os.path.exists(pathToNorm):
        os.makedirs(pathToNorm)

    normaliseAudioFolder(path)
    ps.printStats(pathToNorm)
