from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import csv
from csv import writer

driver = webdriver.Chrome(executable_path="chromedriver.exe")
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait

# driver.get('https://www.edmunds.com/cars-for-sale-by-owner/')

print('<----------------------------------------------------->')
driver.get('https://www.tred.com/buy?body_style=&distance=50&exterior_color_id=&make=&miles_max=100000&miles_min=0&model=&page_size=24&price_max=100000&price_min=0&query=&requestingPage=buy&sort=desc&sort_field=updated&status=active&year_end=2022&year_start=1998&zip=')

sleep(5)
print(driver.title)

driver.maximize_window()



radius = driver.find_element_by_xpath('/html/body/section/div/div/div[3]/div/section/div/div[1]/div/section/form/div[1]/div[2]/div[1]/select')
radius.click()
radius.send_keys('100')

radius.click()

Search = driver.find_element_by_xpath('/html/body/section/div/div/div[3]/div/section/div/div[1]/div/section/form/div[1]/div[2]/div[2]/input')

Search.click()
Search.send_keys('90011')

print('<----------------------------------------------------->')
# sleep(10)

# open = driver.find_element_by_xpath('/html/body/section/div/div/div[3]/div/section/div/div[2]/div[1]/div/div[1]/div')
# (print(open.text))
# cr = driver.find_element_by_class_name('grid-car')

# print(cr.text)


# all = driver.find_element_by_xpath('/html/body/section/div/div/div[3]/div/section/div/div[2]/div[1]/div')
# print(all.text)
# print(all.text)



sleep(2)
# all = driver.find_elements_by_class_name('info')
# print(all.h5.text)


# for a in all.find_elements_by_class_name('grid-car'):
#     a2 = a    
# # aa.find_elements_by_class_name('card ')
# print(a2.text)


# aaa = driver.findElement(By.XPATH("(//*[@class='grid-box-container'])[1]"))
# print(aaa)
# print(aaa.text)
# aaa.click()
sleep(3)
index = 0
# num_of_loops = 1
# while num_of_loops > 0:

file = open('Car.csv', 'w',encoding='utf8')
writer = csv.writer(file)
writer.writerow(['Price', 'Name', 'Table','Table2'])
file.close()



while True:
    divs = driver.find_elements_by_class_name('grid-box-container')
    # divs = driver.find_elements_by_class_name('usurp-inventory-card')
    # divs = driver.find_element_by_xpath('')
    try:        
        divs[index].click()
        sleep(5)
        print('-----------------1')
        
        print('-----------------2')
        wait = WebDriverWait(driver, 10)

        # price = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[4]/div/div/div[2]/div/div/h2')
        try:
            print('-----------------2')
            
            price = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/div[2]/div[4]/div/div/div[2]/div/div/h2')))
            # if price.is_displayed():
            p =  price.text
            print(p)
            print('-----------------')
            sleep(3)
            name = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[5]/div[2]/div/h1[1]')
            n = name.text
            print(n)
            print('-----------------')
            sleep(3)
            summary = driver.find_element_by_class_name('col-md-7')
            s = summary.text
            # print(t)
            print('-----------------')
            sum = []
            sum = s.split()
            print(sum)
            print('-----------------')
            sleep(3)
            option = driver.find_element_by_class_name('col-md-5')
            o = option.text
            # print(t2)
            op = []
            op = o.split()
            print(op)
            print('-----------------')

    
            print('Nyce')
            writer.writerow([p, n, sum,op])
            file.close()
            # List=[p, n, sum,op]
  

            
            print('-----------------')

            # with open('Car.csv','a') as f1:
            #   f1.write(List)
                # writer=csv.writer(f1.write(List), delimiter='\t',lineterminator='\n',)
            # with open('event.csv', 'a') as f_object:
            #     print('12-----------------')

            # # Pass this file object to csv.writer()
            # # and get a writer object
            #     writer_object = writer(f_object)
            #     print('13-----------------')

            # # Pass the list as an argument into
            # # the writerow()
            #     writer_object.writerow(List)
            #     print('14-----------------')

            # #Close the file object
            #     f_object.close()
            
            print('-----------------End')


        except:
            print('Not Disappere')
            pass

       

    except IndexError:
       break  # no more elements, exit the loop
       print('BReak')
   # do smth
   # ...
    sleep(3)
    driver.back()
    sleep(5)
#    num_of_loops = num_of_loops -1
    index += 1

