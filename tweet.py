from twitter_scraper import get_tweets
from colorama import Fore
keyword = input(Fore.RED + "[" + Fore.WHITE + "keyword>>" + Fore.RED + "] ")
for t in get_tweets(keyword):
	print (Fore.RED + "[*] " + t['text'])
