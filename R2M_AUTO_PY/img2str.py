import pytesseract
from time import sleep
import cv2
import time
import os
import msdata as ms
from datetime import datetime
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
nameText = "텍스트 인식"
verText = "ver 1.0"
dateText = "210730"
makerText = "made by sms"
desText = "  " + "이미지 인식 후 텍스트 파일로 저장"
warnText= "  " + "테스트 전 장착한 장비를 모두 해제하고, 인벤토리 내부 슬롯을 최상단으로 맞추세요."


def Img2Str():
    global path, mergePath
    
    path = "./screenshot/Img2str"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    

    ms.SetMainUI(nameText,verText,dateText,makerText,desText,warnText)
    print("┌" + "┐".rjust(107,'─'))
    print("이미지 인식 대상을 선택해주세요.")
    print(" [1]인벤토리 아이템 [2]중앙채팅창 [3]변신/서번트 카드 수량")
    print(" [0]테스트메뉴")
    print("└" + "┘".rjust(107,'─'))
    #type = int(ms.InputNum(3))
    selectedNum = int(ms.InputNum(3))
    ms.clear()
    if selectedNum==0:
        ms.MainMenu()
    elif selectedNum==1:
        Img2Str_Inventory()
    elif selectedNum==2:
        Img2Str_CenterChatBox()
    elif selectedNum==3:
        Img2Str_CardAmountBox()
    #     DropCheck1()
    # elif num2==2:
    #     DropCheck2()
        
        
    Img2Str()
        
def ResetTxtFile(txtName,info) :
    with open(txtName,'w',encoding='utf-8') as tx:
        tx.write(info+'\n')


def Indiv(txtName,imgName):
    img = cv2.imread(imgName)
    img = cv2.bitwise_not(img)
    _, binary = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    data = pytesseract.image_to_string(binary, lang='kor',config='--psm 6')
    data1 = data.replace("","")

    with open(txtName,'a',encoding='utf-8') as tx:
        tx.write(data1)

#def ScreenShotMenu():



def Indiv_Engrave(txtName,imgName):
    img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    result = 234- img
    data = pytesseract.image_to_string(result, lang='kor+eng')
    
