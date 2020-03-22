from typing import Any, List
from dataclasses import dataclass
import os
import time

import requests
import xmltodict


@dataclass
class Weather:
    temperature: float
    condition: str
    condition_icon: str  # corresponds to an icon image file in static/images/
    forecasts: List[Any]

    @classmethod
    def parse(cls, xmldict) -> "Weather":
        temperature = float(
            xmldict["siteData"]["currentConditions"]["temperature"]["#text"]
        )
        condition = xmldict["siteData"]["currentConditions"]["condition"]
        condition_icon = xmldict["siteData"]["currentConditions"]["iconCode"]["#text"]

        raw_forecasts = xmldict["siteData"]["forecastGroup"]["forecast"][0:3]
        forecasts = [
            (
                x["abbreviatedForecast"]["textSummary"],
                x["abbreviatedForecast"]["iconCode"]["#text"],
                x["temperatures"]["textSummary"],
            )
            for x in raw_forecasts
        ]

        return Weather(
            temperature=temperature,
            condition=condition,
            condition_icon=condition_icon,
            forecasts=forecasts,
        )


def fetch(force=False):
    cache = "latest.xml"

    if force or is_old(cache):
        print('fetching fresh...')
        response = requests.get(
            "https://dd.weather.gc.ca/citypage_weather/xml/ON/s0000430_e.xml"
        )
        response.raise_for_status()
        content = response.text
        with open(cache, "w", encoding="latin-1") as file:
            file.write(content)
    else:
        print('using cache')
        with open(cache, "r", encoding="latin-1") as file:
            content = file.read()


    return Weather.parse(xmltodict.parse(content))

def is_old(path) -> bool:
    fifteen_minutes = 60 * 15
    return (time.time() - os.path.getmtime(path)) > fifteen_minutes