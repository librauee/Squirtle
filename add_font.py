# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:56:19 2020

@author: 老肥
@WeChat Official Accounts:老肥码码码
@Wechat: jennnny1216

Happy Python，Happy Life!
"""

from PIL import Image,ImageDraw,ImageFont



def add_font(text):

    font=ImageFont.truetype('simhei.ttf', 50)
    img=Image.open('jieni12_19760.jpg')
    print(img.size)
    draw=ImageDraw.Draw(img)
    draw.text((370,50),text,font=font,fill='white')
    img.show()
    img.save('add_font.jpg')
    
    
add_font("钢铁憨憨")