import pyttsx3
import datetime
import time
import speech_recognition as sr
import webbrowser
import pyautogui
import pygame
import google.generativeai as genai

genai.configure(api_key="AIzaSyCvTQDk-Cp5Auc-B6pug2KuBtshI-IMrvY")
for m in genai.list_models():
    if 'genarateContent' in m.supported_generation_methods:
        print(m.name)
model = genai.GenerativeModel('gemini-pro')

pygame.mixer.init()

texto_fala = pyttsx3.init()
som_on = pygame.mixer.Sound('Sound-on.wav')


#   FUNÇÂO FALAR 

def falar(audio):

    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate", 170) # ---Alterar a Velocidade da Voz---
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id) # ---Alteração de Voz---
    texto_fala.say(audio)
    texto_fala.runAndWait()

#   FUNÇÂO BEM VINDO E ATIVAÇÂO
    
def saudacoes():
    hora = datetime.datetime.now().hour

    if hora >=6 and hora <12:
        falar("Bom dia Chefe!")
        falar("Que hoje seja um dia abençoado, e que Deus no de forças para vencer mais uma luta, bora para o trabalho!")
    elif hora >=12 and hora <18:
        falar("Boa tarde Chefe!")
    elif hora >=18 and hora <24:
        falar("Boa noite Chefe!")
        falar("Tenha uma ótima noite, bom descanso")
    else:
        falar("Boa noite Chefe!, já está tarde em!")
    
def aguardar_ativacao():
    while True:
        print("Aguardando ativação...")
        comando = microfone().lower()
        if 'spark' in comando:
            som_on.play()
            return True

    # COMANDOS INTERATIVOS

def estou_bem():
    falar("Que Maravilha!")


def boladao():
    falar("EU SOU BOLADÃO!")

def isso_ai():
    falar("ISSO AÍ!")

  # COMANDOS PARA O SPARKY
       
def desligar_pc():
    falar("Ok Chefe!, até a próxima")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.click(x=21, y=1016)
    time.sleep(2)
    pyautogui.click(x=18, y=931)
    pyautogui.click(x=18, y=931)

def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M")
    falar("Agora são:")
    falar(Tempo)

def discord():
    pyautogui.press("win")
    pyautogui.write("Discord")
    pyautogui.press("enter")
    falar("Abrindo Discord Chefe!")

def assistir():
    pyautogui.press("win")
    pyautogui.write("Netflix")
    pyautogui.press("enter")
    time.sleep(2)
    falar("O que você deseja assistir Chefe?")
    assistir = microfone()
    pyautogui.click(x=1794, y=58)
    time.sleep(1)
    pyautogui.write(assistir)
    time.sleep(1)
    pyautogui.click(x=189, y=239)
    time.sleep(2)
    falar(f"Esse" + assistir + "?")
    resposta = microfone()
    if "sim" in resposta:
        pyautogui.click(x=957, y=216)
        falar("Bom cinema!")

    elif "não" in resposta:
        pyautogui.click(x=1314, y=55)
        falar("Desculpa, pode por favor selecionar o correto?")
    else:
        falar("Desculpa, pode por favor selecionar o correto?")

def jogar():
    falar("Qual jogo você quer jogar Chefe?")
    comando = microfone()

    if 'Vavá' in comando:
        url = f"https://www.youtube.com/watch?v=HuJOVEaOrmw&list=RDHuJOVEaOrmw&start_radio=1"
        webbrowser.open(url)
        pyautogui.press("win")
        pyautogui.write("Valorant")
        pyautogui.press("enter")
        falar("Aqui está Chefe, boa jogatina!")

    elif 'RPG' in comando:
        url = f"https://www.youtube.com/watch?v=HuJOVEaOrmw&list=RDHuJOVEaOrmw&start_radio=1"
        webbrowser.open(url)
        pyautogui.press("win")
        pyautogui.write("Path of Exile")
        pyautogui.press("enter")
        falar("Aqui está Chefe, boa jogatina!")

    elif 'Mine' or 'Maine' in comando:
        url = f"https://www.youtube.com/watch?v=HuJOVEaOrmw&list=RDHuJOVEaOrmw&start_radio=1"
        webbrowser.open(url)
        pyautogui.press("win")
        pyautogui.write("TLaucher")
        pyautogui.press("enter")
        falar("Aqui está Chefe, boa jogatina!")
    
    

def data():
    ano = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    falar("A data atual é:")
    falar(dia)
    falar("do" + mes)
    falar("de" + ano)


def pesquisar():
    falar("O que você gostaria de Pesquisar Chefe?")
    comando = microfone()
    url = f"https://www.google.com/search?q={comando}"
    webbrowser.open(url)
    falar(f"Aqui está os resultados para {comando}.")


def tocar_musica():
    falar("Qual música você gostaria de ouvir Chefe?")
    comando = microfone()

    if 'Nirvana' in comando:
        url = f"https://www.youtube.com/watch?v=hTWKbfoikeg&list=RDEMDz952MrmDXLULMlo7SEXUw&start_radio=1"
        webbrowser.open(url)
        falar(f"Aqui está uma playlist insana do {comando}.")

    elif 'minhas músicas' in comando:
        url = f"https://www.youtube.com/watch?v=HuJOVEaOrmw&list=RDHuJOVEaOrmw&start_radio=1"
        webbrowser.open(url)
        falar(f"Aqui está, suas musicas preferidas meu Chefe!")

    else:
        query = f"youtube {comando}"
        url = f"https://www.youtube.com/results?search_query={'+'.join(query.split())}"
        webbrowser.open(url)
        falar(f"Aqui estão os resultados para {comando}.")

def microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Reconhecendo...")
        comando = r.recognize_google(audio, language='pt-br')
        print(comando)
    
    except Exception as e:
        return "None"

    return comando

if __name__ == "__main__":

    # Aguarda ativação
    assistente_ativo = False

    while True:
        if not assistente_ativo:
            assistente_ativo = aguardar_ativacao()

        else:
            comando = microfone().lower()


            if comando:
                if 'bom dia' in comando:
                    saudacoes()

                elif 'boa tarde' in comando:
                    saudacoes()
                
                elif 'boa noite' in comando:
                    saudacoes()

                elif 'desligar computador' in comando:
                    desligar_pc()

                elif 'como você está' in comando:
                    falar("Estou Feliz com a sua companhia meu Pai, e Você?")

                elif 'o que você é' in comando:
                    boladao()
                
                elif 'você é o quê' in comando:
                    boladao()
                
                elif 'é o quê' in comando:
                    boladao()
                
                elif 'boladão' in comando:
                    isso_ai()

                elif 'estou bem' in comando:
                    estou_bem()
                    
                elif 'hora' in comando:
                    tempo()
                    assistente_ativo = False
                elif 'data' in comando:
                    data()
                    assistente_ativo = False
                elif 'pesquisar' in comando:
                    pesquisar()
                    assistente_ativo = False
                elif 'jogar' in comando:
                    jogar()
                    assistente_ativo = False
                elif 'música' in comando:
                    tocar_musica()
                    assistente_ativo = False
                elif 'abrir discord' in comando:
                    discord()
                    assistente_ativo = False
                elif 'assistir' in comando:
                    assistir()
                    assistente_ativo = False
                else:
                    response = model.generate_content(comando)
                    falar(response.text)
                    assistente_ativo = False
