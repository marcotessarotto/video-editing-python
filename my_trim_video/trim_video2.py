import sys
import ffmpeg

from my_trim_video.trim_video_length import show_info

input_video_file_name = '/media/marco/76E8-CACF/media/Meeting-20210914_103237-Meeting Recording.mp4'

output_video_file_name = '/media/marco/76E8-CACF/media/video-out.mp4'


show_info(input_video_file_name)


START_TIMESTAMP = 3271  # seconds
DURATION = 12204 - 3271  # seconds

in_file = ffmpeg.input(input_video_file_name)
audio = in_file.audio.filter('atrim', start=START_TIMESTAMP, duration=DURATION)
video = in_file.trim(start=START_TIMESTAMP, duration=DURATION)

out = ffmpeg.output(audio, video, output_video_file_name).overwrite_output()

ffmpeg.run(out)

print("finished!")



