import os, re, requests, time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Get facebook's group link
grupo_url=input('Facebook group URL: ')
if grupo_url[-1]==r'/':
    thing_url=grupo_url+'files'
else:
    thing_url=grupo_url+r'/files'

# Create a folder to save downloaded files
group_name_or_id= ''.join(re.findall(r'https://www.facebook.com/groups/(\w*)', thing_url))
download_dir = 'Files_'+group_name_or_id
try:
    os.mkdir(download_dir)
except FileExistsError:
    print("Directory " , download_dir ,  " already exists")
download_dir=os.getcwd()+'\\'+download_dir
print('Files saved in: ' + download_dir)

# Disable notifications and save PDF in folder
chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,
    "profile.default_content_setting_values.notifications" : 2
    }
)

# Initialize browser
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver, options=chrome_options)

# Open Facebook Group website
driver.get(thing_url)

# Facebook Login
driver.find_element_by_css_selector('#email').send_keys('YOUR FACEBOOK LOGIN')
driver.find_element_by_css_selector('#pass').send_keys('YOUR FACEBOOK PASSWORD')
driver.find_element_by_css_selector('#loginbutton').click()

# Extract source code - Initial
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")
site_id= ''.join(re.findall(r'group_id=(\w*)', str(soup))[0])

# Clicando em "Ver mais" até carregar todos os arquivos
connected = True
while connected:
    try:
        driver.find_element_by_css_selector(r'#group_files_pager_'+site_id).click()
        time.sleep(1)
    except:
        connected = False
        pass

# Extract source code
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")

# Get Group's Archive - Filename and Link
arquivos_fonte=soup.find(id="group_files_"+site_id)
for arquivo in arquivos_fonte.findAll('a'):
    try:
        if arquivo.contents[0][:5]!=r'<abbr':
            print(arquivo.contents[0])
    except:
        pass
    if arquivo['href'][:7]!=r'/groups':
        print(arquivo['href'])
        driver.get('https://www.facebook.com'+arquivo['href'])