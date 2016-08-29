# coding=UTF-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import time
import traceback
import ingrex
import json
import os
import time
import requests
from ingrex import Intel, Utils
import telepot
from urllib.request import urlopen
from telegram.error import NetworkError, BadRequest
from telepot.exception import TooManyRequestsError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xml.etree.ElementTree as ET
from telegram import Emoji
global remem

bot = telepot.Bot('247649707:xxxx')

global location_def,lati,longi
location_def = 0
lati = 0
longi = 0

#mobile_emulation = { "deviceName": "Google Nexus 6" }#responsive
#options = webdriver.ChromeOptions()
#options.add_extension("tampermonkey.crx")
#options.add_experimental_option("mobileEmulation", mobile_emulation)
#driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)
#driver.set_window_size(430, 696) # optional
#driver.rotate(ScreenOrientation.LANDSCAPE);

#main_window = driver.current_window_handle
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
#driver.switch_to.window(main_window)

#driver.get('https://accounts.google.com/ServiceLogin?service=ah&passive=true&continue=https%3A%2F%2Fappengine.google.com%2F_ah%2Fconflogin%3Fcontinue%3Dhttps%3A%2F%2Fwww.ingress.com%2Fintel&ltmpl=gm&shdf=ChMLEgZhaG5hbWUaB0luZ3Jlc3MMEgJhaCIUDxXHTvPWkR39qgc9Ntp6RlMnsagoATIUG3HUffbxSU31LjICBdNoinuaikg#identifier')
#driver.find_element_by_id("Email").send_keys('xxx@gmail.com')
#driver.find_element_by_id("next").click()
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.ID,'Passwd')))
#driver.find_element_by_id("Passwd").send_keys("xxx")
#driver.find_element_by_id("signIn").submit()
#time.sleep(3)
#driver.get('http://iitc.jonatkins.com/release/total-conversion-build.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/portal-level-numbers.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/portal-names.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/show-linked-portals.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/portal-highlighter-forgotten.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/player-tracker.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/link-show-direction.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/portal-highlighter-high-level.user.js')
#driver.get('http://iitc.jonatkins.com/release/plugins/default-intel-detail.user.js')
#driver.get('https://gist.github.com/neon-ninja/0ef22dae138d31604983/raw/0bfbbc7d81469979e57b1cfbdd3006dd77ebc6d4/iitc-player-tracker-names-alt.user.js')

def weather_func():
    weathersite = urlopen("http://www.smg.gov.mo/smg/c_forecast.xml?id=0.15822404594121342")
    wsource = weathersite.read()
    weather_file = open("weather.xml",'wb+')
    weather_file.write(wsource)
    weather_file.close()
#today
#print(root[1][0][0].tag,root[1][0][0].text) // today date
#print(root[1][0][1].tag,root[1][0][1].text) // today weather
#tommorrow
#print(root[1][1][0].tag,root[1][1][0].text) // tommorrow date
#print(root[1][1][1].tag,root[1][1][1].text) // tommorrow weather

#result = intel.fetch_msg(tab='faction')
#result = intel.fetch_map(['17_29630_13630_0_8_100'])
#result = intel.fetch_portal(guid='ac8348883c8840f6a797bf9f4f22ce39.16')
#result = intel.fetch_score()
#result = intel.fetch_region()
#result = intel.fetch_artifacts()

def intel_information_score_world():
    field = {
        'minLngE6':113531287,
        'minLatE6':22112090,
        'maxLngE6':113589600,
        'maxLatE6':22216029,
    }
    with open('cookie') as cookies:
        cookies = cookies.read().strip()
    intel = ingrex.Intel(cookies, field)
    result = intel.fetch_score()
    return result

def intel_information_score_region():
    field = {
        'minLngE6':113531287,
        'minLatE6':22112090,
        'maxLngE6':113589600,
        'maxLatE6':22216029,
    }
    with open('cookie') as cookies:
        cookies = cookies.read().strip()
    intel = ingrex.Intel(cookies, field)
    result = intel.fetch_region()
    return result['gameScore']

