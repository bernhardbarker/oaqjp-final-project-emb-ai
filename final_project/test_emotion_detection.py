import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector_joy(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    def test_emotion_detector_anger(self):
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

    def test_emotion_detector_disgust(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

    def test_emotion_detector_sadness(self):
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

    def test_emotion_detector_fear(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")
