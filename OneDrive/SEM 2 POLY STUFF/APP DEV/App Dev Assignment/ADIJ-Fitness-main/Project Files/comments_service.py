import shelve


db_comments = 'comments'
db_comments_key = 'commentsKey'


def save_comments(comment):
    comments_dict = {}
    data = shelve.open(db_comments)

    if db_comments_key in data:
        comments_dict = data[db_comments_key]

    comments_dict[comment.id] = comment
    data[db_comments_key] = comments_dict
    data.close()


def get_comments_list():
    comments_dict = {}
    data = shelve.open(db_comments)

    if db_comments_key in data:
        comments_dict = data[db_comments_key]

    data.close()
    comments_list = comments_dict.values()
    return comments_list


def get_comments(uid):
    result = None
    comments_dict = {}
    data = shelve.open(db_comments)

    if db_comments_key in data:
        comments_dict = data[db_comments_key]

    data.close()

    if uid in comments_dict:
        result = comments_dict[uid]
    return result


def delete_comment(uid):
    comments_dict = {}
    data = shelve.open(db_comments)

    if db_comments_key in data:
        comments_dict = data[db_comments_key]
        comments_dict.pop(uid)
        data[db_comments_key] = comments_dict
        data.close()


# prog_dict = {}
# db = shelve.open(db_comments)
# if db_comments_key in db:
#     prog_dict = db[db_comments_key]
# db.close()
# prog_list = prog_dict.values()
# print(prog_dict)
# print(list(prog_list))
# for i in prog_list:
#     print(i.post)


def unique_comment_dict(commID, postID):
    commentDict = {}

    for id1 in postID:
        commentDict[id1] = commID.count(id1)

    return commentDict

# db = shelve.open(db_comments)
# db.clear()
# db.close()
