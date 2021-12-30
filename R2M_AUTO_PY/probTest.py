from img2str import Img2Str
from img2str import Indiv_Num_Return
import pytesseract
from time import sleep
import cv2
import time
import os
import msdata as ms
from datetime import datetime
import shutil
import img2str
import pyautogui as pag
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

# path = "./screenshot/Img2str"+ time.strftime("_%m%d")
# if not os.path.isdir(path):                                                           
#     os.mkdir(path)
    
#global path, mergePath

line_UL = "┌"
line_UR = "┐"
line_DL = "└"
line_DR = "┘"
line_H = "│"
line_W = "─"
nameText = "확률 테스트"
verText = "ver 1.0"
dateText = "211020"
makerText = "made by sms"
desText = "  " + "이미지 인식 후 텍스트 파일로 저장"
warnText= "  " + "테스트 전 장착한 장비를 모두 해제하고, 인벤토리 내부 슬롯을 최상단으로 맞추세요."


def ProbTest():
    global path, mergePath
    
    path = "./screenshot/ProbTest"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    

    ms.SetMainUI(nameText,verText,dateText,makerText,desText,warnText)
    print("┌" + "┐".rjust(107,'─'))
    print("테스트를 선택해주세요.")
    print(" [1]스킬강화 [2]매터리얼합성 [3]장비강화 [4]영혼부여")
    print(" [0]뒤로")
    print("└" + "┘".rjust(107,'─'))
    #type = int(ms.InputNum(3))
    selectedNum = int(ms.InputNum(4))
    ms.clear()
    if selectedNum==0:
        ms.MainMenu()
    elif selectedNum==1:
        EnchantSkill()
    elif selectedNum==2:
        CombineMaterial()
    elif selectedNum==3:
        ReinforceEquipment()
    elif selectedNum==4:
        EnchantSoul()
        
    ProbTest()
        
def EnchantSkill() :
    ms.clear()
            

    skillID = input("확인할 스킬 ID 입력 :")
    skillRarity = input("스킬 등급 입력 [350]희귀 [351]영웅 [352]전설 : ")#350 351 352
    testCount = int(input("반복횟수 입력 :"))
    
    curPath = path + "/" +time.strftime("_%H%M") + "_enchantSkill"
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)  
    
    #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(count*(interval/1000 - 0.35077)) +")")
    print("실행 중...", end='\r')

    #ms.ResetFirst()
    #sleep(0.1)
    for i in range(0, testCount):

        ms.Command("changeskillenchant "+skillID+" 0")
        ms.Command("additem 999 1000000000")
        ms.Command("additem "+skillRarity+" 100000")
        ms.Move(ms.enchantSkillStartBtn)
        sleep(0.1)

        j = 0
        
        while not Indiv_Num_Return == "AUTO" :

            ms.Move(ms.enchantSkillBtn)
            sleep(0.1)
            ms.Move(ms.centerPos)
            sleep(2)
            ms.Capture(curPath+"/"+skillID+"_"+str(j))
            sleep(0.1)
            ms.Move(ms.centerPos)

            j = j+1

    ProbTest()

def CombineMaterial() :
    
    ms.ResetFirst()
    sleep(0.1)

    materialID = input("확인할 매터리얼 ID 입력 :")
    testCount = int(input("반복횟수 입력(회당 30번) :"))


    curPath = path + "/" +time.strftime("_%H%M") + "_combineMaterial"
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)  
    

    ms.Command("additem 999 1000000000")

    for i in range(0, testCount):
        
        ms.Command("cleanupmaterial")
        ms.Command("addmaterial "+materialID+" 120")
        ms.Move(ms.menuPos4)
        sleep(0.05)
        ms.Move(ms.menuPos8)
        sleep(0.05)

        for j in range(0,3):

            ms.Move(ms.materialCombineTabBtn)
            ms.Move(ms.materialAutoInputBtn)
            ms.Move(ms.materialCombineBtn)
            sleep(0.1)
            ms.Move(ms.materialCombineOkBtn)
            sleep(0.5)
            ms.Escape()

            if j == 2 :
                ms.Capture(curPath+"/"+materialID+"_"+str(i))


    ProbTest()

    
