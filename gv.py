import cv2
import numpy as np
import pyautogui
import time
import sys

# 1. Pega a resolução exata da tela onde o programa está rodando (EVITA O ERRO)
LARGURA, ALTURA = pyautogui.size() 

DURACAO_MAXIMA_SEGUNDOS = 120 # Limite de 2 minutos
FPS = 10.0

# 2. Mudança para codec altamente compatível com Windows
fourcc = cv2.VideoWriter_fourcc(*"XVID") 
out = cv2.VideoWriter("captura_automacao.avi", fourcc, FPS, (LARGURA, ALTURA))

print(f"=== GRAVADOR CORRIGIDO ({LARGURA}x{ALTURA}) ===")
print("Gravação iniciada...")
print("Para parar, aperte CTRL+C nesta janela ou feche o terminal.")
print("-" * 30)

tempo_inicio = time.time()

try:
    while True:
        if (time.time() - tempo_inicio) > DURACAO_MAXIMA_SEGUNDOS:
            print("\n[Aviso] Limite de tempo atingido.")
            break
            
        print(".", end="", flush=True)
        img = pyautogui.screenshot()
        
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Escreve o frame corrigido
        out.write(frame)
        
        time.sleep(1 / FPS) 

except KeyboardInterrupt:
    print("\n\n[Sucesso] Gravação interrompida pelo usuário.")
except Exception as e:
    print(f"\n\n[Erro] Ocorreu uma falha: {e}")
finally:
    out.release()
    print("[Pronto] O arquivo 'captura_automacao.avi' foi salvo!")
    sys.exit()