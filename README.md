# tweets-sentiment-analysis-america

The steps below will help you set up your twitter account to be able to access the live stream.

Create a twitter account if you do not already have one.
Go to Twitter Dev and log in with your twitter credentials.
Click "Create New App"
Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
On the next page, click the "API Keys" tab along the top, then scroll all the way down until you see the section "Your Access Token"
Click the button "Create My Access Token". You can Read more about Oauth authorization.
You will now copy four values into twitterstream.py. These values are your "API Key", your "API secret", your "Access token" and your "Access token secret". All four should now be visible on the API Keys page. (You may see "API Key" referred to as "Consumer key" in some places in the code or on the web; they are synonyms.)
Open twitterstream.py and set the variables corresponding to the api key, api secret, access token, and access secret. You will see code like the below:
