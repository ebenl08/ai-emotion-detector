import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        test_case = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }
        for statement in test_case.keys():
            self.assertEqual(emotion_detector(statement)['dominant_emotion'], test_case[statement])
    
if __name__ == "__main__":
    unittest.main()