





<!-- 
## Local Run 
`pip install --upgrade google-cloud-vision`
`pip install opencv-python` 


## For local run 
1. Change the secrete address to that in your pc (absolute address (right click vscode))
    `os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ...... `
2. Change input image for testing 
    `path = './test/test5.webp'`
3. A few tests in test/ folder




> __Keep Secret Folder Properly it has service accout json__ -->


# Music Trend Collector 

A selenium based data miner which scrapes the internet for spotify playlists and 

## Based around reddit
- Contains corpus which is easier to parse and contains inherent tags (subreddit, context)
- `old.reddit.com` provides viewport which is easier to navigate from a DOM perspective. 


## Why recommendations 

### Traditional Recommendation Systems 
- Music recommendation systems use a combination of machine learning algorithms and data analysis to suggest music to users. They typically rely on data such as a user's listening history, their ratings of songs or artists, and their demographic information to make recommendations.

- The most common approach is to use __collaborative filtering__, which finds other users with similar music preferences and suggests songs that they have listened to. Collaborative filtering can be either user-based, where it finds similar users, or item-based, where it finds similar songs.

- Another approach is __content-based filtering__, which uses information about the songs themselves, such as genre, tempo, and lyrics, to make recommendations.

- Hybrid methods also exist, which combine both collaborative and content-based filtering to make recommendations. These systems use different algorithms such as K-nearest neighbors, matrix factorization, and deep learning to analyze and make recommendations based on the data.

- Music streaming platforms like Spotify, Apple Music, and Pandora use these methods to provide personalized recommendations to their users.

### Importance of Human Recommendations 
- Human recommendations are often considered to be better than machine recommendations because humans have the ability to understand context and take into account personal preferences, whereas machines may only be able to make recommendations based on algorithms and data.
- Humans can also use their __intuition and experience to make recommendations that may not be easily quantifiable by a machine__. Additionally, humans can provide explanations and reasoning for their recommendations, which can help people understand why a certain content is being recommended to them.

> The goal of this data miner is to generate context along with the recommendation to gain insight into the intuition factor that traditional recommendation options do not consider. 

### Recommendations Systems are good for everyone 
- Recommendations are essential for any modern content provider. 
- Helps Discovery of new pieces of media. 
    - From an artist perspective : It makes mores sense to only focus on the music and rely on publishing platforms with better discovery which finds the right audience for you. 
    - From a user perspective : Good recommendations are a bit motivations when looking for platforms from users[1]



## Technical Details 

### Search Scope 
- 1 month, 6 month, 12 months 
    - limitation of reddit (it recently removed custom dates)

### Dataset Format 
|Playlist Link|Post Title|Comment Tree|Thread URL|
|-|-|-|-|
|`https://open.spotify.com/playlist/...`|Title of post|Comment tree which contains the playlist|https://www.reddit.com/r/MusicVideos...|

### Subreddits Covered 

- r/Music
- r/musicsuggestions
- r/ofmd
- r/MusicVideos
- r/HipHopHeads
- r/PopHeads
- r/Popmusic
- r/Lofi


## Future Scope 
- It makes more sense to scrape on a site wide basis to provide additional context for music. 
    - Subreddits like r/UCDavis, r/soccer among others also have several playlist links which refer to music but the context of that subreddit. This additional data point is currently not being captured 
    - [reference post 1](https://www.reddit.com/r/india/comments/10gpsp3/i_want_to_make_a_spotify_playlist_for_our_foreign/), [reference post 2](https://www.reddit.com/r/Emo/comments/10g6yt9/emo_lullabies_looking_for_better_music_to_play/), [reference post 3](https://www.reddit.com/r/FrankOcean/comments/10jaqrh/i_created_this_playlist_with_songs_that_make_you/)
- Next improvement will be adding google based search (parametric) rather than reddit based search. `Expect mix 2023`
    - Will utilize expert queries like : `site:reddit.com "spotify.com/playlist/"`
- If this catches on this could be a monthly data pipeline which connects to kaggle and posts the data gathered. 

## Sub based search utils 
- The miner works based on subreddit specific search 
    ```python
    def scrape_reddit_search(search_term, subreddit):
        import selenium
        driver = selenium.webdriver()
        driver.get(f"https://www.reddit.com/r/{subreddit}")
        search_bar = driver.find_element_by_css_selector("input[name='q']")
        search_bar.send_keys(search_term)
        search_bar.submit()
        elements = driver.find_elements_by_css_selector("css_selector")
        data = []
        for element in elements:
            data.append(element.text)
        driver.close()
        return data
        
    search_term = "example search term"
    subreddit = "example_subreddit"
    data = scrape_reddit_search(search_term, subreddit)
    print(data)
    ```

## Ref
[1](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-022-00592-5)
