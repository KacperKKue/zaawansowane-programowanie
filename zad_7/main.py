
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
            f"Województwo/stan: {self.state_province or '-'}\n"
            f"Kod pocztowy: {self.postal_code or '-'}\n"
            f"Kraj: {self.country or '-'}\n"
            f"Długość geograficzna: {self.longitude or '-'}\n"
            f"Szerokość geograficzna: {self.latitude or '-'}\n"
            f"Telefon: {self.phone or '-'}\n"
            f"Strona WWW: {self.website_url or '-'}"
        )


def main() -> None:
    try:
        response = requests.get(
            API_URL,
            params={"per_page": 20},
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()

        breweries = [Brewery(**item) for item in data]

        for brewery in breweries:
            print(brewery)
            print("-" * 50)

    except requests.RequestException as error:
        print(f"Błąd połączenia z API: {error}")
    except (ValueError, TypeError) as error:
        print(f"Błąd przetwarzania danych: {error}")


if __name__ == "__main__":
    main()