#region 오타수정
    data = data.replace("","")
    data = data.replace('\n\n', "\n")
    data = data.replace('SAS', "공격력")
    data = data.replace('AISEt', "치명타")
    data = data.replace('AI SE}', "치명타")
    data = data.replace('AIHE}', "치명타")
    data = data.replace('#2]', "물리")
    data = data.replace('SHB', "확률")
    data = data.replace('SS', "확률")
    data = data.replace('SB', "확률")
    data = data.replace('96', "%")
    data = data.replace('9%', "%")
    data = data.replace('ICH', "최대")
    data = data.replace('희', "회")
    data = data.replace('흠', "흡")
    data = data.replace('5\/', "PVP")
    data = data.replace('[0\/미', "[PVP]")
    data = data.replace('148', "MP")
    data = data.replace('떼몬', "데몬")
    data = data.replace('a+', "힘+1")
    data = data.replace('YAS', "감소율")
    data = data.replace('7}', "추가")
    data = data.replace('1『', "HP")
    data = data.replace('S+', "흡수")
    data = data.replace('Als', "지능")
    data = data.replace(' 2e2|', "물리")
    data = data.replace('St', "확률")
    data = data.replace(' Grey', "마법")
    data = data.replace('PvP', "PVP")
    data = data.replace('[6\/미', "[PVP]")
    data = data.replace('ACH', "최대")
    data = data.replace(',', ".")
    data = data.replace('2A', "감소율")
    data = data.replace(' S2|', "물리")
    data = data.replace('AISEF', "치명타")
    data = data.replace('[0\/]', "[PVP]")
    data = data.replace('38', "확률")
    data = data.replace('BAS', "감소율")
    data = data.replace(' 22]', "물리")
    data = data.replace(' 물리', "물리")
    data = data.replace('1"', "HP")
    data = data.replace('10회복량+2', "HP 회복량 +2")
    data = data.replace('때?', "때 HP")
    data = data.replace('A확률', "획득량")
    data = data.replace('마범', "마법")
    data = data.replace('크리체', "크리처")
    data = data.replace('최대186', "최대 HP")
    data = data.replace('최대18', "최대 HP")
    data = data.replace('AlCH', "최대")
    data = data.replace('확률S', "회복량")
    data = data.replace('BJF', "추가")
    data = data.replace('AlcH', "최대")
    data = data.replace('변신 시 추가?', "변신 시 추가 HP")
    data = data.replace('최대1ㅁ', "최대 HP ")
    data = data.replace('네몬', "데몬")
    data = data.replace('A|CH', "최대")
    data = data.replace('변신 시 추가|ㅁ', "변신 시 추가 HP")
    data = data.replace('AlcH RP', "최대 HP")
    data = data.replace('24', "근접")
    data = data.replace('¥', "V")
    data = data.replace('소치', "소지")
    data = data.replace('>', "")
    data = data.replace('B+', "흡수")
    data = data.replace('[\이', "[PVP]")
    data = data.replace('{', "(")
    data = data.replace('쿨리', "물리")
    data = data.replace('[2이', "[PVP]")
    data = data.replace('명증', "명중")
    data = data.replace('[?\미]', "[PVP]")
    data = data.replace(' Ba]', "물리")
    data = data.replace('*', "+")
    data = data.replace('AIBEL', "치명타")
    data = data.replace('A/ BEL', "치명타")
    data = data.replace('[2\미', "[PVP]")
    data = data.replace('확률E', "회복률")
    data = data.replace('(PYP]', "[PVP]")
    data = data.replace('4|CH', "최대")
    data = data.replace('AISEL', "치명타")
    data = data.replace('19', "10")
    data = data.replace('S| S25', "회복량")
    data = data.replace('클리', "물리")
    data = data.replace('HP 확률', "HP 흡수")
    data = data.replace('(8이', "[PVP]")
    data = data.replace('떠', "때")
    data = data.replace('alc', "최대")
    data = data.replace('클리', "물리")
    data = data.replace('3|CH', "최대")
    data = data.replace('44?', "MP")
    data = data.replace('[0이', "[PVP]")
    data = data.replace('A\CHHP?', "최대 HP")
    data = data.replace('4『', "HP ")
    data = data.replace('근절', "근접")
    data = data.replace('PyP', "PVP")
    data = data.replace('AIC', "최대")
    data = data.replace(' Be]', "물리")
    data = data.replace('PYP', "PVP")
    data = data.replace('확률', "획득")
    data = data.replace('[0\이', "[PVP]")
    data = data.replace('니0ㅁ', " HP ")
    data = data.replace('룰리', "물리")
    data = data.replace('RISE', "치명타")
    data = data.replace('MPS ', "MP 흡수")
    data = data.replace('최대 +35', "최대 HP +35")
    data = data.replace('치명타? 흡수', "치명타 MP 흡수")
    data = data.replace('회복륨', "회복률")
    data = data.replace('무거울 때 4 『회복량', "무거울 때 HP 회복량")
    data = data.replace('치명타는 Bs', "치명타 HP 흡수")
    data = data.replace('PAS WMP 회복량', "무거울 때 MP 회복량")
    data = data.replace('최대비', "최대 HP")
    data = data.replace('/이', "[PVP]")
    data = data.replace('+1.60%', "+1.00%")
    data = data.replace('[PVP]치명타 획득', "[PVP]치명타 확률")
    data = data.replace('최대님?', "최대 HP")
    data = data.replace('포션 SRS', "포션 회복량")
    data = data.replace('ABEL HP BS', "치명타 HP 흡수")
    data = data.replace('S|} HP', "최대 HP")

    data = data.replace('ABE HP BF', "치명타 HP 흡수")
    data = data.replace('무거울 때 HP S| Sek', "무거울 때 HP 회복량")
    data = data.replace('[보스]물리 $44 (28)', "[보스]물리 공격력(근접)")
    #data = data.replace('+?', "+7")
    data = data.replace('Beis', "크리처")
    data = data.replace('MP 흡수+2', "MP 흡수 +2")
    data = data.replace('MP 3) 32', "MP 회복량")
    data = data.replace('000이', "[PVP]")
    data = data.replace('ABE', "치명타")
    data = data.replace('trel', "마법")
    data = data.replace('ALQEp', "치명타")
    data = data.replace('AIBE}', "치명타")
    data = data.replace('+4.G0%', "+4.00%")

    data = data.replace('MP Sie', "MP 회복량")
    data = data.replace('무거울 GHP', "무거울 때 HP")
    data = data.replace('[PVP] Be!', "[PVP]물리")
    data = data.replace('0/0]', "[PVP]")
    data = data.replace('무거울 HP SRS', "무거울 때 HP 회복량")


    data = data.replace('A\LH', "최대")
    data = data.replace('430', "+30")
    data = data.replace('S최대', "최대")
    data = data.replace('230', "+30")
    data = data.replace('마럽', "마법")
    data = data.replace('따법', "마법")

    data = data.replace('(CHP', "최대 HP")
    data = data.replace('[Bela lore 회복량', "[크리처]마법 명중력")
    data = data.replace('(Helo', "[데몬]마법")
    data = data.replace('[SAY', "[보스]마법")
    data = data.replace('[BAO', "[보스]마법")

    data = data.replace('10회복', "HP 회복")
    data = data.replace('1ㅁ회복', "MP 회복")
    data = data.replace('A최대', "최대")
    data = data.replace('회볼량', "회복량")
    data = data.replace('S123', "회복량")
    data = data.replace('S122', "회복량")
    data = data.replace('AA', "감소")
    data = data.replace('+16%', "+10%")
    data = data.replace('Sistah', "회복량")
    data = data.replace('RP', "HP")
    data = data.replace('226', "+20")
    data = data.replace('SiS}', "회복량")
    data = data.replace('+26%', "+20%")
    data = data.replace('+46%', "+40%")
    data = data.replace('BS', "획득")

    data = data.replace('[BIAS', "[데몬]치명타")
    data = data.replace('공격력 +?', "공격력 +7")
    data = data.replace('[SEE }Bel', "[언데드]물리")
    data = data.replace('[BAJA BE', "[보스]치명타")
    data = data.replace('Bel', "물리")
    data = data.replace('ASH)', "감소(근접)")
    data = data.replace('[SEIS]', "[데몬]물리")
    data = data.replace('획득B', "회복량")
    data = data.replace('S28', "회복량")
    data = data.replace('타 획득', "타 확률")
    data = data.replace('치덩타', "치명타")
    data = data.replace('B획득', "획득량")
    data = data.replace('AS', "소모")
    data = data.replace('AG', "소모")
    data = data.replace('소도', "소모")
    data = data.replace('G소모', "소모")
    data = data.replace('힘+1', "힘 +1")
    data = data.replace('힘+2', "힘 +2")
    data = data.replace('힘+3', "힘 +3")
    data = data.replace('회북량', "회복량")
    data = data.replace('MP 획득', "MP 회복")
    data = data.replace('[0/]', "[PVP]")
    data = data.replace('[0/미', "[PVP]")
    data = data.replace('/]', "[PVP]")
    data = data.replace('/0]', "[PVP]")
    data = data.replace('[/미', "[PVP]")
    data = data.replace('/미', "[PVP]")
    data = data.replace('덩중', "명중")
    data = data.replace('[[PVP]', "[PVP]")
    data = data.replace('[『[PVP]', "[PVP]")
    data = data.replace('[PP]', "[PVP]")
    data = data.replace('[PUP]', "[PVP]")
    data = data.replace('[PUPA', "[PVP]")
    data = data.replace('[04]', "[PVP]")
    data = data.replace('A SE', "치명타")
    data = data.replace('[PVP [OPS', "[PVP]마법")
    data = data.replace('[PVP era', "[PVP]마법")
    data = data.replace('[PVP ita', "[PVP]마법")
    data = data.replace('[PVP joerg', "[PVP]마법")
    data = data.replace('[PVP OPS', "[PVP]마법")
    data = data.replace('[PVP ora', "[PVP]마법")
    data = data.replace(' 2742]', "원거리")
    data = data.replace(' 32]', "물리")
    data = data.replace(' Bal', "물리")
    data = data.replace(' gel', "물리")
    data = data.replace(' Ber', "치명타")
    data = data.replace(' HAE', "원거리")
    data = data.replace(' HAH', "원거리")
    data = data.replace(' Sal 피해', "물리 피해")
    data = data.replace(' Se]', "물리")
    data = data.replace(' Sel', "물리")
    data = data.replace(' Ze]', "물리")
    data = data.replace('[PVP] 물리', "[PVP]물리")
    data = data.replace('22]', "물리")
    data = data.replace('22|', "물리")
    data = data.replace('2e|', "물리")
    data = data.replace('2i 7a]', "원거리")
    data = data.replace('A] Set', "치명타")
    data = data.replace('AI Set', "치명타")
    data = data.replace('AIBE:', "치명타")
    data = data.replace('Cra', "마법")
    data = data.replace('ohe', "마법")
    data = data.replace('OPS', "마법")
    data = data.replace('OPY', "마법")
    data = data.replace('ore', "마법")
    data = data.replace('Ure', "마법")
    data = data.replace('OPY', "마법")
    data = data.replace('Ze|', "물리")
    data = data.replace('ㅎ3', "+3")
    data = data.replace('치명타t', "치명타")
    data = data.replace('치령타', "치명타")
    data = data.replace('흘수', "흡수")
    data = data.replace('[PVPJ', "[PVP]")
    data = data.replace('[면[PVP]', "[PVP]")
    data = data.replace('\[PVP]', "[PVP]")
    data = data.replace('0[PVP]', "[PVP]")
    data = data.replace('00]', "[PVP]")
    data = data.replace('S52', "획득량")
    data = data.replace('회록량', "회복량")
    data = data.replace('소지 SA]', "소지 무게")
    data = data.replace('소지 SAL', "소지 무게")
    data = data.replace('4120', "+120")
    data = data.replace('470', "+70")
    data = data.replace('무거울 때 (?', "무거울 때 HP")
    data = data.replace('무거울 때 1?', "무거울 때 HP")
    data = data.replace('무거울 HP', "무거울 때 HP")
    data = data.replace('무거을', "무거울")
    data = data.replace('지능+1', "지능 +1")
    data = data.replace('민접+1', "민첩 +1")
    data = data.replace('민접+2', "민첩 +2")
    data = data.replace('민접+3', "민첩 +3")
    data = data.replace('민접+4', "민첩 +4")
    data = data.replace('민접+5', "민첩 +5")
    data = data.replace('YS', "획득")
    data = data.replace('7.509', "7.50%")
    data = data.replace('무게 120', "무게 +20")
    data = data.replace('무게 330', "무게 +30")
    data = data.replace('무게 390', "무게 +90")
    data = data.replace('무게 410', "무게 +10")
    data = data.replace('무게 420', "무게 +20")
    data = data.replace('무게 540', "무게 +40")

    data = data.replace('몰리', "물리")
    data = data.replace('leet', "회복량")
    data = data.replace('sleet', "회복량")
    data = data.replace('Z최대', "최대")
    data = data.replace('S| 2B', "회복률")
    data = data.replace('세몬', "데몬")
    data = data.replace('무계', "무게")
    data = data.replace('힘+4', "힘 +4")

    
    data = data.replace('YABB)', "감소(근접)")
    data = data.replace('SHE', "무거울")
    data = data.replace('SHS', "무거울")
    data = data.replace('회복를', "회복률")
    data = data.replace('[근전)', "(근접)")
    data = data.replace('[[PVP]', "[PVP]")
    data = data.replace('페몬', "데몬")
    data = data.replace('헤몬', "데몬")
    data = data.replace('혜몬', "데몬")
    data = data.replace('혜본', "데몬")
    data = data.replace('(근접]', "(근접)")
    #211025
    data = data.replace('근점', "근접")
    data = data.replace('둘리', "물리")
    data = data.replace('를리', "물리")
    data = data.replace('다법', "마법")
    data = data.replace('GA', "감소")
    data = data.replace('(CH', "최대")
    data = data.replace('(cH', "최대")
    data = data.replace('(eH', "최대")
    data = data.replace('(EH', "최대")
    data = data.replace('2) HP', "최대 HP")
    data = data.replace('2\CH', "최대")
    data = data.replace('2\cH', "최대")
    data = data.replace('2\cl', "최대")
    data = data.replace('2\EH', "최대")
    data = data.replace('2c HP', "최대 HP")
    data = data.replace('2H HP', "최대 HP")
    data = data.replace('a\cl', "최대")
    data = data.replace('A\EH', "최대")
    data = data.replace('MP 회복량+3', "MP 회복량 +3")
    data = data.replace('SEH', "최대")
    data = data.replace('Z\EH', "최대")
    data = data.replace('AEH', "최대")
    data = data.replace('AIH', "최대")
    data = data.replace('B\CH', "최대")
    data = data.replace('BCH', "최대")
    data = data.replace('최대 +15', "최대 HP +15")
    data = data.replace('최대ㅁ+45', "최대 HP +45")
    data = data.replace('최대ㅁ+35', "최대 HP +35")
    data = data.replace('최대ㅁ+25', "최대 HP +25")
    data = data.replace('최대 HP 225', "최대 HP +25")
    data = data.replace('최대 HP 250', "최대 HP +50")
    data = data.replace('최대 HP #50', "최대 HP +50")
    data = data.replace('최대 HP #15', "최대 HP +15")
    data = data.replace('최대8+40', "최대 HP +40")
    data = data.replace('(Ble', "[데몬]마법")
    data = data.replace('(ZION', "[데몬]마법")
    data = data.replace('(EON', "[데몬]마법")
    data = data.replace('[HE [OHS', "[데몬]마법")
    data = data.replace('[HE [oe', "[데몬]마법")
    data = data.replace('[HEA BE', "[데몬]치명타")
    data = data.replace('마법 회복량', "마법 명중력")
    data = data.replace(' Si742t', "원거리")
    data = data.replace('[HE]', "[데몬]")
    data = data.replace('[HE [', "[데몬]")
    data = data.replace('[BA]', "[보스]")
    data = data.replace(' SA]', "물리")
    data = data.replace('[HE|S7 2]', "[데몬]원거리")
    data = data.replace('마번', "마법")
    data = data.replace('마벌', "마법")
    data = data.replace('처명타', "치명타")
    data = data.replace('+?', "+7")
    data = data.replace('[제몬]', "[데몬]")
    data = data.replace('왼거리', "원거리")
    data = data.replace('치평타', "치명타")
    data = data.replace('[언데드1', "[언데드]")
    data = data.replace('[코스]', "[보스]")
    data = data.replace('라법', "마법")
    data = data.replace('크리쳐', "크리처")
    data = data.replace('BA 경험치', "변신 경험치")
    data = data.replace('Be]', "[데몬]물리")
    data = data.replace('dl 경험치', "변신 경험치")
    data = data.replace('HA 경험치', "변신 경험치")
    data = data.replace('Hal 경험치', "변신 경험치")
    data = data.replace('감소 경험치', "변신 경험치")
    data = data.replace('련신 경험치', "변신 경험치")
    data = data.replace('무게 100', "무게 +100")
    data = data.replace('무게 90', "무게 +90")
    data = data.replace('무게 580', "무게 +80")
    data = data.replace('무게 350', "무게 +50")
    data = data.replace('무게 50', "무게 +50")
    data = data.replace('무게 150', "무게 +50")
    data = data.replace('무게 40', "무게 +40")
    data = data.replace('무게 530', "무게 +30")
    data = data.replace('무게 420', "무게 +20")
    data = data.replace('무게 510', "무게 +10")

    data = data.replace('포션 회복량 +1.00%', "포션 회복률 +1.00%")
    data = data.replace('포션 회복량 +1.50%', "포션 회복률 +1.50%")
    data = data.replace('포션 회복량 +2.00%', "포션 회복률 +2.00%")
    data = data.replace('포션 회복량 +2.50%', "포션 회복률 +2.50%")
    data = data.replace('포션 회복량 +3.00%', "포션 회복률 +3.00%")
    data = data.replace('포션 회복량 +3.50%', "포션 회복률 +3.50%")
    data = data.replace('포션 회복량 +4.00%', "포션 회복률 +4.00%")
    data = data.replace('포션 회복량 +4.50%', "포션 회복률 +4.50%")
    data = data.replace('포션 회복량 +5.00%', "포션 회복률 +5.00%")
    data = data.replace('포션 회복량 +5.50%', "포션 회복률 +5.50%")
    data = data.replace('포션 회복량 +6.00%', "포션 회복률 +6.00%")
    data = data.replace('포션 회복량 +6.50%', "포션 회복률 +6.50%")
    data = data.replace('포션 회복량 +7.00%', "포션 회복률 +7.00%")
    data = data.replace('포션 회복량 +7.50%', "포션 회복률 +7.50%")
    data = data.replace('포션 회복량 +8.00%', "포션 회복률 +8.00%")
    data = data.replace('포션 회복량 +8.50%', "포션 회복률 +8.50%")
    data = data.replace(' 41.50%', " +1.50%")
    data = data.replace(' 42.50%', " +2.50%")
    data = data.replace(' 43.00%', " +3.00%")
    data = data.replace('포션 SEB', "포션 회복률")


    data = data.replace('지능 11', "지능 +1")
    data = data.replace('지능 +d', "지능 +1")
    data = data.replace('지능 th', "지능 +1")
    data = data.replace('지능 4h', "지능 +1")
    data = data.replace('치명다', "치명타")
    data = data.replace('치명타 획득', "치명타 확률")
    data = data.replace('따나 소모', "마나 소모")

    data = data.replace('WMP 회복량', "때 MP 회복량")
    data = data.replace('무거울 MP', "무거울 때 MP")
    data = data.replace('때 |?', "때 HP")
    data = data.replace('Mp', "MP")
    data = data.replace('『ㅁ회복량', "MP 회복량")
    data = data.replace('『회복량', "HP 회복량")
    data = data.replace('\ㅇ회복량', "MP 회복량")
    data = data.replace('때 4?', "때 MP")
    data = data.replace('때 17', "때 HP")

    data = data.replace('MP M획득', "MP 회복량")
    data = data.replace('MP 회복률', "MP 회복량")
    data = data.replace('MP SIRS', "MP 회복량")
    data = data.replace('MP SiS', "MP 회복량")
    data = data.replace('MP SIs', "MP 회복량")
    data = data.replace('MP Sis', "MP 회복량")
    data = data.replace('MP SRS', "MP 회복량")
    data = data.replace('MP 회복량 +S', "MP 회복량 +5")
    data = data.replace('MP 회복 +4', "MP 회복량 +4")
    data = data.replace('MP 회복 +2', "MP 회복량 +2")
    data = data.replace('MP 회복 +S', "MP 회복량 +5")
    data = data.replace('MP 회복량 43', "MP 회복량 +3")
    data = data.replace('MP회복량', "MP 회복량")

    data = data.replace('[0[PVP]', "[PVP]")
    data = data.replace('[0\]', "[PVP]")
    data = data.replace('[0\미', "[PVP]")
    data = data.replace('[00이', "[PVP]")
    
    data = data.replace('[『미', "")
    data = data.replace('[『', "")
    data = data.replace('[0미', "[PVP]")
    data = data.replace('[8[PVP]', "[PVP]")
    data = data.replace('[8]', "[PVP]")
    data = data.replace('[8\미', "[PVP]")
    data = data.replace('[8\이', "[PVP]")

    
    data = data.replace('217421', "원거리")
    data = data.replace('21742!', "원거리")
    data = data.replace('21742]', "원거리")
    data = data.replace('2712!', "원거리")
    data = data.replace('21742}', "원거리")
    data = data.replace('21742', "원거리")
    data = data.replace('27421', "원거리")
    data = data.replace('27i2t', "원거리")
    data = data.replace('27a!', "원거리")

    data = data.replace('[PVP] 원거리', "[PVP]원거리")

    data = data.replace('A Set', "치명타")
    data = data.replace('AI BEF', "치명타")
    data = data.replace('AI BEt', "치명타")
    data = data.replace('AI SEF', "치명타")
    data = data.replace('AIBER', "치명타")
    data = data.replace('AIBEt', "치명타")
    data = data.replace('[PVPIAI SE', "[PVP]치명타")
    data = data.replace('[PVPIA Bet', "[PVP]치명타")
    data = data.replace('[PVPI치명타', "[PVP]치명타")
    data = data.replace('00이마법', "[PVP]마법")
    data = data.replace('04이마법', "[PVP]마법")

    data = data.replace('[PVPIA BE', "[PVP]치명타")
    data = data.replace('[PVPIA Et', "[PVP]치명타")
    data = data.replace('[PVPIA| BEt 무거울', "[PVP]치명타 확률")
    data = data.replace('[PVPIAI BE', "[PVP]치명타")

    data = data.replace('[PVP} 82]', "[PVP]물리")
    data = data.replace('[며[PVP]', "[PVP]")
    data = data.replace('[미[PVP]', "[PVP]")
    data = data.replace('HP BH', "HP 흡수")
    data = data.replace('HP BE', "HP 흡수")
    data = data.replace('HP Bs', "HP 흡수")
    data = data.replace('HP BA', "HP 흡수")
    data = data.replace('HP 획득', "HP 흡수")
    data = data.replace('HP Bt', "HP 흡수")
    data = data.replace('HP EA', "HP 흡수")
    data = data.replace('HP SE', "HP 흡수")
    data = data.replace('HP SH', "HP 흡수")


    data = data.replace('[00미', "[PVP]")
    data = data.replace('언테드', "언데드")
    data = data.replace('BA 시', "변신 시")
    data = data.replace('MP Seek', "MP 회복량")
    data = data.replace('[PVP OHM!', "[PVP]마법")
    data = data.replace('불리', "물리")
    data = data.replace('치명타 획득', "치명타 확률")
