import pytest

import weather

@pytest.mark.vcr()
def test_weather_fetch():
    thing = weather.fetch()
    assert thing.temperature == 1.3
    assert thing.condition == "Mostly Cloudy"
    assert thing.condition_icon == "03"
