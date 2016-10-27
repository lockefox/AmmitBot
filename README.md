# AmmitBot
Managing a wide open chatroom can get ugly.  Though the wide majority of your community is well behaved, a few bad apples can ruin the bunch.  What's worse is veteran bad-posters know how to skirt around the rules and can be very hard to prune without flagrant rule violations.  80% of problems come from 20% of users.

Blacklists and language filters are ineffective.  Bad users can skirt the letter of the law while still causing harrasment and an unwelcoming atmosphere.

AmmitBot looks to attack this problem with big-data.  Using [NLTK](http://www.nltk.org/) as a backbone, AmmitBot stores chats and helps admins grade their community internally and externally.  Deploy an instance of AmmitBot and public chats will be logged, graded, and easily displayed for users to check their standing.  Also, utilizing a global database, bad-actors can be more easliy tracked with their chat-scores following them.

The goal is to, as generically as possible, build up each user's, guild's, and chat's profile.  Using these profiles and some basic statistical processing, gud/bad posters should be able to be identified from the cluster.  

AmmitBot does not execute admin commands.  Instead, it listens and responds to some useful commands.  The grades are meant to give a "flavor" of the community and help identify troublemakers; humans are still responsible for pulling the trigger on bad posters.  Far be it from me to force communities to be "positive", but if you want to affect something, it's best to measure it first!

In all, this is a science experiment to see the power/usefulness of NLTK to help cull bad behavior.  

# Requirements
AmmitBot is built on the back of [discord.py](http://discordpy.readthedocs.io/en/latest/index.html) using [NLTK](http://www.nltk.org/) inline to quantify chat responses.  This is a Python3.5 project.

Additionally, AmmitBot relies on:

* [Pandas](http://pandas.pydata.org/) for statistical processing
* [tinyDB](http://tinydb.readthedocs.io/en/latest/) for caching
* [tinymongo](https://github.com/schapman1974/tinymongo)/[pymongo](https://api.mongodb.com/python/current/) for warehousing
* [ujson](https://pypi.python.org/pypi/ujson) for JSON parsing (requests/tinyDB)
* [requests](http://docs.python-requests.org/en/master/) for direct HTTP work (webhooks)
* [pytest](http://docs.pytest.org/en/latest/) for testing


