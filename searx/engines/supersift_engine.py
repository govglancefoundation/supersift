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
    params['url'] = f"http://134.122.22.254/search/?q={_query}&limit=1&skip=0"

    # params['headers']['Referer'] = site_url.format(query=urlencode({'i': query}))
    params['method'] = 'GET'
    params['headers']['Content-type'] = "application/json"
    params['headers']['X-API-Key'] = f"{api_key}"

    return params


# get response from search-request
def response(resp):
    results = []
    json_result = loads(resp.text)
    
    title = "Supersift Engine"
    results.append(
            {
                'title': f'{title}',
                'id': '',
                'content': response_content,
                'urls': sources_results,
                'template': 'default.html'
            }
        )
        
    return results
