#!/usr/bin/env python3

import sys

"""
Stanford CS106AP Tweets Project
"""


def add_tweet(user_tags, tweet):
    """
    Given a user_tags dict and a tweet, parse out the user and tags,
    and add those counts to the user_tags dict which is returned.
    If no user exists in the tweet, return the user_tags dict unchanged.
    Note: call the parse_tags(tweet) and parse_user(tweet) functions to pull
    the parts out of the tweet.
    >>> add_tweet({}, '@alice: #apple #banana')
    {'@alice': {'#apple': 1, '#banana': 1}}
    >>> add_tweet({'@alice': {'#apple': 1, '#banana': 1}}, '@alice: #banana')
    {'@alice': {'#apple': 1, '#banana': 2}}
    >>> add_tweet({'@alice': {'#apple': 1, '#banana': 2}}, '@bob: #apple')
    {'@alice': {'#apple': 1, '#banana': 2}, '@bob': {'#apple': 1}}
    """
    tags_list = tweet.split(' ')
    user= tags_list[0].strip(':')
    tags_list.pop(0)
    tags_dict = {}
    for tag in tags_list:
        if tag not in tags_dict:
            tags_dict[tag] = 1
        else:
            tags_dict[tag] += 1
    if user not in user_tags:
        # if tags_dict != {}:
        user_tags[user] = tags_dict
    else:
        user_current_tags = user_tags[user]
        for tag in tags_dict:
            if tag not in user_current_tags:
                user_current_tags[tag] = tags_dict[tag]
            else:
                user_current_tags[tag] += tags_dict[tag]

        user_tags[user] = user_current_tags

    return user_tags





def parse_tweets(filename):
    """
    Given a file of tweets, 1 per line, build and return a user_tags dict
    of all the tweet data.
    """
    user_tags = {}
    with open(filename, encoding='UTF8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split(' ')
            if line_list[0][0] == '@':
                tweet = line_list[0]

                for i in range(1,len(line_list)):
                    if line_list[i] != '' and line_list[i][0] == '#':
                        tweet += ' ' + line_list[i].strip(',.!?')

                user_tags = add_tweet(user_tags, tweet)

    return user_tags


def flat_counts(user_tags):
    """
    (Extension Problem)
    Given a user_tags dicts, sum up the tag counts across all users,
    return a "flat" counts dict with a key for each tag,
    and its value is the sum of that tag's count across users.
    >>> flat_counts({'@alice': {'#apple': 1, '#banana': 2}, '@bob': {'#apple': 1}})
    {'#apple': 2, '#banana': 2}
    """
    counts_dict = {}
    for user1 in user_tags:
        tags_dict = user_tags[user1]
        for user in user_tags:
            if user != user1:
                tags_dict_user = user_tags[user]
                for tag in tags_dict_user:
                    if tag not in tags_dict:
                        tags_dict[tag] = tags_dict_user[tag]
                    else:
                        tags_dict[tag] += tags_dict_user[tag]
        break
    return tags_dict


"""
Feel free to peruse the code below here,
but it isn't necessary to solve the problem.
"""


def parse_tags(tweet):
    """
    (provided)
    Given a tweet like '@bob: this #is #it', returns
    a list of tags like ['#is', '#it'].
    >>> parse_tags('This #tweet is #fire')
    ['#tweet', '#fire']
    >>> parse_tags('@user: #tag1 #tag2')
    ['#tag1', '#tag2']
    >>> parse_tags('This tweet is on fire')
    []
    >>> parse_tags('A # starts a Python comment')
    []
    >>> parse_tags('#run#together')
    ['#run', '#together']
    """
    hash_tags = []
    search = 0
    while True:
        hash = tweet.find('#', search)
        if hash == -1:
            break

        end = hash + 1
        # isalnum() = alpha or digit
        while end < len(tweet) and tweet[end].isalnum():
            end += 1

        hash_tag = tweet[hash:end]
        if len(hash_tag) > 1:
            hash_tags.append(hash_tag)
        search = end  # tricky: #tags#adjacent
    return hash_tags


def parse_user(tweet):
    """
    (provided)
    Given a tweet like '@bob: hello #woot', returns
    the user '@bob' or '' if no user is found.
    >>> parse_user('@jonathan: tweet')
    '@jonathan'
    >>> parse_user('@ThisIsATest: #oh #yeah')
    '@ThisIsATest'
    >>> parse_user('meh')
    ''
    """
    colon = tweet.find(':')
    if colon == -1:
        return ''
    return tweet[:colon]


def print_counts(tags):
    """
    (provided)
    Given a counts dict mapping tag -> count, prints
    out the tags in order like
      #apple -> 13
      #boat -> 1
      #zebra -> 12
    """
    for tag in sorted(tags.keys()):
        print(' ' + tag + ' -> ' + str(tags[tag]))
        # alternate technique: str.format() like this:
        # print(' {} -> {}'.format(tag, tags[tag]))


def main():
    args = sys.argv[1:]
    # 5 ways to run from terminal:
    # filename            # prints out all users and tag_counts
    # -users filename     # prints just user names
    # -user user filename # prints data for a particular user
    # -flat filename      # prints flat tag counts
    # -most filename      # prints most common tag

    # args: filename
    if len(args) == 1:
        user_tags = parse_tweets(args[0])
        for user in sorted(user_tags.keys()):
            print(user)
            counts = user_tags[user]
            print_counts(counts)

    # args: -users filename
    if len(args) == 2 and args[0] == '-users':
        # args[1] is tweets
        user_tags = parse_tweets(args[1])
        print('users')
        for user in sorted(user_tags.keys()):
            print(user)

    # args: -user user filename
    if len(args) == 3 and args[0] == '-user':
        # args[1] is user, args[2] is tweets
        user_tags = parse_tweets(args[2])
        print('user:', args[1])
        counts = user_tags[args[1]]  # pull out tags for just that user
        print_counts(counts)

    # args: -flat filename
    if len(args) == 2 and args[0] == '-flat':
        user_tags = parse_tweets(args[1])
        counts = flat_counts(user_tags)
        print('flat')
        print_counts(counts)


if __name__ == '__main__':
    main()
