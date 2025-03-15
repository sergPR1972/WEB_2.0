import asyncio
import aiohttp
from datetime import date, timedelta
import sys
import logging

logging.basicConfig(level=logging.INFO)


async def request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    r = await response.json()
                    return r
                logging.error(f"Error status {response.status} for {url}")
        except aiohttp.ClientConnectorError as e:
            logging.error(f"Connection error {url}: {e}")
        return None


async def get_exchange(delta_day):
    date_delta = (date.today() - timedelta(days=delta_day)).strftime('%d.%m.%Y')
    url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date_delta}"
    res = await request(url)
    exchange, *_ = list(filter(lambda el: el['currency'] == 'EUR', res['exchangeRate']))
    exchange_US, *_ = list(filter(lambda el: el['currency'] == 'USD', res['exchangeRate']))

    dict_exchange_day = {res['date']: {'EUR': {'sale': exchange['saleRate'], 'purchase': exchange['purchaseRate']}},
                         'USD': {'sale': exchange_US['saleRate'], 'purchase': exchange_US['purchaseRate']}}

    return dict_exchange_day


async def calculate_days():
    bank = []
    try:
        delta_days = int(sys.argv[1])
        if 0 <= delta_days <= 10:
            for el in range(1, delta_days+1):
                r = await get_exchange(el)
                bank.append(r)
        else:
            logging.warning("Date is larger of 10 days.")
    except (ValueError, IndexError) as err:
        logging.error(err)
    return bank


async def main():
    results_exchange = await calculate_days()
    return results_exchange


if __name__ == '__main__':
    result_exchange = asyncio.run(main())
    print(result_exchange)
