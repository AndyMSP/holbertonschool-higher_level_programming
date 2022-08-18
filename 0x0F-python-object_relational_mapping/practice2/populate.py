#!/usr/bin/python3

from main import Post, User, session



# new_user = User(
#     username = 'testuser',
#     email = 'testuser@gmail.com'
# )

# session.add(new_user)
# session.commit()

user = session.query(User).filter(User.id==1).first()


# posts = [
#     {
#         "title":"post1",
#         "content":"content1"
#     }, {
#         "title":"post2",
#         "content":"content2"
#     }, {
#         "title":"post3",
#         "content":"content3"
#     }, {
#         "title":"post4",
#         "content":"content4"
#     },
# ]

# for post in posts:
#     new_post = Post(
#         title = post['title'],
#         content = post['content'],
#         author=user
#     )
#     session.add(new_post)
#     session.commit()

