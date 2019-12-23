#!/usr/bin/python

from data.repeaters.combined import *                    
from data.onehitters.combined import *              
import requests
import json


#EMAIL = "slaytanicpower@gmail.com"
EMAIL = "asdf@asdf.com"

def send_dnc(verbose_lvl):
    for RAND_ZIP in range(0,10):
        RAND_PHONE = str("%010d" % (RAND_ZIP))
        RAND_ZIP = str("%05d" % (RAND_ZIP))
        print("[R][->] Sending 1 request to DNC")
        if verbose_lvl > 1:
            print("[R][->] %s" % payload_dnc(EMAIL,RAND_ZIP,RAND_PHONE))
#        req = requests.post(url=url_dnc(),data=json.dumps(payload_dnc(EMAIL,RAND_ZIP,RAND_PHONE)),headers=headers_dnc())
        print("\t----------------")


def send_worldcare(verbose_lvl):
    print("[1][->] Sending 1 request to Worldcare")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_worldcare(EMAIL))
#    req = request.post(url=url_worldcare(),data=json.dumps(payload_worldcare(EMAIL)),headers=headers_worldcare())
    print("\t----------------")

def send_katespade(verbose_lvl):
    print("[1][->] Sending1 request to KateSpade")
    if verbose_lvl > 1:
        print("[1][->] %s" % url_katespade(EMAIL))
#    req = request.get(url=url_katespade(EMAIL),headers=headers_katespade())
    print("\t----------------")

def send_aimsurplus(verbose_lvl):
    print("[1][->] Sending1 request to AimSurplus")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_aimsurplus(EMAIL))
#    req = requests.post(url=url_aimsurplus(),data=json.dumps(payload_aimsurplus(EMAIL)),headers=headers_aimsurplus())
    print("\t----------------")

def send_naa(verbose_lvl):
    print("[1][->] Sending1 request to NAA")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_naa(EMAIL))
#    req ':' requests.post(url':'url_naa(),data':'json.dumps(payload_naa(EMAIL)),headers':'headers_naa())
    print("\t----------------")


def send_23eats(verbose_lvl):
    print("[1][->] Sending1 request to 23eats")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_23eats(EMAIL))
#    req ':' requests.post(url':'url_23eats(),data':'json.dumps(payload_23eats(EMAIL)),headers':'headers_23eats())
    print("\t----------------")

def send_smashingmag(verbose_lvl):
    print("[1][->] Sending1 request to smashingmag")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_smashingmag(EMAIL))
#    req ':' requests.post(url':'url_smashingmag(),data':'json.dumps(payload_smashingmag(EMAIL)),headers':'headers_smashingmag())
    print("\t----------------")

def send_wateraid(verbose_lvl):
    print("[1][->] Sending1 request to wateraid")
    if verbose_lvl > 1:
        print("[1][->] %s" % url_wateraid(EMAIL))
#    req ':' requests.post(url':'url_wateraid(EMAIL),headers':'headers_wateraid())
    print("\t----------------")

def send_lefsetz(verbose_lvl):
    print("[1][->] Sending1 request to lefsetz")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_lefsetz(EMAIL))
#    req ':' requests.post(url':'url_lefsetz(),data':'json.dumps(payload_lefsetz(EMAIL)),headers':'headers_lefsetz())
    print("\t----------------")

def send_mini_airs(verbose_lvl):
    print("[1][->] Sending1 request to mini_airs")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_mini_airs(EMAIL))
#    req ':' requests.post(url':'url_mini_airs(),data':'json.dumps(payload_mini_airs(EMAIL)),headers':'headers_mini_airs())
    print("\t----------------")

def send_thisistrue(verbose_lvl):
    print("[1][->] Sending1 request to thisistrue")
    if verbose_lvl > 1:
        print("[1][->] %s" % payload_thisistrue(EMAIL))
#    req ':' requests.post(url':'url_thisistrue(),data':'json.dumps(payload_thisistrue(EMAIL)),headers':'headers_thisistrue())
    print("\t----------------")

send_thisistrue(2)
send_mini_airs(2)
send_lefsetz(2)
send_wateraid(2)
send_smashingmag(2)
send_23eats(2)
send_naa(2)
send_aimsurplus(2)
send_katespade(2)
send_worldcare(2)
send_dnc(2)
