# Raspberry Pi S3 Twitter Sync

Raspberry Pi compatible S3 Twitter Sync Docker container.

## Install

Docker Pull Command

``docker pull moorinteractive/rpi-s3-twitter-sync``

## Usage

Environment variables

```
TWITTER_CONSUMER_KEY=...
TWITTER_SECRET=...
TWITTER_ACCESS_TOKEN=...
TWITTER_ACCESS_TOKEN_SECRET=...
TWITTER_USERNAME=example
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET_NAME=example.com
AWS_S3_TWITTER_PATH=api/twitter/statusses.json

```

Docker Run Command

``docker run --name rpi-s3-twitter-sync moorinteractive/rpi-s3-twitter-sync``
