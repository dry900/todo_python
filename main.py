import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Cores customizadas
COR_FUNDO = "#F8F9FA"
COR_FRAME = "#FFFFFF"
COR_TEXTO = "#212529"
COR_BOTAO = "#4CAF50"
COR_BOTAO_HOVER = "#45A049"
COR_LISTBOX_BG = "#F1F3F5"
COR_LISTBOX_SELECAO = "#D3D3D3"

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Digite uma tarefa válida!")

# Função para remover tarefa
def remover_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        lista_tarefas.delete(indice)
    except IndexError:
        messagebox.showwarning("Erro", "Selecione uma tarefa para remover.")

# Efeitos hover nos botões
def on_enter(e):
    e.widget["background"] = COR_BOTAO_HOVER

def on_leave(e):
    e.widget["background"] = COR_BOTAO

# Criar janela principal
janela = tk.Tk()
janela.title("📝 Lista de Tarefas")
janela.geometry("300x600")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

# Frame principal
frame = tk.Frame(janela, bg=COR_FRAME, bd=1, relief="solid")
frame.pack(padx=20, pady=30, fill="both", expand=True)

# Título
titulo = tk.Label(frame, text="📋 Minhas Tarefas", font=("Segoe UI", 18, "bold"), bg=COR_FRAME, fg=COR_TEXTO)
titulo.pack(pady=(20, 10))

# Entrada de tarefa
entrada_tarefa = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=35,
    relief="solid",
    bd=1,
    bg="#FFFFFF",   # fundo branco puro
    fg="#212529",   # texto mais escuro
    insertbackground="#212529"  # cursor visível
)
entrada_tarefa.pack(pady=(5, 10))

# Botão Adicionar
botao_adicionar = tk.Button(
    frame,
    text="➕ Adicionar Tarefa",
    font=("Segoe UI", 11, "bold"),
    bg=COR_BOTAO,
    fg="#FFFFFF",
    activebackground=COR_BOTAO_HOVER,
    relief="flat",
    cursor="hand2",
    command=adicionar_tarefa
)
botao_adicionar.pack(pady=(0, 10), ipadx=10, ipady=5)
botao_adicionar.bind("<Enter>", on_enter)
botao_adicionar.bind("<Leave>", on_leave)

# Lista de tarefas
lista_tarefas = tk.Listbox(
    frame,
    font=("Segoe UI", 12),
    width=45,
    height=10,
    bg=COR_LISTBOX_BG,
    fg=COR_TEXTO,
    bd=0,
    highlightthickness=1,
    selectbackground=COR_LISTBOX_SELECAO,
    activestyle="none"
)
lista_tarefas.pack(pady=10)

# Botão Remover
botao_remover = tk.Button(
    frame,
    text="🗑️ Remover Selecionada",
    font=("Segoe UI", 11, "bold"),
    bg=COR_BOTAO,
    fg="#FFFFFF",
    activebackground=COR_BOTAO_HOVER,
    relief="flat",
    cursor="hand2",
    command=remover_tarefa
)
botao_remover.pack(pady=(5, 20), ipadx=10, ipady=5)
botao_remover.bind("<Enter>", on_enter)
botao_remover.bind("<Leave>", on_leave)

# Rodapé
label_credito = tk.Label(
    janela,
    text="Trabalho da professora: Suzane",
    font=("Segoe UI", 9),
    fg="#868E96",
    bg=COR_FUNDO
)
label_credito.pack()

# Iniciar interface
janela.mainloop()
