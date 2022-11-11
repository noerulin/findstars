import requests
import codecs
import asyncio
from lxml import etree
from bs4 import BeautifulSoup

m_gameList = []

"""
取得遊戲名稱
"""
def GetGameName(id):
    response = requests.get("https://www.findstars.cn/detail/" + str(id))

    # tree = html.fromstring(response.content)

    soup = BeautifulSoup(response.text, "html.parser")
    dom = etree.HTML(str(soup))

    try:
        result = dom.xpath('//*[@id="__nuxt"]/div/main/div[1]/div/div[2]/div/h2/text()')
    except:
        result = ''

    if result == []:
        result = ['']

    return result

"""
寫入檔案
"""
def WriteFile():
    path = 'output.txt'
    f = codecs.open(path, 'w', 'utf-8')
    f.writelines(m_gameList)
    f.close()

"""
取得目前最新遊戲列表
"""
async def GetGameList():
    for i in range(1, 1000):
        name = str(i) + ': ' + GetGameName(i)[0] + '\n'
        print(name)

        m_gameList.append(name)
        await asyncio.sleep(0.2)

    WriteFile()

async def main():
    await GetGameList()

asyncio.run(main())