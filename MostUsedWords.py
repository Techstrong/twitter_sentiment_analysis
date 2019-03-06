def user_tweets(user, count):
#
    #Create list to hold tweets
    all_tweets = []

    #Authenticate
    auth = OAuthHandler(twi_api_credentials.consumer_key, twi_api_credentials.consumer_secret)
    auth.set_access_token(twi_api_credentials.access_token, twi_api_credentials.access_secret)

    #API let's us in. Grants us access to Twitter
    api = tweepy.API(auth)


    #get total amount of tweets
    tot_tweets = api.get_user(user).statuses_count
    print(tot_tweets)

    #access user timeline
    tweets = api.user_timeline(screen_name = user, count = count, include_rts = True)

    #Add each tweet to a list
    all_tweets.extend(tweets)

    # save the id of the oldest tweet less one
    oldest = all_tweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(tweets) > 0:


        # all subsiquent requests use the max_id param to prevent duplicates
        tweets = api.user_timeline(screen_name=user, count=200, max_id=oldest)

        # save most recent tweets
        all_tweets.extend(tweets)

        # update the id of the oldest tweet less one
        oldest = all_tweets[-1].id - 1

        # print("...%s tweets downloaded so far" % (len(all_tweets)))
