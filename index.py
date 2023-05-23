import qrcode

# Función para generar un código QR
def generar_codigo_qr(data, nombre_archivo):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    imagen = qr.make_image(fill_color="black", back_color="white")
    imagen.save(nombre_archivo)

# Datos para generar el código QR
datos = "Hola, esto es un código QR de ejemplo."
nombre_archivo = "codigo_qr.png"

# Generar el código QR
generar_codigo_qr(datos, nombre_archivo)

print("Código QR generado exitosamente.")