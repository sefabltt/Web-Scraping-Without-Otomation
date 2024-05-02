import time
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


browser = webdriver.Chrome()  # veya başka bir tarayıcı için uygun webdriver kullanın

browser.get("https://www.hastane.com.tr/adana-hastaneleri.html")

link = browser.find_element(By.LINK_TEXT,"ADANA ALADAĞ İLÇE DEVLET HASTANESİ")
link.click()
hastaneadı1 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası1 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası1 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres1 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe1 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il1 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Çukurova Devlet Hastanesi")
link.click()

hastaneadı2 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası2 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası2 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres2 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe2 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il2 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Çukurova Özel Göz Hastanesi")
link.click()

hastaneadı3 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası3 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası3 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres3 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe3 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il3 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Devlet Hastanesi")
link.click()

hastaneadı4 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası4 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası4 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres4 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe4 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il4 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Dr. Ekrem Tok Ruh Sağlığı ve Hastalıkları Hastanesi")
link.click()

hastaneadı5 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası5 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası5 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres5 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe5 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il5 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Fatma Kemal Timuçin Ağız ve Diş Sağlığı Hastanesi")
link.click()

hastaneadı6 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası6 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası6 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres6 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe6 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il6 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Feke İlçe Devlet Hastanesi")
link.click()

hastaneadı7 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası7 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası7 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres7 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe7 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il7 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Hiperbarik Oksijen Tedavi ve Yara Bakım Merkezi")
link.click()

hastaneadı8 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası8 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası8 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres8 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe8 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il8 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana İmamoğlu Devlet Hastanesi")
link.click()

hastaneadı9 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası9 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası9 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres9 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe9 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il9 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Kadın Doğum ve Çocuk Hastalıkları Hastanesi")
link.click()

hastaneadı10 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası10 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası10 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres10 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe10 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il10 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Numune Eğitim ve Araştırma Hastanesi")
link.click()

hastaneadı11 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası11 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası11 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres11 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe11 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il11 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Adana Şehir Hastanesi")
link.click()

hastaneadı12 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası12 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası12 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres12 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe12 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il12 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Başkent Üniversitesi Adana Uygulama ve Araştırma Merkezi")
link.click()

hastaneadı13 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası13 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası13 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres13 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe13 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il13 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Ceyhan Devlet Hastanesi")
link.click()

hastaneadı14 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası14 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası14 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres14 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe14 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il14 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Çukurova Dr. Aşkım Tüfekçi Devlet Hastanesi")
link.click()

hastaneadı15 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası15 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası15 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres15 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe15 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il15 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Çukurova Üniversitesi Diş Hekimliği Fakültesi")
link.click()

hastaneadı16 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası16 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası16 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres16 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe16 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il16 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Çukurova Üniversitesi Tıp Fakültesi Balcalı Hastanesi")
link.click()

hastaneadı17 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası17 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası17 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres17 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe17 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il17 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Karaisalı Devlet Hastanesi")
link.click()

hastaneadı18 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası18 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası18 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres18 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe18 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il18 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Karaisalı Devlet Hastanesi")
link.click()

hastaneadı19 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası19 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası19 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres19 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe19 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il19 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"Karataş Devlet Hastanesi")
link.click()

hastaneadı20 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası20 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası20 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres20 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe20 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il20 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

browser.back()
link = browser.find_element(By.LINK_TEXT,"2")
link.click()

link = browser.find_element(By.LINK_TEXT,"Kozan Devlet Hastanesi")
link.click()

hastaneadı21 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası21 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası21 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres21 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe21 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il21 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Ortadoğu Özel Sağlık Hastanesi")
link.click()

hastaneadı22 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası22 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası22 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres22 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe22 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il22 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Adana Cerrahi Tıp Merkezi")
link.click()

hastaneadı23 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası23 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası23 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres23 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe23 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il23 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Adana Hastanesi")
link.click()

hastaneadı24 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası24 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası24 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres24 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe24 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il24 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Adana Hayat Tıp Merkezi")
link.click()

hastaneadı25 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası25 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası25 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres25 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe25 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il25 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Adana Metro Hastanesi")
link.click()

hastaneadı26 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası26 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası26 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres26 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe26 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il26 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Adana Ortadoğu Hastanesi")
link.click()

hastaneadı27 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası27 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası27 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres27 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe27 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il27 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Adana Şifa Tıp Merkezi")
link.click()

hastaneadı28 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası28 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası28 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres28 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe28 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il28 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Akdeniz Üroloji Merkezi")
link.click()

hastaneadı29 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası29 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası29 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres29 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe29 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il29 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Algomed Hastanesi")
link.click()

hastaneadı30 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası30 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası30 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres30 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe30 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il30 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Batıkent Hastanesi")
link.click()

