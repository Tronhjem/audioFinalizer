from ffmpeg_normalize import FFmpegNormalize
import printStats as ps
import os
import sys


def normaliseFile(path, file):
    """takes a path and and file name
    Normalises audio file to -21LUFS with -3dB peak
    set to 44100hZ"""
    # TODO add variable target level, true peak and sample rate.

    print("analysing audio for " + file)
    ffmpeg_normalize = FFmpegNormalize(
        target_level=-21.0,
        true_peak=-3.3,
        sample_rate=44100,
        loudness_range_target=5.5,
        progress=True,
    )
    ffmpeg_normalize.add_media_file(
        file, path + "/normalised/" + os.path.basename(file)
    )
    ffmpeg_normalize.run_normalization()
    print("done for " + file)
    print("_")


def normaliseAudioFolder(path):
    """Takes a path and loops through all .wav files in that path."""
    fileList = os.listdir(path)
    print("================================================")
    print("NORMALISING...")
    print("================================================")
    for file in fileList:
        filePath = os.path.join(path, file)
        splitFileName = os.path.basename(file).split(".")
        fileType = splitFileName[len(splitFileName) - 1]

        if fileType == "wav":
            normaliseFile(path, filePath)
    print("================================================")
    print("DONE NORMALISING")
    print("================================================")


if __name__ == "__main__":
    """normalise and prints stats for all files in path from sys.argv"""
    path = sys.argv[1]
    pathToNorm = path + "/normalised/"
    if not os.path.exists(pathToNorm):
        os.makedirs(pathToNorm)

    normaliseAudioFolder(path)
    ps.printStats(pathToNorm)
