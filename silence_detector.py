
import librosa
import numpy as np


class SilenceDetector:
    def __init__(self, silence_threshold_sec=5, amplitude_threshold=0.01):
        self.silence_threshold_sec = silence_threshold_sec
        self.amplitude_threshold = amplitude_threshold

    def analyze_audio(self, audio_file):

        audio, sr = librosa.load(audio_file, sr=None)

        frame_length = 2048
        hop_length = 512

        rms = librosa.feature.rms(
            y=audio,
            frame_length=frame_length,
            hop_length=hop_length
        )[0]

        silent_frames = rms < self.amplitude_threshold

        max_silence = 0
        current_silence = 0

        longest_start = 0
        longest_end = 0
        current_start = None

        frame_duration = hop_length / sr

        for i, frame in enumerate(silent_frames):

            if frame:

                if current_silence == 0:
                    current_start = i * frame_duration

                current_silence += frame_duration

                if current_silence > max_silence:
                    max_silence = current_silence
                    longest_start = current_start
                    longest_end = current_start + current_silence

            else:
                current_silence = 0
                current_start = None

        result = {
            "silence_detected": max_silence >= self.silence_threshold_sec,
            "duration_sec": round(max_silence, 2),
            "start_sec": round(longest_start, 2),
            "end_sec": round(longest_end, 2)
        }

        return result


if __name__ == "__main__":
    detector = SilenceDetector(
        silence_threshold_sec=5,
        amplitude_threshold=0.01
    )

    result = detector.analyze_audio("sample.wav")

    print(result)
