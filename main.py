import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Cores e estilos
COR_FUNDO = "#E7D4CF"
COR_FRAME = "#FFFFFF"
COR_TEXTO = "#343A40"
COR_BOTAO = "#747297"
COR_BOTAO_HOVER = "#645BB4"
COR_ESTRELA = "★"  # Estrela preenchida
COR_ESTRELA_VAZIA = "☆"  # Estrela vazia

tarefas = []  # Lista de dicionários: {"texto": "Tarefa", "favorito": False}

# Funções
def atualizar_telas():
    for widget in frame_tarefas.winfo_children():
        widget.destroy()
    for widget in frame_favoritos.winfo_children():
        widget.destroy()

    for i, tarefa in enumerate(tarefas):
        criar_item_tarefa(frame_tarefas, i, tarefa)

        if tarefa["favorito"]:
            criar_item_tarefa(frame_favoritos, i, tarefa, em_favoritos=True)

def criar_item_tarefa(pai, indice, tarefa, em_favoritos=False):
    frame = tk.Frame(pai, bg=COR_FRAME, pady=5)
    frame.pack(fill="x", padx=10, pady=3)

    lbl_texto = tk.Label(frame, text=tarefa["texto"], font=("Segoe UI", 12), bg=COR_FRAME, fg=COR_TEXTO, anchor="w")
    lbl_texto.pack(side="left", padx=(10, 5), fill="x", expand=True)

    btn_estrela = tk.Button(
        frame,
        text=COR_ESTRELA if tarefa["favorito"] else COR_ESTRELA_VAZIA,
        font=("Segoe UI", 14),
        bg=COR_FRAME,
        fg="#FFC107",
        bd=0,
        activebackground=COR_FRAME,
        cursor="hand2",
        command=lambda: alternar_favorito(indice)
    )
    btn_estrela.pack(side="right", padx=10)

    if not em_favoritos:
        btn_remover = tk.Button(
            frame,
            text="🗑",
            font=("Segoe UI", 12),
            bg=COR_FRAME,
            fg="#DC3545",
            bd=0,
            activebackground=COR_FRAME,
            cursor="hand2",
            command=lambda: remover_tarefa(indice)
        )
        btn_remover.pack(side="right", padx=5)

def adicionar_tarefa():
    texto = entrada_tarefa.get().strip()
    if texto:
        tarefas.append({"texto": texto, "favorito": False})
        entrada_tarefa.delete(0, tk.END)
        atualizar_telas()
    else:
        messagebox.showwarning("Entrada Inválida", "Digite uma tarefa válida!")

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        atualizar_telas()

def alternar_favorito(indice):
    tarefas[indice]["favorito"] = not tarefas[indice]["favorito"]
    atualizar_telas()

def on_enter(e):
    e.widget["background"] = COR_BOTAO_HOVER

def on_leave(e):
    e.widget["background"] = COR_BOTAO

# Interface
janela = tk.Tk()
janela.title("📝 Lista de Tarefas com Estrelas")
janela.geometry("400x720")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

# Abas
abas = tk.ttk.Notebook(janela)
abas.pack(padx=10, pady=10, fill="both", expand=True)

aba_tarefas = tk.Frame(abas, bg=COR_FUNDO)
aba_favoritos = tk.Frame(abas, bg=COR_FUNDO)
abas.add(aba_tarefas, text="Tarefas")
abas.add(aba_favoritos, text="Favoritos")

# Entrada e botões
entrada_tarefa = tk.Entry(
    aba_tarefas, font=("Segoe UI", 13),
    width=30, relief="solid", bd=1,
    bg=COR_FRAME, fg=COR_TEXTO, insertbackground=COR_TEXTO
)
entrada_tarefa.pack(pady=(20, 10), padx=10)

btn_adicionar = tk.Button(
    aba_tarefas, text="➕ Adicionar Tarefa",
    font=("Segoe UI", 11, "bold"),
    bg=COR_BOTAO, fg="#FFFFFF", relief="flat",
    activebackground=COR_BOTAO_HOVER, cursor="hand2",
    command=adicionar_tarefa
)
btn_adicionar.pack(pady=(0, 10), ipadx=10, ipady=5)
btn_adicionar.bind("<Enter>", on_enter)
btn_adicionar.bind("<Leave>", on_leave)

# Containers para listas
frame_tarefas = tk.Frame(aba_tarefas, bg=COR_FUNDO)
frame_tarefas.pack(fill="both", expand=True)

frame_favoritos = tk.Frame(aba_favoritos, bg=COR_FUNDO)
frame_favoritos.pack(fill="both", expand=True)

# Rodapé
rodape = tk.Label(janela, text="Trabalho da professora: Suzane", font=("Segoe UI", 9), bg=COR_FUNDO, fg="#868E96")
rodape.pack(pady=(0, 10))

janela.mainloop()
