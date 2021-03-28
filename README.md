# twitterwipe
0) use pip to install the stuff you need from requirements.txt.

1) Authorization - Pt. I<br>
get your consumer keys from twitter. copy keys.example.json to keys.json, and put your consumer keys into the json.
if you have app_key & app_secret, put those in now and skip to step (3).

2) Authorization - Pt. II<br>
run auth.py. it will print your app_key and app_secret to console. put those into your keys.json. this feels bad to do; there's probably a more secure way of doing this (i think you can get these from the twitter site, but also think that's being deprecated). feel free to do this another way, all you need are the app_key and app_secret.

3) Configure<br>
put in the number of days worth of past data (starting from runtime) you want to preserve into config.yaml. anything further in the past than this time period will be deleted (save some favorites; please see the epilogue).

4) run the program with python:<br>
python twitterwipe.py

5) logs will be written to logs.logs, which is registered in the .gitignore.

# epilogue
if you have more than a certain number of favorites, this script might not destroy them in totality (i think it's like ~3k likes). Here's a link to what i did to get them all:

https://gist.github.com/aymericbeaumet/d1d6799a1b765c3c8bc0b675b1a1547d
