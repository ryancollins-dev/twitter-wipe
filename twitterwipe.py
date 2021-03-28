import os
import tweepy
import json
import yaml
import logging
import concurrent.futures
from datetime import timedelta, datetime

full_path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename=full_path + '/log.log', level=logging.INFO,
        format='%(asctime)s %(message)s')

logger = logging.getLogger(__name__)

def main():
    logger.info('starting twitterwipe')

    with open(full_path + '/config.yaml', 'r') as yamlfile:
        config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    delete_timestamps = get_delete_timestamps(config)
    purge_activity(delete_timestamps)

    logger.info('done')


def get_delete_timestamps(config):
    curr_dt_utc = datetime.utcnow()

    days = config['days_to_save']
    likes = days['likes']
    retweets = days['retweets']
    tweets = days['tweets']

    likes_delta = timedelta(likes)
    retweets_delta = timedelta(tweets)
    tweets_delta = timedelta(tweets)

    likes_time = curr_dt_utc - likes_delta
    retweets_time = curr_dt_utc - retweets_delta
    tweets_time = curr_dt_utc - tweets_delta

    return (likes_time, retweets_time, tweets_time)


def purge_activity(delete_timestamps):
    api = get_api()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.submit(delete_tweets, api, delete_timestamps[2])
        e.submit(delete_retweets, api, delete_timestamps[1])
        e.submit(delete_favorites, api, delete_timestamps[0])


def delete_tweets(api, ts):
    logger.info('deleting tweets before {}'.format(str(ts)))

    count = 0

    for status in tweepy.Cursor(api.user_timeline).items():
        if status.created_at < ts:
            try:
                api.destroy_status(status.id)
                count += 1
            except Exception as e:
                logger.error("failed to delete {}".format(status.id), exc_info=True)

    logger.info('{} tweets deleted'.format(count))

    return


def delete_retweets(api, ts):
    logger.info('deleting retweets before {}'.format(str(ts)))

    count = 0

    for status in tweepy.Cursor(api.user_timeline).items():
        if status.created_at < ts:
            try:
                api.unretweet(status.id)
                count+=1
            except:
                logger.error('failed to unretweet {}'.format(status.id),exc_info=True)
    logger.info('{} retweets deleted'.format(count))


    return


def delete_favorites(api, ts):
    logger.info('deleting favorites before {}'.format(str(ts)))

    count = 0

    for status in tweepy.Cursor(api.favorites).items():
        if status.created_at < ts:
            try:
                api.destroy_favorite(status.id)
                count+=1
            except:
                logger.error('failed to delete favorite'.format(status.id), exc_info=True)

    logger.info('{} favorites deleted'.format(count))

    return


def get_api():
    with open(full_path + '/keys.json', 'r') as f:
        d = json.load(f)

    auth = tweepy.OAuthHandler(d['consumer_key'], d['consumer_secret'])
    auth.set_access_token(d['app_key'], d['app_secret'])

    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


if __name__ == '__main__':
    main()
