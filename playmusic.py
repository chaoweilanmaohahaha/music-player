import pygame
import time
import tkinter
from tkinter import filedialog
def play():
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def getMusic():
    file = filedialog.askopenfilename(title='选择歌曲：')
    if(file != ''):
        listbox.insert(0, file)
        pygame.mixer.init()
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.queue(file)



win = tkinter.Tk()
win.title('音乐播放器')
win.geometry("400x400+200+50")
frame = tkinter.Frame(win)
frame.pack(side='bottom')
listbox = tkinter.Listbox(win, width=50, height=10, selectmode=tkinter.BROWSE)
listbox.pack()
button0 = tkinter.Button(frame, text='导入', command=getMusic, justify='right')
button0.pack(side="top")
button1=tkinter.Button(frame, text='播放', command=play, justify="right", anchor="ne")
button1.pack(side='left')
button2=tkinter.Button(frame, text='停止', command=stop, justify="right", anchor="ne")
button2.pack(side='left')
button3=tkinter.Button(frame, text='暂停', command=pause, justify="right", anchor="ne")
button3.pack(side='left')
button4=tkinter.Button(frame, text='继续', command=unpause, justify="right", anchor="ne")
button4.pack(side='left')
win.mainloop()
