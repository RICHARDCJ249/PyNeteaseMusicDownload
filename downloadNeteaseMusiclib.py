import re
import requests
import sys
import eyed3
import os
import time



HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
}


def fetch_song_list(id) -> list:
    '''
    获取歌单id列表

    :param id: 歌单id.\n
    :return: 歌单id列表.\n

    '''

    url = "http://music.163.com/playlist?id={0}".format(id)
    r = requests.get(url, headers=HEADERS)
    contents = r.text
    pattern = r'<li><a href="/song\?id=(\d+)">.+?</a></li>'
    song_list = re.findall(pattern, contents)
    song_name = re.findall(r'<h2 class="f-ff2 f-brk">(.*?)</h2>',contents)[0]
    if not song_list:
        raise Exception('不能解析歌单 url\n')
    return song_name, song_list


def download_music_by_id(saveFolder,information,updateFun) -> bool:
    respon = requests.get(information['url'], headers=HEADERS, stream=True)
    if 'Content-Length' not in respon.headers:
        raise Exception('{} 下载失败'.format(information['name']))
    length = int(respon.headers['Content-Length'])
    t = 0
    with open('{}\{} - {}.mp3'.format(saveFolder,re.sub(r"[\/\\\:\*\?\"\<\>\|]", '-', information['author']),re.sub(r"[\/\\\:\*\?\"\<\>\|]", '-', information['name'])), 'wb') as f:
        for content in respon.iter_content(chunk_size=128):
            f.write(content)
            t += 128
            if (t/128)%1000 == 0:
                updateFun(length,t)
    return True


def getInformationByID(id) -> dict:
    data = requests.get(
        'https://music.163.com/song?id={0}'.format(id), headers=HEADERS)
    i = {}
    i['url'] = "http://music.163.com/song/media/outer/url?id={}.mp3".format(id)
    i['name'] = re.findall(
        '<meta property="og:title" content="(.*?)" />', data.text)[0]
    i['author'] = re.findall(
        '<meta property="og:music:artist" content="(.*?)" />', data.text)[0]
    i['album'] = re.findall(
        '<meta property="og:music:album" content="(.*?)"/>', data.text)[0]
    i['img'] = re.findall(
        '<meta property="og:image" content="(.*?)" />', data.text)[0]
    # i['lyric'] = requests.get('http://music.163.com/api/song/media?id={0}'.format(id),headers=HEADERS).json()['lyric']
    return i


def fillInformation(saveFolder,information) -> bool: 
    mp3 = eyed3.load('{}\{} - {}.mp3'.format(saveFolder,re.sub(r"[\/\\\:\*\?\"\<\>\|]", '-', information['author']), re.sub(
        r"[\/\\\:\*\?\"\<\>\|]", '-', information['name'])))
    mp3.tag.title = information['name']
    mp3.tag.album = information['album']
    mp3.tag.artist = information['author']
    #mp3.tag.lyrics = str(information['lyric'])
    imagedata = requests.get(information['img'], headers=HEADERS).content
    mp3.tag.images.set(3, imagedata, "image/jpeg", information['name'])
    mp3.tag.save()
    return True

