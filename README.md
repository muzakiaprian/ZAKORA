# ZAKORA

**ZAKORA** merupakan aplikasi web toko online sederhana yang dikembangkan menggunakan Flask. Aplikasi ini menyediakan halaman informasi produk kebutuhan mahasiswa serta dashboard admin untuk menampilkan statistik dan mengelola data produk secara sederhana.

## Fitur

### Website
- Halaman beranda
- Halaman tentang ZAKORA
- Halaman daftar produk
- Halaman detail produk
- Halaman kontak
- Profil pengguna
- Pengecekan username
- Halaman error 404

### Admin Dashboard
- Dashboard statistik produk, pengguna, dan penjualan
- Ringkasan data penjualan
- Halaman kelola produk
- Informasi stok produk
- Status ketersediaan produk
- Tampilan responsive untuk desktop dan mobile

## Teknologi

- Python
- Flask
- HTML
- CSS
- Jinja2
- Git & GitHub

## Struktur Project

```text
ZAKORA/
├── app.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── admin/
│   │   ├── base_admin.html
│   │   ├── dashboard.html
│   │   └── produk.html
│   ├── base.html
│   ├── index.html
│   ├── produk.html
│   ├── detail_produk.html
│   ├── tentang.html
│   ├── kontak.html
│   ├── cek.html
│   ├── user.html
│   └── 404.html
└── README.md
```

## Cara Menjalankan Aplikasi

### 1. Clone repository

```bash
git clone https://github.com/muzakiaprian/ZAKORA.git
```

### 2. Masuk ke direktori project

```bash
cd ZAKORA
```

### 3. Buat virtual environment

```bash
python -m venv venv
```

### 4. Aktifkan virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\activate
```

### 5. Install Flask

```bash
pip install flask
```

### 6. Jalankan aplikasi

```bash
python app.py
```

### 7. Buka aplikasi

Website:

http://127.0.0.1:5000/

Admin Dashboard:

http://127.0.0.1:5000/admin

Kelola Produk:

http://127.0.0.1:5000/admin/produk

## Pengembangan

Project ini dikembangkan sebagai bagian dari pembelajaran pengembangan sistem berbasis web menggunakan Flask, HTML, CSS, dan template Jinja2.

---

**ZAKORA — Online Shopping Platform**