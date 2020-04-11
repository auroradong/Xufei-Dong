import requests
from lxml import etree
import urllib
from urllib import request
from urllib.request import urlopen
import time
import urllib.error
import http.client
import dns.resolver
import csv
import socket


#for one site find 20pages

for i in range(20):
    page_num = i * 10
    url = 'https://www.google.com/search?q=filetype:pdf+site:sz&start='+ str(page_num)
    
    #headers={
    #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    #}

    html = requests.get(url)
    # print(html.text)
    page = html.content
    with open('D:\\Sublime Text 3/test111.html','wb') as f:
        f.write(page)
    #print(html.text)
    etree_html = etree.HTML(html.text)
    #a = etree_html.xpath('//*[@id="mainContent"]/div/div/div[2]/a/@href')
    a = etree_html.xpath('//*[@id="main"]/div/div/div[1]/a/@href')
    #print(a)
   
    for j in a:
        pureurl=j[7:j.find('&sa=')]
        f=open("D:\\Sublime Text 3/urls2.csv",'a')
        f.write(pureurl+'\n')



# Calculate throughut
class IpAddrConverter(object):

    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    @staticmethod
    def _get_bin(target):
        if not target.isdigit():
            raise Exception('bad ip address')
        target = int(target)
        assert target < 256, 'bad ip address'
        res = ''
        temp = target
        for t in range(8):
            a, b = divmod(temp, 2)
            temp = a
            res += str(b)
            if temp == 0:
                res += '0' * (7 - t)
                break
        return res[::-1]

    def to_32_bin(self):
        temp_list = self.ip_addr.split('.')
        assert len(temp_list) == 4, 'bad ip address'
        return ''.join(list(map(self._get_bin, temp_list)))



lists=[]

pathh='D:\\Sublime Text 3/urls2.csv'
with open(pathh,'r',newline='',encoding='utf-8') as f:
    readers = csv.reader(f)
    for row in readers:
        listss=row[0]
        lists.append(listss)

l1 = [] 
l2 = [] 

for i in range(7222,len(lists)):
    pathpdf = str(lists[i])

    #pathpdf= 'https://www.maid2clean.co.uk/privacy-notice.pdf'

    #pathtopp = 'www.maid2clean.co.uk'
    
    # Converts to the name of the host system 
    pathopp=pathpdf.split('/')[2]

    # Remove duplicate host systems
    l1.append(pathopp)  
    for j in l1: 
        if not j in l2: 
            l2.append(j)
            try:
                # Returns the IP address of the host
                ipadd = socket.gethostbyname(pathopp)

                # Header
                headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
                }

                try:
                    
                    req=urllib.request.Request(pathpdf, headers=headers)
                    t1=time.time()
                    response=urllib.request.urlopen(req)
                    t2=time.time()

                    #print(response.read().decode(“utf-8”))
                    lenth_content = len(response.read())

                    delta_time=t2-t1
                    throughput=lenth_content/delta_time
                    throughput_MB=throughput/1000000
                    throughput_MB_clear='%.3f'%throughput_MB  #取三位小数

                    print('throughput',i,':',throughput_MB_clear,"MB/s")
                  
                except urllib.error.URLError as e:
                    if  isinstance(e.reason, socket.timeout):
                            print('Time out!')
               
                #avoid slow start
                #According to RFC 5681, an SMSS of 1460 bytes would give us an initial CWND of 4380 bytes (3 * 1460 = 4380)
                if lenth_content > 4380 : 
                    
                    #path for dataset
                    pathd='D:\Sublime Text 3\dataset2.csv'
                    #convert to 32 bit vector
                    ip = IpAddrConverter(ipadd)
                    ip_32bin=ip.to_32_bin()
                    
                    with open(pathd,'a',newline='',encoding='utf-8') as f:
                        writers = csv.writer(f)
                        writers.writerow([ip_32bin,throughput_MB_clear])
                else:
                    pass

            except socket.gaierror:
                print(' getaddrinfo failed')

        else:
            pass

