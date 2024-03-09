# SPDX-License-Identifier: AGPL-3.0-or-later

from json import loads
from dateutil import parser
from urllib.parse import urlencode
from searx.exceptions import SearxEngineAPIException
import anthropic
import json

# about
about = {
    "website": 'https://www.anthropic.com',
    # "wikidata_id": 'Q866',
    "official_api_documentation": 'https://docs.anthropic.com/claude/reference/getting-started-with-the-api',
    "use_official_api": True,
    "require_api_key": True,
    "results": 'JSON',
}


# engine dependent config
categories = ['ai', 'general']
paging = False
api_key = None

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key= api_key
)
# do search-request
def request(query, params):
    content_block = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="Super Sift Claude Search is a search assistant that finds the best and most official sources.\n\nIt only responds in JSON format that must contain 1 short concise written response to the query along with 5 of the best sources that must contain a title and https link to the webpage.",
        messages =
            [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"{query}"
                        }
                    ]
                }
            ]
        )

    return content_block

# get response from search-request
def response(resp):

    content_block = resp

    text_content = content_block[0].text

    search_results = json.loads(text_content)

    results = []


    # return empty array if there are no results
    if 'items' not in search_results:
        return []

    if 'response' in search_results:
        results.append(
            {
                'url': None,
                'title': search_results['response'],
                'response': None,
                'template': 'key-value.html'
            }
        )
    # parse results

    for result in search_results['source']:

        # append result
        results.append(
            {
                'url': result['link'],
                'title': result['title'],
            }
        )

    # return results
    return results
