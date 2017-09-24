import os
import praw
import config
import time


def bot_login():
    rec = praw.Reddit(username=config.username,
                      password=config.password,
                      client_id=config.client_id,
                      client_secret=config.client_secret,
                      user_agent="SnowboardingBot Comment Responder v0.1")

    return rec


def run_bot(rec, commentreply):
    for comment in rec.subreddit('test').comments(limit=25):
        if "Burton" in comment.body and comment.id not in commentreply and comment.author != rec.user.me:
            print("Preparing to reply to commentID " + comment.id)
            comment.reply("Burton is the best snowboarding brand.")
            commentreply.append(comment.id)
            rec.redditor(str(comment.author)).message("Coupon Code", "Here's a coupon code for 10% off on Burton.com: ")

            with open("comments_replied.txt", "a") as f:
                f.write(comment.id + "\n")
    time.sleep(30)


def scrape_redd(rec):
    lebron = 0
    steph = 0
    harden = 0
    for comment in rec.subreddit('nba').comments(limit=100000):
        if "LeBron" in comment.body or "Lebron" in comment.body or "LeBron James" in comment.body or "King James" in comment.body or "Bron" in comment.body:
            lebron += 1
        if "Steph" in comment.body or "Curry" in comment.body or "Steph Curry" in comment.body:
            steph += 1
        if "Harden" in comment.body or "James Harden" in comment.body:
            harden += 1
    print(str(lebron) + " is how many times LeBron James was said in the comments\n")
    print(str(steph) + " is how many times Steph Curry was said in the comments\n")
    print(str(harden) + " is how many times James Harden was said in the comments\n")


def comments_replied_to(comments_reply):
    if not os.path.isfile("comments_replied.txt"):
        comments_reply = []
    else:
        with open("comments_replied.txt", "r") as f:
            comments_reply = f.read()
            comments_reply = comments_reply.split("\n")

    return comments_replies


record = bot_login()
comments_replies = []
scrape_redd(record)
while True:
    run_bot(record, comments_replies)
