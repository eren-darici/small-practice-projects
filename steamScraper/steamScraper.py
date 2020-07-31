import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


my_url = str(input("Web adresini giriniz:"))


uClient = uReq(my_url)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"id": "search_resultsRows"})

titleDF = []
discountDF = []
priceDF = []

for container in containers:
    title_html = container.find_all("div", {"class": "col search_name ellipsis"})
    for title in title_html:
        titleFinal = title.span.text
        titleDF.append(titleFinal)

    discount_html = container.find_all("div", {"class": "col search_price_discount_combined responsive_secondrow"})

    for discount in discount_html:
        discountRate = discount.div.span

        if discountRate != None:
            discountRate = discount.div.span.text
            discountDF.append(discountRate)

            price_html = container.find_all("div", {"class": "col search_price discounted responsive_secondrow"})

            for price in price_html:
                priceFinal = price.text.split("TL")
                priceDF.append(priceFinal[1].strip() + " TL")
                

        else:
            discountRate = "İndirim Yok."
            discountDF.append(discountRate)

headers = ["Oyun", "İndirim Oranı"]
df = pd.DataFrame(list(zip(titleDF, discountDF)))
df.columns = headers

for i in range(0, len(titleDF)):
    if df["İndirim Oranı"][i] == "İndirim Yok.":
        priceDF.insert(i, "-")

df["Fiyat"] = priceDF[0:50]

print(df)
df.to_excel("steamList.xls", index=False, engine ='xlsxwriter')
