import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime


# converte data de (2026-05-14T16:10:00Z) para o formato BR (14/05/2026 16:10)
def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%d/%m/%Y %H:%M")
    except:
        return "Data desconhecida"
    

# buscar as atividades recentes do usuário
def get_github_activity():
    username = entry_username.get().strip()
    
    if not username:
        messagebox.showwarning("Aviso!", 
            "Digite o nome do usuário do GitHub.")
        return
    
    # limpar a área do texto antes de apresentar as respostas
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, f"Buscando atividades de {username}...\n\n")
    
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro ao acessar a API:\n{e}")
        return
    
    events = response.json()
    
    if not events:
        text_output.insert(tk.END, 
                        "Nenhuma atividade encontrada.\n")
        return
    
    text_output.insert(tk.END, f"Atividades recentes encontradas de {username}:\n\n")
    
    # exibição de 10 eventos recentes
    for event in events[:10]:
        event_type = event.get("type", "Desconhecido")
        repo = event.get("repo", {}).get("name", "Desconhecido")
        created_at = format_date(event.get("created_at"))
        
        text_output.insert(tk.END, f"{event_type}\n")
        text_output.insert(tk.END, f"Repositório: {repo}\n")
        text_output.insert(tk.END, f"Data: {created_at}\n")
        
        payload = event.get("payload", {})
        
        if event_type == "PushEvent":
            commits = payload.get("commits", [])
            for commit in commits:
                message = commit.get("message", "Sem mensagem")
                text_output.insert(tk.END, 
                                f"    - {message}\n")
        
        elif event_type == "CreateEvent":
            ref_type = payload.get("ref_type", "desconhecido")
            text_output.insert(tk.END, f"Criou: {ref_type}\n")
            
        elif event_type == "IssuesEvent":
            action = payload.get("action", "desconhecido")
            text_output.insert(tk.END, f"Issue: {action}\n")
        
        elif event_type == "ForkEvent":
            text_output.insert(tk.END, "Fork do respositório\n")
            
        text_output.insert(tk.END, "-" * 40 + "\n\n")
    
    # move a barra de rolagem para cima
    text_output.see("1.0")

# tela Janela Principal

root = tk.Tk()
root.title("Visualizador de Arividades do GitHub")
root.geometry("800x600")
root.resizable(True, True)

# ======================== ÁREA 1: TÍTULO ========================
frame_title = ttk.Frame(root, padding=20)
frame_title.pack(fill="x")

label_title = tk.Label(frame_title, text="Visualizador de Atividades do GitHub", font=("Arial", 24, "bold"), bg="lightblue", fg="#333333")
label_title.pack()

# ÁREA 2: BUSCA
frame_search = ttk.Frame(root, padding=15)
frame_search.pack(pady=10)

# Texto instrucional
label_instruction = ttk.Label(frame_search, text="Digite um nome de usuário do GitHub:", font=("Arial", 11))
label_instruction.pack(anchor="w", pady=(0, 8))

# Frame para entrada e botão
frame_input = ttk.Frame(frame_search)
frame_input.pack(fill="x", pady=5)

# campo de entrada
entry_username = ttk.Entry(frame_input, width=40, font=("Arial", 11))
entry_username.pack(side="left", padx=(0, 10))
entry_username.focus()

# botão de buscar
button_search = ttk.Button(frame_input, text="Buscar", command=get_github_activity)
button_search.pack(side="left")

# pressionar enter
root.bind("<Return>", lambda event: get_github_activity())

# ÁREA 3: RESULTADOS 
frame_output = ttk.LabelFrame(root, text="Atividades Encontradas", padding=10)
frame_output.pack(fill="both", expand=True, padx=10, pady=10)

# barra de rolagem
scrollbar = ttk.Scrollbar(frame_output)
scrollbar.pack(side="right", fill="y")

# área do texto
text_output = tk.Text(frame_output, wrap="word", yscrollcommand=scrollbar.set, font=("Consolas", 10), height=25)
text_output.pack(fill="both", expand=True)

# conecta scrollbar ao Text
scrollbar.config(command=text_output.yview)

# texto inicial
text_output.insert(tk.END, "")

# iniciar interface
root.mainloop()