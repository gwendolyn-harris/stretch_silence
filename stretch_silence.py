#!/usr/bin/env python3

from pydub import AudioSegment, silence
import argparse

def process_vocab():
    clip = AudioSegment.from_mp3("Downloads/Lesson 2.mp3")
    # TODO: Process filepath
    clip_split = silence.split_on_silence(clip, 500, -30, 300, 1)

    silence_bounds = silence.detect_silence(clip, 500, -30, 2)[0]
    base_silence = clip[silence_bounds[0] + 200:(silence_bounds[1] - 200)]
    silence_multiplier = 1000 // ((silence_bounds[1] - 200) - (silence_bounds[0] + 200))

    clip_with_space = base_silence * silence_multiplier
    for segment in clip_split:
        clip_with_space += (segment + base_silence * silence_multiplier * 2)

    clip_with_space.export("Lesson 2 with space.mp3")

def change_speed(clip, speed=1.0):
    clip_with_change = clip._spawn(clip.raw_data, overrides={
        "frame_rate": int(clip.frame_rate * speed)
    })

    return clip_with_change.set_frame_rate(clip.frame_rate)


def process_phrases():
    clip = AudioSegment.from_mp3("Downloads/Lesson 1 Phrases.mp3")

    new_clip = change_speed(clip, 0.85)
    new_clip_split = silence.split_on_silence(new_clip, 500, -30, 300, 1)
    silence_bounds = silence.detect_silence(clip, 500, -30, 2)[0]
    base_silence = clip[silence_bounds[0] + 200:(silence_bounds[1] - 200)]
    silence_multiplier = 1000 // ((silence_bounds[1] - 200) - (silence_bounds[0] + 200))

    clip_with_space = base_silence * silence_multiplier

    for segment in new_clip_split:
        clip_with_space += (segment + base_silence * silence_multiplier * 2)

    clip_with_space.export("Lesson 1 Phrases with space.mp3")
