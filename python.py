import yt_dlp
import os

def descargar_mp3(url, carpeta_destino):
    # Opciones de descarga
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
    }

    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Descargar el audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Ejemplo de uso
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Reemplaza esto con la URL del video que quieres descargar
carpeta_destino = "C:/Users/TuUsuario/Music/Descargas"  # Reemplaza esto con la ruta de tu carpeta local

descargar_mp3(url, carpeta_destino)
print("Descarga completada.")
