import tkinter as tk
import webbrowser

class SearchApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # JANELA
        self.title("Pantera Cor de Rosa")
        self.geometry("800x600")
        self.configure(bg="#FFE4F2")
        self.minsize(400, 300)

        main_frame = tk.Frame(self, bg="#FFE4F2")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # TÍTULO ALTERADO
        title_label = tk.Label(
            main_frame,
            text="PANTERA COR DE ROSA",
            font=("Arial", 30, "bold"),
            fg="#FF1493",
            bg="#FFE4F2"
        )
        title_label.pack(pady=20)

        # BARRA DE PESQUISA
        search_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid")
        search_frame.pack(ipadx=10, ipady=5)

        self.placeholder = "Digite sua pesquisa"
        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            width=40,
            bd=0,
            fg="grey"
        )

        self.search_entry.pack(side="left", padx=5)
        self.search_entry.insert(0, self.placeholder)

        self.search_entry.bind("<FocusIn>", self.on_click)
        self.search_entry.bind("<FocusOut>", self.off_click)
        self.search_entry.bind("<Return>", self.perform_search)

        # BOTÃO
        btn = tk.Button(
            main_frame,
            text="Pesquisar",
            font=("Arial", 12, "bold"),
            bg="#FF69B4",
            fg="white",
            command=self.perform_search
        )
        btn.pack(pady=20)

    def on_click(self, event):
        if self.search_entry.get() == self.placeholder:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="black")

    def off_click(self, event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder)
            self.search_entry.config(fg="grey")

    def perform_search(self, event=None):
        query = self.search_entry.get()

        if query and query != self.placeholder:
            webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()