def intel_trcomplete(chat_id):
    no_training = 0
    no_newlink = 0
    no_newcap = 0
    no_newfield = 0
    agent_name1 = ''
    agent_name2 = ''
    agent_name3 = ''
    agent_name4 = ''
    field = {
        'minLngE6':113531287,
        'minLatE6':22112090,
        'maxLngE6':113589600,
        'maxLatE6':22216029,
    }
    with open('cookie') as cookies:
        cookies = cookies.read().strip()
    intel = ingrex.Intel(cookies, field)
    result = intel.fetch_msg(tab='faction')
    for x in range(0,len(result)-1,1):
        agentlog = {}
        if 'completed training' in result[x][2]['plext']['text']:
            agentlog = result[x][2]['plext']['text'].split(' ')
            agent_name1 += '@'+agentlog[1][0:-1]+' '
            if no_training == 0:
                no_training = 1
        if 'first Link' in result[x][2]['plext']['text']:
            agentlog = result[x][2]['plext']['text'].split(' ')
            agent_name2 += '@'+agentlog[2]+' '
            if no_newlink == 0:
                no_newlink = 1
        if 'first Portal' in result[x][2]['plext']['text']:
            agentlog = result[x][2]['plext']['text'].split(' ')
            agent_name3 += '@'+agentlog[2]+' '
            if no_newcap == 0:
                no_newcap = 1
        if 'first Control Field'in result[x][2]['plext']['text']:
            agentlog = result[x][2]['plext']['text'].split(' ')
            agent_name4 += '@'+agentlog[2]+' '
            if no_newfield == 0:
                no_newfield = 1
    if no_training == 0:
        bot.sendMessage(chat_id,'Completed training:\n'+'最近faction log無人complete training wo')
    else:
        bot.sendMessage(chat_id,'Completed training:\n'+agent_name1)
    time.sleep(1)
    if no_newlink == 0:
        bot.sendMessage(chat_id,'First Link:\n'+'最近faction log無人first new link wo')
    else:
        bot.sendMessage(chat_id,'First Link:\n'+agent_name2)
    time.sleep(1)
    if no_newcap == 0:
        bot.sendMessage(chat_id,'First Capture:\n'+'最近faction log無人first new cap wo')
    else:
        bot.sendMessage(chat_id,'First Capture:\n'+agent_name3)
    time.sleep(1)
    if no_newfield == 0:
        bot.sendMessage(chat_id,'First CF:\n'+'最近faction log無人first new field wo')
    else:
        bot.sendMessage(chat_id,'First CF:\n'+agent_name4)
    time.sleep(1)

def welcome_msg(agent_name,chat_id):
    global remem
    field = {
        'minLngE6':113531287,
        'minLatE6':22112090,
        'maxLngE6':113589600,
        'maxLatE6':22216029,
    }
    with open('cookie') as cookies:
        cookies = cookies.read().strip()
    intel = ingrex.Intel(cookies, field)
    result = intel.send_msg(str(agent_name)+' 你好呀，澳門人嗎?有興趣加入澳門藍軍群組嗎，會有老手帶新手升級等活動及資訊', tab='faction')
    bot.sendMessage(chat_id,'\U0001F4F2成功傳送歡迎信息')
    log(remem,'歡迎訊息已傳送')

def email_msg(agent_name,chat_id):
    field = {
        'minLngE6':113531287,
        'minLatE6':22112090,
        'maxLngE6':113589600,
        'maxLatE6':22216029,
    }
    with open('cookie') as cookies:
        cookies = cookies.read().strip()
    intel = ingrex.Intel(cookies, field)
    result = intel.send_msg(' '+str(agent_name)+' 可以下載一個叫Hangout的應用程式，再跟我聯繫,我的email: asdfghj1237890@gmail.com', tab='faction')
    bot.sendMessage(chat_id,'\U0001F4F2成功傳送email信息')
    log(remem,'Email訊息已傳送')

def location_map(lati,longi,response):
    driver.get('https://www.ingress.com/intel?ll='+str(lati)+','+str(longi)+'&z='+str(response))
    #wait = WebDriverWait(driver, 10)
    time.sleep(25)
    driver.save_screenshot('intelscreen.jpg') # save a screenshot to disk

