def price_fetcher(company ,url, postalcode, count ,browser):    
    from collections import OrderedDict
    from urllib.parse import urlencode
    import requests
    
    if(company == 'lämpöpuisto'):
        params = urlencode(dict({'product': 501150, 'postalcode':postalcode,'count':count, 'campaign':''}))
        r=requests.get(url, params)
        data = r.json()
        print(data['offer']['total'].replace(" ", "").replace(",","."))
    if(company=='st1'):
        params = urlencode(dict({'service':'payments', 'postal-code':postalcode,'amount':count,'product-id': 115412, 'campaign':'','format':'json', 'type':'kuluttaja'}))
        r=requests.get(url, params)
        data = r.json()
        print(data["data"]["payments"]["payment_1"]["total_price"])
    if(company== 'hankkia'):
        parameters = {'method':'laskeRahtiKauko', 'ttid':6422, 'maara':count, 'postinumero':postalcode}
        r = requests.post(url, data=parameters)
        a=r.json()['HINTYHTEENSAALV']
        print(float(a.replace('\xa0', '').replace(",",".")))
    if(company=='teboil'):
        parameters = {'Y128':'005400', 'Y129':300000, 'Y114':'00100', 'Y169':1, 'Y193':'', 'Y999':'COU'}
        session=requests.Session()
        req=session.get(url)
        link = req.text.split("href='")[1].split("\n")[0][:-1]
        url1=session.get(link)
        value = re.findall('href=(.*?)">', url1.text) 
        url2= value[0][1:-1]+'/'
        respo=session.get(url2,params=parameters)
        final= session.post(respo.text.split("href='")[1].split('?')[0],data=parameters)
        textVal = final.text.split('Yhteensä')[1].replace(" ", "").replace(":&nbsp;","" ).split('euroa')[0]
        print(textVal)