#211110

    data = data.replace('경험치 획득량 +10.며\n', "경험치 획득량 +10.00%")
    data = data.replace('경험치 획득량 +10.0!\n', "경험치 획득량 +10.00%")
    data = data.replace('27i2t', "원거리")
    data = data.replace('민첩+1', "민첩 +1")
    data = data.replace('힘+5', "힘 +5")
    data = data.replace('피해 ZA', "피해 감소")
    data = data.replace('령중력', "명중력")
    data = data.replace('피해 감소 4', "피해 감소 +4")
    data = data.replace('마법 획득량', "마법 공격력")
    data = data.replace('무거물', "무거울")
    data = data.replace('2742 때', "무거울 때")
    data = data.replace('무거울 매', "무거울 때")
    data = data.replace('무거울 맥', "무거울 때")
    data = data.replace('무거울 of', "무거울 때")
    data = data.replace('무거울 tt', "무거울 때")
    data = data.replace('무거울 때 + 회복량', "무거울 때 HP 회복량")
    data = data.replace('무거울 때 +7 회복량', "무거울 때 HP 회복량")
    data = data.replace('HP Bet', "HP 회복량")
    data = data.replace('HP Be', "HP 회복량")
    data = data.replace('HP Set', "HP 회복량")
    data = data.replace('HP Se', "HP 회복량")
    data = data.replace('HP s회복량', "HP 회복량")
    data = data.replace('BAZ 때', "무거울 때")
    data = data.replace('감소율 때', "무거울 때")
    data = data.replace('(cl', "최대")
    data = data.replace('4|c', "최대")
    data = data.replace('4\cH', "최대")
    data = data.replace('4\c', "최대")
    data = data.replace('\cH', "최대")
    data = data.replace('2[cH', "최대")
    data = data.replace('2|cH', "최대")
    data = data.replace('2\Ch', "최대")
    data = data.replace('2lch', "최대")
    data = data.replace('2leh', "최대")
    data = data.replace('4[eh', "최대")
    data = data.replace('A[eh', "최대")
    data = data.replace('a최대', "최대")
    data = data.replace('A최대', "최대")
