# needed to brew install ffmpeg
# needed to pip install pydub

from pydub import AudioSegment
from pydub.playback import play

# Function to generate a tone at a specified frequency and duration
def generate_tone(frequency, duration):
    return AudioSegment.sine_wave(frequency=frequency, duration=duration)

# Define a sequence of tones with their frequency in Hz and duration in milliseconds
tone_sequence = [
    (440, 500),   # A4 note, 500ms duration
    (880, 500),   # A5 note, 500ms duration
    (1320, 500),  # E6 note, 500ms duration
]

# Generate and play the tones in the sequence with a short pause between each tone
for frequency, duration in tone_sequence:
    tone = generate_tone(frequency=frequency, duration=duration)
    play(tone)