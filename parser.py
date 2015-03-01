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
def norm(str):
     return str.lstrip(chr(0xD)).lstrip('\n').lstrip(' ').rstrip(' ').rstrip('\n')
def main():
    if len(sys.argv)<=1:
       print ("getfromint: нехватает параметров\nИспользование: parser URL обьявления")
       sys.exit(2)
    page=get_page(sys.argv[1])
    titlepath = ".//*[@id='item']/div[4]/div[1]/div[2]/h1/text()"
    pricepath=".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/span/span/text()"
    pricepath2= ".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/span/span/text()"
    sellertypepath=".//*[@id='i_contact']/div[1]/div/text()"
    roomspath=".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/a[1]/text()"
    roomspath2=".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]/text()"    
    citytypepath=".//*[@id='i_contact']/div[5]/div[1]/text()"
    citypath=".//*[@id='map']/span/text()"
    streetpath=".//*[@id='toggle_map']/span/text()"
    housetypepath=".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/a[2]/text()"
    housetypepath2=".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a[2]/text()"
    descr1path=".//*[@id='item']/div[4]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/text()[2]"
    descr2path=".//*[@id='desc_text']/p/text()"
    numberpath=".//*[@id='item_id']/text()"
    doc = html.document_fromstring(page)
    if len(doc.xpath(roomspath))>0:
       rooms = norm(doc.xpath(roomspath)[0])
    else:
       rooms = norm(doc.xpath(roomspath2)[0])
    
    title=norm(doc.xpath(titlepath)[0])
    ts=title.split(',')
    square=norm(ts[1])
    floor=norm(ts[2])
    sellertype=norm(doc.xpath(sellertypepath)[0])
    sellernamepath=".//*[@id='seller']/strong/text()"
    if len (doc.xpath(pricepath))>0:
       price=norm(doc.xpath(pricepath)[0])
    else:
       price=norm(doc.xpath(pricepath2)[0])
    citytype=norm(doc.xpath(citytypepath)[0])
    city=norm(doc.xpath(citypath)[0])
    street=norm(doc.xpath(streetpath)[0])
    if len(doc.xpath(housetypepath))>0:
        housetype=norm(doc.xpath(housetypepath)[0])
    else:
        housetype=norm(doc.xpath(housetypepath2)[0])
    descr2=norm(doc.xpath(descr2path)[0])
    number=norm(doc.xpath(numberpath)[0])
    root=etree.Element('advertisement')
    sellername=norm(doc.xpath(sellernamepath)[0])
    sb=etree.SubElement(root,'id')
    sb.text=number
    sb=etree.SubElement(root,'title')
    sb.text=title
    sb=etree.SubElement(root,'seller')
    sb2=etree.SubElement(sb,'type')
    sb2.text=sellertype
    sb2=etree.SubElement(sb,'name')
    sb2.text=sellername
    sb=etree.SubElement(root,'address')
    sb2=etree.SubElement(sb,'citytype')
    sb2.text=citytype
    sb2=etree.SubElement(sb,'name')
    sb2.text=city
    sb2=etree.SubElement(sb,'street')
    sb2.text=street
    sb=etree.SubElement(root,'description')
    sb2=etree.SubElement(sb,'rooms')
    sb2.text=rooms
    sb2=etree.SubElement(sb,'housetype')
    sb2.text=housetype
    sb2=etree.SubElement(sb,'square')
    sb2.text=square
    sb2=etree.SubElement(sb,'floor')
    sb2.text=floor
    sb2=etree.SubElement(sb,'text')
    sb2.text=descr2
    sb=etree.SubElement(root,'price')
    sb.text=price
    print etree.tostring(root, pretty_print=True, encoding="UTF-8", xml_declaration=True)
    #Работает
    #print title[0]
    #print rooms[0]
    #print "тип ",sellertype[0]
    #print price[0]

if __name__ == "__main__":
    main()
