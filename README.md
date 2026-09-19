Ternyata skrip `verify.py` mendeteksi bahwa **README.md utama di root folder** harus memiliki **5 judul bagian (*heading*) dengan nama yang sangat spesifik** berikut:

1. **Prasyarat**
2. **Layanan**
3. **Cara menjalankan**
4. **Cara memverifikasi**
5. **Masalah yang sering muncul**

Saat kita menggabungkannya tadi, nama-nama *heading* tersebut berubah sehingga skrip verifikasi menganggapnya belum ada.

---

### Solusi: Ganti Isi `README.md` Utama (Root Folder)

Buka file **`README.md`** di root folder repositorimu, lalu ganti seluruh isinya dengan format 5 bagian presisi di bawah ini:

```markdown
# Aplikasi Manajemen Tiket Event

Proyek *Full-Stack Web Application* untuk sistem manajemen dan pemesanan tiket event berbasis FastAPI (Backend) dan Vue 3 (Frontend).

## 1. Prasyarat
Sebelum menjalankan proyek ini, pastikan perangkat kamu telah terpasang:
- **Python:** versi 3.10 atau lebih baru
- **Node.js:** versi 18 atau lebih baru (termasuk `npm`)
- **Git:** untuk *version control*

## 2. Layanan
Aplikasi ini terdiri dari dua layanan utama:
- **Backend Service (FastAPI):** Menyediakan REST API di port `8000` (termasuk rute `/health`).
- **Frontend Service (Vue 3 + Vite):** Menyediakan antarmuka pengguna berbasis komponen web di port `5173`.

## 3. Cara menjalankan

### Menjalankan Backend
1. Aktifkan *virtual environment*:
   ```bash
   source .venv/bin/activate

```

2. Pastikan dependensi terpasang:
```bash
pip install -r backend/requirements.txt

```


3. Jalankan server FastAPI:
```bash
uvicorn backend.app.main:app --reload

```



### Menjalankan Frontend

1. Masuk ke folder `frontend`:
```bash
cd frontend

```


2. Install dependensi Node.js:
```bash
npm install

```


3. Jalankan server pengembang:
```bash
npm run dev

```



## 4. Cara memverifikasi

Untuk memverifikasi bahwa seluruh struktur repositori telah memenuhi standar *Definition of Done* (DoD) Sesi 2, jalankan skrip berikut di root repositori:

```bash
python verify.py --sesi 2

```

## 5. Masalah yang sering muncul

* **Error `command not found: Remove-Item`:** Terjadi jika menggunakan terminal Git Bash. Gunakan perintah `rm` sebagai gantinya.
* **Port `8000` atau `5173` sudah digunakan:** Hentikan proses yang sedang berjalan atau matikan server sebelumnya dengan tombol `Ctrl + C`.
* **Module `fastapi` / `uvicorn` tidak ditemukan:** Pastikan *virtual environment* (`.venv`) sudah diaktifkan sebelum menjalankan backend.

```
