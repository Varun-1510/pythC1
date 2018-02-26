import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "rnWkBhVORs6c6B6rw030gHgJd",
    "consumer_secret"     : "mJGFvjYMKH6Pn8EsjeYMDP2uT4veVKXpjDWuEMEFOaCkoZtiuw",
    "access_token"        : "968052338798792704-FmfXn6eXmY1NFPuN6zJHHA41hFmshtr",
    "access_token_secret" : "CJ3I571GCu43UhQpCZakgBRtSWjVXhS4W2acA4CHjTxoq"
    }


  api = get_api(cfg)
  tweet = "Am Varun Yogi Photographer"
  status = api.update_status(status=tweet)
  print("My message is tweeted")
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
