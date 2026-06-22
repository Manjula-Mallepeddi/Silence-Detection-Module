# Silence Detection Module

## Overview

The Silence Detection Module is a Python-based audio processing system that detects prolonged periods of silence in audio recordings.

The module analyzes audio signals, measures silence duration, and generates a structured output indicating whether a predefined silence threshold has been exceeded.

This project was developed as part of an internship task focused on handling no-response scenarios in AI-based systems.

---

## Objective

* Detect silence in audio recordings
* Measure silence duration
* Identify no-response scenarios
* Generate structured output
* Support configurable silence thresholds

---

## Features

* Audio file processing
* Silence detection using RMS energy analysis
* Configurable silence threshold
* Duration calculation
* Silence start and end timestamp detection
* JSON-based output
* Supports WAV audio files

---

## Technologies Used

* Python
* Librosa
* NumPy
* SoundFile

---

## Project Structure

```text
silence_detector/
│
├── silence_detector.py
├── test_silence_detector.py
├── sample.wav
├── silence.wav
├── speech.wav
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd silence_detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

```text
librosa
numpy
soundfile
```

---

## Usage

Run the script:

```bash
python silence_detector.py
```

The program analyzes the audio file and returns the silence detection result.

---

## Sample Output

```json
{
  "silence_detected": true,
  "duration_sec": 9.76,
  "start_sec": 3.47,
  "end_sec": 13.23
}
```

---

## How It Works

1. Load the audio file using Librosa.
2. Calculate RMS (Root Mean Square) energy values.
3. Identify silent frames using an amplitude threshold.
4. Measure continuous silence duration.
5. Track the start and end timestamps of the longest silence segment.
6. Compare duration with the configured threshold.
7. Generate structured JSON output.

---

## Edge Cases Handled

### Background Noise

Detection performance may vary depending on environmental noise levels. The amplitude threshold can be adjusted to reduce false detections in different recording environments.

### Low-Volume Speech

Quiet speech may require threshold tuning to achieve accurate detection results.

### Partial Speech and Pauses

Detection behavior depends on the configured threshold values and audio characteristics. Thresholds can be adjusted based on the expected speech patterns and recording conditions.

---

## Test Results

```text
Running Silence Detection Tests...

PASS: sample.wav detects silence correctly
PASS: speech.wav does not detect prolonged silence
PASS: sample.wav with high threshold returns False

Testing Complete
```

---

## Future Improvements

* Real-time microphone monitoring
* Voice Activity Detection (VAD)
* Noise reduction preprocessing
* Dashboard visualization
* Integration with AI interview systems

---

## Learning Outcomes

This project helped improve skills in:

* Audio processing
* Python programming
* Librosa library usage
* Signal analysis
* Debugging and troubleshooting
* AI system workflow integration

---

## Author

**Manjula**

Prompt Engineering Intern
