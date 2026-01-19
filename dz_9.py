import requests


class CurrencyConverter:

    NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    def __init__(self):
        self.usd_rate = self._get_usd_rate()

    def _get_usd_rate(self) -> float:
        response = requests.get(self.NBU_API_URL)
        response.raise_for_status()

        data = response.json()
        for currency in data:
            if currency["cc"] == "USD":
                return currency["rate"]

        raise ValueError("Курс USD не знайдено")

    def uah_to_usd(self, amount_uah: float) -> float:
        return amount_uah / self.usd_rate


def main():
    print("Конвертер валют (UAH → USD)")
    print("Отримання курсу з НБУ...")

    try:
        converter = CurrencyConverter()
        print(f"Актуальний курс USD: {converter.usd_rate:.2f} грн")

        amount = float(input("Введіть суму в гривнях: "))
        result = converter.uah_to_usd(amount)

        print(f"{amount:.2f} грн = {result:.2f} USD")

    except Exception as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()
