from pandas.io import excel
from img2str import Img2Str
import pyautogui as pag
from time import sleep
import multicommand as multi
from setappsize import SetAppSize
from resolution import Resolution
from statperlv import StatPerLv
from setclass import SetClass
from equipcheck import EquipCheck
from reincheck import ReinCheck
from engraveCheck import EngraveCheck
from dropCheck import DropCheck
from itemInfoCheck import ItemInfoCheck
from probTest import ProbTest
import os
import time
import datetime
import pandas as pd

#####기본 세팅(폴더생성)
path_screenshot = "./screenshot"
if not os.path.isdir(path_screenshot):                                                           
    os.mkdir(path_screenshot)
######################

with open("info.txt") as infoFile:
    infoTxt = infoFile.read().splitlines()

#infoTxt[0] : 개발모드/알파모드 확인
#infoTxt[0] : 알파모드 앱사이즈 세팅 확인
if infoTxt[0]== "0" :
    devMode = 0

    with open("info_appsize.txt") as infoAppsizeFile:
        infoAppsizeTxt = infoAppsizeFile.read() 
    infoAppsizeFile.close()

    if infoAppsizeTxt== "0" :
        with open("appsize.txt") as f:
            appPos = f.read().splitlines()
        #print("A")
    else :
        with open("appsize_"+infoAppsizeTxt+".txt") as f:
            appPos = f.read().splitlines()

        #print("B")

elif infoTxt[0]== "1" : 
    devMode =1
    
    with open("appsize_dev.txt") as f:
        appPos = f.read().splitlines()


infoFile.close()

# with open("appsize.txt") as f:
#     appPos = f.read().splitlines()

appX = int(appPos[0])
appY = int(appPos[1])
appW = int(appPos[2])
appH = int(appPos[3])

f.close()


#region mouse position
menuPos0=[0.773,0.043]
menuPos1=[0.82,0.043]
menuPos2=[0.865,0.043]
menuPos3=[0.914,0.043]
menuPos4=[0.961,0.043]
menuPos5=[0.773,0.157]
menuPos6=[0.82,0.157]
menuPos7=[0.865,0.157]
menuPos8=[0.914,0.157]
menuPos9=[0.961,0.157]
menuPos10=[0.773,0.271]
menuPos11=[0.82,0.271]
menuPos12=[0.865,0.271]
menuPos13=[0.914,0.271]
menuPos14=[0.961,0.271]
menuPos15=[0.773,0.385]
menuPos16=[0.82,0.385]
menuPos17=[0.865,0.385]
menuPos18=[0.914,0.385]
menuPos19=[0.961,0.385]
menuPos20=[0.773,0.499]
menuPos21=[0.82,0.499]

invenBtnUp2=[0.947,0.157]

invenBtn0=[0.73,0.247]
invenBtn1=[0.788,0.247]
invenBtn2=[0.846,0.247]
invenBtn3=[0.906,0.247]
invenBtn4=[0.968,0.247]
invenBtn5=[0.73,0.353]
invenBtn6=[0.788,0.353]
invenBtn7=[0.846,0.353]
invenBtn8=[0.906,0.353]
invenBtn9=[0.968,0.353]
invenBtn10=[0.73,0.456]
invenBtn11=[0.788,0.456]
invenBtn12=[0.846,0.456]
invenBtn13=[0.906,0.456]
invenBtn14=[0.968,0.456]
invenBtn15=[0.73,0.559]
invenBtn16=[0.788,0.559]
invenBtn17=[0.846,0.559]
invenBtn18=[0.906,0.559]
invenBtn19=[0.968,0.559]

invenBtnRein=[0.813,0.756]#강화
invenBtnDown1=[0.858,0.756]#분해,분해내 일괄선택
invenBtnDown2=[0.945,0.754]#상세,분해 내 분해

invenDesPos=[0.812,0.821]#인벤중간(드래그용)
invenAddDesPos=[0.961,0.697]#추가정보

invenExitBtn=[0.977,0.153]#우상단X버튼

invenSoulBtn=[0.961,0.581]#영혼석 버튼

