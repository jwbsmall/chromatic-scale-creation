# IT BLOODY WORKS BABAYYY

import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub.playback import play

# Function to generate a tone at a specified frequency and duration
def generate_tone(frequency, duration):
    sample_rate = 44100  # Sample rate (Hz)
    samples = np.arange(duration * sample_rate // 1000)
    sine_wave = np.sin(2 * np.pi * frequency * samples / sample_rate)
    audio_data = (sine_wave * 32767).astype(np.int16)  # Convert to 16-bit PCM format
    write('/tmp/tone.wav', sample_rate, audio_data)  # Save as WAV file temporarily
    return AudioSegment.from_file('/tmp/tone.wav', format='wav')

# Define a sequence of tones with their frequency in Hz and duration in milliseconds

# 14 Note Chromatic Scale
tone_sequence = [
	(330.000, 200), # E
	(347.654, 200), # F
	(371.250, 200), # F#
	(391.111, 200), # G
	(412.035, 200), # G# Alternate (reducing A)
	(417.656, 200), # G#
	(440.000, 200), # A
	(463.539, 200), # A#
	(469.863, 200), # A# Alternate (increasing A)
	(495.000, 200), # B
	(521.481, 200), # C
	(556.875, 200), # C#
	(586.667, 200), # D
	(618.052, 200), # D# (reducing A)
	(626.484, 200), # D# (increasing A)
	(660.000, 200), # E
]

# 12 note equal temperament chromatic scale
# tone_sequence = [
# 	(330.000, 200),
# 	(349.623, 200),
# 	(370.412, 200),
# 	(392.438, 200),
# 	(415.774, 200),
# 	(440.497, 200),
# 	(466.690, 200),
# 	(494.441, 200),
# 	(523.842, 200),
# 	(554.992, 200),
# 	(587.993, 200),
# 	(622.957, 200),
# 	(660.000, 200),
# ]

# Oh shit I think this is a proper chromatic scale
# 12 note base
# E Major scale
# tone_sequence = [
# 	(330.000, 200), # E
# 	# (347.654, 200), # F
# 	(371.250, 200), # F#
# 	# (391.111, 200), # G
# 	(417.656, 200), # G#
# 	(440.000, 200), # A
# 	# (463.539, 200), # A#
# 	(495.000, 200), # B
# 	# (521.481, 200), # C
# 	(556.875, 200), # C#
# 	# (586.667, 200), # D
# 	(618.052, 200), # D#
# 	(626.484, 200), # D# Alternate (multiplying rather than dividing)
# 	(660, 200), #E
# ]

# 12 note base
# E Minor scale
# OOOHHH SHIIIT the minor scale is actually just the first three on either side
# Meaning that, IMO, minor is the default scale
# tone_sequence = [
# 	(330, 200), # E
# 	# (347.654321, 200), # F
# 	(371.25, 200), # F#
# 	(391.1111111, 200), # G
# 	# (417.65625, 200), # G#
# 	(440, 200), # A
# 	# (463.5390947, 200), # A#
# 	(495, 200), # B
# 	(521.4814815, 200), # C
# 	# (556.875, 200), # C#
# 	(586.6666667, 200), # D
# 	# (618.052	1262, 200), # D#
# 	(660, 200), # E
# ]

# 12 note base
# Everything that's in both E Major and E Minor
# tone_sequence = [
# 	(330, 200), # E
# 	# (347.654321, 200), # F
# 	(371.25, 200), # F#
# 	# (391.1111111, 200), # G
# 	# (417.65625, 200), # G#
# 	(440, 200), # A
# 	# (463.5390947, 200), # A#
# 	(495, 200), # B
# 	# (521.4814815, 200), # C
# 	# (556.875, 200), # C#
# 	# (586.6666667, 200), # D
# 	# (618.052	1262, 200), # D#
# 	(660, 200), # E
# ]

# Oooooh this sounds like Japanese or something
# 5 note
# tone_sequence = [
# 	(330, 200),
# 	(391.1111111, 200),
# 	(440, 200),
# 	(495, 200),
# 	(586.6666667, 200),
# 	(660, 200),
# ]

# 12 note base
# Opposite-Major scale
# tone_sequence = [
# 	(330.000, 200), # E
# 	(347.654, 200), # F
# 	# (371.250, 200), # F#
# 	(391.111, 200), # G
# 	(412.035, 200), # G# Alternate (reducing A)
# 	# (417.656, 200), # G#
# 	(440.000, 200), # A
# 	# (463.539, 200), # A#
# 	# (469.863, 200), # A# Alternate (increasing A)
# 	# (495.000, 200), # B
# 	(521.481, 200), # C
# 	# (556.875, 200), # C#
# 	(586.667, 200), # D
# 	# (618.052, 200), # D# (reducing A)
# 	# (626.484, 200), # D# (increasing A)
# 	(660.000, 200), # E
# ]

# Generate and play the tones in the sequence with a short pause between each tone
for frequency, duration in tone_sequence:
    tone = generate_tone(frequency=frequency, duration=duration)
    play(tone)