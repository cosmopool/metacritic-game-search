import urllib.request
from bs4 import BeautifulSoup

class SearchResults:
    """Search Results Class"""
    def __init__(self):
        """def search results"""
        self.search_result_id = None
        self.title = None

class MetacriticGame:
    """info of a metacritic item"""
    def __init__(self):
        self.item_id = None
        self.title = None
        self.system = None
        self.metascore = None
        self.user_score = None
        self.genres = None
        self.link = None
        self.date = None
        self.summary = None

games_genre = {
    "action" : "action",
    "adventure" : "adventure",
    "fighting" : "fighting",
    "first_person" : "first-person",
    "flight" : "flight",
    "party" : "party",
    "platformer" : "platformer",
    "puzzle" : "puzzle",
    "racing" : "racing",
    "real_time" : "real-time",
    "rpg" : "role-playing",
    "simulation" : "simulation",
    "sports" : "sports",
    "strategy" : "strategy",
    "third_person" : "third-person",
    "turn_based" : "turn-based",
    "wargames" : "wargame",
    "wrestling" : "wrestling"
}

games_platform = {
    "switch" : "switch",
    "ps4" : "ps4",
    "wii_u" : "wii-u",
    "pc" : "pc",
    "3ds" : "3ds",
    "xbox_series_x" : "xbox-series-x",
    "ps5" : "ps5",
    "ds" : "ds",
    "psp" : "psp",
    "gba" : "gba",
    "wii" : "wii",
    "xbox" : "xbox",
    "ps" : "ps",
    "gamecube" : "gamecube",
    "dreamcast" : "dreamcast",
    "ps3" : "ps3",
    "n64" : "n64",
    "ps2" : "ps2",
    "xbox360" : "xbox360",
    "xbox_one" : "xboxone",
    "ps_vita" : "vita"
}

sort_by = {
    "userscore" : "userscore",
    "metascore" : "metascore"
}

class Metacritic:
    """metacritic search methods and info"""

    game_list = []

    def get_games(platform, genre, sort):
        """get games by genre"""
        url = "https://www.metacritic.com/browse/games/genre/"+ sort_by[sort]+"/"+ games_genre[genre]+"/"+games_platform[platform]+"?view=detailed"
        html = get_html(url)
        soup = BeautifulSoup(html)
        #results = soup.findAll("a", "title")
        results = soup.findAll("td", "clamp-summary-wrap")
        game = MetacriticGame()
        print(results[0])

        #for item in results:
            #result_type = results.find()


    def search(self, platform, genre, sort):
        """function to search for a game on metacritic"""
        base_url = "https://www.metacritic.com/search/game/results?search_type=advanced"
        url = base_url +"&"+ games_platform[platform] +"&"+ games_genre[genre] +"&"+ sort_by[sort]
        html = get_html(url)
        soup = BeautifulSoup(html)
        results = soup.findAll("li", "title")

def get_html(url):
    """to get a gtml from a url"""
    user_agent = "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101"
    try:
        request = urllib.request.Request(url)
        request.add_header("User-Agent", user_agent)
        html = urllib.request.urlopen(request).read()
        return html
    except:
        print ("Error accessing:", url)
        return None

searchq = Metacritic.get_games
searchq("switch", "action", "userscore")
