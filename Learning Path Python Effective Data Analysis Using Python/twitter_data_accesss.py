import Json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = 'W4vatXbYSgnTPhP3krd9Hle0Z'
consumer_secret = 'cbMUSJiaHMvpo9y1Ql9DxCdRPY0hKILvtkZbiBY2QztsOMWSbh'
access_token = '811617846396653568-WXcxBCS2r8stgHTttJ6egMO1om4x0ep'
access_token_secret = 'lZuj4sBuQ3kTRi9yICJ1ohHREdbn1o3PJ8N01a7sZcLtg'

#autentification to twitter
auth = OAuthHandler(consumer_key,
                    consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        print(status.text)
        print(status.author.screen_name,
              status.created_at,
              status.source,
              '\n')
    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True #keep stream alive
    def on_timeout(self):
        print('Listener timedout!')
        return True #keep stream alive

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    language = ('ja','en') #language of the tweet
    stream.sample(languages=language)

if __name__== '__main__':
    print_to_terminal()