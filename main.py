from transformers import pipeline
import pyttsx3

# ChatBot sınıfı - Chatbot ile ilgili tüm işlemleri yapacak sınıf
class ChatBot:
    
    def __init__(self):
        # DialoGPT modelini yükle
        self.chatbotPipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")
        
        # Sesli yanıt motorunu başlat
        self.speechEngine = pyttsx3.init()
    
    def speak(self, text):
        # Metni sesli olarak okut
        self.speechEngine.say(text)
        self.speechEngine.runAndWait()
    
    def chatWithBot(self):
        # ChatBot ile başlatıcı mesaj
        print("ChatBot: Merhaba! Size nasıl yardımcı olabilirim?")
        self.speak("Merhaba! Size nasıl yardımcı olabilirim?")
        
        while True:
            userInput = input("Siz: ")
            
            if userInput.lower() == "çık" or userInput.lower() == "exit":
                print("ChatBot: Görüşmek üzere!")
                self.speak("Görüşmek üzere!")
                break
            
            # Modelden cevap al
            response = self.chatbotPipeline(userInput, max_length=1000, num_return_sequences=1)
            
            # Cevabı ekrana yazdır
            botResponse = response[0]['generated_text']
            print(f"ChatBot: {botResponse}")
            
            # Cevabı sesli ilet
            self.speak(botResponse)

# Ana fonksiyon - ChatBot'u başlatacak ve kullanıcı ile etkileşimi sağlayacak
if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.chatWithBot()