def ReinforceEquipment():  
    print("--------------------------------------------------------------")
    print("※주의사항※")   
    print("실행 전 '장비강화.txt'에 아이템 아이디를 한 줄씩 입력해주세요.")   
    print("--------------------------------------------------------------")
    
    # itemNum = input("강화할 장비 id를 입력해주세요(안전강화 이상) // [0]뒤로 : ")
    # if itemNum == "0" : 
    #     ProbTest()

    print("[1]일반강화 [2]다중강화 // [0]뒤로 : ")
    type2Num = int(ms.InputNum(2))
    if type2Num == 0 : 
        ProbTest()

    count = int(input("테스트 횟수를 입력해주세요(다중강화는 회당 16번) // [0]뒤로: "))
    if count == 0 : 
        ProbTest()
        

    print("[1]무기 [2]방어구 [3]장신구 [4]전리품 // [0]뒤로 : ")
    type0Num = int(ms.InputNum(4))
    if type0Num == 0 : 
        ProbTest()

    if type0Num <=3 :
        print("[1]일반 [2]축복 [3]저주 [4]고대 // [0]뒤로 : ")
        type1Num = int(ms.InputNum(4))
        if type1Num == 0 : 
            ProbTest()
    # else :
    #     print("수호팔찌340/파괴가면341/생명금관342")
    #     print("숙련나팔343/영혼부적344/극복성배345")
    #     print("전리품강화주문서 ID 입력 // [0]뒤로 : ")
    #     bookNum = int(ms.InputNum(999))
    #     if bookNum == 0 : 
    #         ProbTest()



    with open("장비강화.txt") as f:
        lines = f.read().splitlines()

    for itemNum in lines:
        print("총 예상 종료 시간 : "+ms.GetElapsedTime((10+ count * 17)*len(lines)) +")")

#아이템 별 폴더 추가 생성
        #if folderCheck == 1:
        startTime = time.strftime("_%m%d%H%M")
        
        extraPath = path + "/"+ itemNum + startTime
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  

        if count <= 0 :
                
            print("처음부터 다시 입력해주세요.")
            ReinforceEquipment()

        else :
            if type2Num == 1 :
                print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 17) +")")

                #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")

                ms.ResetFirst()
                ms.Command("cleanupinventory")


                if type0Num <=3 :
                    bookNum = 300 + (type1Num-1)*10 + (type0Num-1)
                elif type0Num == 4:
                    if int(itemNum) <=430008 :
                        bookNum = 340
                    elif int(itemNum) <=431008:
                        bookNum = 341
                    elif int(itemNum) <=432008:
                        bookNum = 342
                    elif int(itemNum) <=433008:
                        bookNum = 343
                    elif int(itemNum) <=434008:
                        bookNum = 344
                    elif int(itemNum) <=435008:
                        bookNum = 345
                ms.Command("additem "+str(bookNum)+" "+str(count))

                ms.Command("additem 999 1500000000")
                ms.Command("additem "+itemNum+" "+str(count*2))

                sleep(0.01)
                #인벤열기 >
                ms.Move(ms.menuPos1)
                sleep(ms.waitTime)
                #강화UI 오픈
                ms.Move(ms.invenBtnRein)
                sleep(0.2)
                
                ms.Move(ms.invenReinBtnUp1)
                ms.Move(ms.invenBtn0)
                ms.Move(ms.invenReinBtnUp0)

                txtName = path+"/"+str(itemNum)+"_"+str(bookNum)+"_"+str(count)+startTime+".txt"

                for i in range(0,count) :
                    print(str(i+1) +"/" + str(count), end='\r')
                    ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
                    ms.Move(ms.invenReinBtnDown1)
                    sleep(1.5)    
                    ms.Move(ms.centerPos)         
                    sleep(1.5)       
                    ms.CaptureReinforceResult(extraPath+"/"+str(i))
                    img2str.Indiv_Item(txtName,extraPath+"/"+str(i)+".jpg")
                        
                    sleep(0.3)       
                    ms.Move(ms.invenReinBtnDown1) 
            #다중강화
            elif type2Num == 2 :
                print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 18) +")")

                
                for i in range(0,count) :
                    print(str(i+1) +"/" + str(count), end='\r')
                    ms.ResetFirst()

                    ms.Command("cleanupinventory")

                    if type0Num <=3 :
                        bookNum = 300 + (type1Num-1)*10 + (type0Num-1)
                    elif type0Num == 4:
                        if int(itemNum) <=430008:
                            bookNum = 340
                        elif int(itemNum) <=431008:
                            bookNum = 341
                        elif int(itemNum) <=432008:
                            bookNum = 342
                        elif int(itemNum) <=433008:
                            bookNum = 343
                        elif int(itemNum) <=434008:
                            bookNum = 344
                        elif int(itemNum) <=435008:
                            bookNum = 345
                    ms.Command("additem "+str(bookNum)+" 100000")

                    ms.Command("additem 999 1500000000")
                    ms.Command("additem "+itemNum+" 16")

                    sleep(0.01)
                    #인벤열기 >
                    ms.Move(ms.menuPos1)
                    sleep(ms.waitTime)
                    #강화UI 오픈
                    ms.Move(ms.invenBtnRein)
                    sleep(0.2)
                    #다중강화 클릭
                    ms.Move(ms.invenReinBtnLeft1)
                    #주문서등록
                    ms.Move(ms.invenReinBtnUp1)
                    ms.Move(ms.invenBtn0)
                    #장비등록준비
                    ms.Move(ms.invenReinBtnUp0)
                    #장비등록
                    for k in range(0,16):
                        ms.Move(getattr(ms, 'invenBtn{}'.format(k)))
                    
                    txtName = path+"/"+str(itemNum)+"_"+str(bookNum)+"_"+str(count*16)+startTime+".txt"
                    #강화도 클릭
                    phaseNum = (int(itemNum) % 10) + 1
                    ms.Move(getattr(ms, 'reinPhase{}'.format(phaseNum)))

                    #강화시작 클릭
                    ms.Move(ms.invenReinBtnDown2)

                    #2초대기     
                    sleep(3)       

                    #스샷저장
                    if phaseNum < 9 :
                        ms.CaptureReinMultiResultBox(extraPath+"/"+str(i))
                    else : 
                        ms.Capture(extraPath+"/"+str(i))


                    #반복종료 리턴(끝)

    ReinforceEquipment()



