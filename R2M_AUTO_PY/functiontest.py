import pyautogui as pag
import msdata as ms
from time import sleep
from equipcheck import EquipCheck
from reincheck import ReinCheck
from engraveCheck import EngraveCheck
from soulCheck import SoulCheck
from dropCheck import DropCheck
from itemInfoCheck import ItemInfoCheck
import img2str
from probTest import ProbTest
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
#import sys, numpy

#pag.moveTo(10,10)
#pag.screenshot('my_region.png', region=(0, 0, 300, 300))
#im1 = pag.screenshot('pyautogui.png')

# ms.Move(ms.statdetailPos)
# ms.DragUp(ms.statdetailPos)
# sleep(2)2
# ms.Move(ms.statdetailPos)
# ms.DragUp(ms.statdetailPos)

#ms.Move(ms.menuPos1)
#EquipCheck()
#ReinCheck()
#ms.Resolution()
#EngraveCheck()
#ms.DragDown(ms.invenBtn2)
#SoulCheck()
#DropCheck()
#ItemInfoCheck()
# for idx in range(5) : 
#     ms.Move(getattr(ms, 'invenBtn{}'.format(idx)))


# ms.CaptureInvenDes("test",2)
# img2str.Indiv_Item('result.txt','test.jpg')

#global var

# def Test() :
#     global var
#     var = 3

# def Print() :
#     print(var)

# Test()
# Print()
# for i in range(0,10) :
#     print(0.094*float(i))


#ms.CaptureCenterChatBox("test")

#img2str.Indiv_Item("result_210907.txt","test_20210907_125445.jpg")

#img2str.Img2Str_CardAmountBox()

#ProbTest()
#EngraveCheck()


getFile = pd.read_excel("itemList.xlsx",sheet_name='DT_Item')
#data_np = pd.DataFrame.to_numpy(getFile)
df = pd.DataFrame(getFile)
getFile.set_index('mID', inplace = True)
#getXl = openpyxl.load_workbook('itemList2.xlsx')
#sheet = getXl.get('DT_Item')
#sheet
print(int(getFile.index[getFile['mName']=='+0 아이언 폴액스'][0]))
#print(int(df.index[df['mName'].str.contains('아이언')][0]))
#print(df.index[df['mName'].str.contains('포션')][2])
#print(len(df.index[df['mName'].str.contains('포션')]))