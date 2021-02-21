import json
import requests
import pandas as pd
from config import creds
from token_retrevial import get_token
import datetime as dt

with open('token_data.json') as token_file:
    token_data = json.load(token_file)
token = 'bearer ' + token_data['access_token']

def check_token():
    #flag - clean up process, find better way
    base_url = 'https://oauth.reddit.com'
    headers = {'Authorization': token, 'User-Agent': '{} by {}'.format(creds['app_name'], creds['username'])}
    response = requests.get(base_url + '/api/v1/me', headers=headers)
    return response.status_code

def get_comments():
    payload = {'limit': 100, 'sort': 'top', 't':'hour'}
    api_url = 'https://oauth.reddit.com/'
    headers = {'Authorization': token, 'User-Agent': '{} by {}'.format(creds['app_name'], creds['username'])}
    response = requests.get(api_url + 'r/CryptoCurrency/top', headers=headers, params=payload)
    values = response.json()
    reddit_df = pd.DataFrame()
    comment_id = []
    author = []
    time = []
    text = []
    title = []
    upvotes = []
    upvote_ratio = []
    #flag - clean up process, find better way
    for x in values['data']['children']:
        comment_id.append(x['data']['name'])
        author.append(x['data']['author_fullname'])
        time.append(x['data']['created'])
        text = x['data']['selftext']
        text.append(text)
        title.append(x['data']['title'])
        upvotes.append(x['data']['ups'])
        upvote_ratio.append(x['data']['upvote_ratio'])
    reddit_df['created_at'] = pd.Series([dt.datetime.now().strftime("%Y-%m-%d %H:%M")] * len(comment_id))
    reddit_df['comment_id'] = comment_id
    reddit_df['author_id'] = author
    reddit_df['time'] = time
    reddit_df['title'] = title
    reddit_df['text'] = text
    reddit_df['upvotes'] = upvotes
    reddit_df['upvote_ratio'] = upvote_ratio
    print(reddit_df[['title', 'upvotes', 'upvote_ratio']].head(100))
    with open('top_subreddit_data.json','w') as reddit_file:
        json.dump(values ,reddit_file)

# Make sure API is chugging along smoothly
auth_status = check_token()
while auth_status != 200:
    get_token()
else:
    print("Connected!")

get_comments()