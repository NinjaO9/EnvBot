This discord bot is a self-hosted bot. You will have to provide your own bot token, server id, and newsapi key to use it. Instructions on how to find the required fields are in the 'keys.txt' file.

The intention of this bot is to the search the internet and find articles that are atleast in some way related to keywords put in by the user. Some articles may be exactly what you are looking for and others may seem to steer off course.

###################################

Q: How do I format the 'time'?

A: The 'time' variable requires an input in the format: "YYYY-MM-DD". This will be the oldest an article that the bot seaches for can be.


Q: How do I get my channel ID for the 'channel' field?

A: Follow the instuctions listed here: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID


Q: What can I put into the 'keywords' field?

A: Inputs such as "plastic pollution recycle energy plants waste" work, with spaces indicating a new word. The bot will try its best to find an article satisfying all keywords. Be aware, more keywords means less results, which is something to keep in mind when running the autonomous command.


Q: What can I put into the 'sortby' field?

A: If you choose to put results into this field, be sure you follow the exact format of the following choices:" relevancy , popularity , publishedAt ". You can only do one soort type at a time.


Q: What can I put for the 'count' field?

A: The count field accepts any range of numbers, however it will only display as many articles as allowed within the discord character limit(2,000).


Q: How does the autonews work?

A: The autonews command is slated to only send one article at a time, every hour. This is to prevent from the bot getting too far off course, assuming that there will be enough articles to satisfy. Depending on the keywords given to the bot, it may begin to post irrelevant articles sooner or later. Additionally, the autocommand calls for articles that are posted in the current day, further limiting the relevancy available.

