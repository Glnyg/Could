import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}


def get_card_url(card: str):
    return f'https://bff.gds.org.cn/gds/searching-api/ProductService/ProductListByGTIN?PageSize=30&PageIndex=1&SearchItem={card:0>14}'


def get_snack_json(card: str):
    url = get_card_url(card)
    res = httpx.get(
        url=url,
        headers=headers,
        timeout=10,
        verify=False)
    return res.json()
