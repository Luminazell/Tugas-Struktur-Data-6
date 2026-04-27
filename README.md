Data Structure — Queue Visualizer

Aplikasi visualisasi struktur data Queue menggunakan Python GUI.
Program ini menampilkan 5 studi kasus penggunaan Queue dalam satu aplikasi desktop dengan sistem tab.

Project ini dibuat untuk membantu memahami konsep FIFO (First In First Out) serta implementasi queue dalam berbagai skenario dunia nyata.

Fitur Aplikasi

Program memiliki 5 simulasi queue:

1. Printer Queue

Simulasi antrian dokumen pada printer bersama.

Fitur:

Menambahkan dokumen ke antrian (enqueue)
Mencetak dokumen sesuai urutan
Reset antrian
Statistik jumlah dokumen yang sudah dicetak

Konsep yang digunakan:

FIFO Queue
2. Hot Potato (Circular Queue)

Simulasi permainan Hot Potato dimana objek diputar antar pemain.

Fitur:

Menambahkan pemain
Mengoper kentang (rotasi queue)
Eliminasi pemain

Konsep yang digunakan:

Circular Queue
3. Rumah Sakit (Priority Queue)

Simulasi antrian pasien di rumah sakit berdasarkan tingkat prioritas.

Fitur:

Menambahkan pasien
Mengatur prioritas pasien
Memanggil pasien dengan prioritas tertinggi

Konsep yang digunakan:

Priority Queue
4. BFS Graf

Simulasi traversal graf menggunakan algoritma Breadth First Search.

Fitur:

Menjalankan BFS traversal
Menampilkan urutan node yang dikunjungi

Konsep yang digunakan:

Queue pada algoritma BFS
5. Bandara

Simulasi antrian penumpang pada loket bandara.

Fitur:

Menambahkan penumpang
Melayani penumpang sesuai urutan

Konsep yang digunakan:

FIFO Queue
Teknologi yang Digunakan

Project ini menggunakan:

Python
Tkinter
Collections deque (Python Standard Library)
Struktur Project

Contoh struktur repository:

queue-visualizer
│
├── main.py
├── README.md
└── requirements.txt
Cara Menjalankan Program
1. Clone Repository
git clone https://github.com/username/queue-visualizer.git
2. Masuk ke Folder Project
cd queue-visualizer
3. Jalankan Program
python main.py
Tampilan Aplikasi

Aplikasi memiliki tampilan berbasis tab seperti berikut:

Printer
Hot Potato
Rumah Sakit
BFS Graf
Bandara

Setiap tab menampilkan simulasi queue yang berbeda.

Tujuan Project

Project ini dibuat untuk:

Memahami implementasi struktur data Queue
Mempelajari penggunaan queue dalam berbagai kasus nyata
Menyediakan visualisasi interaktif untuk pembelajaran struktur data
Author

Nama: Muhammad Dava Desvilano
Project: Struktur Data — Queue Visualizer