def EnchantSoul():
    print("--------------------------------------------------------------") 
    print("실행 전 영혼무기.txt에 아이템 ID, 영혼석.txt에 영혼석 ID를 한 줄씩 입력해주세요.")   
    print("--------------------------------------------------------------")

    contentPath = path + "/EnchantSoul"
    if not os.path.isdir(contentPath):                                                           
        os.mkdir(contentPath)      

    count = int(input("영혼 부여 횟수를 입력해주세요(1~) : "))
    
    # fileName = input("불러올 txt 파일명 입력해주세요(기본 : 영혼무기)([0]돌아가기) : ")
    # if fileName =="0":
    #     SoulCheck()
    # try :
    #     with open(fileName +".txt") as f:
    #         lines = f.read().splitlines()
    #     f.close
    # except : 
    #     print("파일이 존재하지 않습니다.")
    #     SoulCheck2()


    # fileName_Soul = input("불러올 txt 파일명 입력해주세요(기본 : 영혼석)([0]돌아가기) : ")
    # if fileName_Soul =="0":
    #     SoulCheck()
    # try :
    #     with open(fileName_Soul +".txt") as f:
    #         lines_Soul = f.read().splitlines()
    #     f.close
    # except : 
    #     print("파일이 존재하지 않습니다.")
    #     SoulCheck2()
    

    with open("영혼무기.txt") as f1:
        itemLines = f1.read().splitlines()
    with open("영혼석.txt") as f2:
        scrollLines = f2.read().splitlines()

    print("전체 실행횟수 : " + str(len(itemLines)))
    print("전체 예상 종료 시각 : " + str(ms.GetElapsedTime((10+count * 3.7 )* float(len(itemLines)))))


    for i in range(0,len(itemLines)):
        print("실행 중... (예상 종료 시각 : "+ms.GetElapsedTime(10+count * 3.7) +")")
        #텍스트는 어차피 결과 쌓으면되니까 메인에 생성, 스크린샷은 아이템 폴더 내 내부로
        txtName = contentPath+"/"+str(itemLines[i])
        #extraPath = extraPath + "/"+ itemLines[i] + time.strftime("_%H%M")
        extraPath = contentPath + "/"+ itemLines[i]
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  
            

#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")

        ms.Command("additem "+ itemLines[i] +" 25")
        ms.Command("additem "+ scrollLines[i] +" "+str(count))

        ms.Command("additem 999 1500000000")
        ms.Move(ms.menuPos1)
        sleep(0.1)
        ms.Move(ms.invenBtnUp2)
        ms.Move(ms.invenBtn0)
#영혼석 UI 오픈
        ms.Move(ms.invenBtn0)
        sleep(0.2)

#인벤열기 >
        
        for j in range(0,count):
            print(str(j+1) +"/" + str(count), end='\r')
            ms.Move(ms.soulTargetBtn)
            ms.Move(ms.soulEnchantBtn)
            sleep(1.5)    
            ms.Move(ms.centerPos)         
            sleep(1.5)     
            
            ms.CaptureReinforceResult(extraPath+"/"+str(j))
            img2str.Indiv_Item(txtName+".txt",extraPath+"/"+str(j)+".jpg")  
            
            sleep(0.3)       
            ms.Move(ms.soulEnchantBtn)
    EnchantSoul()
    