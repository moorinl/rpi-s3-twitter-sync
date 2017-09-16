#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    from s3_twitter_sync import tasks
    tasks.sync_tweets_to_s3_bucket()
