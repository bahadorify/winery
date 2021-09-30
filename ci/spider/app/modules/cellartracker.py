#!/usr/bin/env python3
import re

import requests
from lxml import html
from unidecode import unidecode

from . import logging


def scorer(score, integer=False):
    """Use this helper to safely convert score."""
    score = re.sub(r'[A-Za-z ]+', '', score)
    try:
        if not integer:
            return float(score)
        return int(score)
    except ValueError:
        return score


def matches_parser(matches, url_template, y, wine):
    """Use this helper to get matches."""
    for i in matches:
        potential = i.xpath('string(./div/a[contains(@href, "m")])')
        logging.info(f'\t\t{potential}')
        if unidecode(i.xpath('string(./div/a[contains(@href, "m")])')).lower() == \
                f'{y} {wine}'.lower().replace('`', "'"):
            logging.info("\tWine found!")
            score = i.xpath('string(./div[@class="wine-result-data"]/div/span)')
            id_num = re.sub(r'\D', '', i.xpath('string(./div/a[contains(@href, "m")]/@href)'))
            link = url_template.format(id_num)
            response = requests.get(link)
            tree = html.fromstring(response.text)
            reviews = tree.xpath('string(//div[@class="scores"]/span)')
            return scorer(score), scorer(reviews, integer=True), link
    return None, None, None


def parse_score(wine, y, producer, district):
    """Get the CT of the wine."""
    logging.info(f' Processing "{y} {wine}"')
    url_template = "https://www.cellartracker.com/wine.asp?iWine={}"
    response = requests.get(
        f"https://www.cellartracker.com/m/wines/search?q={producer} {wine} {y}&o=Quantity+DESC"
    )
    tree = html.fromstring(response.text)
    matches = tree.xpath('//div[@class="wine-result"]')

    # Only one wine found and it was opened as page
    if not matches:
        score = tree.xpath('string(//div[@class="scores"]/a)')
        reviews = tree.xpath('string(//div[@class="scores"]/span)')
        id_num = re.sub(r'\D', '', response.url)
        if score:
            logging.info("\tWine found!")
            return scorer(score), scorer(reviews, integer=True), url_template.format(id_num)
    logging.info(f'\tFound {len(matches)} matches')

    # Multiple matches are found
    processed_matches = matches_parser(matches, url_template, y, wine)
    if processed_matches:
        return processed_matches

    # No exact match found in results
    response = requests.get(
        f"https://www.cellartracker.com/m/wines/search?q={producer} {wine} {y} {district}&o=Quantity+DESC"
    )
    tree = html.fromstring(response.text)
    matches = tree.xpath('//div[@class="wine-result"]')
    logging.info("\tSelecting possibly matching wine!")
    if matches:
        processed_matches = matches_parser(matches, url_template, y, wine)
        if processed_matches:
            return processed_matches

        score = matches[0].xpath('string(./div[@class="wine-result-data"]/div/span)')
        id_num = re.sub(r'\D', '', matches[0].xpath('string(./div/a[contains(@href, "m")]/@href)'))
        link = url_template.format(id_num)
        response = requests.get(link)
        tree = html.fromstring(response.text)
        reviews = tree.xpath('string(//div[@class="scores"]/span)')

        return scorer(score), scorer(reviews, integer=True), url_template.format(id_num)

    logging.info("\tWine not found")
    return None, None, None