hastaneadı31 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası31 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası31 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres31 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe31 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il31 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Can Doğum ve Cerrahi Hastanesi")
link.click()

hastaneadı32 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası32 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası32 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres32 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe32 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il32 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Ceyhan Çınar Hastanesi")
link.click()

hastaneadı33 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası33 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası33 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres33 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe33 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il33 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Çare Hastanesi")
link.click()

hastaneadı34 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası34 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası34 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres34 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe34 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il34 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Çukurova Diyaliz Merkezi")
link.click()

hastaneadı35 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası35 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası35 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres35 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe35 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il35 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Dermancan Tıp Merkezi")
link.click()

hastaneadı36 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası36 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası36 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres36 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe36 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il36 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel EPC Hastanesi")
link.click()

hastaneadı37 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası37 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası37 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres37 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe37 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il37 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Galleria KBB Dal Merkezi")
link.click()

hastaneadı38 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası38 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası38 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres38 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe38 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il38 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Güney Adana Hastanesi")
link.click()

hastaneadı39 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası39 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası39 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres39 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe39 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il39 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Güney Adana Hastanesi")
link.click()

hastaneadı40 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası40 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası40 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres40 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe40 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il40 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel İsa Alataş Tıp Merkezi")
link.click()

hastaneadı41 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası41 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası41 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres41 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe41 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il41 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"3")
link.click()

link = browser.find_element(By.LINK_TEXT,"Özel Kalepark Hastanesi")
link.click()
hastaneadı42 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası42 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası42 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres42 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe42 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il42 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Kozan Diyaliz Merkezi")
link.click()
hastaneadı43 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası43 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası43 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres43 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe43 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il43 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Medline Adana Hastanesi")
link.click()
hastaneadı44 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası44 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası44 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres44 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe44 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il44 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Özülkü Tıp Merkezı")
link.click()
hastaneadı45 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası45 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası45 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres45 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe45 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il45 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Sevgi Göz Teşhis ve Tedavi Merkezi")
link.click()
hastaneadı46 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası46 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası46 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres46 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe46 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il46 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Sezar Hospital Hastanesi")
link.click()
hastaneadı47 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası47 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası47 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres47 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe47 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il47 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Sistem Tıp Merkezi")
link.click()
hastaneadı48 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası48 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası48 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres48 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe48 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il48 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Türkmenbaşı Tıp Merkezi")
link.click()
hastaneadı49 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası49 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası49 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres49 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe49 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il49 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Özel Ziyapaşa Kadın Doğum ve Çocuk Hastalıkları Merkezi")
link.click()
hastaneadı50 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası50 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası50 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres50 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe50 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il50 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Pozantı 80. Yıl Devlet Hastanesi")
link.click()
hastaneadı51 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası51 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası51 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres51 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe51 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il51 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Prof. Dr. Nusret Karasu Göğüs Hastalıkları Hastanesi")
link.click()
hastaneadı52 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası52 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası52 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres52 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe52 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il52 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Saimbeyli Şehit Uzman Çavuş Adem Ambarcı İlçe Devlet Hastanesi")
link.click()
hastaneadı53 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası53 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası53 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres53 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe53 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il53 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Seyhan Uygulama Ve Araştırma Hastanesi")
link.click()
hastaneadı54 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası54 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası54 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres54 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe54 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il54 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Tufanbeyli Devlet Hastanesi")
link.click()
hastaneadı55 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası55 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası55 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres55 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe55 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il55 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text
browser.back()

link = browser.find_element(By.LINK_TEXT,"Yumurtalık Devlet Hastanesi")
link.click()
hastaneadı56 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').text
telefonnumarası56 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]').text
faksnumarası56 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]').text
adres56 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td[2]').text
ilçe56 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]').text
il56 = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_fvHospital"]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td[2]').text

