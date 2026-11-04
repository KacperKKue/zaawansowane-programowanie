
import argparse
from dataclasses import dataclass
from typing import Optional

import requests


API_URL = "https://api.openbrewerydb.org/v1/breweries"


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: Optional[str]
    state_province: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    longitude: Optional[str]
    latitude: Optional[str]
    phone: Optional[str]
    website_url: Optional[str]
    state: Optional[str]
    street: Optional[str]

    def __str__(self) -> str:
        return (
            f"Browar: {self.name}\n"
            f"ID: {self.id}\n"
            f"Typ: {self.brewery_type}\n"
            f"Adres: {self.address_1 or '-'}\n"
            f"Miasto: {self.city or '-'}\n"
            f"Stan/region: {self.state_province or '-'}\n"
            f"Kod pocztowy: {self.postal_code or '-'}\n"
            f"Kraj: {self.country or '-'}\n"
            f"Telefon: {self.phone or '-'}\n"
            f"Strona WWW: {self.website_url or '-'}"
        )


def get_breweries(city: Optional[str] = None) -> list[Brewery]:
    params = {"per_page": 20}

    if city:
        params["by_city"] = city

    response = requests.get(
        API_URL,
        params=params,
        timeout=15,
    )
    response.raise_for_status()

    data = response.json()
    return [Brewery(**item) for item in data]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pobieranie browarów z Open Brewery DB"
    )
    parser.add_argument(
        "--city",
        type=str,
    )
    args = parser.parse_args()

    try:
        breweries = get_breweries(args.city)

        if not breweries:
            print("Nie znaleziono browarów dla podanych kryteriów.")
            return

        print(f"Liczba pobranych browarów: {len(breweries)}\n")

        for brewery in breweries:
            print(brewery)
            print("-" * 50)

    except requests.RequestException as error:
        print(f"Błąd połączenia z API: {error}")
    except (ValueError, TypeError) as error:
        print(f"Błąd przetwarzania danych: {error}")


if __name__ == "__main__":
    main()
