Queue Visualizer — Data Structure Simulation

Visualisasi interaktif dari struktur data Queue menggunakan Python GUI.
Aplikasi ini menampilkan beberapa studi kasus nyata penggunaan Queue untuk membantu memahami konsep FIFO, Circular Queue, Priority Queue, dan Breadth-First Search (BFS) secara visual.

Project ini dibuat sebagai media pembelajaran untuk mata kuliah Struktur Data.

Overview

Queue merupakan salah satu struktur data dasar dalam ilmu komputer dengan prinsip FIFO (First In, First Out).
Dalam project ini, konsep queue diimplementasikan ke dalam beberapa simulasi nyata seperti antrian printer, permainan hot potato, sistem prioritas rumah sakit, traversal graf, dan antrian bandara.

Aplikasi ini dibuat menggunakan GUI Python sehingga pengguna dapat berinteraksi langsung dengan simulasi.

Teknologi GUI yang digunakan adalah Tkinter.

Features

Aplikasi menyediakan 5 simulasi Queue dalam satu program:

Printer Queue

Simulasi antrian dokumen pada printer bersama.

Fitur:

Menambahkan dokumen ke antrian
Mencetak dokumen sesuai urutan
Reset antrian
Statistik dokumen yang telah dicetak

Konsep yang digunakan:

FIFO Queue
Hot Potato (Circular Queue)

Simulasi permainan Hot Potato di mana objek diputar di antara pemain hingga satu pemain tereliminasi.

Fitur:

Menambahkan pemain
Rotasi pemain (oper kentang)
Eliminasi pemain

Konsep yang digunakan:

Circular Queue
Rumah Sakit (Priority Queue)

Simulasi sistem antrian pasien berdasarkan tingkat prioritas.

Fitur:

Menambahkan pasien
Menentukan prioritas pasien
Memanggil pasien dengan prioritas tertinggi

Konsep yang digunakan:

Priority Queue
BFS Graph Traversal

Simulasi algoritma Breadth-First Search pada graf.

Fitur:

Menjalankan traversal BFS
Menampilkan urutan node yang dikunjungi

Konsep yang digunakan:

Queue pada algoritma BFS
Airport Queue

Simulasi antrian penumpang pada loket bandara.

Fitur:

Menambahkan penumpang
Melayani penumpang sesuai urutan

Konsep yang digunakan:

FIFO Queue
Screenshots

Contoh tampilan aplikasi:

Tab Printer Queue
Tab Hot Potato
Tab Rumah Sakit
Tab BFS Graph
Tab Bandara

(Screenshot aplikasi dapat ditambahkan di sini)

Tech Stack

Project ini menggunakan teknologi berikut:

Python 3
Tkinter
Python Standard Library (collections.deque)
Project Structure

Struktur folder project:

queue-visualizer
│
├── main.py
├── README.md
└── requirements.txt

Jika project diperluas, struktur dapat menjadi:

queue-visualizer
│
├── main.py
├── cases
│   ├── printer.py
│   ├── hot_potato.py
│   ├── hospital.py
│   ├── bfs.py
│   └── airport.py
│
├── assets
│   └── screenshots
│
└── README.md
Installation

Clone repository:

git clone https://github.com/username/queue-visualizer.git

Masuk ke folder project:

cd queue-visualizer
Usage

Jalankan program dengan Python:

python main.py

Setelah program berjalan, pengguna dapat memilih simulasi melalui tab:

Printer
Hot Potato
Rumah Sakit
BFS Graph
Bandara
Learning Objectives

Project ini dibuat untuk membantu memahami:

Konsep Queue (FIFO)
Circular Queue
Priority Queue
Implementasi queue dalam Breadth-First Search
Penggunaan queue dalam simulasi dunia nyata
Contribution

Kontribusi sangat terbuka.

Jika ingin berkontribusi:

Fork repository
Buat branch baru
Commit perubahan
Buat pull request
Author

Muhammad Dava Desvilano
Project: Queue Visualizer — Data Structure Simulation

License

Project ini dibuat untuk tujuan pembelajaran dan dapat digunakan secara bebas untuk keperluan akademik.
