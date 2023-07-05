from gtts import gTTS
import os

def speak(text, language='tr'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

# Metni buraya girin
metin = "anıl klimayı kapat elektirik gidiyor"

#Merhaba ayhan bey, sesli metin projesi için deneme yapıyorum ve kalite ortalama olarak bu şekilde olucak. Bu tarz sesli içerikleri aylık 10 dakika ucretsiz kullanılabiliyor. Ücretli versiyonu aylık 30 dolar olarak murf.com da satılıyor . ama bu sitenin bir eksisi var. Videoları bu sitede düzenleyemiyorsunuz. Düzenleme kısmını ayrıyetten yapılması gerekiyor
# Metni sesli olarak okutun
speak(metin)