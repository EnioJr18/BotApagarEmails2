## 📧 Gmail Cleaner Bot (RPA)

Um bot de automação visual desenvolvido em Python para limpar categorias específicas do Gmail (Social, Promoções, Atualizações) em múltiplas contas automaticamente.

## 🎯 Objetivo

O *Gmail* costuma acumular milhares de e-mails inúteis nas abas Social, Promoções e Atualizações. Apagar isso manualmente é repetitivo e cansativo.

Este projeto automatiza o processo: <br>
    **1.Abre o Chrome no perfil específico do usuário.** <br>
    **2.Navega até o Gmail.** <br>
    **3.Entra nas abas configuradas.** <br>
    **4.Seleciona todos os e-mails e os envia para a lixeira.** <br>
    **5.Repete o processo para garantir que múltiplas páginas sejam limpas.** <br>

## ⚠️ Pré-requisitos e Limitações

Por ser uma automação visual (baseada em coordenadas de tela X, Y), este bot *é dependente da resolução do monitor*.

* *Não mexa no mouse* enquanto o bot estiver rodando.
* O navegador deve abrir sempre maximizado ou na mesma posição e tamanho.
* Se você trocar de monitor, precisará recalibrar as coordenadas (veja abaixo).

## 🛠️ Instalação

1.Certifique-se de ter o Python instalado. <br>
2.Instale a biblioteca pyautogui: <br>
      pip install pyautogui <br>


## ⚙️ Configuração (Importante)

Antes de rodar, você precisa ajustar o script bot_gmail.py com os seus dados.

#### 1. Descobrindo o Perfil do Chrome
O script precisa saber o nome da pasta do perfil para abrir o navegador logado.

  1.Abra seu Chrome manualmente na conta desejada. <br>
  2.Digite chrome://version na barra de endereço. <br>
  3.Procure por Caminho de perfil (Profile Path). <br>
  4.Copie o nome final da pasta (Ex: Default, Profile 1, Profile 2). <br>
  5.Atualize o dicionário CONTAS no código. <br>

#### 2. Calibrando as Coordenadas
Use o script auxiliar calibrador.py para descobrir onde clicar na sua tela.

1.Rode o script: <br>
   python pega_posicao_mouse.py <br>

2.Posicione o mouse sobre o botão desejado (Ex: Aba Social). <br>
3.Anote o X e Y que aparecer no terminal. <br>
4.Atualize o dicionário COORDS no arquivo principal. <br>

*Coordenadas necessárias:*
* Aba Social / Promoções / Atualizações
* Quadradinho "Selecionar Tudo" (Canto superior esquerdo da lista).
* Botão Lixeira (Opcional, caso o delete do teclado falhe).

## 🚀 Como Usar

      Execute o arquivo principal:
          python bot_gmail.py

1.O terminal mostrará as contas cadastradas. <br>
2.Digite o e-mail da conta que deseja limpar. <br>
3.Solte o mouse e veja a mágica acontecer. <br>

## 🛑 Parada de Emergência (Fail-safe)

Se o bot começar a clicar em lugares errados (ex: abriu uma janela inesperada), faça o seguinte movimento rápido:

**Arraste o mouse bruscamente para o canto SUPERIOR ESQUERDO da tela.**

Isso aciona o <i>pyautogui.FailSafeException</i> e encerra o programa imediatamente.

## 📝 Estrutura do Projeto

* bot_gmail.py: O código principal da automação.
* calibrador.py: Utilitário para pegar posição X e Y do mouse.
* README.md: Este arquivo de documentação.

## 👨‍💻 Autor
Desenvolvido por Enio Jr como parte de um portfólio de Engenharia de Software Backend.

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
