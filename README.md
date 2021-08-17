# twitterwipe

1.  run: pip3 install -r requirements.txt

2.  User Authorization:

Go to <https://dev.twitter.com/apps/new> and log in, if necessary, Supply the necessary required fields, accept the Terms Of Service, and solve the CAPTCHA. Submit the form, Go to the API Keys tab, there you will find your Consumer key and Consumer secret keys. Copy the consumer key (API key) and consumer secret from the screen into our application.

3.  App Authorization:

run auth.py. it will print a link to visit with a code to enter, your app_key and app_secret will be printed to the console. put those into your keys.json.

4.  Configure:

Add the number of days worth of past data (starting from runtime) that you want to preserve into config.yaml.
Anything further in the past than this time period will be deleted.

5.  Run the program:

python3 twitterwipe.py

6.  logs:

Logs will be written to `log.log`

7.  .gitignore

Make sure to add log.log and keys.json to .gitignore!
