import requests
import pandas as pd
import csv

api_url = "https://api-berita-indonesia.vercel.app"


try:
    response = requests.get(api_url)
    data = response.json()['endpoints']
    df = pd.DataFrame(data)
    names = df['name']

    data_post = pd.DataFrame()

    for name in names:
        berita = api_url + "/" + name + "/terbaru"
        response = requests.get(berita)

        if response.status_code == 200:
            try:
                data = response.json()['data']['posts']
                df = pd.DataFrame(data)

                data_post = pd.concat([data_post, df], ignore_index=True)

            except KeyError:
                print(f"Data tidak ditemukan untuk nama {name}")

    data_post.to_csv("data_berita.csv", index=False)

except Exception as e:
    print(e)
