from tkinter import scrolledtext
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TBPM, TKEY


def inject_data(DIR, BPM, KEY):
    try:
        audio = ID3(DIR)
    except ID3NoHeaderError:
        audio = ID3()

    audio.add(TBPM(text=[BPM]))
    audio.add(TKEY(text=[KEY]))
    audio.save(DIR)
    print(audio.getall("TBPM"))
    print(audio.getall("TKEY"))
    return True 

    


"""Saves audio file wt metadata"""
#def save():
#    """
#    Args: Audio File, BPM, Key
#   Return: Saved file at desired locaton
#    """
