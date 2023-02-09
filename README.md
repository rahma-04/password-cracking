# password-cracking

Untuk menjalankan program, yang harus dijalankan pertama kali adalah server. Server
membuat koneksi dengan metode RPC menggunakan alamat IP 127.0.0.1 dan port
8000. Jika koneksi berhasil dibuat, maka server akan menampilkan output “Server
berhasil dibuat!”. Setelah koneksi berhasil dibuat, maka program client bisa
dijalankan untuk proses password cracking. Proses kerjanya adalah client memberikan
parameter pada fungsi, kemudian fungsi tersebut dipanggil pada client. Nantinya,
fungsi tersebut akan terhubung pada server dan server yang mengeksekusi fungsi
tersebut menghasilkan hasil eksekusi yang diberikan kembali ke client. 
