import spynner
from bs4 import BeautifulSoup
import sys

def EUN(Username, Password):
    #Logging in
    br = spynner.Browser()
    br.load("http://www.bits-pilani.ac.in:12349/Login.aspx")
    br.wk_fill('input[name="TextBox1"]', Username)
    br.wk_fill('input[name="TextBox2"]', Password)
    br.click("input[type=submit]", wait_load=True, wait_requests=None, timeout=None)

    #Password chck
    if str(br.url) == "http://www.bits-pilani.ac.in:12349/Student/StudentHome.aspx":
        #Loading the arrears page
        br.load("http://www.bits-pilani.ac.in:12349/Student/Dues.aspx")
        br.click("input[name=Button2]", wait_load=True, wait_requests=None, timeout=None)

        #Creating a soup object
        plain_text = str(br.html)
        soup = BeautifulSoup(plain_text)

        #Extraction of data
        tableData = soup.find("table", attrs={"id":"arrearGridView"})
        cells = tableData.findAll('td')
        #Printing the dues
        for item in cells[-1]:
            print "Your dues : "+item.string
    else:
        print "Entered Username and Password do not match"
    br.close()

u = str(raw_input("Username : "))
p = str(raw_input("Password : "))
EUN(u,p)



