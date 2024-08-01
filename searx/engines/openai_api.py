# SPDX-License-Identifier: AGPL-3.0-or-later
"""
 OpenAI (Science)
"""

from json import loads, dumps

# about
about = {
    "website": 'https://www.wolframalpha.com',
    "wikidata_id": 'Q207006',
    "official_api_documentation": 'https://products.wolframalpha.com/api/',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSON',
}

categories = ['general']
# search-url
# search_url = 'https://api.wolframalpha.com/v2/query?appid={api_key}&{query}'
search_url = 'https://api.openai.com/v1/chat/completions'
# site_url = 'https://www.wolframalpha.com/input/?{query}'
api_key = ''  # defined in settings.yml


# do search-request
def request(_query, params):
    params['url'] = search_url
    # params['headers']['Referer'] = site_url.format(query=urlencode({'i': query}))
    params['method'] = 'POST'
    params['headers'] = {
    "Authorization": (f"Bearer {api_key}")
    }
    params['headers']['Content-type'] = "application/json"

    params['data'] = dumps({
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": '''Respond with an answer and website links to relevant sources. The response should be in the following JSON format {"response": "Example response", "links": ["https://example1.com", "https://example2.com"]}. Do not use newline syntax. Escape the the double qoutes if in the response value. Make sure the response value is in double qoutes. In the values use singles quotes Respond with 400 tokens or less.'''},
        {"role": "user", "content": f"{_query}"}
    ],
    "max_tokens": 500
    })
    return params


# get response from search-request
def response(resp):
    results = []

    json_result = loads(resp.text)
    data_openai = loads(json_result['choices'][0]['message']['content'])
    response_content = data_openai['response']
    sources_ai = data_openai['links']
    sources_results = []
    for source in sources_ai:
        sources_results.append({'title':source,'url': source})
    
    results.append(
            {
                'infobox': 'GPT-4o-mini',
                'id': '',
                'content': response_content,
                'urls': sources_results
            }
        )
        
    return results

    title = "Open AI: gpt-4o-mini (%s)" % infobox_title

    # append infobox
    results.append(
        {
            'infobox': infobox_title,
            # 'attributes': result_chunks,
            'urls': [{'title': 'OpenAI|gpt-4o-mini', 'url': resp.request.headers['Referer']}],
        }
    )

    # append link to site
    results.append({'url': resp.request.headers['Referer'], 'title': title, 'content': result_content})

    return results
