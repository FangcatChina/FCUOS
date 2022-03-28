import easygui as eg
from requests import  get
from bs4 import BeautifulSoup as bs
res = get('http://fcnemo.gitee.io/FCUOSWebService/versionPatch.pinf')
contont = list(eval(bs(res.text,'html.parser').text).values())

msg = contont[0]+'\n作者：'+contont[1]+'\n推送时间：'+contont[2]+'\n更新网址：'+contont[-1]
eg.msgbox(msg,'升级')