#아이템 상세 전체
invenDesPos0=[0.698,0.133]
invenDesPos1=[0.996,0.133]
invenDesPos2=[0.698,0.861]
#아이템 이름만
# invenNamePos0=[0.711,0.139]#왼쪽위
# invenNamePos1=[0.960,0.139]#오른쪽위
# invenNamePos2=[0,0.181]#왼쪽아래
#print("CCC")
invenNameBox=[0.721*appW + appX,0.132*appH + appY, appW*0.243, appH*0.046]
#아이템 수량만
# invenAmountPos0=[0.836,0.311]#왼쪽위
# invenAmountPos1=[0.915,0.311]#오른쪽위
# invenAmountPos2=[0.836,0.358]#왼쪽아래
invenAmountBox=[0.859*appW + appX,0.319*appH + appY, appW*0.067, appH*0.04]

#중앙 채팅창
centerChatBox = [0.355 *appW + appX, 0.758*appH + appY , appW*0.336, appH*0.031]


#능력치만
invenOnlyDesPos0=[0.698,0.314]
invenOnlyDesPos1=[0.925,0.314]
invenOnlyDesPos2=[0.698,0.861]
#강화UI
invenReinBtnUp0=[0.77,0.175]
invenReinBtnUp1=[0.92,0.175]
invenReinBtnLeft0=[0.07,0.144]
invenReinBtnLeft1=[0.07,0.221]
invenReinBtnDown0=[0.404,0.91]#단일강화>자동강화
invenReinBtnDown1=[0.558,0.91]#단일강화>강화
invenReinBtnDown2=[0.361,0.952]#다중강화>강화시작
invenReinBtn9=[0.587,0.589]
reinResultTextBox=[0.376*appW+appX,0.14*appH+appY,0.248*appW,0.047*appH]#왼쪽위X,왼쪽위Y,가로,세로]
reinPhase1=[0.176,0.765]
reinPhase2=[0.135,0.591]
reinPhase3=[0.144,0.392]
reinPhase4=[0.206,0.228]
reinPhase5=[0.305,0.139]
reinPhase6=[0.418,0.141]
reinPhase7=[0.514,0.226]
reinPhase8=[0.579,0.393]
reinPhase9=[0.589,0.587]
reinMultiResultBox=[0.245*appW+appX,0.366*appH+appY,0.236*appW,0.418*appH]#왼쪽위X,왼쪽위Y,가로,세로]
#각인UI
engraveBtn=[0.496,0.896]
#engraveResultBox=[0.384*appW+appX,0.55*appH+appY,0.248*appW,0.172*appH]#왼쪽위X,왼쪽위Y,가로,세로
engraveResultBox=[0.389*appW+appX,0.547*appH+appY,0.252*appW,0.224*appH]#왼쪽위X,왼쪽위Y,가로,세로

#영혼석UI
soulTargetBtn=[0.861,0.26]
soulEnchantBtn=[0.489,0.849]

#자동사냥
autoBtn=[0.784,0.906]
#퀵슬롯
quickBtn0=[0.273,0.859]
quickBtn1=[0.336,0.859]
quickBtn2=[0.398,0.859]
quickBtn3=[0.46,0.859]
quickBtn4=[0.539,0.859]
quickBtn5=[0.602,0.859]
quickBtn6=[0.663,0.859]
quickBtn7=[0.723,0.859]

centerPos=[0.5,0.5]
centerUpPos=[0.5,0.4]
commandPos=[0.5,0.734]
executePos=[0.952,0.734]
okPos=[0.583,0.63]
cancelPos=[0.423,0.63]
appUpPos=[0.019,-0.026]

lvBtn=[0.023,0.048]
statBtn=[0.264,0.156]
statdetailBtn=[0.231,0.794]
statdetailPos=[0.435,0.798]

