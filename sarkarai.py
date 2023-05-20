import pyttsx3
import pyaudio
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import keyboard
import pyjokes
#from PyDictionary import PyDictionary as Dic
Assistant=pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
 
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',160 )
 
def Speak(audio):
 
     print("  ")
     Assistant.say(audio)
     print(f":{audio}")
     print("  ")
     Assistant.runAndWait()    

def takecommand():
     command=sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening.....")
         command.pause_threshold=1
         audio=command.listen(source)
         
         try:
             print("Recognizing...")
             query=command.recognize_google(audio,language='en-in')
             print(f"You Said:{query}")
         except Exception as Error:
              return "none"
         return query.lower()

query=takecommand()

if 'hi' in query:
     Speak("hi sir")
else:
     Speak("no command found") 
def TaskExe():
     def Music():
         Speak("tell me the name of the song")
         musicname=takecommand()
         pywhatkit.playonyt(musicname)
         Speak("your song has been started,maza lo")
     def OpenApps():
         Speak("ok ,you have to wait")
         
         if 'notepad plus plus' in query:
             os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
         elif 'whatsapp' in query:
             os.startfile("C:\\Users\\Atharva Dhamdhere\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
         elif 'microsoft word' in query:
             os.startfile("C:\\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
         elif 'chrome' in query:
             os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
         elif 'facebook' in query:
             webbrowser.open('https://www.facebook.com/')
         elif 'instagram' in query:
             webbrowser.open('https://www.instagram.com/')
         elif 'amazon' in query:
             webbrowser.open('https://www.amazon.com/')
         elif 'youtube' in query:
             webbrowser.open('https://www.youtube.com')        
         Speak("your app is open")   
     def CloseApps():
         Speak("ok i will close it")
         if 'youtube' in query:
             os.system("TASKKILL /F /im chrome.exe")
         elif 'chrome' in query:
             os.system("TASKKILL /F /im chrome.exe") 
         elif 'microsoft word' in query:
             os.system("TASKKILL /F /im WINWORD.EXE")
         elif 'notepad plus plus' in query:
             os.system("TASKKILL /F /im notepad++.exe")              
         elif 'whatsapp' in query:
             os.system("TASKKILL /F /im WhatsApp.exe")
         Speak("your commandhas been succesfully completed!")             
     def youtubeauto():
         Speak("Whats your command")
         comm=takecommand()
         
         if 'pause' in comm:
             keyboard.press('space bar')
         elif 'restart' in comm:
             keyboard.press('0')
         elif 'mute' in comm:
             keyboard.press('m')
         elif 'skip' in comm:
             keyboard.press('l')
         elif 'back' in comm:
             keyboard.press('j')
         elif 'full screen' in comm:
             keyboard.press('f')
         elif 'film mode' in comm:
             keyboard.press('t')
         elif 'pause' or 'play' in comm:
             keyboard.press('k')    
         Speak("done sir")
#     def Dict():
#        Speak("Activated Dictionary!")
#         Speak("tell me the problem!")
#         probl=takecommand()
#         if 'meaning' in prob1:
#            prob1=probl.replace("what is the","")
#             probl=prob1.replace("baburao","")
#             probl=probl.replace("of")
#             probl=probl.replace("meaning of","")
#             result=Dic.meaning(probl)
#             Speak(f"the meaning for {probl} is {result}")
#         elif 'synonym' in probl:
#             probl=probl.replace("what is the","")
#             probl=probl.replace("baburao","")
#             prob1=prob1.replace("of","")
#             probl=probl.replace("synonym of","")
#             result=Dic.synonym(prob1)
#             Speak(f"the meaning for {prob1} is {result}")
#         elif 'antonym' in probl:
#             prob1=prob1.replace("what is the ","")
#             prob1=prob1.replace("baburao","")
#             probl=probl.replace("of","")
#             probl=probl.replace("antonym of","")
#             result=Dic.antonym(probl)
#             Speak(f"the antonym for {probl} is {result}")
#         Speak("exited dictionary")"""             
     def ChromeAuto():
         Speak("Chrome automation started")
         command=takecommand()
         if 'close this tab' in command:
             keyboard.press_and_release('ctrl+w')
         elif 'open new tab' in command:
             keyboard.press_and_release('ctrl+t')
         elif 'open new window' in command:
             keyboard.press_and_release('ctrl+n')
         elif 'history' in command:
             keyboard.press_and_release('ctrl+h')         
     while True:
         query=takecommand()
         if 'hello' in query:
             Speak("hello sir , i am baburao")
             Speak("Your AI friend!")
             Speak("how may i help you?")
         elif 'tell me about ganesh' in query:
             Speak("ganesh is the most handpump guy in the college")
         elif 'tell me about tejas' in query:
             Speak("tejas is the chocolate boy of college")
         elif 'tell me about srinath' in query:
             Speak("srinath likes to see girls")
         elif 'tell me about srinath' in query:
             Speak("he is a reel star")         
         elif 'keep quiet' in query: 
             Speak("ok boss,bye and get out")
             break
         elif 'youtube search' in query:
             Speak("ok sir,this is what i have found ")
             query=query.replace("baburao","")
             query=query.replace("youtubesearch","")
             web='https://www.youtube.com/results?search_query='+ query
             webbrowser.open(web)
             Speak("done boss")  
         elif 'google search' in query:
             Speak("this is what i found for your search")
             query=query.replace("baburao","")
             query=query.replace("google search","")
             pywhatkit.search(query)
             Speak("done ")
         elif 'website' in query:
             Speak("ok sir, launching....")
             query=query.replace("baburao","")
             query=query.replace("website","")
             query=query.replace(" ","")
             web1=query.replace("open","")
             web2='https://www.'+web1+'.com'
             webbrowser.open(web2)
             Speak("launched!")  
         elif 'play music' in query:
             Music()
         elif 'wikipedia' in query:
             Speak("searching wikipedia....")
             query=query.replace("baburao","")
             query=query.replace("wikipedia","")
             wiki=wikipedia.summary(query,2)
             Speak(f"According to wikipedia {wiki}")             
         elif 'open notepad plus plus' in query:
             OpenApps()
         elif 'open whatsapp' in query:
             OpenApps()
         elif 'open microsoft word' in query:
             OpenApps()
         elif 'open chrome' in query:
             OpenApps()
         elif 'open facebook' in query:
             OpenApps()
         elif 'open instagram' in query:
             OpenApps()    
         elif 'open amazon' in query:
             OpenApps() 
         elif 'open youtube' in query:
             OpenApps()             
         elif 'close yotube' in query:
             CloseApps()
         elif 'close chrome' in query:
             CloseApps()
         #elif 'close microsoft word' in query;
          #   CloseApps()
         elif 'close notepad plus plus' in query:
             CloseApps()
         elif 'close whatsapp' in query:
             CloseApps()
         elif 'pause' in query:
             keyboard.press('space bar')
         elif 'restart' in query:
             keyboard.press('0')
         elif 'mute' in query:
             keyboard.press('m')
         elif 'skip' in query:
             keyboard.press('l')
         elif 'back' in query:
             keyboard.press('j')
         elif 'full screen' in query:
             keyboard.press('f')
         elif 'film mode' in query:
             keyboard.press('t')
         elif 'pause' in query:
             keyboard.press('k')
         elif 'youtube commands' in query:
             youtubeauto()
         elif 'close this tab' in query:
             keyboard.press_and_release('ctrl+w')
         elif 'open new tab' in query:
             keyboard.press_and_release('ctrl+t')
         elif 'open new window' in query:
             keyboard.press_and_release('ctrl+n')
         elif 'history' in query:
             keyboard.press_and_release('ctrl+h')
         elif 'chrome automation' in query:
             ChromeAuto()
         elif 'jokes' in query:
             get=pyjokes.get_joke()
             Speak(get)
         elif 'repeat my words' in query:
             Speak("Speak sir!")
             jj=takecommand()
             Speak(f"you said :{jj}") 
         """elif 'open dictionary' in query:
             Dict()"""  
TaskExe()             