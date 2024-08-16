import ctypes
import tkinter as tk

# Função para esvaziar a lixeira no Windows
def esvaziar_lixeira():
    # Exibir janela de progresso
    janela_progresso = tk.Tk()
    janela_progresso.title("Esvaziando Lixeira")
    janela_progresso.geometry("300x100")
    
    # Texto de progresso
    label = tk.Label(janela_progresso, text="Esvaziando a lixeira, por favor, aguarde...")
    label.pack(pady=20)
    
    # Atualizar a interface antes de esvaziar a lixeira
    janela_progresso.update()
    
    # Esvaziar a lixeira
    ctypes.windll.shell32.SHEmptyRecycleBinW(0, None, 0x0007)
    
    # Fechar a janela de progresso após concluir
    janela_progresso.destroy()

    # Criar uma nova janela para a mensagem de conclusão
    janela_concluido = tk.Tk()
    janela_concluido.title("Concluído")
    janela_concluido.geometry("300x100")
    
    label_concluido = tk.Label(janela_concluido, text="A lixeira foi esvaziada com sucesso!")
    label_concluido.pack(pady=20)
    
    # Fechar automaticamente após 5 segundos
    janela_concluido.after(5000, janela_concluido.destroy)
    
    # Executar a janela
    janela_concluido.mainloop()

# Chame a função para esvaziar a lixeira
esvaziar_lixeira()