#변신/서번트 카드 수량
cardAmountBox=[0.03*appW+appX,0.82*appH+appY,0.039*appW,0.034*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardNextPageBtn=[0.582,0.898]
cardFirst=[0.073,0.758]
cardSecond=[0.167,0.758]

#변신 등급버튼
transformCardRarityBtn6=[0.906,0.2]
transformCardRarityBtn5=[0.906,0.27]
transformCardRarityBtn4=[0.906,0.34]
transformCardRarityBtn3=[0.906,0.41]
transformCardRarityBtn2=[0.906,0.48]
transformCardRarityBtn1=[0.906,0.55]
transformCardRarityBtn0=[0.906,0.62]

#변신 카드 일반~전체 페이지
transformCardPage0 = 2
transformCardPage1 = 3
transformCardPage2 = 6
transformCardPage3 = 6
transformCardPage4 = 2
transformCardPage5 = 1
transformCardPage6 = 18

servantCardPage0 = 1

#스킬강화 버튼
enchantSkillStartBtn=[0.57,0.757]
enchantSkillBtn=[0.505,0.895]

#매터리얼 UI 버튼
materialCombineTabBtn=[0.214,0.126]
materialAutoInputBtn=[0.182,0.621]
materialCombineBtn=[0.448,0.692]
materialCombineOkBtn=[0.566,0.631]

#자동사냥 AUTO 텍스트 위치 ( 메인화면 확인용 )
autoBtnBox=[0.768*appW+appX,0.887*appH+appY,0.039*appW,0.032*appH]#왼쪽위X,왼쪽위Y,가로,세로



#endregion

waitTime = 0.3
waitTime2 = 0.3

        
# def ApplyAppSize():
            
#     with open("appsize.txt") as f:
#         appPos = f.read().splitlines()

#     appX = int(appPos[0])
#     appY = int(appPos[1])
#     appW = int(appPos[2])
#     appH = int(appPos[3])

def MainMenu():

    while True :
        clear()
        PrintUB_Bold()
        PrintInfo()
        print("AppSize :", appX, appY, appW, appH)
        #print(appX, appY, appW, appH)
        #print(invenNameBox[0])
        global devMode
        if devMode == 0 :
            print("Type : Alpha")
        else:    
            print("Type : Dev")
        PrintUB()
        print("※R2M 전용")
        PrintUB()

        print("[1]캐릭터 텔레포트\n[2]앱 위치 및 크기 설정\n[3]멀티 커맨드\n[4]명령어 모음")
        print("[5]테스트\n[6]텍스트 인식")  
        PrintUB()

        print("[98]Toggle Dev/Alpha\n[0]종료")    
        PrintUB()

        

        num = int(InputNum(99))
        clear()
        if num==0:
            quit()
        elif num == 1:
            DoTeleport()
        elif num == 2:
            SetAppSize()
        elif num==3:
            multi.multicommand()
        elif num==4:
            CommandBundle()
        elif num==5:
            TestMenu()
        elif num==6:
            Img2Str()
        elif num==98:
            if devMode == 0 :
                devMode=1
            else:
                devMode=0
                
            with open("info.txt",'w',encoding='utf-8') as infoFile:
                infoFile.write(str(devMode))
                
            infoFile.close()
            ResetAppSize()


    #MainMenu()

def clear():
    os.system('cls')

def PrintUB():
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def PrintUB_Bold():
    
    print("〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓")

def Move(des):
    pag.moveTo(des[0]*appW + appX, des[1]*appH + appY)
    #sleep(0.1)
    pag.click()        
    sleep(0.01)

def DragUp(des):
    #pag.dragRel(des[0]*appW + appX, des[1]*appH + appY,3,button='left')
    pag.dragRel(0, -280, 1, button='left')
def DragDown(des):
    #pag.dragRel(des[0]*appW + appX, des[1]*appH + appY,3,button='left')
    pag.dragRel(0, 10, 0.5, button='right')

def Capture(fileName):
    sleep(0.1)
    timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName + timestr + ".jpg", region=(appX, appY, appW, appH))
    sleep(0.1)
def CaptureReinforceResult(fileName):
    sleep(0.1)
    pag.screenshot(fileName + ".jpg", region=(reinResultTextBox[0],reinResultTextBox[1],reinResultTextBox[2],reinResultTextBox[3]))
    sleep(0.1)
