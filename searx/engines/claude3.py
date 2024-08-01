# SPDX-License-Identifier: AGPL-3.0-or-later
"""
 Anthropic (Science)
"""

from json import loads, dumps

# about
about = {
    "website": 'https://www.anthropic.com',
    "wikidata_id": '',
    "official_api_documentation": 'https://docs.anthropic.com/en/api/getting-started',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSON',
}

categories = ['general', 'ai']
# search-url
search_url = "https://api.anthropic.com/v1/messages"
api_key = ''  # defined in settings.yml


# do search-request
def request(_query, params):
    params['url'] = search_url
    # params['headers']['Referer'] = site_url.format(query=urlencode({'i': query}))
    params['method'] = 'POST'
    params['headers']['Content-type'] = "application/json"
    params['headers']['X-API-Key'] = f"{api_key}"
    params['headers']["Anthropic-Version"] = "2023-06-01"

    params['data'] = dumps({
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 500,
    "system": '''Respond with an answer and website links to relevant sources. The response should be in the following JSON format {"response": "Example response", "links": ["https://example1.com", "https://example2.com"]}. Do not use newline syntax. Escape the the double qoutes if in the response value. Make sure the response value is in double qoutes. In the values use singles quotes Respond with 400 tokens or less."''',
    "messages" : [
        {"role": "user",
         "content": [
             {"type": "text", 
              "text": f"{_query}"}
              ]
            }
        ]
    })
    return params


# get response from search-request
def response(resp):
    results = []
    json_result = loads(resp.text)
    data_openai = loads(json_result['content'][0]['text'])
    response_content = data_openai['response']
    sources_ai = data_openai['links']
    sources_results = []
    for source in sources_ai:
        sources_results.append({'title':source,'url': source})
    
    title = "Anthropic AI: claude-3-sonnet"
    results.append(
            {
                'infobox': f'{title}',
                'id': '',
                'content': response_content,
                'urls': sources_results
            }
        )
        
    return results
