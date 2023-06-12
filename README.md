### Heading

Stretch_Silence

This is a quick, easy-to-use CLI created in order to make adjusting language-learning audio files, which often feature a variety of native speakers and thus remain of value to a well-rounded language-learning experience.

The most commonly requested adjustments are to slow the whole track so that phoneme distinctions can be made more easily and to add more space between words or phrases to give the learner more time to attempt to mimic the native speaker’s pronunciation, so those are the capacities this tool has.  It uses AudioTSM to stretch the audio without altering its pitch, and PyDub to traverse the audio track, identify points of silence, and add more as needed.

Slowing a track requires the specification of only one flag, -s, followed by the speed relative to the original that you would like to slow to. I recommend 0.8 to start.

Adding silence can be a bit more complicated depending on the variable quality of your input audio.  Sometimes the “silence” in the track contains enough background static or other noises that PyDub might struggle to identify it as silence.  This can be tweaked using the ‘-b’, or ‘—boundthreshold’ flag, which is in dB. It defaults to -16, which is usually acceptable, but if you find that the CLI is skipping bits of silence, I would recommend bumping up the number a little at a time. So long as the volume of the background noise isn’t too similar to that of the voice you are seeking to learn from, you should be able to identify a filter that will work eventually.  The other factor here is the ‘-m’ flag, or ‘—minsilence’. This defines the duration of whatever your filter for silence identifies in order to decide where to cut the audio and then add whatever extra silence you might need or want to add. It is in milliseconds, because that is what PyDub uses almost exclusively. It defaults to 200, but if you have a particularly fast paced portion of audio where the spaces are very short, you might need to reduce this slightly in order to make sure each space is identified.

If you don’t provide a path for the output of the CLI, it will save it in the same folder as the input, with the same name, with (output) added.

If you find yourself using the same set of parameters over and over again, for example, if you have a set of recordings in the same style or from the same source (especially if you find yourself needing to tweak the min silence and bound threshold) I’ve provided a presets.toml file. You can utilize presets you have determined useful using the ‘-p’ flag.
