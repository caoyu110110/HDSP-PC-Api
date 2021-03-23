# _author_ = caoyu
# data = 2021/3/23
# coding:utf-8


import pytesseract as pytesseract

import time
from tkinter import Image

from selenium import webdriver

# 打开一个Chrome浏览器:地址为Chromedriverexe文件的存放地址
driver = webdriver.Chrome("D:/software/Chromediver/chromedriver.exe")  # Chrome浏览器
# driver = webdriver.Chrome(r'ChromeDriver路径') #还可以指定路径
# driver = webdriver.Firefox()                # Firefox浏览器
# driver = webdriver.Ie() # IE浏览器
# driver = webdriver.Edge() # Edge浏览器
# driver = webdriver.Opera() # Opera浏览器
# driver = webdriver.PhantomJS() # PhantomJS浏览器

# 请求运营平台登录页面
driver.get('https://ordertest.triplezan.com/')
driver.refresh()  # 刷新页面
driver.maximize_window()  # 浏览器最大化
time.sleep(3)  # 等待3秒

#登录页面截图

# driver.save_screenshot("C:/Users/caoyu/Desktop/UI/pic.png")

# 截取验证码图片的位置
code_ele = driver.find_element_by_xpath("//*[@class='login-code']/div/div/div[2]/img")
print("验证码的坐标为：", code_ele.location)#控制台查看{'x': 1086, 'y': 368}
print("验证码的大小为：", code_ele.size)# 图片大小{'height': 40, 'width': 110}
# (4)图片4个点的坐标位置
left = code_ele.location['x']#x点的坐标
top = code_ele.location['y']#y点的坐标
right = code_ele.size['width']+left#上面右边点的坐标
down = code_ele.size['height']+top#下面右边点的坐标

print("验证码的具体位置:"+left, top, right, down)



# homepage = Image.open("C:/Users/caoyu/Desktop/UI/codepage.png")
# #截取图片验证码
# im = homepage.crop((left, top, right, bottom))
# #截取的图片验证码保存为新文件
# im.save('C:/Users/caoyu/Desktop/UI/codepage1.png')
#
# # 打开保存的验证码图片
# image = Image.open("")
# # 将图片转化为字符
# vcode = pytesseract.image_to_string(image)
#
# # 填充用户名密码
# driver.find_element_by_css_selector("用户名").send_keys("admin")
# driver.find_element_by_name("密码").send_keys("admin123")
# driver.find_element_by_name("验证码").send_keys(vcode)
# #点击登录
# driver.find_element_by_id("loginBtn").click()
