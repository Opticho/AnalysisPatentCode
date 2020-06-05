import requests as rq
from bs4 import BeautifulSoup as bs
import os
import sys
import time
from datetime import date, timedelta
import math
import argparse
from PyPDF2 import PdfFileMerger

#default setting
path = os.getcwd()
file_path = os.path.join(path, "patent_search")
pdf_path = os.path.join(path, "patent_pdf")
if os.path.exists(file_path) == False:
    os.makedirs(file_path)
if os.path.exists(pdf_path) == False:
    os.makedirs(pdf_path)
mode = 'a'
    
def process_parser():
    parser = argparse.ArgumentParser(description= 'Processing Search Patent')
    parser.add_argument("-i", type = str, default = "", help = "search, compare, merge, download")
    parser.add_argument("-q", type = str, default = 'TTL/(Ultrasonic OR Ultrasound OR Megasound OR Megasonic OR acoustic) AND TTL/(cover OR cap OR case OR covering OR mantle OR hood OR sheet OR shutter OR vinyl OR cowl OR lid OR mulch OR seal)', help = "search query(only use test mode)")
    parser.add_argument("--file_path","-fp", type = str, default = file_path, help = "change txt save path")
    parser.add_argument("--pdf_path","-pp", type = str, default = pdf_path, help = "change pdf save path")
    args = parser.parse_args()
    return (args.i, args.q, args.file_path, args.pdf_path)

def make_url(page, query):
    command = ['TTL', 'OR', 'AND']
    cal_list = query.replace('TTL/(',')').split(')')
    count = []
    for i in range(1, len(cal_list), 2):
        count.append(cal_list[i].count(command[1]) + cal_list[i].count(command[2]))
    qs = query.replace("/", " ").split(" ")
    p_query = ""
    p_querys = ""
    p_count = 0
    for q in qs:
        if command[0] in q:
            TitlePart = ".TI."
            continue
        if (command[1] in q) or (command[2] in q):
            p_query += q + "+"
            continue
        if ("(" in q):
            if not p_querys == "":
                p_querys += p_query
                p_query = ""
            p_query += q + "+"
            if (")" in q):
                p_querys += p_query
                p_query = ""
            continue
        if (")" in q):
            p_query += q + TitlePart + "+"
            p_querys += "("*(count[p_count]-1) + p_query
            p_query = ""
            p_count+=1
            continue
        p_query += q + ")" + "+"  

    p_querys = "("+ p_querys.strip("+") +")"
    if page == "1":
        print("Send query: ", p_querys)
    print("Page: " + page)
    url01 = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&p='+page+'&f=S&l=50&d=PTXT'
    url02 ='&S1=' + p_querys
    url03 = '&Page=Next'
    print(url01 + url02 + url03)
    return url01 + url02 + url03
    
def get_soup(p, q):
    p = str(p)
    web = rq.get(make_url(p, q))
    soup = bs(web.content, "html.parser")
    return soup

def write_file(l, listMax):
    now =time.gmtime(time.time())
    file_name = str(now.tm_year) + "_" + str(now.tm_mon)+ "_" + str(now.tm_mday) + "_" + str(listMax) + ".txt"
    
    with open(os.path.join(file_path,file_name), mode) as f:
        for i, text in enumerate(l):
            #print(text.string.replace("\n","").replace("     "," "))
            f.write(text.string.replace("\n","").replace("     "," ")+" ")
            if i%3 ==2:
                f.write("\n")
        
def drink_soup(i, q):    
    print("NOTIFY: It takes a time...")
    soup=get_soup(i, q)
    
    try:
        l=soup.find_all('td',{'valign': 'top'})
        listMax = int(soup.find('input',{'name':'TD'}).get('value'))
        pageMax = math.ceil(listMax/50)
    except:
        print("Error Occured, It might be the patent exists.")
        sys.exit()
    
    print("Max list number: "+str(listMax))
    print("Max page number: "+str(pageMax))
    
    write_file(l, listMax)
    
    if i == 1:
        return pageMax

def test():
    print("test def")
    print(file_path)
    print(pdf_path)
            
def download_pdf():
    file_name = get_txt_name(date.today())
    
    with open(os.path.join(file_path,file_name), "r") as f:
        data = f.read()
    data_split= data.split("\n")
    data_split2= []
    for sample in data_split:
        data_split2.append(sample.rstrip(" ").split(" "))
    #마지막 값은 "" 이므로 삭제
    del data_split2[-1]
    
    for i in range(len(data_split2)):
        temp =data_split2[i][1].replace(',','')
        first = temp[-2:]
        second = temp[-5:-2]
        third = temp[0:-5].zfill(3)
        if temp[0].isalpha():
            third = temp[0] + '0' + temp[1:-5]

        if os.path.exists(os.path.join(pdf_path, temp + ".pdf")):
            print("중복된 문서가 존재합니다. iter: "+ str(i+1)+"/"+str(len(data_split2)) +" Patent Nember: " + temp)
            continue

        url = 'https://pdfpiw.uspto.gov/' + first + '/' + second + '/' + third + '/1.pdf'

        with open(os.path.join(pdf_path, temp + ".pdf"), "wb") as f:
            rqs = rq.get(url)
            f.write(rqs.content)
        print("complete, iter: "+ str(i+1) + "/" + str(len(data_split2)) + " Patent Number: " + temp)

def find_name(file_list, name_piece):
    file_name = "empty"
    for i,name in enumerate(file_list):
        if name.find(name_piece) != -1:
            file_name = file_list[i]
    return file_name

def get_txt_name(date_var):
    name_piece = date_var.strftime('%Y_%#m_%#d_')
    file_list = os.listdir(file_path)
    file_name = find_name(file_list, name_piece)
    if os.path.exists(os.path.join(file_path,file_name)) == True: 
        print("already txt file exists: ", file_name)
    return file_name

def read_compare():
    file_name=get_txt_name(date.today())
    ex_file_name=get_txt_name(date.today() - timedelta(1))
    
    with open(os.path.join(file_path,file_name), "r") as f:
        data = f.read()
    with open(os.path.join(file_path,ex_file_name), "r") as f:
        ex_data = f.read()

    if sys.getsizeof(data) == sys.getsizeof(ex_data):
        print("No change")
    else:
        print("download pdf")
        download_pdf()
    
def merge_pdf():
    pdf_list = os.listdir(pdf_path)
    pdf_list.sort(key= len)
    merger = PdfFileMerger()
    
    try:
        for i,pdf in enumerate(pdf_list):
            #print(i)
            merger.append(os.path.join(pdf_path,pdf))
    except:
        print("Error, some PDF files are broken")
    
    if os.path.exists(os.path.join(pdf_path,"merge.pdf")) == False:
        merger.write(os.path.join(pdf_path,"merge.pdf"))
        merger.close()
    else:
        print("already exist")
    
def main():
    x, q, p, pp = process_parser()
    global file_path 
    global pdf_path
    file_path = p
    pdf_path = pp
    
    if x == "search":
        file_name=get_txt_name(date.today())
        if os.path.exists(os.path.join(file_path, file_name)) == False:
            pageMax = drink_soup(1, q)
            [drink_soup(i, q) for i in range(2,pageMax+1)]
        else:
            print("already text exists")
    elif x == "test":    
        print("No query find") if q == "" else test() 
    elif x == "compare":
        read_compare()
    elif x == "merge":
        merge_pdf()
    elif x == "download":
        download_pdf()
    else:
        print("exit message: python uspto_search.py -h to find keyword")
    
    print("process end")
              
if __name__ == "__main__":
    main()
    