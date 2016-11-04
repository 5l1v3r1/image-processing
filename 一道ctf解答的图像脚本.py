# -*- coding:utf-8 -*- 
#来源http://www.cnblogs.com/huangjacky/p/3859786.html
#需要安装Image模块PIL，工具在本目录下。这个安装exe支持python2.7但只支持windows
#PIL下载地址http://www.pythonware.com/products/pil/
#pytesser下载地址http://download.csdn.net/download/pyliang_2008/5564135
#pytesser安装需要PIL，这个也可用来构建验证码破解工具
"""
1、解压pytesser ，将解压后的文件复制到Python安装目录的Lib\site-packages下，直接使用，比如我的安装目录是：C:\Python27\Lib\site-packages。
2、把2个目录添加到环境变量之中。
C:\Python27\Lib\site-packages
C:\Python27\Lib\site-packages\pytesser-v0.0.1
3、还要在C:\Python27\Lib\site-packages下面添加.pth 文件（pytesser-v0.0.1.pth），这个文件里面，
只有 “pytesser-v0.0.1”字符串。(没有引号)
"""
#我主机python2.7这个版本无法安装PIL
#说明pytesser使用的网址如下：
#http://www.cnblogs.com/txw1958/archive/2012/08/09/python-PyTesser.html
import Image
import socket
import base64
import pytesser

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('41.231.53.40',9090))
c=''
while True:
    t=sock.recv(100)
    c=c+t
    if len(t)<100:
        break
with open('t.png','wb').write(base64.decodestring(c[:---8]))
img=Image.new('RGB',(160,20))#创建一个新的图片
out=img.load()
pix=Image.open('t.png').load()
for i in xrange(20):   
    if reduce(lambda x,y:x+y,pix[105+j,190-i]+pix[94-j,9+j])<1000:
        out[i,j]=(255,255,255)
ans=pytesser.image_to_string(img)
print ans
sock.send(ans)
print sock.recv(1024)
    
