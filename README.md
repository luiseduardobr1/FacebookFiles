# FacebookFiles
Download all the PDF's files from a facebook group .

# Requirements
* [Selenium](https://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Chromedriver](https://chromedriver.chromium.org/downloads)
* [Requests](https://requests.readthedocs.io/en/master/)

# How to use
1) Put your facebook's login and password in the code:
```Python
# Facebook Login
driver.find_element_by_css_selector('#email').send_keys('YOUR FACEBOOK LOGIN')
driver.find_element_by_css_selector('#pass').send_keys('YOUR FACEBOOK PASSWORD')
driver.find_element_by_css_selector('#loginbutton').click()
```

2) After running the code, it will create a folder with the PDF's files named *Files_*(*group-name-or-id*). 
