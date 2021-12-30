import pyautogui as pag
import msdata as ms
from setappsize import SetAppSize
from time import sleep
import os.path


def multicommand():
    while True : 
        ms.PrintUB_Bold()
        print("※멀티 커맨드")
        ms.PrintUB()      
        print("[1]Item ID 입력 : +0 ~ +13강 장비 생성\n[2]TXT 파일 실행 : Item ID\n[3]TXT 파일 실행 : 명령어\n[4]Item ID 입력 : 직접 입력")
        ms.PrintUB()      
        print("[0]메인메뉴")
        ms.PrintUB()      
        num2 = int(ms.InputNum(5))
        ms.clear()
        if num2==0:
            break
        elif num2 ==1:
            Command_Additem()
        elif num2 ==2:
            Command_Additems_Text()
        elif num2 ==3:
            Command_Text()
        elif num2 ==4:
            Command_Additems()
    #elif num2 ==5:
    #    Command_Direct2()
    
    #multicommand()


def Command_Additem():
    while True:
        ms.PrintUB_Bold()     
        print("※Item ID 입력 : +0 ~ +13강 장비 생성")
        ms.PrintUB()      
        print("+0강 Item ID를 입력하세요.")
        ms.PrintUB()      
        print("[0]뒤로가기")
        ms.PrintUB()    

        itemNum = (ms.InputNum(99999999))
        if itemNum=="0":
            ms.clear()
            return
        ms.ResetFirst()
        ms.CommandOpen()
        pag.typewrite("additems")
        for j in range(0,14):
            pag.press('space')
            temp = int(itemNum)+j
            pag.typewrite(str(temp))
        ms.CommandClose()


def autoAddItem(id, count):
    if count == "":
        count = 1

    if id == "골드":
        id = 999
    elif id == "화살":
        id = 199030
    elif id == "마법의 크리스탈":
        id = 410
    # elif id == "마일리지":
    #     id = 26
    # elif id == "길드코인":
    #     id = 950
    # elif id == "로얄코인":
    #     id = 952
    # elif id == "명예코인":
    #     id = 951

    ms.ResetFirst()
    ms.CommandOpen()
    pag.typewrite("additem ")
    pag.typewrite(str(id))
    pag.press('space')
    pag.typewrite(str(count))
    ms.CommandClose()

def autoAddItemAll(id):

    ms.ResetFirst()
    ms.CommandOpen()
    pag.typewrite("additems")
    for j in range(0,14):
        pag.press('space')
        temp = int(id)+j
        pag.typewrite(str(temp))
    ms.CommandClose()


def Command_Additems_Text():
    while True :
        ms.PrintUB_Bold()      
        print("※TXT 파일 실행 : Item ID")
        ms.PrintUB()      
        print("불러올 txt 파일명 입력하세요.\n([Enter]입력 시 additems.txt를 불러옵니다.)")
        ms.PrintUB()      
        print("[0]뒤로가기")
        ms.PrintUB() 

        while True  :           
            fileName = input(">")

            #종료 
            if fileName =="0":
                ms.clear()
                return
            #패스(기본 파일 있음)
            elif fileName =="":
                fileName = 'additems'
                break
            #패스(특정 파일 있음)
            elif os.path.isfile(fileName +".txt") :
                break
            else :
                print("파일이 없습니다.")

        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
        f.close()

        ms.ResetFirst()

        ms.CommandOpen()
        pag.typewrite("additems")
        
        for line in lines:
            pag.typewrite(" "+line)
        ms.CommandClose()

def autoAddItemText(filePath):
    with open(filePath) as f:
        lines = f.read().splitlines()
    f.close()
    ms.ResetFirst()
    ms.CommandOpen()
    pag.typewrite("additems")
    for line in lines:
        pag.typewrite(" "+line)
    ms.CommandClose()

def Command_Text():
    while True :
#세팅값 불러오기&저장
        with open("info_mcmd.txt") as setFile:
            setValue = setFile.read().splitlines()
        setFile.close()

        term = int(setValue[0])
        count = int(setValue[1])

