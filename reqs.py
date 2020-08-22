import requests


def main():
    payload = {'base': 'INR', 'symbols': 'USD'}
    response = requests.get('https://api.exchangeratesapi.io/latest',
                            params=payload)

    if response.status_code != 200:
        print(f'Status Code: {response.status_code}')
        raise Exception('Error!')

    data = response.json()
    print(f"JSON data: {data}")


if __name__ == '__main__':
    main()
