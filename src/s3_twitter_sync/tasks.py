import json

from tempfile import NamedTemporaryFile

import boto3
import shutil
import twitter

from s3_twitter_sync import settings
from s3_twitter_sync.logger import logger



api = twitter.Api(
    consumer_key=settings.TWITTER_CONSUMER_KEY,
    consumer_secret=settings.TWITTER_SECRET,
    access_token_key=settings.TWITTER_ACCESS_TOKEN,
    access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET,
)

s3 = boto3.client('s3')


def sync_tweets_to_s3_bucket():
    # Get uset timeline from twitter
    statuses = api.GetUserTimeline(
        screen_name=settings.TWITTER_USERNAME,
        count=5,
        include_rts=True,
        exclude_replies=True,
    )

    # Convert twitter response to json
    data = json.dumps([status.AsDict() for status in statuses], ensure_ascii=False)

    # Write json to temporary file
    temp_file = NamedTemporaryFile(mode='w+t', delete=False)
    temp_file.write(data)
    temp_file.seek(0)
    temp_file.close()

    # Save temporary file to disc
    shutil.copy(temp_file.name, '/tmp/twitter.json')

    # Upload temporary file to s3
    s3.upload_file(
        '/tmp/twitter.json',
        settings.AWS_S3_BUCKET_NAME,
        settings.AWS_S3_TWITTER_PATH,
    )
