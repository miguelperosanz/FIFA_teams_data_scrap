def scrap_fifa(year):
    
    import pandas as pd
    import requests
    from itertools import chain
    import requests
    from bs4 import BeautifulSoup
    import numpy as np

    l= []
    l2= []

    # NUMBER OF UPDATES EVERY YEAR:
    
    if year == 13:
        times = 34
    
    if year == 14:
        times = 52
    
    if year == 15:
        times = 59
    
    if year == 16:
        times = 58
    
    if year == 17:
        times = 99
    
    if year == 18:
        times = 84
    
    if year == 19:
        times = 75
    
    if year == 20:
        times = 61
    
    
    for i in range(1,times+1):
        
        #TAKE THE DATE & FIFA VERSION
        
        year = str(year)    
        request = requests.get('https://sofifa.com/teams?type=club&lg%5B0%5D=16&lg%5B1%5D=19&lg%5B2%5D=31&lg%5B3%5D=53&lg%5B4%5D=13&r=' + year + '00' + '%02d' % i + '&set=true&showCol%5B0%5D=ti&showCol%5B1%5D=oa&showCol%5B2%5D=at&showCol%5B3%5D=md&showCol%5B4%5D=df&showCol%5B5%5D=tb&showCol%5B6%5D=bs&showCol%5B7%5D=bd&showCol%5B8%5D=bp&showCol%5B9%5D=bps&showCol%5B10%5D=cc&showCol%5B11%5D=cp&showCol%5B12%5D=cs&showCol%5B13%5D=cps&showCol%5B14%5D=da&showCol%5B15%5D=dm&showCol%5B16%5D=dw&showCol%5B17%5D=dd&showCol%5B18%5D=dp&showCol%5B19%5D=ip&showCol%5B20%5D=ps&showCol%5B21%5D=sa&showCol%5B22%5D=ta')
        content_web = request.content
        soup = BeautifulSoup(content_web, 'lxml')
        line_date = soup.find_all('title')
        date = str(line_date)

        # TAKE THE LINK
        
        name_r1 = 'https://sofifa.com/teams?type=club&lg%5B0%5D=16&lg%5B1%5D=19&lg%5B2%5D=31&lg%5B3%5D=53&lg%5B4%5D=13&r=' + year + '00' + '%02d' % i + '&set=true&showCol%5B0%5D=ti&showCol%5B1%5D=oa&showCol%5B2%5D=at&showCol%5B3%5D=md&showCol%5B4%5D=df&showCol%5B5%5D=tb&showCol%5B6%5D=bs&showCol%5B7%5D=bd&showCol%5B8%5D=bp&showCol%5B9%5D=bps&showCol%5B10%5D=cc&showCol%5B11%5D=cp&showCol%5B12%5D=cs&showCol%5B13%5D=cps&showCol%5B14%5D=da&showCol%5B15%5D=dm&showCol%5B16%5D=dw&showCol%5B17%5D=dd&showCol%5B18%5D=dp&showCol%5B19%5D=ip&showCol%5B20%5D=ps&showCol%5B21%5D=sa&showCol%5B22%5D=ta'
        name_r2 = 'https://sofifa.com/teams?type=club&lg%5B0%5D=16&lg%5B1%5D=19&lg%5B2%5D=31&lg%5B3%5D=53&lg%5B4%5D=13&r=' + year + '00' + '%02d' % i + '&set=true&showCol%5B0%5D=ti&showCol%5B1%5D=oa&showCol%5B2%5D=at&showCol%5B3%5D=md&showCol%5B4%5D=df&showCol%5B5%5D=tb&showCol%5B6%5D=bs&showCol%5B7%5D=bd&showCol%5B8%5D=bp&showCol%5B9%5D=bps&showCol%5B10%5D=cc&showCol%5B11%5D=cp&showCol%5B12%5D=cs&showCol%5B13%5D=cps&showCol%5B14%5D=da&showCol%5B15%5D=dm&showCol%5B16%5D=dw&showCol%5B17%5D=dd&showCol%5B18%5D=dp&showCol%5B19%5D=ip&showCol%5B20%5D=ps&showCol%5B21%5D=sa&showCol%5B22%5D=ta&offset=60'
    
        r1 = requests.get(name_r1)
        r2 = requests.get(name_r2)
        
        
        l2.append(date)
        l.append(pd.read_html(r1.content))
        l.append(pd.read_html(r2.content))
        print('appended ',date)    
        
    # CONCATENATE THE DIFERENT UPDATES AND EXTEND DATE LIST SO THAT THE DIMENSIONS FIT TOGETHER
    
    df= pd.concat(chain.from_iterable(l))
    l3 = np.repeat(l2,len(df)/(times))
    
    # ADD THE LIST WITH THE DATES & FIFA VERSION TO THE DATABASE
    
    df['Date']=l3

    # SOME FEATURE WORK: 
    
    cols = list(df.columns)
    cols = [cols[-1]] + cols[:-1]
    df = df[cols]
    df = df.drop(['Unnamed: 0'], axis=1)
        
    
    return(df)


