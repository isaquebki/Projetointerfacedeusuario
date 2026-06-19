import tkinter as tk
from tkinter import ttk, messagebox

# ==========================
# JANELA
# ==========================
janela = tk.Tk()
janela.title("TORNEIO DE LUTA")
janela.geometry("450x550")
janela.configure(bg="#121212")
janela.resizable(False, False)

# ==========================
# TÍTULO
# ==========================
tk.Label(
    janela,
    text="⚔️ TORNEIO DE LUTA ⚔️",
    font=("Impact", 22),
    bg="#8B0000",
    fg="gold",
    pady=15
).pack(fill="x")

# ==========================
# COMBOBOX
# ==========================
tk.Label(
    janela,
    text="Escolha seu Guerreiro:",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
).pack(pady=(20, 5))

var_guerreiro = tk.StringVar()

combo = ttk.Combobox(
    janela,
    textvariable=var_guerreiro,
    values=[
        "🥷 Scorpion",
        "🐉 Liu Kang",
        "⚡ Raiden",
        "🔥 Ken",
        "🥋 Ryu"
    ],
    width=25,
    state="readonly",
    font=("Arial", 11)
)

combo.set("Selecione um lutador...")
combo.pack()

# ==========================
# LISTBOX
# ==========================
tk.Label(
    janela,
    text="Escolha seu Golpe Especial:",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
).pack(pady=(20, 5))

listbox = tk.Listbox(
    janela,
    font=("Arial", 11),
    height=6,
    width=28,
    bg="#1E1E1E",
    fg="white",
    selectbackground="#FF4500",
    selectforeground="white",
    bd=2,
    relief="solid"
)

listbox.pack()

golpes = [
    "🔥 Bola de Fogo",
    "⚡ Choque Elétrico",
    "💀 Fatality",
    "🌪️ Tornado Kick",
    "🐉 Dragon Punch",
    "❄️ Congelamento"
]

for golpe in golpes:
    listbox.insert(tk.END, golpe)

# ==========================
# FUNÇÃO
# ==========================
def lutar():

    guerreiro = var_guerreiro.get()
    indice = listbox.curselection()

    if guerreiro == "Selecione um lutador...":
        messagebox.showwarning(
            "Aviso",
            "Escolha um guerreiro!"
        )
        return

    if not indice:
        messagebox.showwarning(
            "Aviso",
            "Escolha um golpe especial!"
        )
        return

    golpe = listbox.get(indice[0])

    messagebox.showinfo(
        "Lutador Pronto!",
        f"⚔️ Guerreiro: {guerreiro}\n\n"
        f"🔥 Golpe: {golpe}\n\n"
        f"Prepare-se para a batalha!"
    )

# ==========================
# BOTÃO
# ==========================
tk.Button(
    janela,
    text="🥊 INICIAR COMBATE",
    command=lutar,
    bg="#B22222",
    fg="white",
    activebackground="#FF4500",
    activeforeground="white",
    font=("Arial", 13, "bold"),
    width=20,
    height=2,
    relief="raised",
    cursor="hand2"
).pack(pady=25)

# ==========================
# PAINEL DE REGRAS
# ==========================
frame = tk.Frame(
    janela,
    bg="#2C2C2C",
    bd=2,
    relief="ridge"
)

frame.pack(
    fill="x",
    padx=20,
    pady=10
)

tk.Label(
    frame,
    text="📜 REGRAS DA ARENA",
    font=("Arial", 11, "bold"),
    bg="#2C2C2C",
    fg="gold"
).pack(anchor="w", padx=10, pady=5)

tk.Label(
    frame,
    text="• Escolha um guerreiro.",
    bg="#2C2C2C",
    fg="white"
).pack(anchor="w", padx=10)

tk.Label(
    frame,
    text="• Escolha um golpe especial.",
    bg="#2C2C2C",
    fg="white"
).pack(anchor="w", padx=10)

tk.Label(
    frame,
    text="• Entre na arena e lute!",
    bg="#2C2C2C",
    fg="white"
).pack(anchor="w", padx=10, pady=(0, 10))

# ==========================
# RODAPÉ
# ==========================
tk.Label(
    janela,
    text="🏆 IFMT FIGHTER EDITION 🏆",
    bg="#121212",
    fg="gray"
).pack(side="bottom", pady=10)

janela.mainloop()