import time
import pyautogui

def apagar_emails():
    pyautogui.click(x=757, y=261)
    time.sleep(2)
    pyautogui.click(x=351, y=211)
    time.sleep(1)
    pyautogui.click(x=542, y=218)
    time.sleep(1.5)
    pyautogui.click(x=1030, y=283)
    time.sleep(0.8)
    pyautogui.click(x=351, y=211)
    time.sleep(0.8)
    pyautogui.click(x=542, y=218)
    time.sleep(1.5)
    pyautogui.click(x=1303, y=301)
    time.sleep(0.8)
    pyautogui.click(x=351, y=211)
    time.sleep(0.8)
    pyautogui.click(x=542, y=218)
    time.sleep(6)
    pyautogui.click(x=501, y=289)


def funcao_conta_2():
    time.PAUSE = 0.8
    time.sleep(6) 
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=1686, y=189)
    time.sleep(3)
    pyautogui.click(x=1879, y=148)
    time.sleep(1.5)
    pyautogui.click(x=1543, y=622)
    time.sleep(3)

def funcao_conta_1():
    time.PAUSE = 0.8 
    time.sleep(6)
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=1686, y=189)
    time.sleep(3)


def selecionar_conta_email():
    contas = {
        "eniojr100@gmail.com": funcao_conta_1,
        "eniojunior111@gmail.com": funcao_conta_2,
    }

    print("Contas disponíveis:")
    for conta in contas:
        print(f"- {conta}")

    conta_digitada = input("Digite o e-mail da conta desejada: ").strip()

    if conta_digitada in contas:
        print(f"Você selecionou: {conta_digitada}")
        contas[conta_digitada]()  # Chama a função correspondente
        return conta_digitada
    else:
        print("Conta não encontrada. Tente novamente.")

        
    
selecionar_conta_email()
apagar_emails()