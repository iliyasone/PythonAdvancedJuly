import requests

url = 'https://api.thecatapi.com/v1/images/search?limit=10'

def main():
    response = requests.get(url).json()

    url_cats = []
    for data in response:
        url_cats.append(data['url'])
        
    for i in range(10):
        file = open(f'cat{i}.jpg', 'wb')
        file.write(
            requests.get(url_cats[i]).content
            )
        file.close()
        
if __name__ == "__main__":
    main()