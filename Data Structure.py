import tkinter as tk
from tkinter import ttk
from collections import deque

# =========================
# WINDOW
# =========================

root = tk.Tk()
root.title("Queue Visualizer - 5 Kasus")
root.geometry("1000x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab_printer = ttk.Frame(notebook)
tab_hotpotato = ttk.Frame(notebook)
tab_hospital = ttk.Frame(notebook)
tab_bfs = ttk.Frame(notebook)
tab_airport = ttk.Frame(notebook)

notebook.add(tab_printer,text="Printer")
notebook.add(tab_hotpotato,text="Hot Potato")
notebook.add(tab_hospital,text="Rumah Sakit")
notebook.add(tab_bfs,text="BFS Graf")
notebook.add(tab_airport,text="Bandara")

# =========================
# 1 PRINTER QUEUE
# =========================

printer_queue = deque()
printed = 0

tk.Label(tab_printer,text="Antrian Printer",font=("Arial",16)).pack(pady=10)

entry_doc = tk.Entry(tab_printer,width=30)
entry_doc.pack()

list_printer = tk.Listbox(tab_printer,width=50,height=10)
list_printer.pack(pady=10)

stats = tk.Label(tab_printer,text="Dicetak: 0")
stats.pack()

def enqueue_doc():
    doc = entry_doc.get()
    if doc:
        printer_queue.append(doc)
        list_printer.insert(tk.END,doc)
        entry_doc.delete(0,tk.END)

def print_doc():
    global printed
    if printer_queue:
        printer_queue.popleft()
        list_printer.delete(0)
        printed += 1
        stats.config(text=f"Dicetak: {printed}")

def reset_printer():
    global printed
    printer_queue.clear()
    list_printer.delete(0,tk.END)
    printed = 0
    stats.config(text="Dicetak: 0")

btn = tk.Frame(tab_printer)
btn.pack()

tk.Button(btn,text="Enqueue",command=enqueue_doc).grid(row=0,column=0,padx=5)
tk.Button(btn,text="Cetak",command=print_doc).grid(row=0,column=1,padx=5)
tk.Button(btn,text="Reset",command=reset_printer).grid(row=0,column=2,padx=5)

# =========================
# 2 HOT POTATO
# =========================

players = deque()

tk.Label(tab_hotpotato,text="Hot Potato (Circular Queue)",font=("Arial",16)).pack(pady=10)

entry_player = tk.Entry(tab_hotpotato)
entry_player.pack()

list_players = tk.Listbox(tab_hotpotato,width=40,height=10)
list_players.pack()

log_hotpotato = tk.Listbox(tab_hotpotato,width=40,height=5)
log_hotpotato.pack(pady=10)

def add_player():
    name = entry_player.get()
    if name:
        players.append(name)
        list_players.insert(tk.END,name)
        entry_player.delete(0,tk.END)

def pass_potato():
    if len(players)>1:
        players.rotate(-1)
        update_players()

def eliminate():
    if players:
        out = players.popleft()
        log_hotpotato.insert(tk.END,f"{out} keluar")
        update_players()

def update_players():
    list_players.delete(0,tk.END)
    for p in players:
        list_players.insert(tk.END,p)

tk.Button(tab_hotpotato,text="Tambah Pemain",command=add_player).pack()
tk.Button(tab_hotpotato,text="Oper Kentang",command=pass_potato).pack()
tk.Button(tab_hotpotato,text="Eliminasi",command=eliminate).pack()

# =========================
# 3 PRIORITY QUEUE RS
# =========================

hospital_queue = []

tk.Label(tab_hospital,text="Antrian Rumah Sakit",font=("Arial",16)).pack(pady=10)

entry_patient = tk.Entry(tab_hospital)
entry_patient.pack()

priority = ttk.Combobox(tab_hospital,values=[1,2,3,4])
priority.pack()

list_hospital = tk.Listbox(tab_hospital,width=40,height=10)
list_hospital.pack()

log_hospital = tk.Listbox(tab_hospital,width=40,height=5)
log_hospital.pack()

def add_patient():
    name = entry_patient.get()
    p = int(priority.get())

    hospital_queue.append((p,name))
    hospital_queue.sort()

    update_hospital()

def call_patient():
    if hospital_queue:
        patient = hospital_queue.pop(0)
        log_hospital.insert(tk.END,f"Memanggil {patient[1]}")
        update_hospital()

def update_hospital():
    list_hospital.delete(0,tk.END)
    for p in hospital_queue:
        list_hospital.insert(tk.END,f"{p[1]} - Prioritas {p[0]}")

tk.Button(tab_hospital,text="Tambah Pasien",command=add_patient).pack()
tk.Button(tab_hospital,text="Panggil Pasien",command=call_patient).pack()

# =========================
# 4 BFS
# =========================

graph = {
"A":["B","C"],
"B":["D","E"],
"C":["F"],
"D":[],
"E":[],
"F":[]
}

tk.Label(tab_bfs,text="BFS Traversal",font=("Arial",16)).pack(pady=10)

result_bfs = tk.Listbox(tab_bfs,width=40,height=10)
result_bfs.pack()

def run_bfs():

    visited=[]
    queue=deque(["A"])

    while queue:

        node=queue.popleft()

        if node not in visited:

            visited.append(node)

            for n in graph[node]:
                queue.append(n)

    result_bfs.delete(0,tk.END)

    for v in visited:
        result_bfs.insert(tk.END,v)

tk.Button(tab_bfs,text="Jalankan BFS",command=run_bfs).pack()

# =========================
# 5 BANDARA
# =========================

airport_queue = deque()

tk.Label(tab_airport,text="Antrian Bandara",font=("Arial",16)).pack(pady=10)

entry_passenger = tk.Entry(tab_airport)
entry_passenger.pack()

list_airport = tk.Listbox(tab_airport,width=40,height=10)
list_airport.pack()

log_airport = tk.Listbox(tab_airport,width=40,height=5)
log_airport.pack()

def add_passenger():

    name = entry_passenger.get()

    if name:
        airport_queue.append(name)
        list_airport.insert(tk.END,name)
        entry_passenger.delete(0,tk.END)

def serve_passenger():

    if airport_queue:

        p = airport_queue.popleft()

        list_airport.delete(0)

        log_airport.insert(tk.END,f"{p} menuju loket")

tk.Button(tab_airport,text="Tambah Penumpang",command=add_passenger).pack()
tk.Button(tab_airport,text="Layani Penumpang",command=serve_passenger).pack()

# =========================

root.mainloop()