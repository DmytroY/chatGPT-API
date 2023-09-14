# experiments with chatGPT API 

```
sudo apt install portaudio19-dev python3-pyaudio
sudo apt install ffmpeg
pip install -r requirements.txt

```

It works but ALSA trow error messages, to hide error messages run application with error redirect to null:
```
python3 main.py 2>/dev/null
```