
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:\\Users\\swara\\PycharmProjects\\SeleniumFirst\\driver\\chromedriver.exe")

driver.get("https://nces.ed.gov/collegenavigator/?s=all&sp=4&pg=1")

driver.minimize_window()

header = ['Name of a College/University', 'Street', 'City', 'State', 'Zipcode', 'Contact', 'Website', 'Type', 'Awards',
          'Campus Setting', 'Campus Housing', 'Student Population', 'Student to faculty ratio']


globaldata=[]
for j in range(1,8):
    driver.get("https://nces.ed.gov/collegenavigator/?s=all&sp=4&pg="+str(j))
    for i in range(1,16):
        maindata = []
        try:
            link = "//*[@id='ctl00_cphCollegeNavBody_ucResultsMain_tblResults']/tbody/tr[" + str(i) + "]/td[2]/a"
            driver.find_element_by_xpath(link).click()
        except NoSuchElementException:
            break

        clgname = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/span/span").text
        maindata.append(clgname)

        address = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/span").text
        address = address.replace(clgname+"\n","")
        caddress = address.split(",")

        count = caddress.__len__()

        maindata.append(caddress[0])
        maindata.append(caddress[1])

        if count == 3:
            splitpin = caddress[2].split(" ")
            maindata.append(splitpin[1])
            maindata.append(splitpin[2])
        elif count == 2:
            splitpin = caddress[1].split(" ")
            maindata.append(splitpin[1])
            maindata.append(splitpin[2])
        else:
            splitpin = caddress[3].split(" ")
            maindata.append(splitpin[1])
            maindata.append(splitpin[2])

        if driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[1]/td[2]").is_displayed():
            ginfo = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[1]/td[2]").text
        else:
            ginfo = ""

        maindata.append(ginfo)

        if driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[2]/td[2]/a").is_displayed():
            website = driver.find_element_by_xpath(
                "//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[2]/td[2]/a").text
        else:
            website = ""

        maindata.append(website)

        if driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[3]/td[2]").is_displayed():
            ctype = driver.find_element_by_xpath(
                "//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[3]/td[2]").text
        else:
            ctype = ""

        maindata.append(ctype)

        if driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[4]/td[2]").is_displayed():
            awards = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[4]/td[2]").text
            awards1=awards.replace('\n', ', ')
        else:
            awards1 = ""

        maindata.append(awards1)

        if driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[5]/td[2]").is_displayed():
            csetting = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[5]/td[2]").text
        else:
            csetting =""

        maindata.append(csetting)

        if driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[6]/td[2]").is_displayed():
            chousing = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[6]/td[2]").text
        else:
            chousing = ""

        maindata.append(chousing)

        if driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[7]/td[2]").is_displayed():
            spopulation = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[7]/td[2]").text
        else:
            spopulation = ""

        maindata.append(spopulation)

        try:
            stfratio = driver.find_element_by_xpath("//*[@id='RightContent']/div[4]/div/div[2]/table/tbody/tr[8]/td[2]").text
        except NoSuchElementException:
            stfratio = ""

        maindata.append(stfratio)

        driver.back()
        globaldata.append(maindata)
        print("Data "+str(i)+" Added from Page - "+str(j))


print(globaldata)


with open('data1.csv','w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(globaldata)


