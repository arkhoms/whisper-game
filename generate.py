# TianTcl - Whisper game - generator

import random

_subject    = ["ฉัน","คุณ","เขา","มัน","พวกเรา","พวกเขา","คน","ชาวบ้าน","ผม"]
ext_sub     = [None,"ที่สูงๆ","ที่กวาดถนนอยู่","ตรงนั้น","ในห้องนั้น"]
_verb       = ["นอน","เดิน","คุยกัน","กิน","ดื่ม","นั่ง","ยืน","วิ่ง","กระโดด","ตบ"]
ext_verb    = [None,"อย่างรวดเร็ว","ช้าๆ","อย่างแรง","ไกล","นิ่งๆ","เฉยๆ","สุดๆ","สบายๆ","ยอดเยี่ยม"]
_object     = [None,"ในลู่วิ่ง","ข้าว","บนบาทวิถี","ใต้ต้นไม้","ลานจอดรถ","สุนัข","บ้าน","หน้าตึก"]
ext_obj     = [None,"กว้าง","อร่อย","ใหญ่","เล็ก","สวย","น่ารัก","ริมถนน"]

def make(_part):

    if _part == "subject":
        word = random.choice(_subject)
    elif _part == "verb":
        word = random.choice(_verb)
    elif _part == "object":
        word = random.choice(_object)
    elif _part == "ext subject":
        word = random.choice(ext_sub)
    elif _part == "ext verb":
        word = random.choice(ext_verb)
    elif _part == "ext object":
        word = random.choice(ext_obj)
    return word

def gen():
    parts =["subject","ext subject","verb","object","ext object","ext verb"]
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence
