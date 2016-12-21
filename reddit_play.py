import random
import praw
from passwords import CLIENT_ID, CLIENT_SECRET, USER_AGENT

def get_joke(joke_type):
    try:
        reddit = connect_to_reddit()
        joke_list = []
#        for subreddit in ['shortcleanfunny', 'cleanjokes', 'badjokes', 'dadjokes', 'puns', 'jokes]:
        for subreddit in ['dadjokes', 'cleanjokes', 'jokes']:
            joke_list.extend(list(reddit.subreddit(subreddit).search(joke_type, limit=10)))
            if len(joke_list)>=30:
                break

        if not joke_list:
            new_type = random.choice(['cows', 'dogs', 'cats', 'bees'])
            joke_type = "{}, because I like {}, but mostly because I couldn't find any jokes about {}.".format(new_type, new_type, joke_type)
            joke_list = list(reddit.subreddit('dadjokes').search(new_type, limit=10))
        joke_id = random.choice(joke_list)
        joke = reddit.submission(id=joke_id)
        joke_type = joke_type + ' from the subreddit {}.'.format(joke.subreddit)

        print('We found a total of {} jokes about {}.'.format(len(joke_list), joke_type))

        return joke.title.replace('\n','.'), joke.selftext.replace('\\','.'), joke_type

    except Exception as e:
        return "Whoops, something went wrong. Try again real soon! ".format(e), "Goodbye!"

def connect_to_reddit():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)

    return reddit


if __name__ == '__main__':
    joke=get_joke('poop')
    print()
    print(joke[0])
    print()
    print(joke[1])
    print()