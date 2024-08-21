from tkinter import *
from Reproductor import *

# Inicializa el reproductor con la canción
musica = Reproductor('gg.mp3')

def play_musica():
    musica.volume(0.8)
    musica.play()
    label_status.config(text="Reproduciendo: gg.mp3")

def pause_musica():
    musica.pause()
    label_status.config(text="Pausado")

def stop_musica():
    musica.stop()
    label_status.config(text="Detenido")

def exit_app():
    master.destroy()

master = Tk()
master.geometry("250x200")
master.title("Spotifay")

# Mensaje de bienvenida
label_welcome = Label(master, text="Bienvenido a Spotifay", font=("Arial", 12))
label_welcome.pack(pady=10)

# Estado de la música
label_status = Label(master, text="Reproduciendo", font=("Arial", 10))
label_status.pack(pady=10)


btn_pause = Button(master, text="Pausar", command=pause_musica)
btn_pause.pack(pady=5)


btn_exit = Button(master, text="Salir", command=exit_app)
btn_exit.pack(pady=10)

mainloop()

