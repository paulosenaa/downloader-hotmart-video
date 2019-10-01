import requests
from tempfile import mkstemp
from shutil import move
import shutil
import json
from os import fdopen, remove
import os
from requests_html import HTMLSession



allFiles = {
    'key' :'https://contentplayer.hotmart.com/video/n3Rd0X9vRm/hls/600/972e6b25-5ddb-4c1e-b0c9-a06418439db2.key',
    'm3u8': 'https://player.hotmart.com/embed/n3Rd0X9vRm/source/playlist/dmlkZW8lMkZuM1JkMFg5dlJtJTJGaGxzJTJGNjAwJTJGNjAwLm0zdTg.m3u8',
    'files':[]   
}
aulas = []
cookies = {
    'CloudFront-Policy': 'eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vY29udGVudHBsYXllci5ob3RtYXJ0LmNvbS92aWRlby9uM1JkMFg5dlJtL2hscy8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNTY2MDg1MTg0fSwiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9fX1dfQ__',
    'CloudFront-Signature': 'JA4wKmdCnpK0IGLiL8uyT~K7DWNlIqHWq8KfRuOmAabecY0RnFFrHxzu2-zjmTEQ2rB7HQAufC09XkSX6tof4HqZu1PWMgdllLiBzjOhvSm~6cpgFHMUSbH~zNzJnRsoTR8ydpuvDBMoOeO7ewEzWDvcRz39cE6f1kOIxBbetyuSMYGxVg6Vy3iVL7iVPqLUl~eSwpnI40Fr-onyW90sgF8nl9afWO~P9tqPNs-6K7pXm~nQITDInrEC1GyQmbFyVGQ8kdKqNpIOcP5snyKbawKUCCjFkpAhRcsYUJo4F8kAVIY6lJpIb0efvuBOy0-UYBW6hSXOPz1xJFuHNoUTtQ__',
    'CloudFront-Key-Pair-Id': 'APKAI5B7FH6BVZPMJLUQ',
    'hmLangCookie': 'pt',
    '_gcl_au': '1.1.531085512.1566045250',
    '_ga': 'GA1.2.1613940760.1566045256',
    '_gid': 'GA1.2.1663333231.1566045256',
    '_fbp': 'fb.1.1566045256051.199888142',
    '_hjid': '910c5411-1a3f-47f3-9d28-eeb0fc32496e',
    'hmClubLoggedFromIntegration': 'false',
    'hmVlcIntegration': 'H4sIAAAAAAAAAIWSS7eiOhCFf9HpBQiiQ94SSaIQHmHi4qFCCIoNRx6%252F%252FuLpHtxZD7JqkFpVtff%252BrjOocqeocQ2CcHFFVLu9%252B%252FCVwnC3btMlkQH2v64zEAspmhNJqfI4%252FDR3NLa%252FvdbnZRv1%252BUbnRaM%252F8tjuckNhuSSoUAINXJoFkWKAJqixIQhoqVqPNDNdwiFtXYnGqKaLzXAcym491oWE3oWzzud9XbRRlRqfY8o5S3zucqF32%252BpdGuLPLS571pBACZqWghZNDWK7ymsdpQmaypgLNNCbNNBJvom2lPQqMsNvyKDiMWtBs7xBZPinhuwz8%252F%252F%252FrJ8QoSI2tQmycISmNmIBzDRBXW72ahAqVhClwLcjndh7m3AfRHajnhO%252FK9udGtr%252B7cxdNYqQhaXziGK7pes9HqEyJXBAjrXAWawoKxQvXn0xS4aciFPGG8p6FZo%252F%252B1fNZxEyKkBiKVhwFbhEp%252ByQ6nFYkjMr3znRxGtbdtiyjdUPcrWGc0xW3UybMClGvFgiYqG8ejej5fzRoeKlXx%252F8W3v1k0eaVOPq85%252BdzFr7qeAZoCoT%252F5lvQFc6nBezu41nsPoljkVrN%252FnGrdeev7yA%252BU9unZAFK1CtXUPHblMHcY9oMpSsYc1lTg1BwU7EvDgcKQk3MAYsZXfxJ%252F8W9VkcfZf2vks%252FULahRNdMqIRqjxQrX%252Fd1RqOgWaxXGkaPwIlK1kKJNqEYTmmwAnw76qpyNo7M2KeTbkbuDW7TWxO8AixAw6LkOZivlpjaxsun93ML0LRFmPDan4LsGEoFMMmMdfvEs8FynndzRZIPeIqGGjUzTMuUb6BhTP538mbOQvybf%252BnG%252FQX5TInmB26aMXtCMONAVsaHm0WLMdkHybm8%252BuR46Z47gwsA5enh96CcELzgd%252B0NpOEi3Dnky3191UZTkVPShvwYWscWtn6IysddyCeFQLJzZBGn8zYS38Dslae8qpW%252B7HgQRWl%252FuGnS8ZWdZA%252BcdPjsnhrS78HloZRdM9y13XVDzr%252Bx9T4eBkUqLS%252FdibP1%252Fr4gqg%252BT6078oMhR0ExdB%252Bz7Vc6miY%252FZKOjV%252BB9fOQ1%252FPAQAAA%253D%253D',
    '_gat_hotmartClub': '1',
}












headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://player.hotmart.com/',
    'Origin': 'https://player.hotmart.com',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}



def formatInputFile():
    #Create temp file
    file_path = 'files/720.m3u8'
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if(line.rstrip().startswith('#EXT-X-KEY')):
                    newLine = line.rstrip().split('IV=')
                    newUrl = '#EXT-X-KEY:METHOD=AES-128,URI="720.key",IV='+newLine[1]
                    new_file.write(line.replace(line.rstrip(),newUrl))
                    continue
                if(line.rstrip().endswith('.ts')):
                    newLine = line.rstrip().split('segment-')
                    new_file.write(line.replace(line.rstrip(), 'tmp/'+newLine[1]))
                    allFiles['files'].append(line.rstrip())
                else:
                    new_file.write(line)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
    # print("[INFO] File formated and dict was create.") 



def downloadInputFile():
    response = requests.get(allFiles['m3u8'], headers=headers,allow_redirects=True,cookies=cookies)
    if(response.status_code == 200):
        with open('files/720.m3u8','wb') as  handle:
            handle.write(response.content) 
        print("[INFO] 720.m3u8 file is done.")
def downloadKeyFile():
    response = requests.get(allFiles['key'], headers=headers,allow_redirects=True,cookies=cookies)
    if(response.status_code == 200):
        with open('files/720.key','wb') as  handle:
            handle.write(response.content) 
        print("[INFO] 720.key file was create!")

def downloadFilesFromInput():
    print("[INFO] Downloading files...") 
    for i in range(len(allFiles['files'])):
            response = requests.get(allFiles['files'][i], headers=headers,allow_redirects=True,cookies=cookies)
            with open('files/tmp/'+str(i)+'.ts','wb') as  handle:
                handle.write(response.content)
                print("[INFO] file "+str(i)+ "/"+str(len(allFiles['files'])-1)+" was create") 
   


def readMyJSON():
    with open('all.json') as json_file:
        data = json.load(json_file)
        for ind in data['pages']:
            aulas.append(ind['firstMediaCode'])
def main():
    
    try:
         os.makedirs('files/tmp')
    except :
        pass
    downloadInputFile()
    downloadKeyFile()
    formatInputFile()
    downloadFilesFromInput()
    os.popen('ffmpeg -allowed_extensions ALL -i "files/720.m3u8" -c copy -bsf:a aac_adtstoasc "Final.mp4"').read()
    shutil.rmtree('files/', ignore_errors=True)
main()


