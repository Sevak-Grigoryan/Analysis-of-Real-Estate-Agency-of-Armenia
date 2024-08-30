from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import time
import csv


# Web Scraping:

value = 390
driver = webdriver.Chrome()
# -----------------------------------Senyak.am-----------------------------------------------
try:
    driver.get(url = "https://www.senyak.am/")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#responsive > li:nth-child(1) > a").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#titlebar > div > div.row.text-center.big-block > div.col-md-20-percent.col-xs-100-percent.padding-top-10.padding-bottom-10").click()
    time.sleep(3)
    info = [["Տարածաշրջան", "Շինության տիպ", "Սենյակներ", "Մակերես", "Հարկ", "Վերանորոգում" , "Գինը"]]
    for i in range(171, 201):
        for j in range(1, 44):
            try:
                new_list = []
                driver.find_element(By.CSS_SELECTOR, f"#propListContainer > article:nth-child({j}) > div > div > div.listing-title > h2 > a").click()
                time.sleep(1)
                for l in range(1 , 8):
                    try:
                        if l == 6:
                            continue
                        content = driver.find_element(By.CSS_SELECTOR, f"#wrapper > main > div:nth-child(1) > div > div > div.col-lg-4.col-md-5 > table > tbody > tr:nth-child({l}) > td").text
                        time.sleep(2)
                        if content[-1] == "²":
                            content = content[:-2]
                        if "/" in content:
                            content = content.split("/")[0]
                        new_list.append(content)
                        time.sleep(2)
                    except:
                        continue
                try:
                    try:
                        price = driver.find_element(By.CSS_SELECTOR , "#wrapper > main > div:nth-child(1) > div.container > div > div.col-lg-4.col-md-5 > div.h3.text-right.margin-top-0 > span").text
                    except:
                        price = driver.find_element(By.CSS_SELECTOR , "#wrapper > main > div:nth-child(1) > div.container > div > div.col-lg-4.col-md-5 > div.h3.text-right.margin-top-0").text
                except:
                    continue
                price = price.replace(" " , "")
                if len(price) > 7 and price[0].isdigit() == False:
                    price = float(int(str(price[1:]))/value)
                    price = "$" + price
                elif len(price) > 7 and price[-1].isdigit() == False:
                    price = float(int(str(price[:-1]))/value)
                    price = "$" + price
                new_list.append(str(price))
                if len(new_list) == 7:
                    info.append(new_list)
                driver.back()
                time.sleep(1)
            except:
                if i == 43:
                    break
                else:
                    continue
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#paginationId > nav.pagination-next-prev > ul > li:nth-child(2) > a").click()
        time.sleep(2)
    time.sleep(2)
except Exception as exx:
    print(exx)


# ----------------------------------------Banaly.am-------------------------------------------------------
try:
    driver.get(url="https://banali.am/vachark/ansharzh-guik-yerevanum")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR , "#app > div.search-page-main.extend-ui > div.search-box > div.search-page-top > div.priority-navigation.main-filters > div > div:nth-child(3) > div > div.filter-summary").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR , "#app > div.search-page-main.extend-ui > div.search-box > div.search-page-top > div.priority-navigation.main-filters > div > div:nth-child(3) > div > div.filter-dropdown > div.filter-content.property_type-content > ul > li:nth-child(1) > div").click()
    time.sleep(2)
    info = []
    columns = ["Տարածաշրջան", "Շինության տիպ", "Սենյակներ", "Մակերես", "Հարկ", "Վերանորոգում" , "Գինը"]
    for j in range(10):
        for i in range(1 , 11):
            time.sleep(2)
            new_listik = []
            try:
                driver.find_element(By.CSS_SELECTOR , f"#app > div.search-page-main.extend-ui > div.d-flex.results-wrapper.mobile-is-post-view > div.scrolling-view-port > div.post-list > div.posts.layout-search > div:nth-child({i}) > a").click()
                time.sleep(2)
            except:
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR , "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div.post-address").text
                full_address = content
                content = ", ".join(content.split(", ")[:2])
                content = content.replace("-" , " ")
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR , "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(3) > div > div._1scNe5JZvUHaGWJa_A_StX > div:nth-child(2) > div.amenity-info" ).text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR , "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(1) > div.amenity-info").text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR , "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(2) > div.amenity-info").text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR , "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > ul > li:nth-child(3) > span").text
                content = content.split("/")[0]
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR , "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(6) > div.amenity-info").text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR , "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div.price-section > span.price-val > div").text
                content = content.replace("," , "")
                content = int(int(content)/390)
                content = "$" + str(content)
                new_listik.append(content)
            except:
                driver.back()
                continue
            time.sleep(2)
            if i > 5:
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            if new_listik in info == False:
                info.append(new_listik)
            driver.back()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR , "#pagination > a:nth-child(7)").click()
        time.sleep(3)


