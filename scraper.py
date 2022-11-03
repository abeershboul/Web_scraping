

import requests
from bs4 import BeautifulSoup
import json

def get_citations_needed_count():
      '''
        A function takes in a url string and returns an the number of citations needed  int

      '''
      URL='https://en.wikipedia.org/wiki/History_of_Mexico'
      page=requests.get(URL)
      soup=BeautifulSoup(page.content,'html.parser')
      #print(soup)
      all=soup.find_all('sup',class_="noprint Inline-Template Template-Fact")
      #print(all)
      count =0
      for post in all:
        citation=post.find_all('a',title="Wikipedia:Citation needed")
        count+=1

      print(count)
      return count

def get_citations_needed_report():
    '''
     Returns a formatted string with each citation needed in separete lines, in the order found
    '''

     
    URL='https://en.wikipedia.org/wiki/History_of_Mexico'
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    #print(soup)
    all=soup.find_all('p')
    results=""
    
    for p in all:
        if p.find('a', title = 'Wikipedia:Citation needed'):
            
            results+=p.text.strip()
            results+='\n'
    print(results) 
    return results        
    
def add_file(results):     
    json_data=json.dumps(results)
    with open('citations_needed.json','w') as file:
        for par in results:
            file.write('["')
            file.write(par)
            file.write('"]')
          

     
    
get_citations_needed_count()
print('---------------------------------------------')
get_citations_needed_report()
result=get_citations_needed_report()
add_file(result)

