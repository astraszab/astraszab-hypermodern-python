"""Client for the Wikipedia REST API, version 1."""

from dataclasses import dataclass
from typing import cast

import click
import desert
import marshmallow
import requests


API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


@dataclass
class Page:
    """Page resource.

    Attributes:
        title: The title of the Wikipedia page.
        extract: A plain text summary.
    """

    title: str
    extract: str


schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})


def random_page(language: str = "en") -> Page:
    url = API_URL.format(language=language)

    try:
        with requests.get(url, timeout=1) as response:
            response.raise_for_status()
            data = response.json()
            return cast(Page, schema.load(data))
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from None
