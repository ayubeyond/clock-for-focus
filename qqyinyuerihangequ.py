# 导入所需的库
import requests
import re
import json
import os

# 定义爬虫类
class QQMusicCrawler:

    # 初始化
    def __init__(self, genre):
        # 设置音乐类型，1为中文，2为日语，3为韩语
        self.genre = genre
        # 设置请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Referer': 'https://y.qq.com/portal/playlist.html'
        }
        # 设置请求参数
        self.params = {
            'ct': '24',
            'qqmusic_ver': '1298',
            'new_json': '1',
            'remoteplace': 'txt.yqq.playlist',
            'searchid': '71414990796156260',
            't': '0',
            'aggr': '1',
            'cr': '1',
            'catZhida': '1',
            'lossless': '0',
            'flag_qc': '0',
            'p': '1',
            'n': '20',
            'w': genre,
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
        }
        # 设置保存路径
        self.path = './qqmusic/' + genre + '/'
        # 创建文件夹
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    # 获取歌单列表
    def get_playlist(self):
        # 构造歌单列表的url
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_music_search_songlist'
        # 发送请求，获取响应
        response = requests.get(url, headers=self.headers, params=self.params)
        # 解析响应，获取json数据
        data = response.json()
        # 提取歌单列表
        playlist = data['data']['list']
        # 返回歌单列表
        return playlist

    # 获取歌曲列表
    def get_songlist(self, playlist):
        # 构造歌曲列表的url
        url = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg'
        # 遍历歌单列表
        for item in playlist:
            # 提取歌单的id和名称
            disstid = item['dissid']
            dissname = item['dissname']
            # 设置请求参数
            params = {
                'type': '1',
                'json': '1',
                'utf8': '1',
                'onlysong': '0',
                'disstid': disstid,
                'format': 'json',
                'g_tk': '5381',
                'loginUin': '0',
                'hostUin': '0',
                'inCharset': 'utf8',
                'outCharset': 'utf-8',
                'notice': '0',
                'platform': 'yqq.json',
                'needNewCode': '0'
            }
            # 发送请求，获取响应
            response = requests.get(url, headers=self.headers, params=params)
            # 解析响应，获取json数据
            data = response.json()
            # 提取歌曲列表
            songlist = data['cdlist'][0]['songlist']
            # 调用下载歌曲的方法
            self.download_song(songlist, dissname)

    # 下载歌曲
    def download_song(self, songlist, dissname):
        # 遍历歌曲列表
        for song in songlist:
            # 提取歌曲的id，名称，歌手，专辑
            songmid = song['songmid']
            songname = song['songname']
            singer = song['singer'][0]['name']
            albumname = song['albumname']
            # 构造歌曲的url
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
            # 设置请求参数
            params = {
                '-': 'getplaysongvkey9065598412273877',
                'g_tk': '5381',
                'loginUin': '0',
                'hostUin': '0',
                'format': 'json',
                'inCharset': 'utf8',
                'outCharset': 'utf-8',
                'notice': '0',
                'platform': 'yqq.json',
                'needNewCode': '0',
                'data': '{"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"3982823384","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"3982823384","songmid":["' + songmid + '"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'
            }
            # 发送请求，获取响应
            response = requests.get(url, headers=self.headers, params=params)
            # 解析响应，获取json数据
            data = response.json()
            # 提取歌曲的vkey
            vkey = data['req_0']['data']['midurlinfo'][0]['vkey']
            # 拼接歌曲的下载链接
            download_url = 'http://ws.stream.qqmusic.qq.com/' + songmid + '.m4a?fromtag=46&vkey=' + vkey
            # 设置歌曲的文件名
            filename = songname + '-' + singer + '-' + albumname + '.m4a'
            # 设置歌曲的保存路径
            filepath = self.path + dissname + '/' + filename
            # 创建歌单的文件夹
            if not os.path.exists(self.path + dissname):
                os.makedirs(self.path + dissname)
            # 下载歌曲
            print('正在下载：' + filename)
            try:
                # 发送请求，获取歌曲的二进制数据
                content = requests.get(download_url, headers=self.headers).content
                # 保存歌曲到本地
                with open(filepath, 'wb') as f:
                    f.write(content)
                print('下载成功：' + filename)
            except Exception as e:
                print('下载失败：' + filename)
                print(e)

    # 运行爬虫
    def run(self):
        # 获取歌单列表
        playlist = self.get_playlist()
        # 获取歌曲列表
        self.get_songlist(playlist)

# 实例化爬虫对象，传入音乐类型
crawler = QQMusicCrawler('中日韩')
# 运行爬虫
crawler.run()
