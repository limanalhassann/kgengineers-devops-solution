#!/usr/bin/env python3

import requests
import json
import sys
from typing import List, Dict
from operator import itemgetter

class BeerAPI:
    def __init__(self):
        self.primary_url = "https://api.punkapi.com/v2/beers"
        self.backup_url = "https://s3-eu-west-1.amazonaws.com/kg-it/devopsTest/api-punkapi-com-v2-beers.json"

    def get_beers(self) -> List[Dict]:
        """Fetch beers from API with fallback to backup URL"""
        try:
            response = requests.get(self.primary_url)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, json.JSONDecodeError) as e:
            print(f"Primary API failed, trying backup URL... ({str(e)})")
            try:
                response = requests.get(self.backup_url)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, json.JSONDecodeError) as e:
                print(f"Error fetching data from both URLs: {str(e)}")
                sys.exit(1)

    def print_all_beers(self, beers: List[Dict]):
        """Print all beer data"""
        print(json.dumps(beers, indent=2))

    def print_beer_csv(self, beers: List[Dict]):
        """Print beer name and ABV in CSV format"""
        for beer in beers:
            print(f"{beer['name']},{beer['abv']}")

    def filter_by_abv(self, beers: List[Dict], min_abv: float) -> List[Dict]:
        """Filter beers by minimum ABV"""
        return [beer for beer in beers if beer['abv'] >= min_abv]

    def sort_by_abv(self, beers: List[Dict], ascending: bool = False) -> List[Dict]:
        """Sort beers by ABV"""
        return sorted(beers, key=itemgetter('abv'), reverse=not ascending)

def main():
    min_abv = None
    if len(sys.argv) > 1:
        try:
            min_abv = float(sys.argv[1])
        except ValueError:
            print(f"Error: Invalid ABV value '{sys.argv[1]}'. Please provide a number.")
            sys.exit(1)

    api = BeerAPI()
    beers = api.get_beers()

    if min_abv is not None:
        beers = api.filter_by_abv(beers, min_abv)

    beers = api.sort_by_abv(beers)

    # Print results in CSV format
    api.print_beer_csv(beers)

if __name__ == "__main__":
    main()