#211111
    data = data.replace('련신', "변신")
    data = data.replace('흡수 획득', "흡수 확률")
    data = data.replace('확률e', "확률")
    data = data.replace('[cH', "최대")
    data = data.replace('[cl', "최대")
    data = data.replace('AL 시', "변신 시")
    data = data.replace('Alc HP', "최대 HP")
    data = data.replace('2)CH HP', "최대 HP")
    data = data.replace('2[ch HP', "최대 HP")
    data = data.replace('2|CH HP', "최대 HP")
    data = data.replace('2lcH HP', "최대 HP")
    data = data.replace('4|ch HP', "최대 HP")
    data = data.replace('alCH HP', "최대 HP")
    data = data.replace('AlCl HP', "최대 HP")

#211112
    data = data.replace('[CH', "최대")
    data = data.replace('[eH', "최대")
    data = data.replace('[EH', "최대")
    data = data.replace('Alcll', "최대")
    data = data.replace('Alc', "최대")
    data = data.replace('AlCl', "최대")
    data = data.replace('AleH', "최대")
    data = data.replace('Ale', "최대")
    data = data.replace('AlEH', "최대")
    data = data.replace('H변신', "변신")
    data = data.replace('드랍를', "드랍률")
    data = data.replace('확률H', "확률")
    data = data.replace('/?]', "[PVP]")
    data = data.replace('(PVP]', "[PVP]")
    data = data.replace('Oe', "마법")
    data = data.replace('Ore', "마법")
    data = data.replace('[0]', "[PVP]")
    data = data.replace('[0#]', "[PVP]")
    data = data.replace('[0?]', "[PVP]")
    data = data.replace('[80]', "[PVP]")
    data = data.replace('[0[PVP]', "[PVP]")
    data = data.replace('[0\[PVP]', "[PVP]")
    data = data.replace('[0/?)]', "[PVP]")
    data = data.replace(' Set', "치명타")
    data = data.replace(' SEt', "치명타")
    data = data.replace(' SE}', "치명타")
    data = data.replace(' SEF', "치명타")
    data = data.replace('치명타 획득', "치명타 확률")
    data = data.replace('SEB', "드랍률")
    data = data.replace('HEHE', "드랍률")
    data = data.replace('아이템 H획득', "아이템 드랍률")
    data = data.replace('아이템 [획득', "아이템 드랍률")
    data = data.replace(' OFS', "마법")
    data = data.replace(' Ory', "마법")
    data = data.replace('[미마법', "[PVP]마법")