def CaptureInvenDes(fileName,pos = 0):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    if pos == 0 :#상세전체
        pag.screenshot(fileName  + ".jpg", region=(invenDesPos0[0]*appW + appX,invenDesPos0[1]*appH + appY, appW*(invenDesPos1[0]-invenDesPos0[0]), appH*(invenDesPos2[1]-invenDesPos0[1])))
    elif pos == 1 :#이름
        pag.screenshot(fileName  + ".jpg", region=(invenNameBox[0],invenNameBox[1],invenNameBox[2],invenNameBox[3]))
    elif pos == 2 :#수량
        pag.screenshot(fileName  + ".jpg", region=(invenAmountBox[0],invenAmountBox[1],invenAmountBox[2],invenAmountBox[3]))
    sleep(0.1)
def CaptureEngraveRes(fileName):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName  + ".jpg", region=(engraveResultBox[0],engraveResultBox[1],engraveResultBox[2],engraveResultBox[3]))
    sleep(0.1)
def CaptureCenterChatBox(fileName):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName + ".jpg", region=(centerChatBox[0],centerChatBox[1],centerChatBox[2],centerChatBox[3]))
    sleep(0.1)
def CaptureCardAmount(fileName, order):
    sleep(0.1)
    if order == 0 :
        #print("A")
        pag.screenshot(fileName + ".jpg", region=(cardAmountBox[0]+(0.004*order*appW+appX),cardAmountBox[1],cardAmountBox[2],cardAmountBox[3]))
    else :
        #print("B")
        pag.screenshot(fileName + ".jpg", region=(cardAmountBox[0]+(0.094*order*appW+appX),cardAmountBox[1],cardAmountBox[2],cardAmountBox[3]))
        #print(cardAmountBox[0])
    #print(int(order))
    #print(cardAmountBox[0]+0.095*float(order))
    sleep(0.1)
def CaptureReinMultiResultBox(fileName):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName  + ".jpg", region=(reinMultiResultBox[0],reinMultiResultBox[1],reinMultiResultBox[2],reinMultiResultBox[3]))
    sleep(0.1)

def CaptureFull(fileName):
    timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName + timestr + ".jpg")
    sleep(0.1)
def Command(command):        
    Move(centerPos)
    #sleep(waitTime)       
    if devMode == 0 :
        pag.hotkey('z','x','c','v')
    else:
        DragDown(centerPos)
    sleep(waitTime)       
    Move(commandPos)
    sleep(waitTime)
    pag.typewrite(command)
    #sleep(waitTime)
    Move(centerUpPos)
    sleep(0.1)
    #pag.click()
    Move(executePos)
    Move(centerUpPos)
    #sleep(0.1)
    #Move(centerUpPos)
    #Move(centerPos)
    #sleep(waitTime)

def CommandOpen():
    Move(commandPos)
    sleep(waitTime)

    if devMode == 0 :
        pag.hotkey('z','x','c','v')
    else:
        DragDown(centerPos)
    sleep(waitTime)    
    Move(commandPos)
    sleep(waitTime)
    
def CommandClose():
    sleep(waitTime)
    Move(executePos)
    sleep(0.1)
    pag.click()
    sleep(waitTime)

def ResetFirst():
    
    Move(appUpPos)
    sleep(0.01)
    Move(centerPos)
    pag.press('esc')
    sleep(0.01)
    pag.press('esc')
    sleep(0.01)
    pag.press('esc')
    sleep(0.01)
    Move(cancelPos)
    sleep(waitTime)

def Escape():
    pag.press('esc')
    sleep(0.01)


def DoTeleport():
    PrintUB()
    print("※이동할 지역 번호를 입력해주세요.")
    PrintUB()
    print("[1]메테오스탑 입구\n[2]왕의무덤 입구\n[3]바이런성\n[4]푸리에성\n[5]로덴성\n[6]블랙랜드성")
    PrintUB()
    print("[0]메인메뉴")
    PrintUB()

    num = int(InputNum(6))
    if num==0:
        MainMenu()
    # print("입력성공")
    # sleep(2)
    ResetFirst()
    if num==1:
        Command("doteleport 0 1860 404")
    elif num==2:
        Command("doteleport 0 1380 165")
    elif num==3:
        Command("doteleport 0 350 1100")
    elif num==4:
        Command("doteleport 0 410 125")
    elif num==5:
        Command("doteleport 0 1740 1150")
    elif num==6:
        Command("doteleport 0 1500 360")

setTeleportNum = 0

