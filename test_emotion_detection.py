"""tests"""
from .emotion_detection import emotion_detector

tests = [
['I am glad this happened','joy'],    ['I am really mad about this','anger'],
     ['I feel disgusted just hearing about this','disgust'],
     ['I am so sad about this','sadness'],
      ['I am really afraid that this will happen',
      'fear']]


def test_joy():
    """test a bunch of items for proper dominant emotion"""
    for test in tests:
        assert emotion_detector(test[0])['dominant_emotion']==test[1]
