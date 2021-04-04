import tkinter
import tkinter.ttk
import os

main_window = tkinter.Tk()

# variable area
main_window_width = 800
main_window_height = 200
info_text = ''' 
Shortcut Launcher
-step 2-
C111032 KJW (AshCircle)
'''

button_column : int = 4
button_row : int = 2
button = [[0 for y in range(button_row)] for x in range(button_column)]
rex = 1/button_column #ratio
rey = 1/button_row #ratio

bgcolor = 'SystemButtonFace'
fgcolor = '#000000'

# function area
def WinResize(onoff):
    main_window.resizable(onoff, onoff)

def TopMostScreen(onoff):
    main_window.wm_attributes("-topmost", onoff)

def ColorChange(posit,r,g,b):
    hex_R = format(r,'X')
    hex_G = format(g,'X')
    hex_B = format(b,'X')
    colorcode = '#'+hex_R.zfill(2)+hex_G.zfill(2)+hex_B.zfill(2)

    if posit == "bg":
        global bgcolor
        bgcolor = colorcode
        ButtonCompose()
    if posit == "fg":
        global fgcolor
        fgcolor = colorcode
        ButtonCompose()
    

def ButtonCompose():
    index = 0
    for y in range(button_row):
        for x in range(button_column):
            if index == 0 : button[x][y] = tkinter.Button(main_window, text="notepad", command=Notepad, bg=bgcolor, fg=fgcolor, activebackground=bgcolor, activeforeground=fgcolor)
            elif index == 1  : button[x][y] = tkinter.Button(main_window, text="calc", command=Calc, bg=bgcolor, fg=fgcolor, activebackground=bgcolor, activeforeground=fgcolor)
            elif index == 2 : button[x][y] = tkinter.Button(main_window, text="c:", command=OpenFolder_C, bg=bgcolor, fg=fgcolor, activebackground=bgcolor, activeforeground=fgcolor)
            elif index == 3 : button[x][y] = tkinter.Button(main_window, text="http://google.com", command=OpenWebsite_Google, bg=bgcolor, fg=fgcolor, activebackground=bgcolor, activeforeground=fgcolor)
            else : button[x][y] = tkinter.Button(main_window, text="blank", bg=bgcolor, fg=fgcolor, activebackground=bgcolor, activeforeground=fgcolor)
        
            button[x][y].place(relx=rex*x, rely=rey*y, relwidth = rex, relheight = rey)
            index += 1

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
    setting_window=tkinter.Toplevel(main_window)
    setting_window.title("프로그램 설정")
    setting_window.geometry("300x200+100+100")
    setting_window.resizable(False, False)

    notebook=tkinter.ttk.Notebook(setting_window)
    notebook.place(relx=0, rely=0, relwidth = 1, relheight = 1)

    # frame no.1 area
    frame1=tkinter.Frame(setting_window)
    notebook.add(frame1, text="창 옵션")

    # frame 1 - winresize
    lbframe_winresize=tkinter.LabelFrame(frame1, text="창 크기 조정 옵션")
    lbframe_winresize.place(relx=0, rely=0, relwidth = 1, relheight = 1/2)

    winresize_onoff=tkinter.IntVar()

    winresize_on = tkinter.Radiobutton(lbframe_winresize, text="켜기", value=1, variable=winresize_onoff, command=lambda: WinResize(1))
    winresize_on.place(relx=0, rely=0, relwidth = 1, relheight = 1/2)
    winresize_off = tkinter.Radiobutton(lbframe_winresize, text="끄기", value=2, variable=winresize_onoff, command=lambda: WinResize(0))
    winresize_off.place(relx=0, rely=1/2, relwidth = 1, relheight = 1/2)

    # frame 1 - topmost
    lbframe_topmost=tkinter.LabelFrame(frame1, text="항상 위 옵션")
    lbframe_topmost.place(relx=0, rely=1/2, relwidth = 1, relheight = 1/2)

    topmost_onoff=tkinter.IntVar()

    topmost_on = tkinter.Radiobutton(lbframe_topmost, text="켜기", value=1, variable=topmost_onoff, command=lambda: TopMostScreen(1))
    topmost_on.place(relx=0, rely=0, relwidth = 1, relheight = 1/2)
    topmost_off = tkinter.Radiobutton(lbframe_topmost, text="끄기", value=2, variable=topmost_onoff, command=lambda: TopMostScreen(0))
    topmost_off.place(relx=0, rely=1/2, relwidth = 1, relheight = 1/2)
    
    # frame no.2 area - color
    frame2=tkinter.Frame(setting_window)
    notebook.add(frame2, text="프로그램 색상")
    
    color_intro = tkinter.Label(frame2, text="R,G,B 값을 각각 0~255 범위 내로 입력해 주세요.", width=10, height=5)
    color_intro.place(relx=0, rely=0, relwidth = 1, relheight = 1/6)

    def ValueCheck_Color(self):
        color_intro.config(text="R,G,B 값을 각각 0~255 범위 내로 입력해 주세요.")
        valid = False
        if self.isdigit():
            if (int(self) <= 255 and int(self) >= 0):
                valid = True
        elif self == '':
            valid = True
        return valid
    
    def ValueError_Color(self):
        color_intro.config(text=str(self) + "은 범위에 속하지 않습니다.")
    
    validate_command_color=(frame2.register(ValueCheck_Color), '%P')
    invalid_command_color=(frame2.register(ValueError_Color), '%P')

    spinbox_r=tkinter.Spinbox(frame2, fg="red", from_ = 0, to = 255, validate = 'all', validatecommand = validate_command_color, invalidcommand=invalid_command_color)
    spinbox_r.place(anchor='n', relx=1/4, rely=1/4, relwidth = 1/3)
    spinbox_g=tkinter.Spinbox(frame2, fg="green", from_ = 0, to = 255, validate = 'all', validatecommand = validate_command_color, invalidcommand=invalid_command_color)
    spinbox_g.place(anchor='n', relx=1/4, rely=2/4, relwidth = 1/3)
    spinbox_b=tkinter.Spinbox(frame2, fg="blue", from_ = 0, to = 255, validate = 'all', validatecommand = validate_command_color, invalidcommand=invalid_command_color)
    spinbox_b.place(anchor='n', relx=1/4, rely=3/4, relwidth = 1/3)

    apply_bgcolor = tkinter.Button(frame2, text = "배경 색에 적용", command=lambda :ColorChange('bg', int(spinbox_r.get()), int(spinbox_g.get()), int(spinbox_b.get())))
    apply_bgcolor.place(anchor='n', relx = 3/4, rely=1/3)
    apply_fgcolor = tkinter.Button(frame2, text = "폰트 색에 적용", command=lambda :ColorChange('fg', int(spinbox_r.get()), int(spinbox_g.get()), int(spinbox_b.get())))
    apply_fgcolor.place(anchor='n', relx = 3/4, rely=2/3)

    setting_window.mainloop()

def InfoMenu():
    info_window = tkinter.Tk()
    info_window.title("프로그램 정보")
    info_window.geometry("300x100+200+200")
    info_window.resizable(False, False)
    
    info=tkinter.Label(info_window, text=info_text)
    info.pack()

    info_window.mainloop()

def CloseMenu():
    main_window.quit()
    main_window.destroy()


# window setting
main_window.title("Shortcut Launcher")
main_window.geometry(str(main_window_width)+"x"+str(main_window_height)+"+100+100")
WinResize(0)
TopMostScreen(0)


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