def log(self,operation):
    time_str = '[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '] '
    self.emit(SIGNAL('STATUS'),time_str + operation)

def handle(msg):
    global remem
    content_type, chat_type, chat_id = telepot.glance(msg)
    weathermessage = ''
    if content_type == 'text':
        log(remem,'[%s %d].[%s] MSG:%s'%(chat_type, chat_id, content_type,msg['text']))
        global location_def
        if '天氣' in msg['text']:
            weather_func()
            tree = ET.parse("weather.xml")
            root = tree.getroot()
            if '今日' in msg['text']:
                bot.sendMessage(chat_id, root[1][0][1].text)
                if '驟雨' in root[1][0][1].text:
                    weathermessage += '有驟雨wo ... 今日出門最好帶番把遮\U0001F327'
                if '酷熱' in root[1][0][1].text:
                    weathermessage += '仲酷熱添，咁熱，比我就唔想出去啦\U0001F525'
            elif '聽日' in msg['text']:
                bot.sendMessage(chat_id, root[1][1][1].text)
                if '驟雨' in root[1][1][1].text:
                    weathermessage += '有驟雨wo ... 聽日出門最好帶番把遮\U0001F327'
                if '酷熱' in root[1][1][1].text:
                    weathermessage += '仲酷熱添，咁熱，比我就唔想出去啦\U0001F525'
            elif '明日' in msg['text']:
                bot.sendMessage(chat_id, root[1][1][1].text)
                if '驟雨' in root[1][1][1].text:
                    weathermessage += '有驟雨wo ... 聽日出門最好帶番把遮\U0001F327'
                if '酷熱' in root[1][1][1].text:
                    weathermessage += '仲酷熱添，咁熱，比我就唔想出去啦\U0001F525'
            if (len(weathermessage) >0 ):
                bot.sendMessage(chat_id, weathermessage);
            log(remem,'傳送了天氣訊息')
        elif '女朋友' in msg['text']:
            if '冇女朋友' in msg['text']:
                bot.sendMessage(chat_id, '我都冇wo,你有冇囡囡介紹比我? >_<')
                time.sleep(1)
                bot.sendMessage(chat_id, '多D上Dcard啦!!!!可以抽下囡囡')
            elif '無女朋友' in msg['text']:
                bot.sendMessage(chat_id, '我都冇wo,你有冇囡囡介紹比我? >_<')
                time.sleep(1)
                bot.sendMessage(chat_id, '多D上Dcard啦!!!!可以抽下囡囡')
            elif '有女朋友' in msg['text']:
                bot.sendMessage(chat_id, '頂你呀，有咩女朋友呀 \_/')
        elif '冇Dcard' in msg['text']:
            bot.sendMessage(chat_id, '澳門幾間大學都可以登記Dcard了 XD')
        elif '冇dcard' in msg['text']:
            bot.sendMessage(chat_id, '澳門幾間大學都可以登記Dcard了 XD')
        elif '台妹' in msg['text']:
            bot.sendMessage(chat_id, '台妹...太嬌滴滴了')
        elif '你要學我講野' in msg['text']:
            bot.sendMessage(chat_id, '我學你講野:'+msg['text'])
        elif '世界戰情分數' in msg['text']:
            bot.sendMessage(chat_id,'等我查下先')
            bot.sendMessage(chat_id,'三四秒時間')
            bot.sendMessage(chat_id,Emoji.FROG_FACE+'綠軍:'+str(intel_information_score_world()[0])+'\n\U0001F42C'+'藍軍:'+str(intel_information_score_world()[1]))
            time.sleep(1)
        elif '澳門戰情分數' in msg['text']:
            bot.sendMessage(chat_id,'等我查下先')
            bot.sendMessage(chat_id,'三四秒時間')
            bot.sendMessage(chat_id,Emoji.FROG_FACE+'澳門綠軍:'+str(intel_information_score_region()[0])+' '+'\n\U0001F42C澳門藍軍:'+str(intel_information_score_region()[1]))
            time.sleep(1)
        elif '有幾多new training' in msg['text']:
            bot.sendMessage(chat_id,'\U0001F4E3等我查下faction先')
            intel_trcomplete(chat_id)
            time.sleep(1)
        elif '歡迎' in msg['text']:
            #bot.sendMessage(chat_id,msg['text'])
            if '@' in msg['text']:
                welcome_msg(msg['text'],chat_id)
                #bot.sendMessage(chat_id,str(agentname))
        elif '新手email' in msg['text']:
            if '@' in msg['text']:
                agent_name = msg['text'].split(' ')
                email_msg(agent_name[1],chat_id)
        elif '更新cookie'in msg['text']:
            cookie_update(chat_id)
        elif location_def == 1:
            global longi,lati
            response = int(msg['text'][0])*10+int(msg['text'][1])
            if ( response < 19 and response > 12 ):
                hide_intel_keyboard = {'hide_keyboard': True}
                bot.sendMessage(chat_id,'你揀左 size'+str(response),reply_markup=hide_intel_keyboard)
                bot.sendMessage(chat_id,'請稍等一下，大概10幾秒鐘時間')
                location_map(lati,longi,response)
                bot.sendPhoto(chat_id,open('intelscreen.jpg','rb'))
                location_def = 0
            else:
                bot.sendMessage(chat_id,'你揀錯左size')
    #if content_type == 'location':
    #    global longi,lati
    #    longi = msg['location']['longitude']
    #    lati = msg['location']['latitude']
    #    #bot.sendMessage(chat_id,'經:'+str(longi)+'緯:'+str(lati))
    #    intel_keyboard = {'keyboard':[['18  長度:半條高士德馬路直線長度','17  長度:高士德馬路直線長度', '16  長度:關閘-水溏直線距離'],['15  長度:關閘-荷蘭園直線距離','14  長度:澳門半島大小', '13  長度:關閘到路環石排灣']]}
    #    bot.sendMessage(chat_id,'請問要幾大既地圖?? 14或以下會冇portal資料',reply_markup=intel_keyboard)
    #    location_def = 1