def CMD_DoTeleport(num):
    # if num == 99 :
    #     num = setTeleportNum
    ResetFirst()
    if num==0:
        MainMenu()
    elif num==1:
        Command("doteleport 0 1860 404")
    elif num==2:
        Command("doteleport 0 1380 165")
    elif num==3 or num == "바이런성":
        Command("doteleport 0 350 1100")
    elif num==4 or num == "푸리에성":
        Command("doteleport 0 410 125")
    elif num==5 or num == "로덴성":
        Command("doteleport 0 1740 1150")
    elif num==6 or num == "블랙랜드성":
        Command("doteleport 0 1500 360")        
    elif num==7 or num == "그렘린숲":
        Command("doteleport 0 527 399")        
        
def TestMenu():
    clear()
    print("---------------------------------------------------------------")
    print("실행할 테스트를 선택해주세요.")
    print("[1]분해\n[2]레벨별스탯\n[3]장비수치확인\n[4]장비강화확인\n")
    print("[5]각인확인\n[6]드랍템확인\n[7]아이템정보확인\n[8]확률")
    print("[0]메인메뉴")
    print("---------------------------------------------------------------")
    
    num = int(InputNum(8))
    clear()
    if num==0:
        MainMenu()
    elif num == 1:
        Resolution()
    elif num == 2:
        StatPerLv()
    elif num == 3:
        EquipCheck()
    elif num == 4:
        ReinCheck()
    elif num == 5:
        EngraveCheck()
    elif num == 6:
        DropCheck()
    elif num == 7:
        ItemInfoCheck()
    elif num == 8:
        ProbTest()
    
    TestMenu()

def CommandBundle():
    print("---------------------------------------------------------------")
    print("실행할 명령어모음 번호를 입력해주세요.")
    print("[1]나이트풀세팅  [2]아처풀세팅   [3]위저드풀세팅 [4]어쌔신풀세팅")
    print("[0]메인메뉴")
    print("---------------------------------------------------------------")
    num = int(InputNum(5))
    clear()
    if num==0:
        MainMenu()
    elif num >= 1 or num<=4:

        print("---------------------------------------------------------------")
        print("타입 선택")
        print("[1]기본세팅  [2]서버이전세팅")
        print("[0]메인메뉴")
        print("---------------------------------------------------------------")
        typeNum = int(InputNum(2))
        clear()
        if typeNum==0:
            CommandBundle()
        elif typeNum==1:
            SetClass(num, True)
        elif typeNum==2:
            SetClass(num, False)

        


def InputNum(a):#최대번호
    num = input(">")
    while num.isalpha() or int(num) > int(a) or int(num)<0:
        print("다시 입력해주세요.")
        num = input(">")
    return num

def PrintInfo():
    #print("---------------------------------------------------------------")
    print("v2.0 | 211215")
    #print("---------------------------------------------------------------")


def ResetAppSize():
    if devMode==0:
        
        with open("appsize.txt") as f:
            appPos = f.read().splitlines()

    else :
        
        with open("appsize_dev.txt") as f:
            appPos = f.read().splitlines()

    global appX,appY,appW,appH,invenNameBox,invenAmountBox,engraveResultBox
    appX = int(appPos[0])
    appY = int(appPos[1])
    appW = int(appPos[2])
    appH = int(appPos[3])
    
    #MainMenu()
    #invenNameBox=[0.721*appW + appX,0.132*appH + appY, appW*0.243, appH*0.046]
    #invenAmountBox=[0.859*appW + appX,0.319*appH + appY, appW*0.067, appH*0.04]
    print(appW)
    engraveResultBox=[0.384*appW+appX,0.55*appH+appY,0.248*appW,0.172*appH]

