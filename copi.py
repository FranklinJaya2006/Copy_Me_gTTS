import speech_recognition  as srec
from gtts import gTTS
import  os

def dengar() :
    tangkap = srec.Recognizer() #mengenali audio

    with srec.Microphone() as source : #microphone
        print("Mendengarkan..........")
        
        audio = tangkap.listen(source,phrase_time_limit=5) #phrase_time_limit berapa lama didengar #listen mendengar
        
        try :
            print("Mengerti..............")
            text=tangkap.recognize_google(audio,language='id-ID')
            print(text)
            return text
        except srec.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None

def duplikasi(dup):
    bic = 'bicara.mp3'
    def titis() :
        tts = gTTS(text=dup,lang='id',slow=False) #penggunaan google TTS
        tts.save(bic)
        os.system(f'afplay {bic}')
    titis()
            
def jalankan() :
    go = dengar() #penggunaan google TTS
    duplikasi(go)
    
    
jalankan()
    