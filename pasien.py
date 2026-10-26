import paho.mqtt.client as mqtt
import time

# --- FUNGSI SAAT TERHUBUNG & MENERIMA PESAN ---

# Dipanggil saat berhasil terhubung ke server
def on_connect(client, userdata, flags, rc):
    print("Aplikasi Pasien Terhubung.")
    # Langsung mendengarkan topik saran dari dokter
    client.subscribe("gula_darah/dokter/saran")

# Dipanggil saat ada pesan balasan dari dokter
def on_message(client, userdata, msg):
    print(f"\nSaran Diterima: '{msg.payload.decode()}'")
    # Hentikan loop agar program bisa berakhir
    client.loop_stop()

# --- PROGRAM UTAMA ---

# Inisialisasi MQTT Client
client = mqtt.Client(client_id="pasien_simple")
client.on_connect = on_connect
client.on_message = on_message

# Hubungkan ke Broker
client.connect("broker.hivemq.com", 1883)

# Jalankan loop di background untuk mendengarkan balasan
client.loop_start()

# Minta input dari pasien
kadar_gula = int(input("Masukkan kadar gula darah (mg/dL): "))

# Jika kadar gula di atas 180, kirim notifikasi
if kadar_gula > 180:
    pesan = f"Gula darah tinggi: {kadar_gula} mg/dL."
    client.publish("gula_darah/pasien/notifikasi", pesan)
    print("-> Notifikasi Terkirim. Menunggu balasan dokter...")
    
    # Tunggu balasan (loop akan dihentikan oleh on_message)
    time.sleep(30) # Beri waktu tunggu maksimal 30 detik
else:
    print("Kadar gula darah normal.")
    client.loop_stop() # Hentikan loop jika tidak ada notifikasi

print("Program Selesai.")
client.disconnect()