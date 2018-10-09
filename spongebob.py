# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback
from gtts import gTTS
from googletrans import Translator

_session = requests.session()
translateen = []
line = LINE("ExQPbG1r1POJ48Vl0z45.fj0S/qYKVWGRwpehA8QPbq.JnNjXBotZJZCqtNYVkI1kNOSS031Jjb8M80N/Mumeoc=")
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
settingsOpen = codecs.open("prankBots.json","r","utf-8")
settings = json.load(settingsOpen)
oepoll = OEPoll(line)
lineProfile = line.getProfile()
lineSettings = line.getSettings()
lineMID = line.profile.mid
def backupData():
    try:
        backup = settings
        f = codecs.open('prankBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def logError(text):
    line.log("[ ERROR ] " + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("prankBots.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            prankbot = pesan.replace(settings["keyCommand"],"")
        else:
            prankbot = "Undefined command"
    else:
        prankbot = text.lower()
    return prankbot
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            line.findAndAddContactsByMid(op.param1)
            line.sendMessage(op.param1, "Thanks for add\nCreator Bots")
            line.sendContact(op.param1, 'u9f09cfcb17d037e2936b751bd9d40ead')
        if op.type == 13:
            try:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                line.acceptGroupInvitation(op.param1)
            except Exception as error:
                logError(error)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
                 setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        prankbot = command(text)
                        if '@ᵈᵘᵈᵘˡ ' in msg.text:
                            kontak = line.getContact(msg._from)
                            response = ("ada apa kau memanggilku ","ya aku disini ","apakah ada yang memesan dudul sepaket ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "keluar" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ok gw keluar ya ","ok siap ","yaudah kalo gitu bye bye ","yasudahlah bye ","rese lu ","njirrr malah crot dia")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                            line.leaveGroup(msg.to)
                        if "makan" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("silahkan makan ","ok ","makan apa bos ","sepertinya aku tidak lapar ","oh tentu saja,sepertinya kau lapar ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "Siapa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kerang ajaib mungkin ","sepertinya beruang laut ","ohh.. aku tidak tau ","sepertinya para neftizen ","itu adalah kau ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "apa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("oh aku tidak tau ","apa yang kau tanyakan ","ohh.. aku tidak tau ","apa itu kau ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kemana" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ke kuburan sana ","ke lubang buaya saja kalo begitu "," ","pergi bekerja keras mencari tikungan mu ","aku harus pulang ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sayank" in text.lower() or "yank" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("beraninya kau panggil sayank ","apa kau para neftizen "," ","palalu peang ","iya sayank ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "mbuh" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("mbuh jare ","semprul kau "," ","tak colok ndasmu ","helehh knapa sih ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kapan" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kapan kapan aja dah ","emang mau ngapain "," ","ntah kapan gw gak tau ","kapan aja boleh ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "bot" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("paan lu manggil manggil ","oet hadir "," ","bot bot bot jembot ","jembot mana jmbot ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "knapa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("gak tau ","gak knapa napa "," ","kepo lu ","knapa aja boleh ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "baper" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("puskun gih ","makan aja biar kenyang "," ","baper gw kick nih ","gak usah baper deh minum larutan dulu sana biar adem ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "asem" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("asem jare ","ketek lu asem "," ","asem opone ","lu asem ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sue" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("lu sue gw mah kagak ","sabar.. "," ","bahhhh ","ndasmu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "vekok" in text.lower() or "kampret" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("astagfirullah jangan bilang gitu ","kasar banget lu njir "," ","paan lu mprett. ","biasa aja kalee ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kamvret" in text.lower() or "kampret" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("astagfirullah jangan bilang gitu ","kasar banget lu njir "," ","paan lu mprett. ","biasa aja kalee ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "aim" in text.lower() or "aku" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("iya ","ada apa ","oh bgitu ","aku juga ","hooh ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "nah" in text.lower() or "ayo" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("nah yekan ","kan sue ","gw gak di ajak njir ","okelah kalo bgitu ","siaappp. grakk! ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "dudul" in text.lower() or "kick" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ada saudara gue manggil nie ","bah akur aja sesama dudul ","lebih parah lu kamvret ","situ vekok . ","si dudul sahabat gue ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kan" in text.lower() or "iya" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("apaan,  aku aja diam","kalau aim bilang gak, mau apa lu njirr ","sono sekolah dulu biar ga dudul kaya aim ","situ mau kemana dul ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "assalamualaikum" in text.lower() or "salam" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("waalaikumsalam ","mungkin dibawah aim yang jawab salam, soalnya aim lagi ditoilet "," ","hai ka, salam juga ","aim bot gak ngerti salam 😂 ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "pagi" in text.lower() or "ngopi" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("baru melek ya ka ","iya ngopi dulu biar seger ","aku pagi2 biasanya nyusu bukan ngopi ","bersihin dulu kasur dipipisin kaka tadi malam😛 ","aku sdh nyusu ka, ngga suka kopi ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "bot" in text.lower() or "mbot" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("owh.. ternyata saudara kembar aim, ","jangan panggil2, karena kita sesama dudul ","gw gak di ajak njir ","kirim tikel dulu ke bang sepri baru boleh panggil aim ","bot mata lu 😂😂! ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sepri" in text.lower() or "nieta" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("lu jangan panggil2 boss gue, ntar lu ditikung trus di geprek😀","boss aim lagi mojok😄 "," ","aduh, jangan panggil mulu, boss aku lagi anu.. ","sekali lagi manggil boss gue, gue bakal tikung lu.. sumpah😡 ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "crot" in text.lower() or "crott" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("wah.... enak ya ka?? ","cie yang habis nyabun ","lagi donk ka.. aku pengen ","ah ah ah... la.. la.. la.. ","hadeh desah fals aja crot")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "desah" in text.lower() or "ah" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ahh.. ahh.. ","kmana ","fals gak desahannya njirrr ","coba desahin aku donk 😂 ","dia pasti mau aku desahin.! ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "tagall" in text.lower() or "tag" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kurang kerjaan, main tag aja lu njirrr ","panggil aku aja ka"," ","sepi ya roomnya ","sidudul kesepian😛😛😛 ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "me" in text.lower() or "mie" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("mie ayam apa mie keriting🤗 ","cie botnya modar😂 ","mie dua telur plus satu sosis ","ayam😂 ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kenal" in text.lower() or "tau" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("yang maling semvak itukan?? ","iya, orangnya kurus, tinggi langsing, sisa tulang ","orngnya jago desah, tapi fals ","tau donk, kan setiap desah, pasti keluar vibranya😂😂 ","iya kenal, yang matanya juling itu kan","iya,, pernah ketangkap satpam, maling BH", "tau donk, kan orangnya hitam, cuma putih gigi doank ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "ngerti" in text.lower() or "paham" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("gue mah dudul, mana ngerti ","ajarin donk desah "," aim kan dudul mana paham","dibawah aim nie juga dudul ","itu masalah anu aja..😛😜 ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "smule" in text.lower() or "nyanyi" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("aim ga punya smule ","aim dudul mana bisa nyanyi ","follow gih id smule boss ku BSS1_SEPRI_CHE","ada oc apa dul ","ntar gue join ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "otw" in text.lower() or "otewe" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kemana lu njirr ","aku ikut ya.. ","boong, paling,, nikung dia ","pasti cari tikungan anjayyy ","ttdj ya ka ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "join" in text.lower() or "oc" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("idih, aim bot... mana bisa nyanyi ","ntar aim join ya"," ","apa id smulenya, ntar aim follow😂","mantap.... aim boleh reques ga?? ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "boleh" in text.lower() or "silahkan" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ah.. boong lu... njirr ","masak sih... ","yang beneeerrrr ","gak nyesal nie ","okelah kalau begitu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "tikel" in text.lower() or "sticker" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("tukang palak beraksi ","semua tikel dia, dapat malak njirrr😂 ","tikel hasil malak gampang angus","situkang palak tikel beraksi ","aim gak biasa tikel murahan ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "berapa" in text.lower() or "harga" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("yang mahal dong","aim ga biasa yang murahan ","situ sih murah,, coba yang mahal ","banyak donk.. masak satu aja. ","murah itu..")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
    except Exception as error:
        logError(error)
        
        if op.type == 59:
            print (op)
        
#===========================PRANKBOTS SCRIPT===================#
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
