import tkinter
import tkVideoPlayer
import pygame

pygame.init()

pygame.mixer.music.load('sounds/matue.mp3')


tela = tkinter.Tk()
tela.title('Guerra de Troia')
tela.geometry('720x480+300+100')
tela.resizable(0,0)
tela.config(background='gray')

video = tkVideoPlayer.TkinterVideo(tela,scaled=True)

def play():
    video.play()
    pygame.mixer.music.play(1)


    

play = tkinter.Button(tela, text='play',relief='flat', width=100, borderwidth=2 , command=play).grid(row=0, column=0, padx=10, pady=10)


video.load('videos/video.mp4')
video.grid(row=1,column=0, columnspan= 3, sticky='we', ipady=170)
tela.mainloop()