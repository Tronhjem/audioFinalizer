from ffmpeg_normalize import FFmpegNormalize
from pydub import AudioSegment
import pyloudness

# input_file = "/Users/christian/Desktop/Regel_no_5_cd01_b.3_test.wav"
input_file = (
    "/Users/christian/Music/Logic/SwannStudio/Regelno5/mastered/Regel nr 5 cd06 b.wav"
)
output_file = "/Users/christian/Desktop/newOne.wav"


def printStats(file):
    loudness_stats = pyloudness.get_loudness(file)
    print("_________________")
    print("Loudness :  " + str(loudness_stats["Integrated Loudness"]["I"]))
    print("Peak     :  " + str(loudness_stats["True Peak"]["Peak"]))
    print("_________________")
    for x in loudness_stats:
        print(loudness_stats[x])
        # for y in loudness_stats[x]:
        #     print(loudness_stats[x][y])


def normaliseAudio(file):
    print("analysing audio....")
    ffmpeg_normalize = FFmpegNormalize(target_level=-21, true_peak=-3.5)
    ffmpeg_normalize.add_media_file(file, output_file)
    ffmpeg_normalize.run_normalization()
    print("done for " + file)


normaliseAudio(input_file)
printStats(output_file)
