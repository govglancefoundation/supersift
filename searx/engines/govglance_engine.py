# SPDX-License-Identifier: AGPL-3.0-or-later
"""
 Anthropic (Science)
"""

from json import loads, dumps

# about
about = {
    "website": 'https://www.supersift.net',
    "wikidata_id": '',
    "official_api_documentation": 'https://api.supersift.net/docs',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSON',
}

categories = ['general']
# search-url
api_key = ''  # defined in settings.yml


# do search-request
def request(_query, params):
    params['url'] = f"https://api.govglance.org/search/?limit=10&skip=0&search_term={_query}"

    # params['headers']['Referer'] = site_url.format(query=urlencode({'i': query}))
    params['headers'] = {'Authorization': 'Bearer ' + api_key}

    return params


# get response from search-request
def response(resp):
    results = []
    json_result = loads(resp.text)
    print(json_result)
    title = "Gov Glance Engine"
    for result in json_result:
        results.append(
                {
                    'title': result['title'],
                    'id': '',
                    'content': result['description'],
                    'url': result['url'],
                }
            )
        
    return results
