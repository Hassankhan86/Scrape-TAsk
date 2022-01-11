from os import spawnle
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome(executable_path='C:\Users\HP\Desktop\New folder\chromedriver.exe')

# zipcode_input = input("Enter ZIp Code \n ")
# print("Select the radius of your search")
# miles_input = input(
#     "options \n 0) 10 miles \n 1) 25 miles \n 2) 50 miles \n 3) 75 miles \n 4) 100 miles \n 5) 200 miles \n 6) 500 miles \n")

print("<--------------------------------------------------->")
with open('combined_file.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['Name', 'Price', 'VIN','Summary','Features'])

    name = 0
    writer.writerow([name,name,name,name,name])
    name = [1,2]
    writer.writerow([name,name,name,name,name])
    # writer.writerow("title, post")
    # writer.writerow("\n")

# print("File Create")

# file = open('Car_Data.csv', 'w',encoding='utf8')
# writer = csv.writer(file)

# write title row
# writer.writerow(['Name', 'Price','Vin', 'Summary', 'Features'])

sleep(5)
# name = 
# name = [1,23]
# writer.writerow([name,name,name,name,name])
# writer.writerow([name,name,name,name,name])

# file.close
print("<--------------------------------------------------->")

driver = webdriver.Chrome(executable_path="chromedriver.exe")
actionChains = ActionChains(driver)
driver.get('https://www.edmunds.com/cars-for-sale-by-owner/')
# driver.implicitly_wait(15)


# zip_code = driver.find_element_by_name('zip')
# actionChains.double_click(zip_code).perform()
# time.sleep(5)
# zip_code.send_keys(Keys.BACKSPACE)
# zip_code.send_keys(zipcode_input)
# time.sleep(5)
# zip_code.send_keys(Keys.ENTER)

# miles_range = driver.find_element_by_id('search-radius-range-min')
# miles_range_value = miles_range.get_attribute('value')
# miles_range_value = int(miles_range_value)

# print(miles_range_value,"dasdasd")

# if miles_range_value < int(miles_input):
#     while miles_range_value != int(miles_input):
#         miles_range.send_keys(Keys.RIGHT)
#         miles_range_value += 1

# elif miles_range_value > int(miles_input):
#     while miles_range_value != int(miles_input):
#         miles_range.send_keys(Keys.LEFT)
#         miles_range_value -= 1
# else:
#     print('middle')
#     pass

# miles_range.send_keys(Keys.RIGHT)
# miles_range.send_keys(Keys.RIGHT)
# miles_range.send_keys(Keys.RIGHT)
# value = miles_range.get_attribute('value')
sleep(5)

index = 0
bro = driver.current_url

while True:
    driver.get(bro)
    print("Index No : ", index)
    divs = driver.find_elements_by_class_name('mb-md-1_5')

    
    sleep(5)
    divs[index].click()
    sleep(5)
    
    try:        
            print('-----------------1')
            
            
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '')))

            print('-----------------2')
            # sleep(3)
            # name = [1,23,123]
            try:
                # name = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/h1')
                name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/h1')))
                n =  name.text
                print("Name : ",n)
            except:
                print("Name is Not Found")
                pass
            
                


            print('-----------------')
            sleep(3)
            # p = [123]
            try:
                # price = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/span')
                price  = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/span')))
                p = price.text
                print("Price : ",p)
                # writer.writerow([p,p,p,p])
            except:
                print("Price is Not Found")
                pass

            print('-----------------')
            sleep(3)

            try:
                # vin = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/div[2]/div/span[1]')
                vin = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/div[2]/div/span[1]')))
                vi = vin.text
                print("VIN",vi)
        #     writer.writerow([n, p, vi])
        #     file.close()
        #     with open('combined_file.csv', 'w', newline='') as outcsv:
            # writer.writerow([n,p,vi])
            except:
                print("VIN is Not Found")
                pass

            print('-----------------')
            sleep(3)

            try:
                # Vehicle_Summary = driver.find_element_by_class_name('vehicle-summary')
                Vehicle_Summary = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'vehicle-summary')))
                sss = Vehicle_Summary.text
                # print("SSS : ",sss)
                sum = []
                sum = sss.split()
                S2 = ' '.join(sum)
                print("Vehicle_Summary : ",S2)
            except:
                print("Vehicle_Summary is Not FounD")
                S2 = ""
                pass

            print('-----------------')
            sleep(3)

            try:
                # features = driver.find_element_by_class_name('features-and-specs')
                features = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'features-and-specs')))
                o = features.text
                # print("OOOO : ",o)
                op = []
                op = o.split()
                O2 = ' '.join(op)
            
                # writer.writerow([username, uploads, views])
                print("features : ",O2)
            except:
                print("features is Not FounD")
                O2 = ""
                pass

            with open('combined_file.csv', 'a', newline='') as outcsv:
                writer = csv.writer(outcsv)
                # writer.writerow(['Name', 'Price', 'VIN','Summary','Features'])

                
                writer.writerow([n,p,vi,S2,O2])
            
    except:
            print('Not Disappere')
            pass
    print('-----------------')
    # driver.back()
    print("Back Button")
    print('-----------------')
    index += 1

time.sleep(5)
print('______________')
print(value)
print('______________')
# time.sleep(15)
driver.quit()
