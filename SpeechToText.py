import speech_recognition as sr
import os
import threading

from mtranslate import translate

from colorama import Fore , Style , init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.GREEN + "Listning..." , end="" , flush = True)
        print(Style.RESET_ALL , end="" , flush=True)

def translate_hindi_to_english(text):
    eng_text = translate(text , "en-us")
    return eng_text

def speech_to_text_python():
    recognizer = sr.Recognizer()

    #These lines can be skipped its just this makes it efficient
    recognizer.dynamic_energy_threshold = False  #Reduces machine noises and other noises etc
    recognizer.energy_threshold = 4000 # energy of the voice (can change)
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3 #if we stop speaking for 0.3 sec the ai will understand we stopped talking
    recognizer.operation_timeout = None #It listens to however long we speak basically timeout nhi hoga
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2 #jitne time tk nhi bola uske baad recognise krega

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "Listning..." , end="" , flush = True)
            try:
                audio = recognizer.listen(source,timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Recog..." , end="" , flush=True)
                raw_text = recognizer.recognize_google(audio, language="hi-IN")  # CAN THROW ERROR
                recognizer_text = raw_text.lower()
                if recognizer_text:
                    translated_text = translate_hindi_to_english(recognizer_text)
                    print("\r" + Fore.BLUE + "User: " + translated_text)
                    return translated_text
                
                else:
                    return ""
            except sr.UnknownValueError:
                recognizer_text = ""
            finally:
                print("\r" , end="" , flush=True)

            os.system("cls" if os.name == "nt" else "clear")

        stt_thread = threading.Thread(target=speech_to_text_python)
        print_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_thread.start()
        stt_thread.join()
        print_thread.join()


speech_to_text_python()
            
            
