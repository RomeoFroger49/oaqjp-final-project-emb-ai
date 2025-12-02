from EmotionDetection.emotion_detection import predict_emotion
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test case for domiant joy emotion
        result_1 = predict_emotion('I am glad this happened')
        self.assertEqual(result_1['dominante_emotion'], 'joy')
        # Test case for dominant anger emotion
        result_2 = predict_emotion('I am really mad about this')
        self.assertEqual(result_2['dominante_emotion'], 'anger')
        # Test case for dominant disgust emotion
        result_3 = predict_emotion('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominante_emotion'], 'disgust')
        # Test case for dominant sadness emotion
        result_4 = predict_emotion('I am so sad about this')
        self.assertEqual(result_4['dominante_emotion'], 'sadness')
        # Test case for dominant fear emotion
        result_5 = predict_emotion('I am really afraid that this will happen')
        self.assertEqual(result_5['dominante_emotion'], 'fear')

unittest.main()