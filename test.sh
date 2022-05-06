arecord -f S16_LE -d 3 -r 16000 test-mic.wav
python3 train.py
