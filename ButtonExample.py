# tkinter
# 버튼 카운터를 만든다
    # 버튼
    # 버튼을 눌렀을 때 카운팅을 한다
        # 카운트 숫자가 0
        # 버튼을 누르면 카운트를 1 증가시킨다
    # 카운트한 숫자를 보여준다
        # print를 통해서 숫자를 보여준다
import tkinter

window = tkinter.Tk()

buttonPushedCount : int = 0

def CountButton():
    """
    CountButton()
    check button has pushed and adds one into [buttonPushedCount] global variable.

    :return: None
    """
    global buttonPushedCount
    buttonPushedCount += 1
    print("button pushed : "+ str(buttonPushedCount))

window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False,False)

# main program
button = tkinter.Button(window, overrelief='solid', width=15, command=CountButton, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()