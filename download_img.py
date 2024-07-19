#hurtowe pobieranie obrazów z linków podanych w Excel 

import requests
import pandas

def download_images(urls, file_paths):
    if not urls or not file_paths or len(urls) != len(file_paths):
        return ["Invalid input. The number of URLs and file paths must be equal and non-empty."]

    status_messages = []

    for url, file_path in zip(urls, file_paths):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                status_messages.append(f"Downloaded and saved: {file_path}")
            else:
                status_messages.append(f"Failed to download from {url}. HTTP status code: {response.status_code}")
        except Exception as e:
            status_messages.append(f"Error occurred while downloading from {url}: {e}")

    return status_messages


#excel file with IMG links
file_path='excelfile.xlsx'

#dataframe structure definition
df = pandas.read_excel(file_path)
urls = df["Value"]
file_paths=df["name"]

#go through loop 
liczba_wierszy = urls.count()
licznik = 0 

for licznik in range(liczba_wierszy):
    download_images(urls, file_paths)
    print(urls[licznik])
