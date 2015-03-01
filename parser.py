#!/usr/bin/python
#coding: utf8
import requests
from lxml import html
from lxml import etree
import sys
def get_page(url):
    page=None
    r=requests.get(url)
    if r.status_code==200:
        page=r.text
    return page
def main():
    if len(sys.argv)<=1:
       print ("getfromint: нехватает параметров\nИспользование: parser URL обьявления")
       sys.exit(2)
    page=get_page(sys.argv[1])
    titlepath = ".//*[@id='item']/div[4]/div[1]/div[2]/h1/text()"
    pricepath=".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/span/span/text()"
    sellertypepath=".//*[@id='i_contact']/div[1]/div/text()"
    roomspath=".//*[@id='item']/div[4]/div[1]/div[2]/div[1]/div[2]/a[5]/text()"
    doc = html.document_fromstring(page)
    rooms = doc.xpath(roomspath)
    title=doc.xpath(titlepath)
    sellertype=doc.xpath(sellertypepath)[0].lstrip(chr(0xD)).lstrip('\n').lstrip(' ').rstrip(' ')
    #print doc.xpath(sellertypepath)
    sellernamepath=".//*[@id='seller']/strong/text()"
    price=doc.xpath(pricepath)
    root=etree.Element('advertisement')
    sellername=doc.xpath(sellernamepath)[0].lstrip(chr(0xD)).lstrip('\n').lstrip(' ').rstrip(' ')
    sb=etree.SubElement(root,'title')
    sb.text=title[0]
    sb=etree.SubElement(root,'seller')
    sb2=etree.SubElement(sb,'type')
    sb2.text=sellertype
    sb2=etree.SubElement(sb,'name')
    sb2.text=sellername
    print etree.tostring(root, pretty_print=True, encoding="UTF-8", xml_declaration=True)
    #print title[0]
    #print rooms[0]
    #print "тип ",sellertype[0]
    #print price[0]

if __name__ == "__main__":
    main()
