import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

# Create a list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# Or load the list of posts we have replied to
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Pull the hottest 10 entries from a subreddit of your choosing
subreddit = reddit.subreddit('books')
for submission in subreddit.hot(limit=10):
    print(submission.title)
    if re.search("science fiction", submission.title, re.IGNORECASE):
        reddit.redditor('RushAndRelaxx').message('Test','it worked?')
    # Make sure you didn't already reply to this post
    if submission.id not in posts_replied_to:

        # Not case sensitive
        if re.search("martin", submission.title, re.IGNORECASE):
            # Reply
            #submission.reply("My favourite!")
            print("Bot replying to : ", submission.title)

            # Store id in list
            posts_replied_to.append(submission.id)

# Write updated list to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")