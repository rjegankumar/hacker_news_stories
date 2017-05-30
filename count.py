import read
import re
import collections

def headlines_to_str(hl):
    global headlines
    if type(hl) == float:
        return
    headlines+= " "
    headlines+= hl
    return

if __name__=="__main__":
    hacker_news = read.load_data()
    headlines = hacker_news.loc[0, 'headline']
    hacker_news.loc[1:, 'headline'].apply(headlines_to_str)
    headlines = headlines.lower()
    headline_words = re.findall(r"[a-zA-Z]{2,}", headlines)
    headline_words_counter = collections.Counter(headline_words)
    hl_wrds_ctr = {}
    for key in headline_words_counter:
        if key not in ['the','a','is','and','or','in','on','as','of','for','to','then','there','with','how','your','you','who','why','what','it','at','an','from','do','i','not','by','are','this','that','be','s']:
            hl_wrds_ctr[key] = headline_words_counter[key]
    hl_wrds_ctr = collections.Counter(hl_wrds_ctr)
    print(hl_wrds_ctr.most_common(100))
