# 自动操作浏览器
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,requests,json,colorama
def get_QQMusic(id):
    global 歌单名,歌曲信息,歌曲名,歌手名
    url='https://y.qq.com/musicmac/v6/playlist/detail.html?id={}'.format(id)
    edge_settings=webdriver.EdgeOptions()
    #禁用日志输出
    edge_settings.add_experimental_option('excludeSwitches',['enable-logging'])
    #浏览器最小化
    edge_settings.add_argument('--headless')
    drive=webdriver.Edge(options=edge_settings)
    drive.get(url)
    #等待页面加载完成
    time.sleep(3)
    #获取歌单名,h1标签
    歌单名=drive.find_element(By.TAG_NAME,'h1').text
    #获取歌单内歌曲名
    歌曲名=drive.find_elements(By.CLASS_NAME,'mod_songname__name')
    歌曲名=[i.text for i in 歌曲名]
    #获取歌单内歌手名
    歌手名=drive.find_elements(By.CLASS_NAME,'singer_name')
    歌手名=[i.text for i in 歌手名]
    #关闭浏览器
    drive.quit()
    #合并歌曲名和歌手名
    歌曲信息=[i+'-'+j for i,j in zip(歌曲名,歌手名)]
    print(歌单名,歌曲信息)
    for i in 歌曲名:
        get_beatsaber_info(i)
def get_kuwoMusic_info(id):
    pass
def get_beatsaber_info(song_name):
    url='https://beatsaver.com/api/search/text/0?sortOrder=Relevance&q={}'.format(song_name)
    r=requests.get(url)
    json1=json.loads(r.text)
    #获取结果
    song_list=[]
    try:
        for i in range(1):
            j=json1['docs'][i]['metadata']['songName']
            k=json1['docs'][i]['metadata']['levelAuthorName']
            song_list.append(j+'-'+k)
    except:
        song_list.append('未找到')
    print("搜索结果:",song_list,"  歌单内歌曲:",song_name)
    #等待输入
    input()
get_QQMusic(7020194240)