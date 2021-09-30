#!/usr/bin/env python3
import logging
import simplejson

import requests

from modules.cellartracker import parse_score
from modules.mongoo import client

###
# Configuration
# Logging
logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
                    level=logging.INFO, datefmt='%Y/%m/%dT%H:%M:%S')

# Requests headers and links
headers = {"X-Requested-With": "XMLHttpRequest",
           "User-Agent":
               ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "Version/14.0.2 Safari/605.1.15")}
domain = "https://www.vinmonopolet.no"
catalog = ("{}/api/search?q=:relevance:visibleInSearch:true:mainCategory:{}"
           "&searchType=product&fields=FULL&pageSize=100&currentPage={}")
item = "{}/api/products/{}?fields=FULL"

# DB objects
db = client["wines"]
coll = db[f"vinmonopolet"]

# Session
requests = requests.Session()
requests.get(domain)


def parse_wine_details(wine):
    """Use this parser to parse full wine JSON data and write into DB."""
    logging.info(f"Wine: {wine}")
    try:
        response = requests.get(item.format(domain, wine), headers=headers).json()
        code = response["code"]
        score, reviews, link = parse_score(response["name"],
                                           response["year"],
                                           response["main_producer"]["name"],
                                           response["district"]["name"])
        logging.info(f"CT: {score}")
        response.update({"ct": {"score": score, "reviews": reviews, "link": link}})
        query = {"code": code}
        coll.replace_one(query, response, True)
    except simplejson.errors.JSONDecodeError as e:
        logging.critical(e)


def parse_wines(category):
    """Use this parser to get wines catalog items."""
    logging.info(f"Category: {category}")
    page = 0
    while True:
        logging.info(f"Page: {page}")
        response_json = None
        try:
            response = requests.get(catalog.format(domain, category, page))
            response_json = response.json()
            c_items = response_json["productSearchResult"]["products"]
            if not c_items:
                break
            [parse_wine_details(d["code"]) for d in c_items]
        except (simplejson.errors.JSONDecodeError, KeyError) as e:
            logging.critical(response_json)
            logging.critical(e)
        page += 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--categories", help="Categories of wines for scraping.",
                        nargs='+', required=True, choices=["rødvin", "hvitvin"])
    args = parser.parse_args()

    # List of categories to parse
    for cat in args.categories:
        parse_wines(cat)