data1 = {
    'Hastane Adı': [hastaneadı1,hastaneadı2,hastaneadı3,hastaneadı4,hastaneadı5,hastaneadı6,hastaneadı7,hastaneadı8,hastaneadı9,hastaneadı10,hastaneadı11,hastaneadı12,hastaneadı13,hastaneadı14,hastaneadı15,hastaneadı16,hastaneadı17,hastaneadı18,hastaneadı19,hastaneadı20,hastaneadı21,hastaneadı22,hastaneadı23,hastaneadı24,hastaneadı25,hastaneadı26,hastaneadı27,hastaneadı28,hastaneadı29,hastaneadı30,hastaneadı31,hastaneadı32,hastaneadı33,hastaneadı34,hastaneadı35,hastaneadı36,hastaneadı37,hastaneadı38,hastaneadı39,hastaneadı40,hastaneadı41,hastaneadı42,hastaneadı43,hastaneadı44,hastaneadı45,hastaneadı46,hastaneadı47,hastaneadı48,hastaneadı49,hastaneadı50,hastaneadı51,hastaneadı52,hastaneadı53,hastaneadı54,hastaneadı55,hastaneadı56],
    'Telefon Numarası': [telefonnumarası1,telefonnumarası2,telefonnumarası3,telefonnumarası4,telefonnumarası5,telefonnumarası6,telefonnumarası7,telefonnumarası8,telefonnumarası9,telefonnumarası10,telefonnumarası11,telefonnumarası12,telefonnumarası13,telefonnumarası14,telefonnumarası15,telefonnumarası16,telefonnumarası17,telefonnumarası18,telefonnumarası19,telefonnumarası20,telefonnumarası21,telefonnumarası22,telefonnumarası23,telefonnumarası24,telefonnumarası25,telefonnumarası26,telefonnumarası27,telefonnumarası28,telefonnumarası29,telefonnumarası30,telefonnumarası31,telefonnumarası32,telefonnumarası33,telefonnumarası34,telefonnumarası35,telefonnumarası36,telefonnumarası37,telefonnumarası38,telefonnumarası39,telefonnumarası40,telefonnumarası41,telefonnumarası42,telefonnumarası43,telefonnumarası44,telefonnumarası45,telefonnumarası46,telefonnumarası47,telefonnumarası48,telefonnumarası49,telefonnumarası50,telefonnumarası51,telefonnumarası52,telefonnumarası53,telefonnumarası54,telefonnumarası55,telefonnumarası56],
    'Faks Numarası': [faksnumarası1,faksnumarası2,faksnumarası3,faksnumarası4,faksnumarası5,faksnumarası6,faksnumarası7,faksnumarası8,faksnumarası9,faksnumarası10,faksnumarası11,faksnumarası12,faksnumarası13,faksnumarası14,faksnumarası15,faksnumarası16,faksnumarası17,faksnumarası18,faksnumarası19,faksnumarası20,faksnumarası21,faksnumarası22,faksnumarası23,faksnumarası24,faksnumarası25,faksnumarası26,faksnumarası27,faksnumarası28,faksnumarası29,faksnumarası30,faksnumarası31,faksnumarası32,faksnumarası33,faksnumarası34,faksnumarası35,faksnumarası36,faksnumarası37,faksnumarası38,faksnumarası39,faksnumarası40,faksnumarası41,faksnumarası42,faksnumarası43,faksnumarası44,faksnumarası45,faksnumarası46,faksnumarası47,faksnumarası48,faksnumarası49,faksnumarası50,faksnumarası51,faksnumarası52,faksnumarası53,faksnumarası54,faksnumarası55,faksnumarası56],
    'Adres': [adres1,adres2,adres3,adres4,adres5,adres6,adres7,adres8,adres9,adres10,adres11,adres12,adres13,adres14,adres15,adres16,adres17,adres18,adres19,adres20,adres21,adres22,adres23,adres24,adres25,adres26,adres27,adres28,adres29,adres30,adres31,adres32,adres33,adres34,adres35,adres36,adres37,adres38,adres39,adres40,adres41,adres42,adres43,adres44,adres45,adres46,adres47,adres48,adres49, adres50,adres51,adres52,adres53,adres54,adres55,adres56],
    'İlçe': [ilçe1,ilçe2,ilçe3,ilçe4,ilçe5,ilçe6,ilçe7,ilçe8,ilçe9,ilçe10,ilçe11,ilçe12,ilçe13,ilçe14,ilçe15,ilçe16,ilçe17,ilçe18,ilçe19,ilçe20,ilçe21,ilçe22,ilçe23,ilçe24,ilçe25,ilçe26,ilçe27,ilçe28,ilçe29,ilçe30,ilçe31,ilçe32,ilçe33,ilçe34,ilçe35,ilçe36,ilçe37,ilçe38,ilçe39,ilçe40,ilçe41,ilçe42,ilçe43,ilçe44,ilçe45,ilçe46,ilçe47,ilçe48,ilçe49, ilçe50,ilçe51,ilçe52,ilçe53,ilçe54,ilçe55,ilçe56],
    'İl': [il1,il2,il3,il4,il5,il6,il7,il8,il9,il10,il11,il12,il13,il14,il15,il16,il17,il18,il19,il20,il21,il22,il23,il24,il25,il26,il27,il28,il29,il30,il31,il32,il33,il34,il35,il36,il37,il38,il39,il40,il41,il42,il43,il44,il45,il46,il47,il48,il49, il50,il51,il52,il53,il54,il55,il56]
}

df1 = pd.DataFrame(data1, columns= ["Hastane Adı","Telefon Numarası","Faks Numarası","Adres","İlçe","İl"])
df1.to_excel('AdanaHastaneler.xlsx',index = False)

