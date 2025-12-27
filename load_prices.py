import sqlite3
from scripts import webscrapers as wb


conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()
c.execute("""SELECT url_flipkart, url_jiomart, url_amazon
             FROM products_product""")
database_urls = c.fetchall()


for rows in database_urls:
    for url in rows:
        if "flipkart.com" in url:
            flipkart_price = wb.flipkart_scrape(url)
            # print(flipkart_price)
            c.execute("""UPDATE products_product
                         SET price_flipkart=?
                         WHERE url_flipkart=?""", (flipkart_price, url))

        elif "jiomart.co.uk" in url:
            jiomart_price = wb.jiomart_scrape(url)
            # print(jiomart_price)
            c.execute("""UPDATE products_product
                         SET price_jiomart = ?
                         WHERE url_jiomart=?""", (jiomart_price, url))

        elif "amazon.com" in url:
            amazon_price = wb.amazon_scrape(url)
            # print(amazon_price)
            c.execute("""UPDATE products_product
                         SET price_amazon=?
                         WHERE url_amazon=?""", (amazon_price, url))

        else:
            print("FLAG: Is the following url correct? {}".format(url))

conn.commit()
c.close()
conn.close()