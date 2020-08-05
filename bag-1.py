import pyHook
import pythoncom

#引用gettool
bag=[1,1,5]

#包包內容選單  查看 刪除沒事
Propslist=["search","delete","nothink"]
#指標
Propspoint=0

#指向
def Propsdirection(MoverPoint):
    startpoint=MoverPoint
    bagQuantity = len(bag)-1
    if startpoint > bagQuantity:
       startpoint = bagQuantity-bagQuantity  #0
    elif startpoint<bagQuantity:
        startpoint=bagQuantity
    return startpoint

def Mover(Movevalue):
    startpoint=Propspoint
    bagQuantity = len(bag)-1
    if(Movevalue.Key == "Right"):
        startpoint=Propspoint+1
        if(startpoint>bagQuantity):
            Propsdirection(startpoint)
            startpoint=Propsdirection(startpoint)
        print(startpoint)
        print(bag[startpoint])
    elif(Movevalue.Key=="Left"):
        startpoint=Propspoint-1
        if(startpoint<bagQuantity):
            Propsdirection(startpoint)
            startpoint=Propsdirection(startpoint)
        print(startpoint)
        print(bag[startpoint])
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