#1115에 해야함 
    data = data.replace('[PVP}ei7izl', "[PVP]원거리")
    data = data.replace('[PVP }obe', "[PVP]마법")
    data = data.replace('치명타}', "치명타")
    data = data.replace('O}e', "마법")
    data = data.replace('O}', "마법")
    data = data.replace('헌데드', "언데드")
    data = data.replace('연데드', "언데드")
    data = data.replace('인데드', "언데드")
    data = data.replace('원데드', "언데드")
    data = data.replace('현데드', "언데드")
    data = data.replace('크리치', "크리처")
    data = data.replace('S/S', "회복량")
    data = data.replace('S152', "회복량")
    data = data.replace('회복량}', "회복량")
    data = data.replace('0회복량', "MP 회복량")
    data = data.replace('S[S 2h', "회복량")
    data = data.replace('Sieh', "회복량")
    data = data.replace('Sie', "회복량")
    data = data.replace('SIS ef', "회복량")
    data = data.replace('SIS et', "회복량")
    data = data.replace('SIS', "회복량")
    data = data.replace('[HEISE', "[데몬]치명타")

    data = data.replace('S]32f', "회복량")
    data = data.replace('S]S25', "회복량")
    data = data.replace('S| 22', "회복량")
    data = data.replace('S|S2}', "회복량")
    data = data.replace('S132}', "회복량")
    data = data.replace('S133}', "회복량")
    data = data.replace('S182}', "회복량")
    data = data.replace('S182F', "회복량")
    data = data.replace('S182', "회복량")
    data = data.replace('(HE치명타', "[데몬]치명타")
    data = data.replace('(HEI소모E', "[데몬]치명타")
    data = data.replace('치명타 획득', "치명타 확률")
    data = data.replace('AicH', "최대")
    data = data.replace('AjcH', "최대")


    data = data.replace('Al 시', "변신 시")
    data = data.replace('At 시', "변신 시")
    data = data.replace('BIC', "최대")

    data = data.replace('최대10', "최대 HP ")
    data = data.replace('최대12', "최대 HP ")
    data = data.replace('최대16', "최대 HP ")
    data = data.replace('HP+', "HP +")

    
    data = data.replace('치명타 BB', "치명타 확률")
    data = data.replace('회목량', "회복량")
