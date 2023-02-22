from selenium import webdriver

d = webdriver.Chrome()
d.maximize_window()
d.get("https://www.google.com/")
print(d.title)
