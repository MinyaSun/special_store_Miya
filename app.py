import streamlit as st
import requests 
 
def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'  
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res

def getCountyOption(items):
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name :  
            specificBookstoreList.append(item)
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['introduction'])
        expander.subheader( 'Address')
        expander.write(item['address'])
        expander.subheader('Open Time')
        expander.write(item['open Time'])
        expander.subheader('Email')
        expander.write(item['email'])
        expanderList.append(expander)
    return expanderList

def app(): 
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    specificBookstoreList = getSpecificBookstore(book)
    num = len(specificBookstore)
    st.write('總共有(num)間書店')
    bookstoreInfo = getBookstoreInfo(specificBookstore)


 if __name__ == '__main__':
    app()