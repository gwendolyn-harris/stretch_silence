#!/usr/bin/env python3

from pydub import AudioSegment, silence
from audiotsm import phasevocoder
from audiotsm.io.wav import WavReader, WavWriter
import argparse

parser = argparse.ArgumentParser(
    prog='Stretch and Add Silence',
    description='A little CLI widget intended to slow and add space to various forms of language-learning audio files, which often feel rushed to newcomers. Thank you to the creators of PyDub and AudioTSM, upon which this program sits.',
    epilog='Happy learning!')
parser.add_argument('infile', type=argparse.FileType('r'), help="The sound file to be processed. Accepts any ffmpeg filetype.")
parser.add_argument('-d, --outfile', type=argparse.FileType('w'), help="Where you want the processed audio to be saved. Defaults to the same location as your input file.")
parser.add_argument('-s', '--speed', type=float, help="Speed for the new audio, relative to the original.")
parser.add_argument('-t', '--type', type=str, help="The filetype you wish to the save your processed audio in. Accepts any ffmpeg filetype and defaults to the same type as the input.")
parser.add_argument('-e', '--emptyspace', default=0, type=int, help='Amount of empty space you would like between sounds, in milliseconds.')
parser.add_argument('-b', '--boundthreshold', default=-16, type=int, help='Volume threshold, in dB, to define as "silence" for the purpose of deciding where to add more space. Try bumping up if your results are not sensitive enough. Defaults to -16 dB.')
parser.add_argument('-p', '--preset', type=str, help='Load a set of predefined parameters, identified with a title of your choosing, defined in presets.toml, to process your audio using. Helpful if you find yourself processing many audio files with similar thresholds and changes.')

def change_speed(input, output, speed=1.0):
    # Saves output temporarily in the user-defined output location for further changes, if necessary
    with WavReader(input) as reader:
        with WavWriter(output, reader.channels,reader.samplerate) as writer:
            tsm = phasevocoder(reader.channels, speed=speed)
            tsm.run(reader, writer)

def add_space(input, space, bounds):
    clip = AudioSegment.from_file(input)
    clip_split = silence.split_on_silence(clip, 600, bounds, 100)
    base_silence = AudioSegment.silent(space)

    clip_with_space = base_silence
    for segment in clip_split:
        clip_with_space += segment + base_silence

    return clip_with_space


# def process_vocab():
#     clip = AudioSegment.from_mp3("Downloads/Lesson 2.mp3")
#     # TODO: Process filepath
#     clip_split = silence.split_on_silence(clip, 500, -30, 300, 1)

#     silence_bounds = silence.detect_silence(clip, 500, -30, 2)[0]
#     base_silence = clip[silence_bounds[0] + 200:(silence_bounds[1] - 200)]
#     silence_multiplier = 1000 // ((silence_bounds[1] - 200) - (silence_bounds[0] + 200))

#     clip_with_space = base_silence * silence_multiplier
#     for segment in clip_split:
#         clip_with_space += (segment + base_silence * silence_multiplier * 2)

#     return clip_with_space

# def change_speed(clip, speed=1.0):
#     clip_with_change = clip._spawn(clip.raw_data, overrides={
#         "frame_rate": int(clip.frame_rate * speed)
#     })

#     return clip_with_change.set_frame_rate(clip.frame_rate)


# def process_phrases():
#     clip = AudioSegment.from_mp3("Downloads/Lesson 1 Phrases.mp3")

#     new_clip = change_speed(clip, 0.85)
#     new_clip_split = silence.split_on_silence(new_clip, 500, -30, 300, 1)
#     silence_bounds = silence.detect_silence(clip, 500, -30, 2)[0]
#     base_silence = clip[silence_bounds[0] + 200:(silence_bounds[1] - 200)]
#     silence_multiplier = 1000 // ((silence_bounds[1] - 200) - (silence_bounds[0] + 200))

#     clip_with_space = base_silence * silence_multiplier

#     for segment in new_clip_split:
#         clip_with_space += (segment + base_silence * silence_multiplier * 2)

#     return clip_with_space
