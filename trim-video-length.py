import sys
import ffmpeg

# very useful:
# https://github.com/kkroening/ffmpeg-python/tree/master/examples


def show_info(file_name):
    try:
        probe = ffmpeg.probe(file_name)
    except ffmpeg.Error as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

    for s in probe['streams']:
        print(s)
        print(
            f"stream #{s.get('index')}, codec_type: {s.get('codec_type')}, codec_long_name: {s.get('codec_long_name')}, {s.get('tags')}")

    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        print('No video stream found', file=sys.stderr)
        sys.exit(1)

    print("video info:")
    print(f'width: {video_stream.get("width")}')
    print(f'height: {video_stream.get("height")}')
    print(f'num_frames: {video_stream.get("num_frames")}')


# duration of input file: 00:01:38.615
#
# stream 0: video, h264 mpeg-4 avc
# stream 1: audio, mpeg aac audio

input_video_file_name = 'data/video-to-trim.mkv'

# need to trim both streams (start: 00:06, stop: 01:34)
output_video_file_name = 'data/video-out.mkv'

show_info(input_video_file_name)

START_TIMESTAMP = 6  # seconds
DURATION = 88  # seconds

in_file = ffmpeg.input(input_video_file_name)
audio = in_file.audio.filter('atrim', start=START_TIMESTAMP, duration=DURATION)
video = in_file.trim(start=START_TIMESTAMP, duration=DURATION)

out = ffmpeg.output(audio, video, output_video_file_name).overwrite_output()

ffmpeg.run(out)

print("finished!")

# video trim OK (but audio stream is not present in output)
# (
#     ffmpeg
#     .concat(
#         # in_file.trim(start='00:00:06', stop='00:01:34')
#         in_file.trim(start='06')
#     )
#     .output(output_video_file_name)
#     .run()
# )