#UI 실행부
        ms.PrintUB_Bold()      
        print("※TXT 파일 실행 : 명령어")
        ms.PrintUB() 
        print("＊명령어 실행 간격 : ", setValue[0], "초")
        print("＊실행횟수 : ", setValue[1], "회")
        ms.PrintUB()  
        print("[9]설정변경")
        print("[0]뒤로가기")
        ms.PrintUB()          
        print("불러올 txt 파일명 입력해주세요\n([Enter]입력 시 multicommand.txt를 불러옵니다.)")
        ms.PrintUB()  

#Input 입력부
        while True  :           
            fileName = input(">")
            #종료 
            if fileName =="0":
                ms.clear()
                return
            #설정변경
            elif fileName == "9":
                setMsg = ["명령어 실행 대기 간격(초)을 입력해 주세요(0~)","실행 횟수를 입력해주세요(1~)"]
                ms.ChangeSetValue("info_mcmd",setMsg)
                print("설정변경 완료!")
                sleep(1)
                ms.clear()
                break
            #패스(기본 파일 있음)
            elif fileName =="":
                fileName = "multicommand"
                break
            #패스(특정 파일 있음)
            elif os.path.isfile(fileName +".txt") :
                break

            else :
                print("파일이 없습니다.")
        
        #설정 변경 시 처음부터 시작
        if fileName == "9":
            continue

#기능 실행부
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
        f.close()

        startTime = ms.GetCurrentTime()
        indivRunTime = len(lines) * 2.5 + term

        ms.clear()
        ms.PrintUB_Bold()      
        print("※TXT 파일 실행 : 명령어")
        ms.PrintUB() 
        print("＊명령어 실행 간격 : ", setValue[0], "초")
        print("＊실행횟수 : ", setValue[1], "회")
        ms.PrintUB()  
        print("총 예상 소요 시간 : ", count * indivRunTime , "초")
        print("총 예상 종료 시각 : ", ms.GetElapsedTime(count * indivRunTime))
        ms.PrintUB()  


        ms.ResetFirst()

        for i in range(0,count) :

            #ms.PrintUB()  
            print(i+1 ,"번 째 실행", end='\r')
            for line in lines:
                ms.Command(line)
                sleep(1)
            
            if i < (count - 1) :
                ms.sleep(term)

#기능 종료부

        endTime = ms.GetCurrentTime()
        totalRuntime = endTime -startTime

        ms.PrintUB() 
        print("실행 완료.") 
        ms.PrintUB()  
        print("총 소요 시간 : ", totalRuntime , "초")
        print("종료 시각 : ", ms.GetCurrentTime())
        ms.PrintUB()  


def Command_Additems():
    while True :
    #UI 실행부
        ms.PrintUB_Bold()      
        print("※Item ID 입력 : 직접 입력")
        ms.PrintUB() 
        print("[0]뒤로가기")
        ms.PrintUB()          
        print("Item ID를 스페이스로 구분하여 입력해주세요.")
        ms.PrintUB() 
        
        itemNums = input(">")
        if itemNums =="0":
            ms.clear()
            return
        ms.ResetFirst()

        ms.CommandOpen()
        pag.typewrite("additems " + str(itemNums))
        ms.CommandClose()



def Command_Direct1():
    
    commandText = input("명령어 입력 : ")
    count = int(input("실행 횟수를 입력해주세요(1~) : "))

    try : 
        if count <= 0 :
                
            print("다시 입력해주세요.")
            Command_Direct1()

        else :
            print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

            ms.ResetFirst()

            for i in range(0,count) :
                ms.Command(commandText)
    
    except : 
        print("다시 입력해주세요.")
        Command_Direct1()

def Command_Direct2():
    print("미완성")
    # commandCountText = "0"
    # commandText = "default"

    # while commandText != "0"
    #     commandCountText = str(int(commandCountText) + 1)
    #     commandText[int(commandCountText)-1] = input(commandCountText + "번째 명령어 입력(종료시 : 0) : ")
        
    # term = int(input("명령어 실행 대기 간격(초)을 입력해 주세요(0~) : "))

    # count = int(input("실행 횟수를 입력해주세요(1~) : "))

    # try : 
    #     if count <= 0 :
                
    #         print("다시 입력해주세요.")
    #         Command_Direct()

    #     else :
    #         print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

    #         ms.ResetFirst()

    #         for i in range(0,count) :
    #             ms.Command(commandText)

    
    # except : 
    #     print("다시 입력해주세요.")
    #     Command_Direct()