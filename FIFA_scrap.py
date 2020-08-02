import pandas as pd
import requests
from itertools import chain
import requests
from bs4 import BeautifulSoup

def scrap_fifa(year):

    global l2
    global i
    
    l = []
    l2 = []
    i=1
    year = str(year)
    
    while i>=1:
#    for i in range(1,65):

        # Using beautifulsoup to get the date:

        request = requests.get('https://sofifa.com/teams?type=club&lg%5B0%5D=16&lg%5B1%5D=19&lg%5B2%5D=31&lg%5B3%5D=53&showCol%5B0%5D=ti&showCol%5B1%5D=oa&showCol%5B2%5D=at&showCol%5B3%5D=md&showCol%5B4%5D=df&showCol%5B5%5D=tb&showCol%5B6%5D=bs&showCol%5B7%5D=bd&showCol%5B8%5D=bp&showCol%5B9%5D=bps&showCol%5B10%5D=cc&showCol%5B11%5D=cp&showCol%5B12%5D=cs&showCol%5B13%5D=cps&showCol%5B14%5D=da&showCol%5B15%5D=dm&showCol%5B16%5D=dw&showCol%5B17%5D=dd&showCol%5B18%5D=dp&showCol%5B19%5D=ip&showCol%5B20%5D=ps&showCol%5B21%5D=sa&showCol%5B22%5D=ta&r=' + year + '00' + '%02d' % i + '&set=true')
        content_web = request.content
        soup = BeautifulSoup(content_web, 'lxml')
        line_date = soup.find_all('title')
        date = str(line_date)
        print(date)
        
        l2.append(date) 
#        print('appended')

        # Exploring the web with requests for getting the data. There are 2 pages:    

        name_r1 = ('https://sofifa.com/teams?type=club&lg%5B0%5D=16&lg%5B1%5D=19&lg%5B2%5D=31&lg%5B3%5D=53&showCol%5B0%5D=ti&showCol%5B1%5D=oa&showCol%5B2%5D=at&showCol%5B3%5D=md&showCol%5B4%5D=df&showCol%5B5%5D=tb&showCol%5B6%5D=bs&showCol%5B7%5D=bd&showCol%5B8%5D=bp&showCol%5B9%5D=bps&showCol%5B10%5D=cc&showCol%5B11%5D=cp&showCol%5B12%5D=cs&showCol%5B13%5D=cps&showCol%5B14%5D=da&showCol%5B15%5D=dm&showCol%5B16%5D=dw&showCol%5B17%5D=dd&showCol%5B18%5D=dp&showCol%5B19%5D=ip&showCol%5B20%5D=ps&showCol%5B21%5D=sa&showCol%5B22%5D=ta&r='+ year + '00'+'%02d' % i+'&set=true')
        name_r2 = ('https://sofifa.com/teams?type=club&lg%5B0%5D=16&lg%5B1%5D=19&lg%5B2%5D=31&lg%5B3%5D=53&showCol%5B0%5D=ti&showCol%5B1%5D=oa&showCol%5B2%5D=at&showCol%5B3%5D=md&showCol%5B4%5D=df&showCol%5B5%5D=tb&showCol%5B6%5D=bs&showCol%5B7%5D=bd&showCol%5B8%5D=bp&showCol%5B9%5D=bps&showCol%5B10%5D=cc&showCol%5B11%5D=cp&showCol%5B12%5D=cs&showCol%5B13%5D=cps&showCol%5B14%5D=da&showCol%5B15%5D=dm&showCol%5B16%5D=dw&showCol%5B17%5D=dd&showCol%5B18%5D=dp&showCol%5B19%5D=ip&showCol%5B20%5D=ps&showCol%5B21%5D=sa&showCol%5B22%5D=ta&r='+ year + '00'+'%02d' % i+'01&set=true&offset=60')

        r1 = requests.get(name_r1)
        r2 = requests.get(name_r2)

        if (l2[i-1] != l2[i-2]) or i<4 or i==48:

            l.append(pd.read_html(r1.content))
            l.append(pd.read_html(r2.content))
            print('appended')    
        
        else:    
            del l2[-1]
            return(pd.concat(chain.from_iterable(l)))
        
        i=i+1
        
def add_fifa_date(data_frame):
    
    data_frame['Date']=0
    
    for j in range(0,len(data_frame),int((len(data_frame)+1)/(i-1))):
        data_frame.iloc[j:j+int(len(data_frame)/len(l2)),-1]=l2[int((j)/int(len(data_frame)/len(l2)))]

    data_frame['Fifa_version']=data_frame['Date'].str[13:21]
    data_frame['Date'] = data_frame['Date'].str[21:34]
    
    return()