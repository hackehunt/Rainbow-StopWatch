from tkinter import *
import time

def Main():
    global root

#------------------------------Screen management
    root = Tk()
    root.title("Stopwatch made by PreyO AhmeD")
    width = 500
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.minsize(500,300)
    root.maxsize(500,300)
    Top = Frame(root, width=400)
    Top.pack(side=TOP)
#-----------------------------frames
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=400)
    Bottom.pack(side=BOTTOM)
#-----------------------------Images
    start_img = PhotoImage(file="img/start.png")
    stop_img = PhotoImage(file="img/stop.png")
    exit_img = PhotoImage(file="img/exit.png")
    reset_img = PhotoImage(file="img/reset.png")
#-----------------------------Buttons
    Start = Button(Bottom, text='START', command=stopWatch.Start,font="consolas 20 bold", image=start_img, compound=LEFT)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='STOP', command=stopWatch.Stop,font="consolas 20 bold", image=stop_img, compound=LEFT)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='RESET', command=stopWatch.Reset,font="consolas 20 bold", image=reset_img, compound=LEFT)
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='CLOSE', command=stopWatch.Exit, font="consolas 20 bold", image=exit_img, compound=LEFT)
    Exit.pack(side=LEFT)
#-----------------------------Labels
    Title = Label(Top, text="StopWatch PreyO AhmeD", font=("arial", 20), fg="red", bg="blue")
    Title.pack(fill=X)
    root.config(bg="skyblue")
    root.mainloop()


class StopWatch(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 45), fg="orange", bg="red")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=5, padx=10)

    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1

    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
            root.destroy()
            exit()

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)


if __name__ == '__main__':
    Main()
