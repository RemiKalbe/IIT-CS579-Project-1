import requests

api_url = 'https://api.stackexchange.com/2.3/questions'
params = {
    'site': 'stackoverflow',  # specifying the stack overflow website
    'tagged': 'python',       # filtering pythong posts
    'pagesize': 10,           # specify number of questions to retrieve
    'filter': 'withbody',     # include the entire question body
    'sort': 'votes',          # sort by votes
    'key': '28240'            # have to include the API key
}

# Make a GET request to the Stack Exchange API
response = requests.get(api_url, params=params)


if response.status_code == 200: # 200 means the GET request is successful
    # Parse the JSON response and extract the relevant information
    data = response.json()

    for item in data['items']:
        print("Title:", item['title'])
        print("Link:", item['link'])
        print("Tags:", item['tags'])
        print("Score:", item['score'])
        print("View Count:", item['view_count'])
        print("Creation Date:", item['creation_date'])
        print("Question Body:", item['body'])
        print("-----------------------------")
else: # any other code means error
    print("Error:", response.status_code)