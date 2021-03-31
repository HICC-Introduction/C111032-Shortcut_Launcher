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

button_column = 4
button_row = 2
#button = [[0 for y in range(button_row)] for x in range(button_column)]
rex = 1/button_column #ratio
rey = 1/button_row #ratio

# function area
def Toplevel_Setting():
    setting_window = tkinter.Tk()
    setting_window.title("프로그램 설정")
    setting_window.geometry("500x500+100+100")
    setting_window.resizable(False, False)
    #frame
    setting_window.mainloop()

def Toplevel_Info():
    info_window = tkinter.Tk()
    info_window.title("프로그램 정보")
    info_window.geometry("300x100+200+200")
    info_window.resizable(False, False)
    
    info=tkinter.Label(info_window, text=info_text, width=20, height=3)
    info.pack()

    info_window.mainloop()

def Close():
    main_window.quit()
    main_window.destroy()

def Notepad():
    os.startfile('notepad')

def Calc():
    os.startfile('calc')

def OpenFolder_C():
    os.startfile('c:')

def OpenWebsite_Google():
    os.system("explorer http://google.com")

# window setting
main_window.title("Shortcut Launcher")
main_window.geometry(str(main_window_width)+"x"+str(main_window_height)+"+100+100")
main_window.resizable(False, False)

# menu setting
menubar = tkinter.Menu(main_window)

menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="프로그램 설정", command=Toplevel_Setting)
menu_1.add_command(label="프로그램 정보", command=Toplevel_Info)
menu_1.add_command(label="프로그램 종료", command=Close)
menubar.add_cascade(label="메뉴", menu=menu_1)

# button setting
b1=tkinter.Button(main_window, text="notepad", command=Notepad)
b2=tkinter.Button(main_window, text="calc", command=Calc)
b3=tkinter.Button(main_window, text="c:", command=OpenFolder_C)
b4=tkinter.Button(main_window, text="http://google.com", command=OpenWebsite_Google)

b5=tkinter.Button(main_window, text="blank")
b6=tkinter.Button(main_window, text="blank")
b7=tkinter.Button(main_window, text="blank")
b8=tkinter.Button(main_window, text="blank")

b1.place(relx=rex*0, rely=rey*0, relwidth = rex, relheight = rey)
b2.place(relx=rex*1, rely=rey*0, relwidth = rex, relheight = rey)
b3.place(relx=rex*2, rely=rey*0, relwidth = rex, relheight = rey)
b4.place(relx=rex*3, rely=rey*0, relwidth = rex, relheight = rey)
b5.place(relx=rex*0, rely=rey*1, relwidth = rex, relheight = rey)
b6.place(relx=rex*1, rely=rey*1, relwidth = rex, relheight = rey)
b7.place(relx=rex*2, rely=rey*1, relwidth = rex, relheight = rey)
b8.place(relx=rex*3, rely=rey*1, relwidth = rex, relheight = rey)

# main program
main_window.config(menu=menubar)

main_window.mainloop()