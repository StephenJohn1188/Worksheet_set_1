#!/usr/bin/env python
# coding: utf-8

# # Q7. scrape First 100 shoes data you get. The data should include “Brand” of the shoes , Short Shoe description, price of the shoe

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[3]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[4]:


driver.get("https://www.myntra.com/shoes")


# In[5]:


price=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label")
price.click()


# In[6]:


colour=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label/span[1]")
colour.click()


# In[7]:


brand=[]
price=[]
product_description=[]


# In[8]:


brand_tags=driver.find_elements(By.XPATH,'//h3[@class="product-brand"]')
for i in brand_tags[0:100]:
    bd=i.text
    brand.append(bd)


# In[9]:


price_tags=driver.find_elements(By.XPATH,'//div[@class="product-price"]')
for i in price_tags[0:100]:
    PR=i.text
    price.append(PR)


# In[10]:


product_tags=driver.find_elements(By.XPATH,'//h4[@class="product-product"]')
for i in product_tags[0:100]:
    PD=i.text
    product_description.append(PD)


# In[11]:


print(len(brand),len(price),len(product_description))


# In[12]:


df=pd.DataFrame({'Brand':brand,'Price':price,'Product Description':product_description})


# In[13]:


df


# # Q6. Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers”

# In[14]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[15]:


driver.get("https://www.flipkart.com/")


# In[16]:


cross=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button")
cross.click()


# In[17]:


product=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
product.send_keys('Sneakers')


# In[18]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[19]:


brand=[]
price=[]
product_description=[]


# In[20]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[0:100]:
    bd=i.text
    brand.append(bd)


# In[21]:


price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags[0:100]:
    PR=i.text
    price.append(PR)


# In[22]:


product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa _2-ICcC"]')
for i in product_tags[0:100]:
    PD=i.text
    product_description.append(PD)


# In[24]:


print(len(brand),len(price),len(product_description))


# In[23]:


df=pd.DataFrame({'Brand':brand,"Price":price, "Product Description":product_description})


# In[24]:


df


# # Q8. Scrape first 10 laptops data.

# In[62]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[63]:


driver.get("https://www.amazon.in/")


# In[64]:


product=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
product.send_keys('Laptops')


# In[65]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div")
search.click()


# In[66]:


CPU=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[14]/span/a/span")
CPU.click()


# In[67]:


title=[]
rating=[]
price=[]


# In[68]:


title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags[0:10]:
    tt=i.text
    title.append(tt)


# In[69]:


price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags[0:10]:
    PR=i.text
    price.append(PR)


# In[70]:


rating_tags=driver.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]//span')
for i in rating_tags[0:10]:
    RA=i.text
    rating.append(RA)


# In[71]:


print(len(rating), len(title),len(price))


# In[74]:


df=pd.DataFrame({'Rating':rating,'Title':title,'Price':price})
df


# # Q9. Python program to scrape the salary data for Data Scientist designation.

# In[205]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[206]:


driver.get("https://www.ambitionbox.com/")


# In[207]:


jobs=driver.find_element(By.XPATH,"/html/body/div[1]/nav[2]/div/ul/li[5]/a")
jobs.click()


# In[208]:


designation=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/span/input")
designation.send_keys('Data Scientist')


# In[209]:


search=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/button")
search.click()


# In[210]:


select=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/i")
select.click()


# In[211]:


location=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input")
location.send_keys('Noida')


# In[212]:


ND=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/label")
ND.click()


# In[213]:


job_title=[]
company_name=[]


# In[214]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title noclick"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[215]:


company_tags=driver.find_elements(By.XPATH,'//div[@class="company-info"]')
for i in company_tags[0:10]:
  company=i.text
  company_name.append(company)


# In[216]:


print(len(job_title),len(company_name))


# In[217]:


df=pd.DataFrame({'Job Title':job_title,'Company Name':company_name})
df


# # Q10.python program to scrape the salary data for Data Scientist designation. You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary.

# In[337]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[338]:


driver.get("https://www.ambitionbox.com/")


# In[339]:


Select=driver.find_element(By.XPATH,"/html/body/div[1]/nav[2]/div/ul/li[3]/a")
Select.click()


# In[340]:


bsalary=driver.find_element(By.XPATH,"/html/body/div[1]/nav[2]/div/ul/li[3]/div/ul/li[1]/div")
bsalary.click()


# In[341]:


designation=driver.find_element(By.XPATH,"/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input")
designation.send_keys('Data Scientist')


# In[342]:


dclick=driver.find_element(By.XPATH,"/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/div/div/div[1]")
dclick.click()


# In[343]:


Experience_Required=[]
company_name=[]
Total_Salary=[]
Average=[]
Minimum=[]
Maximum=[]


# In[344]:


experience_tags=driver.find_elements(By.CLASS_NAME,'sbold-list-header')
for i in title_tags[0:10]:
    exp=i.text
    Experience_Required.append(exp)


# In[345]:


len(Experience_Required)


# In[346]:


company_tags=driver.find_elements(By.XPATH,'//div[@class="company-info"]//a')
for i in company_tags[0:10]:
  company=i.text
  company_name.append(company)


# In[347]:


avg_tags=driver.find_elements(By.XPATH,'//p[@class="averageCtc"]')
for i in avg_tags[0:10]:
  avg=i.text
  Average.append(avg)


# In[348]:


TS_tags=driver.find_elements(By.XPATH,'//span[@class="datapoints"]')
for i in TS_tags[0:10]:
  TS=i.text
  Total_Salary.append(TS)


# In[349]:


min_tags=driver.find_elements(By.XPATH,'//div[@class="value body-medium"]')
for i in min_tags[0:10]:
  min=i.text
  Minimum.append(min)


# In[350]:


max_tags=driver.find_elements(By.XPATH,'//div[@class="value body-medium"]')
for i in max_tags[0:10]:
  max=i.text
  Maximum.append(max)


# In[351]:


print(len(Experience_Required),len(company_name),len(Total_Salary),len(Minimum),len(Maximum))


# In[353]:


df=pd.DataFrame({'Company Name':company_name,"Total Salary Record":Total_Salary,"Maximum Salary":Maximum, "Minimum Salary":Minimum})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




