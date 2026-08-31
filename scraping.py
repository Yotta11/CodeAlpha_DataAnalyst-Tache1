import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
CATALOGUE_URL = urljoin(BASE_URL, "catalogue/page-{}.html")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


data = []


def convert_rating(rating):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating)

def scrape_page(page_number):
    url = CATALOGUE_URL.format(page_number)
    print(f"Scraping de la page {page_number} : {url}")
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            print(f"Erreur HTTP : {response.status_code}")
            return

        response.encoding = "utf-8"

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        books = soup.find_all(
            "article",
            class_="product_pod"
        )

        print(f"{len(books)} livres trouvés.")

        for book in books:

            title_tag = book.find("h3").find("a")
            title = title_tag.get("title", "").strip()

            relative_url = title_tag.get("href")
            book_url = urljoin(url, relative_url)

            price_tag = book.find(
                "p",
                class_="price_color"
            )

            price = price_tag.get_text(strip=True)

            price = (
                price
                .replace("Â", "")
                .replace("£", "")
                .strip()
            )

            try:
                price = float(price)
            except ValueError:
                price = None

            availability_tag = book.find(
                "p",
                class_="availability"
            )

            availability = availability_tag.get_text(
                strip=True
            )

            rating_tag = book.find(
                "p",
                class_="star-rating"
            )

            rating_classes = rating_tag.get("class", [])

            rating = None

            if len(rating_classes) > 1:
                rating = convert_rating(
                    rating_classes[1]
                )

            image_tag = book.find("img")

            image_url = None

            if image_tag:
                image_url = urljoin(
                    url,
                    image_tag.get("src")
                )

            data.append({
                "titre": title,
                "prix_gbp": price,
                "note": rating,
                "disponibilite": availability,
                "url_livre": book_url,
                "url_image": image_url
            })

    except requests.exceptions.RequestException as error:
        print(f"Erreur de connexion : {error}")


for page in range(1, 51):
    scrape_page(page)
    time.sleep(1)

df = pd.DataFrame(data)

df = df.drop_duplicates()

df = df.dropna(
    subset=["titre"]
)

df = df.reset_index(drop=True)

print("\n========== INFORMATIONS ==========")

print(f"Nombre de lignes : {df.shape[0]}")
print(f"Nombre de colonnes : {df.shape[1]}")

print("\nColonnes :")
print(df.columns.tolist())

print("\nAperçu :")
print(df.head())

print("\nValeurs manquantes :")
print(df.isnull().sum())

df.to_csv(
    "books_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n===================================")
print("SCRAPING TERMINÉ")
print("===================================")
print(f"Dataset créé avec {len(df)} livres.")
print("Fichier : books_dataset.csv")
