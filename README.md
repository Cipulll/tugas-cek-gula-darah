# Notifikasi Gula Darah via MQTT

Proyek ini adalah **prototipe edukasi** komunikasi antara aplikasi pasien dan dokter menggunakan MQTT. Aplikasi pasien mengirim notifikasi saat kadar gula darah yang dimasukkan lebih dari 180 mg/dL. Aplikasi dokter menerima notifikasi dan dapat mengirimkan balasan yang ditampilkan oleh aplikasi pasien.

> **Peringatan:** Proyek ini bukan alat medis dan bukan untuk pemantauan atau pengambilan keputusan klinis. Jangan masukkan atau kirim data kesehatan pribadi maupun data pasien sungguhan.

## Kebutuhan

- Python 3
- Koneksi internet
- Paket Python `paho-mqtt`

Pasang dependensi:

```bash
python -m pip install paho-mqtt
```

## Menjalankan

Jalankan aplikasi dokter lebih dahulu di satu terminal:

```bash
python dokter.py
```

Lalu jalankan aplikasi pasien di terminal lain:

```bash
python pasien.py
```

Masukkan kadar gula darah dalam mg/dL pada aplikasi pasien. Jika nilainya lebih dari `180`, aplikasi akan mengirim notifikasi dan menunggu balasan hingga sekitar 30 detik. Jika nilainya `180` atau kurang, notifikasi tidak dikirim.

## Alur dan topik MQTT

Kedua aplikasi saat ini terhubung ke `broker.hivemq.com` melalui MQTT tanpa TLS pada port `1883`.

| Arah pesan | Topik |
| --- | --- |
| Pasien mengirim notifikasi kepada dokter | `gula_darah/pasien/notifikasi` |
| Dokter mengirim saran kepada pasien | `gula_darah/dokter/saran` |

## Batasan dan privasi

- Broker yang digunakan bersifat publik; topik di kode ini tetap dan mudah ditebak. Pesan dapat terlihat oleh atau tercampur dengan aplikasi lain yang menggunakan broker dan topik yang sama.
- Koneksi tidak menggunakan TLS atau autentikasi. Kadar gula darah dan balasan tidak boleh dianggap rahasia atau aman.
- ID klien MQTT juga tetap, sehingga beberapa proses dapat berbenturan saat dijalankan bersamaan.
- Ambang `180 mg/dL` hanya aturan sederhana di dalam demo, bukan diagnosis atau rekomendasi medis.
- Proyek ini belum menyediakan pengelolaan pengguna/pasien, penyimpanan riwayat, validasi klinis, ataupun pengujian otomatis.

Untuk penggunaan selain demonstrasi lokal, ganti broker publik dengan broker yang dikelola sendiri dan dikonfigurasi menggunakan TLS, autentikasi, serta ACL per pengguna/perangkat. Gunakan topik dan ID klien unik, dan lakukan peninjauan privasi serta keselamatan sebelum menangani data kesehatan.
