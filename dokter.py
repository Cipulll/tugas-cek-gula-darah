import paho.mqtt.client as mqtt

# --- FUNGSI SAAT TERHUBUNG & MENERIMA PESAN ---

# Dipanggil saat berhasil terhubung ke server
def on_connect(client, userdata, flags, rc):
    print("Aplikasi Dokter Terhubung.")
    # Langsung mendengarkan topik notifikasi dari pasien
    client.subscribe("gula_darah/pasien/notifikasi")

# Dipanggil saat ada pesan masuk dari pasien
def on_message(client, userdata, msg):
    print(f"\nNotifikasi Diterima: '{msg.payload.decode()}'")
    
    # Meminta input saran dari dokter
    saran = input("Ketik balasan: ")
    # Mengirim balasan ke pasien
    client.publish("gula_darah/dokter/saran", saran)
    print("-> Saran Terkirim.")

# --- PROGRAM UTAMA ---

# Inisialisasi MQTT Client
client = mqtt.Client(client_id="dokter_simple")
client.on_connect = on_connect
client.on_message = on_message

# Hubungkan ke Broker
client.connect("broker.hivemq.com", 1883)

# Jalankan loop untuk terus mendengarkan pesan
print("Menunggu notifikasi pasien...")
client.loop_forever()