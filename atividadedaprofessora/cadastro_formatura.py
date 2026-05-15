import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- JANELA ----------------
janela = tk.Tk()
janela.title("Sistema Neon - Cadastro")
janela.geometry("700x500")
janela.configure(bg="#0D1117")
janela.resizable(False, False)

# ---------------- CORES ----------------
BG = "#0D1117"
NEON = "#00E5FF"
NEON2 = "#FF00FF"
TEXT = "#FFFFFF"
BOX = "#161B22"

# ---------------- TÍTULO ----------------
tk.Label(
    janela,
    text="CADASTRO DE CONVIDADOS",
    font=("Consolas", 22, "bold"),
    bg=BG,
    fg=NEON
).pack(pady=20)

# ---------------- FUNÇÃO CAMPOS ----------------
def criar_campo(texto):
    tk.Label(
        janela,
        text=texto,
        font=("Consolas", 11, "bold"),
        bg=BG,
        fg=NEON2
    ).pack()

    entry = tk.Entry(
        janela,
        font=("Consolas", 12),
        bg=BOX,
        fg=TEXT,
        insertbackground=NEON,
        relief="flat",
        width=40
    )
    entry.pack(pady=5)
    return entry

# ---------------- CAMPOS ----------------
ent_nome = criar_campo("NOME")
ent_cpf = criar_campo("CPF")
ent_email = criar_campo("E-MAIL")

# ---------------- COMBOBOX ----------------
tk.Label(
    janela,
    text="TIPO DE CONVITE",
    font=("Consolas", 11, "bold"),
    bg=BG,
    fg=NEON2
).pack()

combo_tipo = ttk.Combobox(
    janela,
    values=["Pista", "VIP", "Camarote"],
    state="readonly",
    width=37
)
combo_tipo.pack(pady=10)
combo_tipo.current(0)

# ---------------- FUNÇÃO CADASTRAR ----------------
def cadastrar():
    nome = ent_nome.get().strip()
    cpf = ent_cpf.get().strip()
    email = ent_email.get().strip()
    tipo = combo_tipo.get()

    if not nome or not cpf:
        messagebox.showwarning("Erro", "Preencha NOME e CPF!")
        return

    mensagem = f"""
    Cadastro realizado com sucesso!

    Nome: {nome}
    CPF: {cpf}
    E-mail: {email}
    Tipo: {tipo}
    """

    messagebox.showinfo("Sucesso", mensagem)

    ent_nome.delete(0, tk.END)
    ent_cpf.delete(0, tk.END)
    ent_email.delete(0, tk.END)
    combo_tipo.current(0)

# ---------------- BOTÃO ----------------
tk.Button(
    janela,
    text="CADASTRAR",
    font=("Consolas", 14, "bold"),
    bg=NEON,
    fg="black",
    activebackground=NEON2,
    activeforeground="white",
    cursor="hand2",
    relief="flat",
    command=cadastrar
).pack(pady=30, ipadx=10, ipady=5)

# ---------------- LOOP ----------------
janela.mainloop()