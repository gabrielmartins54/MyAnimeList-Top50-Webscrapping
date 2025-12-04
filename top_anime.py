#   Web Scrapper for top 50 anime list on MyAnimeList website   #

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd



url = 'https://myanimelist.net/topanime.php'
response = requests.get(url)
#print(response.status_code)

soup = bs(response.text, 'lxml')
find_animes = soup.find_all('tr', class_='ranking-list')

# Empty lists to store information
anime_names = []
anime_ranking = []
anime_score = []

# Structuring information
for anime in find_animes:

    #Getting the names
    name_tag = anime.find('td', class_=['title', 'al', 'va-t', 'word-break'])
    name = name_tag.select_one("div h3 a").text

    #Getting the ranking
    ranking_tag = anime.find('span', class_=['lightLink', 'top-anime-rank-text', 'rank1']).text

    #Getting the score rating
    score_tag = anime.find('span', class_=['text', 'on', 'score-label', 'score-9']).text
   
    #Appending results
    anime_names.append(name)
    anime_ranking.append(ranking_tag)
    anime_score.append(score_tag)

# Transforming results in a DataFrame

top_anime_rankings = pd.DataFrame()
top_anime_rankings['Rank'] = anime_ranking
top_anime_rankings['Name'] = anime_names
top_anime_rankings['Rating/Score'] = anime_score

top_anime_rankings.to_csv('AnimeRankings.csv', index=False)
    
    
    