def ResetAppSize211214():
    global devMode,appX,appY,appW,appH,invenNameBox,invenAmountBox,engraveResultBox,centerChatBox,reinResultTextBox,reinMultiResultBox,cardAmountBox,autoBtnBox

    with open("info.txt") as infoFile:
        infoTxt = infoFile.read().splitlines()

    #infoTxt[0] : 개발모드/알파모드 확인
    #infoTxt[0] : 알파모드 앱사이즈 세팅 확인
    if infoTxt[0]== "0" :
        devMode = 0

        with open("info_appsize.txt") as infoAppsizeFile:
            infoAppsizeTxt = infoAppsizeFile.read()

        
        if infoAppsizeTxt== "0" :
            with open("appsize.txt") as f:
                appPos = f.read().splitlines()
            #print("A")
        else :
            with open("appsize_"+infoAppsizeTxt+".txt") as f:
                appPos = f.read().splitlines()

            #print("B")

    elif infoTxt[0]== "1" : 
        devMode =1
        
        with open("appsize_dev.txt") as f:
            appPos = f.read().splitlines()


    infoFile.close()

    # with open("appsize.txt") as f:
    #     appPos = f.read().splitlines()

    appX = int(appPos[0])
    appY = int(appPos[1])
    appW = int(appPos[2])
    appH = int(appPos[3])

    infoAppsizeFile.close()
    f.close()

    invenNameBox=[0.721*appW + appX,0.132*appH + appY, appW*0.243, appH*0.046]
    invenAmountBox=[0.859*appW + appX,0.319*appH + appY, appW*0.067, appH*0.04]
    centerChatBox = [0.355 *appW + appX, 0.758*appH + appY , appW*0.336, appH*0.031]
    reinResultTextBox=[0.376*appW+appX,0.14*appH+appY,0.248*appW,0.047*appH]#왼쪽위X,왼쪽위Y,가로,세로]
    reinMultiResultBox=[0.245*appW+appX,0.366*appH+appY,0.236*appW,0.418*appH]#왼쪽위X,왼쪽위Y,가로,세로]
    engraveResultBox=[0.389*appW+appX,0.547*appH+appY,0.252*appW,0.224*appH]#왼쪽위X,왼쪽위Y,가로,세로
    cardAmountBox=[0.03*appW+appX,0.82*appH+appY,0.039*appW,0.034*appH]#왼쪽위X,왼쪽위Y,가로,세로
    autoBtnBox=[0.768*appW+appX,0.887*appH+appY,0.039*appW,0.032*appH]#왼쪽위X,왼쪽위Y,가로,세로




def SetMainUI(_nameText,_verText,_dateText,_makerText,_desText,_warnText):
    
    print("┌" + "┐".rjust(107,'─'))
    print(_nameText.center(100))
    print("│" + "│".rjust(107,'─'))
    print("│" + (_verText + " / " + _dateText + " / " + _makerText).rjust(106) +"│")
    print("├" + "┤".rjust(107,'─'))    
    print("│" + "※ 설명 ※".center(102) +"│")
    print("├" + "┤".rjust(107,'─'))
    print(_desText)
    print("├" + "┤".rjust(107,'─'))
    print("│" +  "※ 사전세팅 ※".center(100) +"│")
    print("├" + "┤".rjust(107,'─'))
    print(_warnText)
    print("└" + "┘".rjust(107,'─'))

def GetElapsedTime(_time):
        
    now = datetime.datetime.now()
    #print((now+datetime.timedelta(seconds=_time)).strftime('%m-%d %H:%M:%S'))
    return (now+datetime.timedelta(seconds=_time)).strftime('%m-%d %H:%M:%S')

def ChangeSetValue(txtFileName, setMsg):


    setVal = list(range(0,len(setMsg)))
    tempMsg = list(range(0,len(setMsg)))
    
    for i in range(len(setMsg)) :
        tempMsg[i] = setMsg[i]

    for i in range(len(setMsg)) :
        
        print(setMsg[i])
        setVal[i] = input(">")


    setFile = open(txtFileName+ ".txt", 'w')

    for j in range(len(setMsg)) :
        setFile.write(str(setVal[j]))
        setFile.write('\n')
    
    setFile.close()



    setVal.clear()

    return

def GetCurrentTime():
        
    return datetime.datetime.now()#.strftime('%m-%d %H:%M:%S')


def GetTimeDifference(_startTime):
        
    now = datetime.datetime.now()
    #return (now - datetime.timedelta(seconds=_startTime)).strftime('%m-%d %H:%M:%S')
    return (now - _startTime)

def GetMousePos():
    return pag.position()

def VlookupData(excelFileName):
    if excelFileName == "" :
        excelFileName = "itemList.xlsx"

    getFile = pd.read_excel(excelFileName)