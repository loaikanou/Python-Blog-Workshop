posts = []

class PostStore:
    # get all posts
    def get_all(self):
        return posts

    # Add post
    def add(self, post):
        posts.append(post)
        return post

    # search for post by id - id
    def get_by_id(self, id):
        result = None
        for post in posts:
            if post.id == id:
                result = post
                break
        return result

    # update post data -> id
    def update(self, id, fields):
        post = self.get_by_id(id)
        post.name = fields['name']
        post.photo_url = fields['photo_url']
        post.body = fields['body']
        post.date = fields['date']
        return post

    # delete post by id -> id
    def delete(self, id):
        post = self.get_by_id(id)
        posts.remove(post)
        return