#211116
    data = data.replace('[0 회복량', "HP 회복량")
    data = data.replace('40 회복량', "HP 회복량")
    data = data.replace('8? 회복량', "HP 회복량")
    data = data.replace('HP aa', "HP 회복량")
    data = data.replace('HP He', "HP 회복량")
    data = data.replace('HP pie', "HP 회복량")
    data = data.replace('HP pi', "HP 회복량")
    data = data.replace('HP ae', "HP 회복량")
    data = data.replace('회독량', "회복량")
    data = data.replace('[8?]', "[PVP]")
    data = data.replace('[8[PVP]', "[PVP]")
    data = data.replace('[[PVP]', "[PVP]")

    data = data.replace('] 치명타 확률', "]치명타 확률")
    data = data.replace('#1 B=} 획득', "치명타 확률")
    data = data.replace('# B=} 획득', "치명타 확률")
    #data = data.replace('# B=}', "치명타 확률")
    data = data.replace('# 획득 획득', "치명타 확률")
    data = data.replace('#) 획득 획득', "치명타 확률")
    data = data.replace('#] 획득 획득', "치명타 확률")
    data = data.replace('#1 Et 획득', "치명타 확률")
    data = data.replace('#1 획득 획득', "치명타 확률")
    data = data.replace('#1치명타 확률', "치명타 확률")
    data = data.replace('소모Et 획득', "치명타 확률")
    data = data.replace('치명타 SH', "치명타 확률")
    data = data.replace('[치명타', "[PVP]치명타")
    data = data.replace('[미치명타', "[PVP]치명타")
    data = data.replace('0?]치명타', "[PVP]치명타")
    data = data.replace('『]치명타', "[PVP]치명타")
    data = data.replace('확를', "확률")
    data = data.replace('#치명타', "치명타")

    data = data.replace('41S&t 획득', "치명타 확률")
    data = data.replace('8?]', "[PVP]")
    data = data.replace('치명타 무거울', "치명타 확률")

    data = data.replace('치명타E 획득', "치명타 확률")
    data = data.replace('치명타t 획득', "치명타 확률")
    data = data.replace('치명탄 획득', "치명타 확률")
    data = data.replace('10\[PVP]', "[PVP]")

    data = data.replace('B2]', "물리")
    data = data.replace('S2]', "물리")
    data = data.replace('S2|', "물리")
    
    data = data.replace('\]', "[PVP]")
    data = data.replace('10\마', "[PVP]")
    data = data.replace('100미', "[PVP]")

    data = data.replace('BA 획득', "흡수 확률")
    data = data.replace('SA 획득', "흡수 확률")
    data = data.replace('S2|', "물리")
    data = data.replace('S2|', "물리")

    data = data.replace('SH 획득', "흡수 확률")
    

    data = data.replace('40', "+0")
    data = data.replace('41', "+1")
    data = data.replace('42', "+2")
    data = data.replace('43', "+3")
    data = data.replace('44', "+4")
    data = data.replace('45', "+5")
    data = data.replace('46', "+6")
    data = data.replace('47', "+7")
    data = data.replace('48', "+8")
    data = data.replace('49', "+9")
    data = data.replace('++0', "+40")
    data = data.replace('++5', "+45")
    
    data = data.replace('[PVPi', "[PVP]")
    data = data.replace('[?비어', "[PVP]")
    data = data.replace('[0?미', "[PVP]")
    data = data.replace('[#[PVP]', "[PVP]")
    data = data.replace('[2\이', "[PVP]")

    data = data.replace(' 2| 공격력', "물리 공격력")
    data = data.replace(' 2| 명중력', "물리 명중력")
    data = data.replace(' 22 명중력', "물리 명중력")
    data = data.replace(' 22 명중력', "물리 명중력")

    data = data.replace(' B2| 명중력', "물리 명중력")
    data = data.replace(' B4l', "물리")
    data = data.replace(' 물리', "물리")
    data = data.replace('블리', "물리")
    data = data.replace('공격 SE', "공격 속도")

    data = data.replace('[PVP ]', "[PVP]")

    data = data.replace('[8이마법', "[PVP]마법")

    data = data.replace('[PVP]Oh4', "[PVP]마법")
    data = data.replace('[PVP]Oh8', "[PVP]마법")
    data = data.replace('[PVP]Ohe', "[PVP]마법")
    data = data.replace('[PVP]OhY', "[PVP]마법")
    data = data.replace('[PVP]Ob#', "[PVP]마법")
    data = data.replace('[PVP]ObH', "[PVP]마법")
    data = data.replace('[PVP]Oh', "[PVP]마법")
    data = data.replace('[PVP]OHY', "[PVP]마법")#######
    data = data.replace('[PVP ich', "[PVP]마법")
    data = data.replace('[PVP Ich', "[PVP]마법")
    data = data.replace('마법#', "마법")
    data = data.replace('[PVP I', "[PVP]")

    
    data = data.replace('A Et', "치명타")
    data = data.replace(' A/S}', "치명타")
    data = data.replace(' #/S=b', "치명타")
    data = data.replace(' #/S=t', "치명타")
    data = data.replace(' A) S=b', "치명타")
    data = data.replace('J치명타', "치명타")#

    data = data.replace(' 2 Aza]', "원거리")
    data = data.replace(' BAe]', "원거리")
    data = data.replace(' Hae', "원거리")
    data = data.replace(' 2 7iat', "원거리")

    data = data.replace(' i7+2)', "원거리")##
    data = data.replace(' S7+2)', "원거리")###########
    data = data.replace('물리 회피력', "원거리 회피력")###
    data = data.replace('[PyYPi gira)', "[PVP]원거리")##########

    data = data.replace('0? ]', "[PVP]")##
    data = data.replace('\?]', "[PVP]")###
    data = data.replace('8[PVP]', "[PVP]")##
    data = data.replace('000미', "[PVP]")

    data = data.replace('+i', "+1")


    data = data.replace('[PVPIORS', "[PVP]마법")######
    data = data.replace('[PVPIORY', "[PVP]마법")######
    data = data.replace('[PVPIA| BEE', "[PVP]치명타")######

    
    data = data.replace('[?[PVP]', "[PVP]")#########
    data = data.replace('[PVP]]', "[PVP]")
    data = data.replace('/[PVP]', "[PVP]")

    data = data.replace('골드 FSA', "골드 획득량")##
    data = data.replace('골드 FSF', "골드 획득량")##
    data = data.replace('골드 FSH', "골드 획득량")##

    data = data.replace('BEN', "경험치")##
    data = data.replace('BE', "골드")##

    data = data.replace('MP #20', "MP +20")#
    data = data.replace('MP #30', "MP +30")

    data = data.replace('MP 215', "MP +15")###
    data = data.replace('MP 225', "MP +25")#
    data = data.replace('MP 235', "MP +35")

    data = data.replace('변신 시 추가 MP +15.', "변신 시 추가 MP +15")
    data = data.replace('무게 +획득', "무게 +35")
    data = data.replace('무게 ㅎ+0', "무게 +40")

    data = data.replace('[데몬1', "[데몬]")
    data = data.replace('휘피력', "회피력")

    data = data.replace('(HES Ae', "[데몬]원거리")
    data = data.replace('(HEISAe', "[데몬]원거리")
    data = data.replace('(HEISE', "[데몬]원거리")
    data = data.replace('(HES 방어력', "[데몬]마법 방어력")
    data = data.replace('(EOS 방어력', "[데몬]마법 방어력")

    data = data.replace('이동 SE', "이동 속도")
    data = data.replace('이동 $5', "이동 속도")
    
    data = data.replace('[SZ 최대S', "[데몬]마법")
    data = data.replace('[BRIA', "[크리처]")
