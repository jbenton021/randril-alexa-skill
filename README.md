# Description
Randril is an Alexa skill that can search for and read tweets from surrealist twitter comedian "@dril". Users can search for specific tweets with voice input and have them read aloud by their Alexa device (i.e., a user could say "'corn cob' tweet" and the skill would search Twitter for the tweet that best matches that query).

##Usage
This skill is not currently hosted publicly. To use this skill:
1. Create a Twitter developer account if you do not currently have one. Create a new app. Generate API credentials and set up a dev environment for the "Full Archive/ Sandbox" endpoint.
2. Clone this repository and install its dependencies using `npm install`.
3. Copy the API credentials into the `Twit` constructor.
4. Host the skill code as an AWS Lambda function and use that Lambda function as an endpoint for an Alexa skill. Add an intent called "SearchIntent" and provide utterances (i.e. "read me the {searchQuery} tweet"). The slot used to pass the search query should be called "searchQuery" and use the AMAZON.SearchQuery slot type.

##To-do
- Much more extensive testing, including testing on actual devices
- Add feature to read random dril tweets
- Add "tweet of the day" feature
