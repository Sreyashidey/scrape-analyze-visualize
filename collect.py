from bs4 import BeautifulSoup
import os
import csv
from datetime import datetime

path_to_html_folder = "data"
output_csv = "output.csv"
def convert_rating_count(rating_count):
    if "K" in rating_count:
        return int(float(rating_count.replace("K", "").strip()) * 1000)
    elif "M" in rating_count:
        return int(float(rating_count.replace("M", "").strip()) * 1000000)
    else:
        try:
            return int(rating_count)
        except ValueError:
            return 0

data = []
rank_counter = 1

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


for filename in os.listdir(path_to_html_folder):
    if filename.endswith(".html"):
        file_path = os.path.join(path_to_html_folder, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

            
            product_containers = soup.find_all("div", class_="sc-57fe1f38-0 eSrvHE")  

            for product in product_containers:
                
                link_tag = product.find("a", href=True)
                sku = link_tag['href'].split("/")[-3] if link_tag else "N/A"

                product_name_div = product.find("div", {"data-qa": "product-name"})
                if product_name_div:
                    product_name = product_name_div.get('title', "N/A")
                    #brand_span = product_name_div.find("span")
                    brand = product_name.split()[0]if product_name else "N/A"
                else:
                    product_name = "N/A"
                    brand = "N/A"
                rating_div = product.find("div", class_="sc-9cb63f72-2 dGLdNc")
                average_rating = rating_div.text.strip() if rating_div else "0"

                
                rating_count_span = product.find("span", class_="sc-9cb63f72-5 DkxLK")
                rating_count = rating_count_span.text.strip() if rating_count_span else "0"
                rating_count = convert_rating_count(rating_count)
                sponsored = "Y" if product.find("div", class_="sc-95ea18ef-24 gzboVs") else "N"
                
                old_price_span = product.find("span", class_="oldPrice")
                if old_price_span:
                    old_price = old_price_span.text.strip() if old_price_span else "N/A"
                else:
                    old_price = "N/A"
                sales_price_div = product.find("div", class_="sc-97957b12-1 fYKLkk")
                if sales_price_div:
                    amount = sales_price_div.find("strong", class_="amount")
                    sales_price = amount.text.strip() if amount else "N/A"
                else:
                    sales_price = "N/A"
                if old_price == "N/A":
                    price = sales_price  
                else:
                    price = old_price
                express = "Y" if product.find("div", class_="sc-d376b94d-3 dFzhiL") else "N"
               
                rank = rank_counter
                rank_counter += 1

                link = link_tag['href'] if link_tag else "N/A"

                
                data.append([
                    current_time, sku, product_name, brand, average_rating,
                    rating_count, sponsored, price, sales_price, express, rank, link
                ])


headers = [
    "Date and Time", "SKU", "Name", "Brand", "Average Rating",
    "Rating Count", "Sponsored", "Price", "Sales Price", "Express", "Rank", "Link"
]

with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Data extraction complete. CSV saved as {output_csv}")

                