#21 11 17
    data = data.replace('[Else]', "[데몬]물리")
    data = data.replace('[Heise]', "[데몬]물리")
    data = data.replace('[eS]', "[언데드]")
    data = data.replace('(HZ) Bet', "[데몬]치명타")
    data = data.replace('[Said]물리 획득량 (SH)', "[크리처]물리 명중력(근접)")

    
    data = data.replace('획복량', "회복량")
    data = data.replace('3/2근접', "회복량")

    data = data.replace('최대0+35', "최대 HP +35")
    data = data.replace('최대l', "최대")
    data = data.replace('최대?', "최대 MP")

    data = data.replace('추가 18', "추가 HP")
    data = data.replace('B7EMP', "추가 MP")
    data = data.replace('MP 근접0', "MP +40")
    data = data.replace('MP 33', "MP +3")

    data = data.replace('S+2', "흡수 +2")
    data = data.replace('S+1', "흡수 +1")
    data = data.replace('S4+1', "흡수 +1")
    data = data.replace('B4 +1', "흡수 +1")
    data = data.replace('B4 +2', "흡수 +2")
    data = data.replace('4 +1', "흡수 +1")
    data = data.replace('16 흡수', "HP 흡수")
    data = data.replace('10 흡수', "HP 흡수")

    data = data.replace('치능', "지능")
#211123
    
    data = data.replace('평중력', "명중력")
    data = data.replace('3}S2', "회복량")
    data = data.replace('31S ef', "회복량")
    data = data.replace('S15', "회복량")
    data = data.replace('SiS ef', "회복량")
    data = data.replace('3] 22', "회복량")
    data = data.replace('3] Sef', "회복량")
    data = data.replace('MP ise', "MP 회복량")

    data = data.replace('\HP', "HP")


    data = data.replace('18회복량', "HP 회복량")
    data = data.replace('\ㅁ회복량', "MP 회복량")

    data = data.replace('버크', "MP")
    data = data.replace('추가 16', "추가 HP")
    data = data.replace('BM 시', "변신 시")
    data = data.replace('AM 시', "변신 시")
    data = data.replace('소지물리', "소지 무게")

    data = data.replace('치명타 HP 회복량', "치명타 HP 흡수")
    
#endregion

    with open(txtName,'a',encoding='utf-8') as tx:
        tx.write(data + "\n")

def Indiv_Item(txtName,imgName):#아이템 이름
    img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    result = 234- img
    data = pytesseract.image_to_string(result, lang='kor',config='--psm 6')
    
    data = data.replace("","")
    data = data.replace('\n\n', "\n")
    data = data.replace('골느', "\b")

    with open(txtName,'a',encoding='utf-8') as tx:
        tx.write(data)

def Indiv_Num(txtName,imgName):#아이템 수량
    # img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    # result = 234- img
    # data = pytesseract.image_to_string(result, lang='kor+eng',config='--psm 6')
    img = cv2.imread(imgName)
    img = cv2.bitwise_not(img)
    _, binary = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    data = pytesseract.image_to_string(binary, lang='kor+eng',config='--psm 6')
    data = data.replace("","")
    data = data.replace('\n\n', "\n")

    with open(txtName,'a',encoding='utf-8') as tx:
        tx.write(data)

def Indiv_Num_Return(txtName,imgName):#아이템 수량
    # img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    # result = 234- img
    # data = pytesseract.image_to_string(result, lang='kor+eng',config='--psm 6')
    img = cv2.imread(imgName)
    img = cv2.bitwise_not(img)
    _, binary = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    data = pytesseract.image_to_string(binary, lang='kor+eng',config='--psm 6')
    data = data.replace("","")
    data = data.replace('\n\n', "\n")

    return data
    # with open(txtName,'a',encoding='utf-8') as tx:
    #     tx.write(data)

def Indiv_Num_Zero(txtName,imgName):#변신/서번트 카드 스샷이 비었을 경우 0으로 처리
    # img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    # result = 234- img
    # data = pytesseract.image_to_string(result, lang='kor+eng',config='--psm 6')
    img = cv2.imread(imgName)
    img = cv2.bitwise_not(img)
    _, binary = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    data = pytesseract.image_to_string(binary, lang='kor+eng',config='--psm 6')
    data = data.replace("","")
    data = data.replace('\n\n', "\n")
    #data = data.replace("", "0")

    if not data :
        data = "0\n"

    print(data)

    with open(txtName,'a',encoding='utf-8') as tx:
        tx.write(data)

