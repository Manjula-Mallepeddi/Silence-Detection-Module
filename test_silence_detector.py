
from silence_detector import SilenceDetector

print("Running Silence Detection Tests...\n")

# Test 1: sample.wav should detect silence
try:
    detector = SilenceDetector(
        silence_threshold_sec=5,
        amplitude_threshold=0.01
    )

    result = detector.analyze_audio("sample.wav")

    assert result["silence_detected"] is True
    assert result["duration_sec"] > 0
    assert result["start_sec"] >= 0
    assert result["end_sec"] > result["start_sec"]

    print("PASS: sample.wav detects silence correctly")

except AssertionError:
    print("FAIL: sample.wav detects silence correctly")


# Test 2: speech.wav should not trigger silence detection
try:
    detector = SilenceDetector(
        silence_threshold_sec=5,
        amplitude_threshold=0.01
    )

    result = detector.analyze_audio("speech.wav")

    assert result["silence_detected"] is False

    print("PASS: speech.wav does not detect prolonged silence")

except AssertionError:
    print("FAIL: speech.wav does not detect prolonged silence")


# Test 3: High threshold should return False
try:
    detector = SilenceDetector(
        silence_threshold_sec=20,
        amplitude_threshold=0.01
    )

    result = detector.analyze_audio("sample.wav")

    assert result["silence_detected"] is False

    print("PASS: sample.wav with high threshold returns False")

except AssertionError:
    print("FAIL: sample.wav with high threshold returns False")


print("\nTesting Complete")
