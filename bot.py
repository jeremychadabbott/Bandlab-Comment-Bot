import time 

from selenium import webdriver 

#Opening the browser 
browser = webdriver.Chrome() 

#Maximize the browser window 
browser.maximize_window() 

#Go to the bandlab web page 
browser.get("https://bandlab.com") 

#Start the loop for creating accounts 
for i in range(20): 

#Click on the "Sign Up" button 
signup_btn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div/div[3]/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/button[1]") 
signup_btn.click() 

#Fill up the form 
name_field = browser.find_element_by_name("username") 
name_field.send_keys("user" + str(i)) 

email_field = browser.find_element_by_name("email") 
email_field.send_keys("user" + str(i) + "@mail.com") 

password_field = browser.find_element_by_name("password") 
password_field.send_keys("password") 

signup_btn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div[3]/div[2]/button[1]") 
signup_btn.click() 

#Go to the explore page 
explore_btn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[1]/ul/li[2]/div/span[2]") 
explore_btn.click() 

#Wait for the page to load 
time.sleep(10) 

#Find the top post and comment on it 
top_post = browser.find_element_by_class_name("explore-item__comments-link") 
top_post.click() 

comment_field = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/form/div/div[2]/div/div/div/div") 
comment_field.send_keys("This is a great post!") 

comment_btn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/form/div/div[3]/div/div/div/div/div/button") 
comment_btn.click() 

#Wait for 20 minutes 
time.sleep(1200) 

#Close the browser 
browser.close()
