import pyHook
import pythoncom

#引用gettool
bag=[0,1,2]

#包包內容選單  查看 刪除沒事
Propslist=["search","delete","nothink"]
#指標
Propspoint=0

#指向
def Propsdirection():
    startpoint=Propspoint
    bagQuantity = len(bag)
    if startpoint > bagQuantity:
       startpoint = bagQuantity-bagQuantity
    elif startpoint<bagQuantity:
        startpoint=bagQuantity-1
    return startpoint

def Mover(Movevalue):
    startpoint=Propspoint
    bagQuantity = len(bag)-1
    if(Movevalue.Key == "Right"):
        startpoint=Propspoint+1
        print(startpoint)
        if(startpoint>bagQuantity):
            Propsdirection()
            print(Propspoint)
    elif(Movevalue.Key=="Left"):
        startpoint=Propspoint-1
        if(startpoint<bagQuantity):
            Propsdirection()
            print(Propspoint)
    return startpoint
    return True
     
#按下右移鍵 point +1
#按下左移鍵 point =10 -1
#刪除裝備
def Deltool():
    print("del")
    deltoole='0'
    bag[point]=int(deltoole)
    return bag[point]
#enter鍵鎖定
#測試包包是否可以撿取物品
hm = pyHook.HookManager()
hm.KeyDown = Mover
hm.HookKeyboard()
    
    #right 右鍵
    #left 左鍵
    

#關閉包包欄

