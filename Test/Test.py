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

print("<--------------------------------------------------->")

# GEtting  a zipcode and Miles Input
zipcode_input = input("Enter ZIp Code \n ")
print("Select the radius of your search")
miles_input = input(
    "options \n 0) 10 miles \n 1) 25 miles \n 2) 50 miles \n 3) 75 miles \n 4) 100 miles \n 5) 200 miles \n 6) 500 miles \n")

driver = webdriver.Chrome(executable_path="chromedriver.exe")
actionChains = ActionChains(driver)
driver.get('https://www.edmunds.com/cars-for-sale-by-owner/')

#Locate zipcode input and paste zipcode 
zip_code = driver.find_element_by_name('zip')
actionChains.double_click(zip_code).perform()
time.sleep(5)
zip_code.send_keys(Keys.BACKSPACE)
zip_code.send_keys(zipcode_input)
time.sleep(5)
zip_code.send_keys(Keys.ENTER)

miles_range = driver.find_element_by_id('search-radius-range-min')
miles_range_value = miles_range.get_attribute('value')
miles_range_value = int(miles_range_value)

print(miles_range_value,"dasdasd")

# Check miles and adjust them
if miles_range_value < int(miles_input):
    while miles_range_value != int(miles_input):
        miles_range.send_keys(Keys.RIGHT)
        miles_range_value += 1

elif miles_range_value > int(miles_input):
    while miles_range_value != int(miles_input):
        miles_range.send_keys(Keys.LEFT)
        miles_range_value -= 1
else:
    print('middle')
    pass




sleep(5)
print("<--------------------------------------------------->")
#Create with and write Heading in it
with open('Cars_Data.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['Name', 'Price', 'VIN','Summary','Features'])
    
sleep(5)
print("<--------------------------------------------------->")

index = 0
CopyURl = driver.current_url
num_of_loops = 21

while  num_of_loops > 0:
    print("Num_of_loop",num_of_loops)
    driver.get(CopyURl)                       #GEt back to Cars URl
    print("Index No : ", index)
    
    
    try:    

        print('-----------------1')                             
        divs = driver.find_elements_by_class_name('mb-md-1_5')          #Locate the cars div
        sleep(5)
        divs[index].click()                                                 #Access cars one by one using indexing
        sleep(5)

        try:
            # Get Name of Car 
            name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/h1')))
            n =  name.text
            print("Name : ",n)
        except:
            print("Name is Not Found")
            n  = ""
            pass
        

        print('-----------------')
        sleep(3)

        try:
            # Get Price of Car 
            price  = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/span')))
            p = price.text
            print("Price : ",p)
        except:
            print("Price is Not Found")
            p  = ""
            pass

        print('-----------------')
        sleep(3)

        try:
            # Get VIN of Car 
            vin = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/div[2]/div/span[1]')))
            vi = vin.text
            print("VIN",vi)
        except:
            print("VIN is Not Found")
            vi = ""
            pass

        print('-----------------')
        sleep(3)

        try:
            # Get Vehicle_Summary of Car 
            Vehicle_Summary = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'vehicle-summary')))
            sss = Vehicle_Summary.text
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
            # Get Features of Car 
            features = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'features-and-specs')))
            o = features.text
            op = []
            op = o.split()
            O2 = ' '.join(op)
        
            print("features : ",O2)
        except:
            print("features is Not FounD")
            O2 = ""
            pass

        print('-----------------')
        sleep(3)

        # Now write data of price,name ,vin,summary and features in file

        with open('Cars_Data.csv', 'a', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow([n,p,vi,S2,O2])
            
    except:
            print('Not Disappere')
            pass
    print('-----------------')
    # driver.back()
    print("Back To URL ")
    print('-----------------')
    index += 1
    num_of_loops = num_of_loops -1

time.sleep(5)
driver.quit()
