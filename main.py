import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    body = {"long_url": url}

    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        json=body,
        headers=headers,
    )
    response.raise_for_status()

    response_text = response.json()
    bitlink = response_text['link']
    return bitlink


def count_clicks(link, token):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'units': -1}

    parsed_link = urlparse(link)
    cut_link = f'{parsed_link.netloc}{parsed_link.path}'

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{cut_link}/clicks/summary'

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    response_text = response.json()
    clicks_count = response_text['total_clicks']
    return clicks_count


def is_bitlink(url, token):
    headers = {'Authorization': f'Bearer {token}'}

    parsed_link = urlparse(url)
    cut_link = f'{parsed_link.netloc}{parsed_link.path}'

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{cut_link}'

    response = requests.get(url, headers=headers)

    return response.ok


if __name__ == '__main__':
    load_dotenv()

    token = os.environ['BITLY_TOKEN']

    parser = argparse.ArgumentParser(
        description='Link shortener and clicks calculator'
        )
    parser.add_argument('link_or_bitlink', help='link or bitlink')
    args = parser.parse_args()
    link = args.link_or_bitlink
        try:
            if is_bitlink(link, token):
                print(count_clicks(link, token))
            else:
                print('Bitlink', shorten_link(link, token))
        except requests.exceptions.HTTPError:
            print("You have entered an invalid affinity.")
