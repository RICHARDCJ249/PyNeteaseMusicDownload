import re
import requests
import tqdm
import sys
import eyed3
import os
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
}


def printInformation():
    print('\n---------------------------------------------------------')
    print('-                                                       -')
    print('-             Name   : Netease Downloader               -')
    print('-             Version: V3.00                            -')
    print('-             Time   : 2020.1.29                        -')
    print('-                                                       -')
    print('-   Information : Can not download "试听" music type    -')
    print('---------------------------------------------------------\n')


def fetch_song_list(id):
    print('---------------------------------------------------------')
    print('-----------> Get Information Of SongList >>>>>')
    print('---------------------------------------------------------')
    url = "http://music.163.com/playlist?id={0}".format(id)
    r = requests.get(url, headers=HEADERS)
    contents = r.text
    pattern = r'<li><a href="/song\?id=(\d+)">.+?</a></li>'
    song_list = re.findall(pattern, contents)
    if not song_list:
        print(
            '不能解析歌单 url\n')
        sys.exit(1)
    print('-----------> Already Get Information Of SongList')
    print('---------------------------------------------------------')
    return song_list


def download_music_by_id(information):
    print('-----------> Downloading >>>>>')
    respon = requests.get(information['url'], headers=HEADERS, stream=True)
    length = int(respon.headers['Content-Length'])
    pbar = tqdm.tqdm(
        total=length, bar_format='-----------> {l_bar} [ {n_fmt} / {total_fmt} | {elapsed} ] ')
    with open('{1} - {0}.mp3'.format(re.sub(r"[\/\\\:\*\?\"\<\>\|]", '-', information['name']), re.sub(r"[\/\\\:\*\?\"\<\>\|]", '-', information['author'])), 'wb') as f:
        for content in respon.iter_content(chunk_size=128):
            f.write(content)
            pbar.update(128)
        pbar.close()
    print('-----------> Already Download')


def getInformationByID(id):
    print('---------------------------------------------------------')
    print('-----------> Get Information >>>>>')
    print('---------------------------------------------------------')
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
    print('-----------> Already Get Information')
    print('---------------------------------------------------------')
    print('->  Name  :   {0}'.format(i['name']))
    print('->  Author:   {0}'.format(i['author']))
    print('->  Album :   {0}'.format(i['album']))
    print('---------------------------------------------------------')
    return i


def fillInformation(information):
    print('-----------> Write Information >>>>>')
    mp3 = eyed3.load('{1} - {0}.mp3'.format(re.sub(r"[\/\\\:\*\?\"\<\>\|]", '-', information['name']), re.sub(
        r"[\/\\\:\*\?\"\<\>\|]", '-', information['author'])))
    mp3.tag.title = information['name']
    mp3.tag.album = information['album']
    mp3.tag.artist = information['author']
    #mp3.tag.lyrics = str(information['lyric'])
    imagedata = requests.get(information['img'], headers=HEADERS).content
    mp3.tag.images.set(3, imagedata, "image/jpeg", information['name'])
    mp3.tag.save()
    print('-----------> Already Write Information')
    print('---------------------------------------------------------')


def downloadOneFile():
    print('-----------> Download Song')
    id = input('-----------> Please Input MusicLink:\n-----------> ')
    _id = re.search(r'song\?id=(\d+)', id).group(1)
    information = getInformationByID(_id)
    download_music_by_id(information)
    fillInformation(information)


def downloadLotOfFile():
    print('-----------> Download Songlist')
    id = input('-----------> Please Input MusicLink:\n-----------> ')
    _id = re.search(r'playlist\?id=(\d+)', id).group(1)
    song_list = fetch_song_list(_id)
    t = 1
    s = []
    for i in song_list:
        f = open('log.txt', 'w', encoding='utf-8')
        f.write('''\n {0}:\n\n DownloadError:\n\n'''.format(
            time.asctime(time.localtime(time.time()))))
        try:
            os.system('cls')
            printInformation()
            print('-----------> Downloading >>>')
            print('-----------> {0} Of All {1} <------------------------------'.format(t, song_list.__len__()))
            information = getInformationByID(i)
            download_music_by_id(information)
            fillInformation(information)
            t += 1
        except:
            s.append(' #######------>  {1}\n'.format(information['name']))
            t += 1
        finally:
            f.writelines(s)
            f.close()


if __name__ == "__main__":
    printInformation()
    mode = input(
        '''-----------> Select a mode:\n-----------> 1.song\n-----------> 2.songlist\n-----------> ''')
    if mode == '1':
        while(1):
            downloadOneFile()
    elif mode == '2':
        while(1):
            downloadLotOfFile()
    else:
        print('Error')
        exit(0)
