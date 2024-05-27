import requests
from bs4 import BeautifulSoup as bs
import json


url = "http://ips.alliance-pipeline.com/Ips/"

loop_counter = 0 
page = requests.get(url + "MainPage.aspx?siteId=1")

while page.status_code != 200 :
    loop_counter += 1
    print ("Requesting Error " + str(loop_counter))
    print ("Requesting ...")
    page = requests.get(url + "MainPage.aspx?siteId=1")
    
print ("Connection successful!")
soup = bs(page.content, features="lxml")

viewstate = (soup.select("#__VIEWSTATE"))[0]["value"]
payload = {
    "ctl00$ScriptManager1" : "ctl00$UpdatePanel1|ctl00$treeview",
    "treeview_ExpandState" : "ennncnnnnncnnncnnnnnnnncncnnnnnnnnnncnnnnnnnnnncnnnnnnnncnnnccnncnnnncnnnncnncnnnnccncnnnnncnnncnnncnnnn",
    "treeview_SelectedNode" : "treeviewt1",
    "__EVENTTARGET" : "ctl00$treeview",
    "__EVENTARGUMENT" : "s20\40",
    "__VIEWSTATE" : viewstate,
    "__VIEWSTATEGENERATOR" : "CDDC97FA",
    "MainContent_ContentDescTxtiFr_clientState" : '|0|03||[[[[]],[],[]],[{},[]],"03"]', 
    "MainContent_ContentDescTxtiFr" : "",
    "MainContent_TspNmTxtiFr_clientState" : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_TspNmTxtiFr' : '', 
    'MainContent_TspNoTxtiFr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_TspNoTxtiFr' : '',
    'MainContent_ExtraTxtiFr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_ExtraTxtiFr' : '',
    'MainContent_PreParmTxtiFr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_PreParmTxtiFr' : '',
    'MainContent_ParmTxtiFr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_ParmTxtiFr' : '',
    'MainContent_DropDowniFr_clientState' : '[[[[null,0,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"04%2F01%2F2024",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]],[],null],[{},[{}]],null]',
    'MainContent_PostParmTxtiFr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_PostParmTxtiFr' : '',
    'MainContent_ContentDescTxtGr_clientState': '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_ContentDescTxtGr' : '',
    'MainContent_TspNmTxtGr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_TspNmTxtGr' : '',
    'MainContent_TspNoTxtGr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_TspNoTxtGr' : '',
    'MainContent_ExtraTxtGr_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]', 
    'MainContent_ExtraTxtGr' : '',
    'MainContent_PreParmTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_PreParmTxt' : '',
    'MainContent_SelParmTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]', 
    'MainContent_SelParmTxt' : '',
    'MainContent_DropDownlst_clientState' : '[[[[null,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]],[],null],[{},[{}]],null]',
    'MainContent_ParmTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_ParmTxt' : '',
    'MainContent_dtJobSchedForGrid_clientState' : '|0|012024-5-27-0-0-0-0||[[[[]],[],[]],[{},[]],"012024-5-27-0-0-0-0"]',
    'MainContent_ToDteTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_dtToGrid_clientState' : '|0|01||[[[[]],[],[]],[{},[]],"01"]',
    'MainContent_PostParmTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_PostParmTxt' : '',
    'MainContent_gridJobSchedForGrid_clientState' : '[[[[null,-1,null]],[[[[[0]],[],null],[null,null],[null]],[[[[4]],[],null],[null,null],[null]],[[[["RowSelectors"]],[],[]],[{},[]],null],[[[["Selection",null,1,null,null,null,null]],[],[]],[{},[]],null],[[[["Sorting"]],[],[{}]],[{},[{}]],null],[[[["ColumnFixing",null]],[[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]]],[{}]],[{},[{}]],null]],null],[{},[{},{}]],[]]',
    'MainContent_FileSrcTitleTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_FileSrcTitleTxt' : '',
    'MainContent_TspNmFileTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_TspNmFileTxt' : '',
    'MainContent_TspNoFileTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]', 
    'MainContent_TspNoFileTxt' : '',
    'MainContent_ContDescTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]', 
    'MainContent_ContDescTxt' : '',
    'MainContent_PosParmFileTxt_clientState' : '|0|03Title||[[[[]],[],[]],[{},[]],"03Title"]',
    'MainContent_PosParmFileTxt' : 'Title',
    'MainContent_StaticTitleTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]', 
    'MainContent_StaticTitleTxt' : '',
    'MainContent_TspNmStatTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_TspNmStatTxt' : '',
    'MainContent_TspNoStatTxt_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_TspNoStatTxt' : '',
    'MainContent_MsgTxt1_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]',
    'MainContent_MsgTxt1' : '',
    'MainContent_MsgTxt2_clientState' : '|0|03||[[[[]],[],[]],[{},[]],"03"]', 
    'MainContent_MsgTxt2' : '',
    'ctl00$MainContent$hidden_website_content_id' : '20',
    '_ig_def_dp_cal_clientState' : '[[null,[],null],[{},[]],"01,2024,05"]',
    'ctl00$_IG_CSS_LINKS_' : 'AplStyleSheet.css|../ig_res/Default/ig_monthcalendar.css|../ig_res/Default/ig_dataGrid.css|../ig_res/Default/ig_dropDown.css|../ig_res/Default/ig_texteditor.css|../ig_res/Default/ig_shared.css',
    '__ASYNCPOST' : 'true',
    'ctl00$MainContent$btnRetrieveJobSchedForGrid' : 'Retrieve',
    'treeview_PopulateLog' : ''
    }

headers = {
    "content_type" : "text/plain"
    }
payload = json.dumps(payload)
data_page = requests.post(url + "MainPage.aspx?siteId=1", headers = headers, data = payload)
loop_counter = 0
while data_page.status_code != 200 :
    loop_counter += 1
    print ("Posting Error " + str(loop_counter))
    print ("Posting ...")
    data_page = requests.post(url + "MainPage.aspx?siteId=1", headers = headers, data = payload)
print ("Post successful!")

data_soup = bs(data_page.content, features = 'lxml')
some_data = data_soup.select("table th tr")
print (some_data)
pretty_data = data_soup.prettify()

with open ('scraped.txt', 'w') as f:
    f.write(pretty_data)