except Exception as exx:
    print(f"Error: {exx}")

finally:
    driver.close()
    driver.quit()


# --------------------------- Data Cleaning: -----------------------------

df = pd.read_csv("final_DataBase.csv")

# Append Data in your DataSet:

try:
    with open('DataBase.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(info)
    print("CSV file created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# Connection 2 CSV files:

df1 = pd.read_csv("Cleaned_Data.csv")
df2 = pd.read_csv("modified_file.csv")


result = pd.concat([df1, df2])

result.to_csv("result.csv", index=False)

print("CSV files combined and saved as 'result.csv'")

# Clean Dublicates:

df = pd.read_csv('result.csv')

df_cleaned = df.drop_duplicates()

df_cleaned.to_csv('Cleaned_result.csv', index=False)

# --------------------------- Data Preprocessing:-----------------------------

# Data Encoding

label_encoder = LabelEncoder()

encoded_df = df.copy()
for column in encoded_df.select_dtypes(include=['object']).columns:
    encoded_df[column] = label_encoder.fit_transform(encoded_df[column])

encoded_df.head()

# Data Standartization:

plt.figure(figsize=(14, 8))
scaler = StandardScaler().fit(encoded_df)
standardized_X = scaler.transform(encoded_df)
plt.plot(standardized_X)
plt.show()

# Data Normalization:

plt.figure(figsize=(14, 8))
scaler = Normalizer().fit(encoded_df)
normalized_X = scaler.transform(encoded_df)
plt.plot(normalized_X)
plt.show()

# ---------------------- Data Analysis (Exploratory Data Analysis (EDA)): ----------------------------

# The count of values:

# -------------------------------------

plt.figure(figsize=(14, 8))
plt.subplot(2, 3, 1)
sns.histplot(df['Մակերես'])
plt.xticks(rotation = 90)
plt.title("Square")
plt.subplot(2, 3, 3)
sns.histplot(df['Սենյակներ'])
plt.xticks(rotation = 90, fontsize = 8)
plt.title("Rooms")

# -------------------------------------

plt.figure(figsize=(14, 8))
plt.subplot(2, 3, 1)
sns.histplot(df['Վերանորոգում'])
plt.xticks(rotation = 90)
plt.title("Repair")
plt.subplot(2, 3, 3)
sns.histplot(df['Շինության տիպ'])
plt.xticks(rotation = 90, fontsize = 8)
plt.title("Building type")

# Correlation of Analysis:

df_corr = encoded_df.corr(numeric_only=True)

# vizualisation of correlation

sns.heatmap(df_corr, annot=True)


# To Compair Values with each other

# ----------------------------

sns.barplot(x=encoded_df['Մակերես'] - 5, y=df['Սենյակներ'], color='blue', label='Square', alpha= 1)
plt.title("Bar plot comparison between Square and Rooms")
plt.ylabel("Category")
plt.xlabel("Values")
plt.legend()
plt.show()

# ----------------------------

sns.barplot(x=encoded_df['Տարածաշրջան'] - 2, y=encoded_df['Գինը'], color='blue', label='Place', alpha=1.0)
plt.title("Bar plot comparison between Place and Price")
plt.xlabel("Category")
plt.xticks(rotation = 90, fontsize = 8)
plt.ylabel("Values")
plt.legend()
plt.show()

# ----------------------------

sns.barplot(x=encoded_df['Հարկ'] - 2, y=encoded_df['Գինը'], color='blue', label='Floor', alpha=1.0)
plt.title("Bar plot comparison between Floor and Price")
plt.xlabel("Category")
plt.xticks(rotation = 90, fontsize = 8)
plt.ylabel("Values")
plt.legend()
plt.show()

# ----------------------------

sns.barplot(x=encoded_df['Տարածաշրջան'] - 2, y=encoded_df['Վերանորոգում'], color='blue', label='Տարածաշրջան', alpha=0.3)
sns.barplot(x=encoded_df['Տարածաշրջան'], y=encoded_df['Վերանորոգում'], color='red', label='Վերանորոգում', alpha=0.3)
plt.title("Bar plot comparison between Տարածաշրջան and Վերանորոգում")
plt.xlabel("Category")
plt.xticks(rotation = 90, fontsize = 8)
plt.ylabel("Values")
plt.legend()
plt.show()