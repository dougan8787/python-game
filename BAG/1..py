import pyHook
import pythoncom

def onKeyboardEvent(event):
    if(event.Key == "Right"):
        print("12")# 返回按下的鍵
    return True


     # 創建管理器
hm = pyHook.HookManager()
    # 監聽鍵盤
hm.KeyDown = onKeyboardEvent   
hm.HookKeyboard()  
        # 監聽鼠標 
        #hm.MouseAll = onMouseEvent   
        #hm.HookMouse()
    # 循環監聽
