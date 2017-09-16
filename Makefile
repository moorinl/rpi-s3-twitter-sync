all: build

build:
	docker build -t rpi-s3-twitter-sync .

tag:
	docker tag rpi-s3-twitter-sync:latest moorinteractive/rpi-s3-twitter-sync:latest

push:
	docker push moorinteractive/rpi-s3-twitter-sync:latest

run:
	 docker run --name rpi-s3-twitter-sync rpi-s3-twitter-sync
