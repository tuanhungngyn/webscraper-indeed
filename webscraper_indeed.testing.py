#%%
from bs4 import BeautifulSoup
import requests

url = "https://de.indeed.com/jobs?q=Werkstudent+Informatik&l=Hamburg&from=searchOnHP&from=gnav-util-jobsearch--indeedmobile&vjk=e59883e9ec1e8542&advn=6013269550973348"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
# %%
cookies = {
    'gonetap': 'closed',
    'CSRF': '6sJ9kJknxSUuw0RBzwHSelmlOa67Ohnf',
    'CTK': '1hpivcitgj3se9ce',
    'LV': '"LA=1712778438:LV=1712689589:CV=1712778438:TS=1712452375"',
    'indeed_rcc': '"LOCALE:PREF:LV:CTK:CO:RQ"',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Apr+10+2024+22%3A56%3A16+GMT%2B0200+(Central+European+Summer+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=78a7a7a7-84c0-4dcd-a088-8ad1ebda1a73&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&AwaitingReconsent=false&geolocation=%3B',
    '__cf_bm': 'DlxBLMeuqSi1MfFI11OX2KuwXmkg2KYDcK_8zKzC1II-1712782375-1.0.1.1-W345FKQmyg7QeuqAsGRhyH1CYuBxg370VgNK8Bzz9xnBska1dRU8_FXUihA065.MPStiMJnLrNSLf1C.orkhWw',
    'RSJC': 'e59883e9ec1e8542:9932c6727f68c194:9347191c42cc2b81:27e5cddd49ba95b8:fb0b6d1feef77ba0:3a7780727a340f69:8934f590f2890fb7:7ee86e810e94ee12:3dd101c074485cd8:831e510e495dcc0f',
    'JSESSIONID': '92181A04BD19FEEC4736AD065D07BE9D',
    'MICRO_CONTENT_CSRF_TOKEN': 'oXqH3CRNhVpuICf2hjthpMarEkonmEkB',
    'PPID': '""',
    '_gcl_au': '1.1.1299872408.1712452924',
    'SURF': 'M3og5WkTNyBTgPhahol4qKpyrovBCzOu',
    'RQ': '"q=Werkstudent+Informatik&l=Hamburg&ts=1712778473247&pts=1712690538311:q=&l=Hamburg&ts=1712690147075"',
    'ENC_CSRF': 'vsrUv4sa3Ncw4lhL5keWYiBO1NSf1Owj',
    'INDEED_CSRF_TOKEN': 'bFcugaLIReUJz1PlbFAbkinacOm6AwrJ',
    'FPID': 'FPID2.2.Xtzy7PJC7rRO8uWhRSueWAsW9aZb7CVV%2Bxy5JEHMnOY%3D.1712769836',
    '_ga_LYNT3BTHPG': 'GS1.1.1712778421.1.1.1712778435.0.0.1757698566',
    'FPLC': 'J%2FoWedfXIXPYIGY1LDDzzUfoHZFMt4MwmZRUqyXf6%2F7WuMDEEiNOJ5VLW2OJ9Cm4EToxodaeAo2RI7UDOPrFSJAqTUwVSooo65Y1rI2jyh2KQ14wrHR3hIB%2FfdBpgg%3D%3D',
    '_ga': 'GA1.1.244207666.1712769836',
    '_cfuvid': 'RIgW.o9AOZYalml1t4xXlCIqbXXhkGPByaGrpDT5WI4-1712778419189-0.0.1.1-604800000',
    '_gid': 'GA1.2.882866618.1712769836',
    'RF': '"1E1vkYxpXEly2hL58AFT3SJBhatMDFIVrJvpM83f2DUwYxVgn0ETaUQGwUtQFjuiYkw1w0jW7_A="',
    'ROJC': '01bb637f55cb1a62:dc421b6128b2cedb:9dfb563b2b178817:e70127db95166fda:dad54c7c5080f306:05785f26ad66b9ef:be1b49014682e149:2b89edff9c4f20ae:7a3faf7280403669:bc535dd96582b181',
    'IA_APPLIED': 'dad54c7c5080f306',
    'RJAS': 'v40d2ac72c4bee66b:vd0e9dcfc2b2fc6c5:vc67d2e7b6d73740d:i52ce252320823bfb:ia6e97d4634fb1e6b:v1572df296595cbbc:i724f787b2a234fe7:idad54c7c5080f306',
    'LOCALE': 'de',
    'LC': '"co=DE&hl=de_DE"',
    'PREF': '"TM=1712452922604:L=Hamburg"',
    'OptanonAlertBoxClosed': '2024-04-07T01:22:38.710Z',
    'CO': 'DE',
    'LOCALE': 'de_DE',
    'CO': 'DE',
    'SHARED_INDEED_CSRF_TOKEN': 'bFcugaLIReUJz1PlbFAbkinacOm6AwrJ',
    'indeed_rcc': 'CTK',
}

headers = {
    'Host': 'de.indeed.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
}

params = {
    'q': 'Werkstudent Informatik',
    'l': 'Hamburg',
    # 'from': [
    #     'searchOnHP',
    #     'gnav-util-jobsearch--indeedmobile',
    # ],
    # 'vjk': 'e59883e9ec1e8542',
    # 'advn': '6013269550973348',
}

response = requests.get(url, headers=headers, cookies=cookies)
# %%
response.text
# %%
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
# %%
import requests

cookies = {
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Apr+10+2024+23%3A16%3A43+GMT%2B0200+(Central+European+Summer+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=30c883db-ea81-4eaa-8300-6d2e74226012&interactionCount=1&landingPath=https%3A%2F%2Fde.indeed.com%2F%3Fr%3Dus&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0',
    'PTK': 'tk=1hr4tsvckjklr801&type=jobsearch&subtype=topsearch',
    'ac': 'nUo+4Pd/Ee6fvs/wnSGnPw#m8sY8Pd/Ee6fvs/wnSGnPw',
    'CSRF': '4D3RFTcRaOMRwj7VrmezAy5qRlUnloFQ',
    'LV': '"LA=1712783785:CV=1712783785:TS=1712783785"',
    'indeed_rcc': 'LV',
    'FPID': 'FPID2.2.QgFjuSMxG4slDg0axwQphyKfpSSL314Dbjzg9P9jBBI%3D.1712783787',
    'FPLC': 'u%2BDXGU8IIZHGUVBFqNWpFEQko7YaeX4vLWhhi9NpJl2YNZU6WF9N5LexVICdgZDO%2B6mhvfqigF1OXICEI8aw8iftP%2FHXlFv46ABXKUdZslns8r9mMfC1RAqDWOOQRg%3D%3D',
    'SURF': 'mB3bBHj8dYjwMnM2mLiLxIycKXEb95f8',
    '_ga': 'GA1.1.172602767.1712783787',
    '_ga_LYNT3BTHPG': 'GS1.1.1712783786.1.0.1712783786.0.0.1645744655',
    'CTK': '1hr4tsv55k7u7800',
    '__cf_bm': 'T6XW1vEZJiUgWp8XGnwzkHg.DUXK0JNEOyeuDp4e60E-1712783785-1.0.1.1-MZir8Mmd6cO10eMuZONqIpYbklVQz8oSG1GWnwgS2cuXI6givR53TYzzFGKDCW5xgqK9TscPf5rdmx0SQvByxQ',
    '_cfuvid': 'x0Q0Z_q0iIxe50kPGbXQHRHOToQPQJzrhzeubEqf.KM-1712783785197-0.0.1.1-604800000',
    'INDEED_CSRF_TOKEN': 'IFRAztGwMjJF3FQcauhkFj6mCFuW8dSq',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Cookie': 'OptanonConsent=isGpcEnabled=0&datestamp=Wed+Apr+10+2024+23%3A16%3A43+GMT%2B0200+(Central+European+Summer+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=30c883db-ea81-4eaa-8300-6d2e74226012&interactionCount=1&landingPath=https%3A%2F%2Fde.indeed.com%2F%3Fr%3Dus&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0; PTK=tk=1hr4tsvckjklr801&type=jobsearch&subtype=topsearch; ac=nUo+4Pd/Ee6fvs/wnSGnPw#m8sY8Pd/Ee6fvs/wnSGnPw; CSRF=4D3RFTcRaOMRwj7VrmezAy5qRlUnloFQ; LV="LA=1712783785:CV=1712783785:TS=1712783785"; indeed_rcc=LV; FPID=FPID2.2.QgFjuSMxG4slDg0axwQphyKfpSSL314Dbjzg9P9jBBI%3D.1712783787; FPLC=u%2BDXGU8IIZHGUVBFqNWpFEQko7YaeX4vLWhhi9NpJl2YNZU6WF9N5LexVICdgZDO%2B6mhvfqigF1OXICEI8aw8iftP%2FHXlFv46ABXKUdZslns8r9mMfC1RAqDWOOQRg%3D%3D; SURF=mB3bBHj8dYjwMnM2mLiLxIycKXEb95f8; _ga=GA1.1.172602767.1712783787; _ga_LYNT3BTHPG=GS1.1.1712783786.1.0.1712783786.0.0.1645744655; CTK=1hr4tsv55k7u7800; __cf_bm=T6XW1vEZJiUgWp8XGnwzkHg.DUXK0JNEOyeuDp4e60E-1712783785-1.0.1.1-MZir8Mmd6cO10eMuZONqIpYbklVQz8oSG1GWnwgS2cuXI6givR53TYzzFGKDCW5xgqK9TscPf5rdmx0SQvByxQ; _cfuvid=x0Q0Z_q0iIxe50kPGbXQHRHOToQPQJzrhzeubEqf.KM-1712783785197-0.0.1.1-604800000; INDEED_CSRF_TOKEN=IFRAztGwMjJF3FQcauhkFj6mCFuW8dSq',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'de.indeed.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
    'Referer': 'https://de.indeed.com/?r=us',
    'Connection': 'keep-alive',
}

params = {
    'q': 'Werkstudent Informatik',
    'l': 'Hamburg',
    'from': 'searchOnHP',
}

response = requests.get('https://de.indeed.com/jobs', params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# %%
soup
# %%
with open("test.html", "w") as f:
    f.write(response.text)
# %%
response.status_code
# %%
import httpx
with httpx.Client(http2=True) as client:
    response = client.get('https://de.indeed.com/jobs', params=params, cookies=cookies, headers=headers)
# %%
response.status_code
# %%

from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://de.indeed.com/jobs?q=werkstudent+Informatik&l=Hamburg&from=searchOnHP&vjk=74a581fd64741df8")
soup = BeautifulSoup(browser.page_source)
for element in soup.find_all("html"):
    print(element)




# %%
