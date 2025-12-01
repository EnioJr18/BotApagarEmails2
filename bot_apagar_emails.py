import time
import pyautogui
import subprocess

pyautogui.PAUSE = 1.0

def abrir_chrome_perfil(perfil_nome):
    print(f"--- Abrindo Gmail no perfil: {perfil_nome} ---")
    url = "https://mail.google.com"
    try:
        subprocess.Popen(f'start chrome --profile-directory="{perfil_nome}" "{url}"', shell=True)
        time.sleep(9) 
    except Exception as e:
        print(f"Erro: {e}")

def apagar_aba(nome_aba, x_aba, y_aba, x_select_all, y_select_all):
    print(f" > Indo para aba: {nome_aba}...")
    
    pyautogui.click(x=x_aba, y=y_aba)
    time.sleep(3) 
    
    print(" > Selecionando e-mails...")
    pyautogui.click(x=x_select_all, y=y_select_all)
    time.sleep(1)
    
    print(" > Apagando...")
    pyautogui.press('delete') 
    # Se o botão delete do teclado não funcionar, descomente a linha abaixo e coloque a coordenada da lixeira
    pyautogui.click(x=551, y=217) 
    
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

def main():
    # --- CONFIGURAÇÃO 1: PERFIS ---
    contas = {
        "eniojr100@gmail.com": "Default",
        "eniojunior111@gmail.com": "Profile 2" 
    }
    
    # Coordenada daquele quadradinho mestre que seleciona todos os e-mails da página
    # (Ele fica no topo esquerdo, acima da lista de e-mails)
    COORD_SELECT_ALL_X = 363  # <--- PREENCHA
    COORD_SELECT_ALL_Y = 217  # <--- PREENCHA
    
    # Coordenadas das Abas (onde você clica para mudar de categoria)
    abas = {
        #"Nome" : (000, 000),
        "Social":     (1052, 271), # <--- PREENCHA O X e Y da aba Social
        "Promoções":  (809, 265), # <--- PREENCHA O X e Y da aba Promoções
        "Atualizações": (1379, 261) # <--- PREENCHA O X e Y da aba Atualizações
    }

    email = input("Digite o e-mail: ").strip()

    if email in contas:
        abrir_chrome_perfil(contas[email])
        print("✅ E-mail encontrado. Iniciando processo de apagar e-mails...\n")
        time.sleep(2.5)
        
        for nome_aba, coords in abas.items():
            if coords[0] != 0: 
                apagar_aba(
                    nome_aba, 
                    coords[0], 
                    coords[1], 
                    COORD_SELECT_ALL_X, 
                    COORD_SELECT_ALL_Y
                )
            else:
                print(f"Pulei {nome_aba} (Coordenadas não preenchidas)")
                
        print("\n✅ Finalizado!")
    else:
        print("❌ E-mail não encontrado.")


if __name__ == "__main__":
    main()