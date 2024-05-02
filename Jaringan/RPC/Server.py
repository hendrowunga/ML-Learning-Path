# Import package RPC
from xmlrpc.server import SimpleXMLRPCServer

# Buat function/proses RPC
def sapaHallo():
    return 'Hallo,ini dikirim ke server RPC'

# Lingkungan koneksi RPC sebagai server
server=SimpleXMLRPCServer(("localhost",8000))

# Tampilkan status server
print("Server is listening on port 80000 .....")

# Register function yang bisa diakses oleh client
server.register_function(sapaHallo)

# server forever
server.serve_forever()