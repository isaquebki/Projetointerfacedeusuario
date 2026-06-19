import tkinter as tk

janela = tk.Tk()
janela.title("🎮 Gamer Volume Control")
janela.geometry("500x350")
janela.configure(bg="#0D1117")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="🎮 GAMER AUDIO PANEL",
    font=("Consolas", 20, "bold"),
    bg="#0D1117",
    fg="#00FFAA"
)
titulo.pack(pady=15)

# Moldura
frame = tk.Frame(
    janela,
    bg="#161B22",
    highlightbackground="#00FFAA",
    highlightthickness=2
)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Variável do volume
var_volume = tk.DoubleVar(value=50)

# Texto
tk.Label(
    frame,
    text="AJUSTE O VOLUME",
    font=("Consolas", 12, "bold"),
    bg="#161B22",
    fg="#58A6FF"
).pack(pady=(15, 10))

# Scale
scale = tk.Scale(
    frame,
    variable=var_volume,
    from_=0,
    to=100,
    orient="horizontal",
    length=350,
    bg="#161B22",
    fg="white",
    troughcolor="#21262D",
    activebackground="#00FFAA",
    highlightthickness=0,
    font=("Consolas", 10),
    sliderlength=25
)
scale.pack(pady=10)

# Resultado
label_resultado = tk.Label(
    frame,
    text="🔊 Volume: 50%",
    font=("Consolas", 16, "bold"),
    bg="#161B22",
    fg="#00FFAA"
)
label_resultado.pack(pady=20)

def mostrar():
    valor = int(var_volume.get())

    if valor == 0:
        emoji = "🔇"
        cor = "#FF4444"
    elif valor < 40:
        emoji = "🔉"
        cor = "#FFD700"
    else:
        emoji = "🔊"
        cor = "#00FFAA"

    label_resultado.config(
        text=f"{emoji} Volume: {valor}%",
        fg=cor
    )

# Botão Gamer
botao = tk.Button(
    frame,
    text="ATUALIZAR",
    command=mostrar,
    font=("Consolas", 12, "bold"),
    bg="#00FFAA",
    fg="black",
    activebackground="#58A6FF",
    activeforeground="white",
    relief="flat",
    width=18,
    cursor="hand2"
)
botao.pack(pady=10)

# Rodapé
tk.Label(
    janela,
    text="POWERED BY PYTHON",
    font=("Consolas", 9),
    bg="#0D1117",
    fg="#8B949E"
).pack(pady=5)

janela.mainloop()