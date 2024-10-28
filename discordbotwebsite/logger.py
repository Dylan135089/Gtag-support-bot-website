import os
import qrcode
import requests

webhook = 'https://discord.com/api/webhooks/1300268622018777088/RK40lbv_UQeAkKRN-M6H2aEM-pErO7yA0lMEIUxv_L6rZprUK2Hgr89R9YEhAm0ITm7m'

def generate_qr_code(text, file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Deleted existing file: {file_name}")
        
    img = qrcode.make(text)
    img.save(file_name)
    return file_name  

text = "http://127.0.0.1:5000/log_user"
file_name = "qrcode.png"
file_path = generate_qr_code(text, file_name)
print(f"QR code saved as {file_path}")

with open(file_path, 'rb') as f:
    requests.post(webhook, files={'file': f})
print("QR code sent to webhook!")