class Worker(QThread):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
    def run(self):
        global remem
        remem = self
        log(self,'Starting')
        log(self,'Listening')
        bot.message_loop(handle)
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setWindowTitle('--Bot--')
        self.setWindowIcon(QtGui.QIcon('ingress.ico'))
        self.resize(900, 500)
        self.text = QtGui.QTextBrowser()
        self.text.setGeometry(QtCore.QRect(10, 10, 781, 481))
        self.text.setStyleSheet("background-color: black;")
        self.text.setFont(QFont("consolas"))
        self.text.setTextColor(QtGui.QColor('white'))
        self.run = QtGui.QPushButton('Run')
        self.run.setGeometry(QtCore.QRect(650, 510, 112, 34))

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.run)
        self.setLayout(layout)

        self.work = Worker()
        # SIGNAL&SLOT
        self.run.clicked.connect(self.start)
        self.connect(self.work, SIGNAL("STATUS"),self.updateUI)
    def start(self):
        self.work.start()
        self.run.setEnabled(False)

    def updateUI(self,status):
        if 'exception' in status:
            self.text.setTextColor(QtGui.QColor('red'))
            self.text.append('%s'%(status))
        elif 'error' in status:
            self.text.setTextColor(QtGui.QColor('red'))
            self.text.append('%s'%(status))
        elif 'changed' in status:
            self.text.setTextColor(QtGui.QColor('Magenta'))
            self.text.append('%s'%(status))
        elif 'new training' in status:
            self.text.setTextColor(QtGui.QColor('yellow'))
            self.text.append('%s'%(status))
        elif 'alert' in status:
            self.text.setTextColor(QtGui.QColor('yellow'))
            self.text.append('%s'%(status))
        elif 'destroyed' in status:
            self.text.setTextColor(QtGui.QColor('lightGray'))
            self.text.append('%s'%(status))
        else:
            self.text.setTextColor(QtGui.QColor('white'))
            self.text.append('%s'%(status))

app = QApplication(sys.argv)
QQ = MainWindow()
QQ.show()
app.exec_()
# Keep the program running.
while 1:
    time.sleep(10)

