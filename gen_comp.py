id_token = \
    't.LXDG3NQizbFMYo8IUfbpc6xCw1zVzU0dXR7IKWDLgDnhVy58tommf_rOTC9Lfp6bBzJrdU_yG8GSrk7AhnmFgQ'
from datetime import datetime, timedelta

from tinkoff.invest import CandleInterval, Client, LastPrice
from tinkoff.invest.token import TOKEN


def main():
    with Client(TOKEN) as client:
        for candle in client.get_all_candles(
                figi="BBG004730N88",
                from_=datetime.utcnow() - timedelta(days=365),
                interval=CandleInterval.CANDLE_INTERVAL_HOUR,
        ):
            print(candle)

    return 0


def main1():
    with Client(TOKEN) as client:
        i = client.market_data.get_last_prices(figi="BBG0013HGFT4")
        print(i)

    return 0


def course():
    with Client(TOKEN) as client:
        id_acc = client.users.get_accounts().accounts[0].id
        ddd = client.operations.get_portfolio(account_id=id_acc)
        return ddd.positions[0].current_price.units


budget = 285
max_cost = ['']
acces = ('термопаста', 'провод', 'адаптер', 'флешка')
components = ['оперативная память', 'корпус', 'блок питания', 'ссд', 'кулер', 'клавиатура', acces]
usd1 = 98.5
usd2 = 102.4
url = ['https://www.nix.ru/autocatalog/memory_modules_Crucial/temporary_product_page_456927.html',
       '-',
       'https://www.mvideo.ru/products/blok-pitaniya-dlya-komputera-gigabyte-gp-p850gm-30057594',
       'https://www.oldi.ru/catalog/element/01062352/?utm_source=Nadavi&utm_medium=cpc&utm_campaign=oldi&utm_term=01062352&utm_content=728',
       '-', '-', '-']
prices = [25003, 7899, (12499+199), (8720+290), 7149, 5000, (1050+720+779)+750]
prices_usd = [25003/usd2, 7899/usd1, (12499+199)/usd2, (8720+290)/usd2, 7149/usd1, 5000/usd2,
              ((1050+720+779)+750)/usd1]
comp_ost = ['блок питания', 'ссд', 'клавиатура']
prices_ost = ['13000', '13000', '3000']
last_comp = ['клавиатура', 'вентилятор']
# print(sum(prices))
res = {x: y for (x, y) in zip(components, prices)}
print(res, sum(prices_usd), sum(prices), sep='\n')