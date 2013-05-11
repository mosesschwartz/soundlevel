import pyaudio
import wave
import sys
import time

def record_sound(chunk=1024, format=pyaudio.paInt8, channels=1, rate=44100, seconds=10):
    p = pyaudio.PyAudio()

    stream = p.open(format = format,
                channels = channels,
                rate = rate,
                input = True,
                frames_per_buffer = chunk)

    print "*", time.strftime('%H:%M:%S')
    all_data = []
    for i in range(0, rate / chunk * seconds):
        data = stream.read(chunk)
        all_data.append(data)

    stream.close()
    p.terminate()
    
    return all_data

def average_raw_sound(all_data):
    chunk_averages = []
    for chunk in all_data:
        ords = [ord(b) for b in chunk]
        chunk_averages.append( sum(ords) / len(ords) )
    return sum(chunk_averages)

def record_sound_all_night():
    try:
        o = open('sounddata.csv','w')
        o.write('time,volume\n')
        st = time.time()
        
        while 1:
            raw_sound = record_sound()
            avg_sound = average_raw_sound(raw_sound)
            o.write(str(time.strftime("%H:%M:%S")) + "," + str(avg_sound) + '\n')
        
    except:
        "Finishing"
        o.close()

if __name__ == "__main__":
    record_sound_all_night()
    
