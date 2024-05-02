# Import package client
import xmlrpc.client
# Buat koneksi RPC ke server
proxy=xmlrpc.client.ServerProxy("http://localhost:8000")

# Akses function RPC
sapaHallo=proxy.sapaHallo()

# Tampilkan Hasil
print(sapaHallo)


