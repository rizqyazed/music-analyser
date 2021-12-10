# Libraries used
import librosa

# Function for finding average music note in a sample
def average(lst):  
    return sum(lst)/len(lst)

def analyse(audio):

    # Referencing the audio file that is being analysed
    audio = audio

    # Loading the audio file using Librosa. p,x is the audio's waveform and the q,y is the sample rate(sr) of the audio. 
    # These variables are important as many fucntions in this library requires it.
    p, q = librosa.load(audio)
    #x, y = librosa.load(audio, duration=25) # This is used to generate the chroma graph which is why only 1 second of the song is used. (Too many data

    # List to store the average abundance of each note in the sample's chroma graph
    key_chrom = []

    tempo, br = librosa.beat.beat_track(y=p, sr=44100) # This fucntions simply outputs the tempo using the variables p(waveform) and the sample rate of the song.
    song_chroma = librosa.feature.chroma_stft(y=p, sr=44100) # THis function generates the chroma graph from the 1 second sample of the audio file

    # The chromatic scale.
    pitches = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

    # Goes through every single child of the list
    for y in range(len(song_chroma)):
        #print(str(pitches[y]) + '\t' + str(song_chroma[y])) (used to test what chroma graph looks like for each note)
        key_chrom.append(average(song_chroma[y])) # Appends the average abundance of each note into key_chrom list using the average function from earlier.
        print(str(pitches[y]) + '\t' + str(key_chrom[y]))

    copy_key= key_chrom[:]
    largest = max(key_chrom)
    copy_key.remove(largest)
    second_largest = max(copy_key)
    pitch_id_1 = key_chrom.index(largest)
    pitch_id_2 = key_chrom.index(second_largest)

    #print(pitches[pitch_id_1])
    #print(librosa.note_to_hz(pitches[pitch_id_1]))

    #print(pitches[pitch_id_2])
    #print(librosa.note_to_hz(pitches[pitch_id_2]))

    if librosa.note_to_hz(pitches[pitch_id_1]) > librosa.note_to_hz(pitches[pitch_id_2]):
        pitch_id = pitch_id_2
        # Finds the location of the note which has the highest abundance
        pitch = pitches[pitch_id] # Links that to to the chromatic scale to find what note it is.

        return  tempo, pitch
    else:
        print("Audio file unsupported...")
        return None, None