def Img2Str_Inventory() :
    ms.clear()
    count = int(input("인벤토리 항목 개수를 입력하세요(1~20)[0]뒤로 : "))

    if count == 0 :
        Img2Str()
    elif count >= 21 :
        ms.clear()
        Img2Str_Inventory()
    # else : 
    #     ms.clear()
    #     Img2Str_Inventory()

    curPath = path + "/" +time.strftime("_%H%M")
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)  


    print("준비 중...", end='\r')

    ms.ResetFirst()

    #인벤오픈
    ms.Move(ms.menuPos1)
    sleep(ms.waitTime)
    #img2str.ResetTxtFile(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_names.txt","name")
    #img2str.ResetTxtFile(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_amts.txt","amt")

    for i in range(0,count):
        print(str(i+1) + "/" + str(count), end='\r')
#0번슬롯터치>상세터치>마우스 화면중간터치>스샷(이름,수량)
        ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
        ms.Move(ms.invenBtnDown2)
        ms.Move(ms.centerPos)
        sleep(1.2)#터치한아이템 이름 사라지는 시간
        ms.CaptureInvenDes(curPath+"/"+str(i)+"_name",1)
        Indiv_Item(curPath+"/result_name.txt",curPath+"/"+str(i)+"_name.jpg")

        ms.CaptureInvenDes(curPath+"/"+str(i)+"_amt",2)
        Indiv_Item(curPath+"/result_amt.txt",curPath+"/"+str(i)+"_amt.jpg")
        
        ms.Move(ms.invenExitBtn)
        sleep(0.01)
    #0~20번슬롯 >반복

def Img2Str_CenterChatBox() :
    ms.clear()
    count = int(input("스크린샷 반복 횟수를 입력하세요(1~)[0]뒤로 : "))
    if count == 0 :
        Img2Str()
            
    

    print("┌" + "┐".rjust(107,'─'))
    print("테스트 옵션을 선택하세요..")
    print(" [1]기본 [2]매터리얼초기화(100회간격) [3]인벤토리초기화(100회간격)")
    print(" [0]테스트메뉴")
    print("└" + "┘".rjust(107,'─'))
    optionNum = int(ms.InputNum(3))
    ms.clear()
    if optionNum==0:
        Img2Str()

    curPath = path + "/" +time.strftime("_%H%M") + "_CenterChatBox"
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)  
        
    timerType = int(input("[1]자동반복간격설정(부정확) [2]0번퀵슬롯터치(정확but마우스계속사용)\n[0]뒤로 : "))
    if timerType == 0 :
        Img2Str()
    elif timerType == 1 :
        interval = float(input("반복 간격을 입력하세요(밀리초)(1~)(상자퀵슬롯:1000) [0]뒤로 : "))
        if interval == 0 :
            Img2Str()


        print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(count*(interval/1000 - 0.35077)) +")")
        #print("실행 중...", end='\r')

        ms.ResetFirst()
        
        for i in range(0,count):
            # if optionNum == 1 :
            #     ms.Move(ms.centerPos)
            # elif optionNum !=1 :
            if i % 100 == 0 :
                if optionNum == 1 :
                    ms.Move(ms.centerPos)
                elif optionNum == 2 :
                    ms.Command("cleanupmaterial")
                elif optionNum == 3:
                    ms.Command("cleanupinventory")
                sleep(1)
            #보정값 테스트
            print(datetime.utcnow().strftime('%M:%S.%f'))
            print(str(i+1) + "/" + str(count), end='\r')
            #print(time.strftime("%M%S%f"))
            sleep(interval/1000 - 0.55077)#보정값 0.35077
            ms.CaptureCenterChatBox(curPath+"/picture")
            Indiv_Item(curPath+"/result.txt",curPath+"/picture.jpg")
            
    elif timerType == 2 :

        print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(count*1.2) +")")
        ms.ResetFirst()
        
        for i in range(0,count):
            if i % 100 == 0 :
                if optionNum == 1 :
                    ms.Move(ms.centerPos)
                elif optionNum == 2 :
                    ms.Command("cleanupmaterial")
                elif optionNum == 3:
                    ms.Command("cleanupinventory")
                sleep(1)

            sleep(0.9)
            ms.Move(ms.quickBtn0)
            sleep(0.1)
            ms.CaptureCenterChatBox(curPath+"/picture")
            Indiv_Item(curPath+"/result.txt",curPath+"/picture.jpg")
            
            
def Img2Str_CardAmountBox() :
    ms.clear()
    #count = int(input("스크린샷 반복 횟수를 입력하세요(1~)[0]뒤로 : "))
    #if count == 0 :
    #    Img2Str()
            
    count = 0

    print("┌" + "┐".rjust(107,'─'))
    print("테스트 옵션을 선택하세요..")
    print(" [1]변신 [2]서번트")
    print(" [0]테스트메뉴")
    print("└" + "┘".rjust(107,'─'))
    optionNum = int(ms.InputNum(2))
    ms.clear()
    if optionNum==0:
        Img2Str()
    elif optionNum==1:

        print("┌" + "┐".rjust(107,'─'))
        print("등급을 선택하세요..")
        print(" [1]일반 [2]고급 [3]희귀 [4]영웅 [5]전설 [6]초월 [7]전체")
        print(" [0]테스트메뉴")
        print("└" + "┘".rjust(107,'─'))
        rarityNum = int(ms.InputNum(8))

        count = getattr(ms,'transformCardPage{}'.format(rarityNum-1))

        #count = 18
    elif optionNum==2:
        count = 1



    
    curPath = path + "/" +time.strftime("_%H%M") + "_CardAmountBox"
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)  
    
    #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(count*(interval/1000 - 0.35077)) +")")
    print("실행 중...", end='\r')

    ms.ResetFirst()
    sleep(0.1)
    ms.Move(ms.menuPos4)
    sleep(0.1)
    if optionNum==1:
        ms.Move(ms.menuPos6)
    elif optionNum==2:
        ms.Move(ms.menuPos7)

    sleep(0.5)


    ms.Move(getattr(ms,'transformCardRarityBtn{}'.format(rarityNum-1)))

    for i in range(0,count):
        print(str(i+1) + "/" + str(count), end='\r')

        for j in range(0,10):
            if j==0 :
                ms.Move(ms.cardSecond)
            elif j==1 :
                ms.Move(ms.cardFirst)
            ms.CaptureCardAmount(curPath+"/picture_"+str(i*10+j),j)
            Indiv_Num_Zero(curPath+"/result.txt",curPath+"/picture_"+str(i*10+j)+".jpg")
        
        ms.Move(ms.cardNextPageBtn)
        sleep(0.3)
        