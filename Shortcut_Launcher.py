import tkinter
import tkinter.ttk
import os

main_window = tkinter.Tk()

# variable area
main_window_width = 800
main_window_height = 200
info_text = ''' 
Shortcut Launcher
'''

button_column : int = 4
button_row : int = 2
button = [[0 for y in range(button_row)] for x in range(button_column)]
rex = 1/button_column #ratio
rey = 1/button_row #ratio


# function area
def TopMostScreen(onoff):
    main_window.wm_attributes("-topmost", onoff)

def GetColor(r,g,b):
    return '#'+format(r,'X')+format(g,'X')+format(b,'X')
    

def ButtonCompose():
    for x in range(button_column):
        for y in range(button_row):
            if(x==0 and y==0) : button[x][y] = tkinter.Button(main_window, text="notepad", command=Notepad)
            elif(x==1 and y==0) : button[x][y] = tkinter.Button(main_window, text="calc", command=Calc)
            elif(x==2 and y==0) : button[x][y] = tkinter.Button(main_window, text="c:", command=OpenFolder_C)
            elif(x==3 and y==0) : button[x][y] = tkinter.Button(main_window, text="http://google.com", command=OpenWebsite_Google)
            else : button[x][y] = tkinter.Button(main_window, text="blank")
        
            button[x][y].place(relx=rex*x, rely=rey*y, relwidth = rex, relheight = rey)

def Notepad():
    os.startfile('notepad')

def Calc():
    os.startfile('calc')

def OpenFolder_C():
    os.startfile('c:')

def OpenWebsite_Google():
    os.system("explorer http://google.com")


# Menu area
def SettingMenu():
    setting_window = tkinter.Tk()
    setting_window.title("프로그램 설정")
    setting_window.geometry("300x300+100+100")
    setting_window.resizable(False, False)

    notebook=tkinter.ttk.Notebook(setting_window)
    notebook.place(relx=0, rely=0, relwidth = 1, relheight = 1)

    # frame no.1
    frame1=tkinter.Frame(setting_window)
    notebook.add(frame1, text="창 옵션")

    # frame 1 - winsize
    lbframe_winsize=tkinter.LabelFrame(frame1, text="창 크기 조정")
    lbframe_winsize.place(relx=0, rely=0, relwidth = 1, relheight = 1/2)

    # frame 1 - topmost
    lbframe_topmost=tkinter.LabelFrame(frame1, text="항상 위 옵션")
    lbframe_topmost.place(relx=0, rely=1/2, relwidth = 1, relheight = 1/2)

    topmost_onoff=tkinter.IntVar()

    topmost_on = tkinter.Radiobutton(lbframe_topmost, text="켜기", value=1, variable=topmost_onoff, command=lambda: TopMostScreen(1))
    topmost_on.place(relx=0, rely=0, relwidth = 1, relheight = 1/2)
    topmost_off = tkinter.Radiobutton(lbframe_topmost, text="끄기", value=2, variable=topmost_onoff, command=lambda: TopMostScreen(0))
    topmost_off.place(relx=0, rely=1/2, relwidth = 1, relheight = 1/2)

    # frame no.2 area
    frame2=tkinter.Frame(setting_window)
    notebook.add(frame2, text="프로그램 색상")

    # frame no.3 area
    frame3=tkinter.Frame(setting_window)
    notebook.add(frame3, text="버튼 개수 조정")

    values=[i for i in range(2, 11)] 

    combobox_x = tkinter.ttk.Combobox(frame3, height=9, values=values)
    combobox_x.place(anchor='s', relx=1/4, rely=1/7, relwidth = 1/3)
    combobox_x.set("가로 버튼수")
    combobox_y = tkinter.ttk.Combobox(frame3, height=9, values=values)
    combobox_y.place(anchor='s', relx=3/4, rely=1/7, relwidth = 1/3)
    combobox_y.set("세로 버튼수")



    '''
    global button_column
    global button_row
    global button
    global rex
    global rey

    button_column = 6
    button_row = 3
    button = [[0 for y in range(button_row)] for x in range(button_column)]
    rex = 1/button_column #ratio
    rey = 1/button_row #ratio

    ButtonCompose() #Work well if get correct Matrix
    '''
    setting_window.mainloop()

def InfoMenu():
    info_window = tkinter.Tk()
    info_window.title("프로그램 정보")
    info_window.geometry("300x100+200+200")
    info_window.resizable(False, False)
    
    info=tkinter.Label(info_window, text=info_text, width=20, height=3)
    info.pack()

    info_window.mainloop()

def CloseMenu():
    main_window.quit()
    main_window.destroy()


# window setting
main_window.title("Shortcut Launcher")
main_window.geometry(str(main_window_width)+"x"+str(main_window_height)+"+100+100")
main_window.resizable(False, False)

# menubar
menubar = tkinter.Menu(main_window)

menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="프로그램 설정", command=SettingMenu)
menu_1.add_command(label="프로그램 정보", command=InfoMenu)
menu_1.add_command(label="프로그램 종료", command=CloseMenu)
menubar.add_cascade(label="메뉴", menu=menu_1)

main_window.config(menu=menubar)


ButtonCompose()

main_window.mainloop()