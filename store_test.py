from Post import Post
from store import PostStore

post_store = PostStore()
dummy_posts = [
    Post(id=1,
        photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50', 
        name='Sara', 
        body='Lorem Ipsum',
        date='1/1/2019'),
    Post(id=2,
        photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100', 
        name='John', 
        body='Lorem Ipsum',
        date='11/4/2019'),
]

def store_should_add_posts():
    for post in dummy_posts:
        post_store.add(post)

    # check if posts list has same length as dummy_posts list
    assert len(post_store.get_all()) == len(dummy_posts)

def get_by_id_should_retrieve_same_object():
    second_post = dummy_posts[1]
    retrieved_second_post = post_store.get_by_id(2)

    assert second_post is retrieved_second_post

def update_should_modify_object():
    fields_to_update = {
        'photo_url': 'https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
        'name': 'Alex', 
        'body': 'Interesting topic right here!',
        'date': '20/4/2019'
    }

    # update second post
    post_store.update(2, fields_to_update)

    assert post_store.get_by_id(2).name == 'Alex'
    assert post_store.get_by_id(2).body == 'Interesting topic right here!'

def delete_should_remove_object():
    post_store.delete(2)

    assert len(post_store.get_all()) == 1
    assert post_store.get_all()[0].id == 1

store_should_add_posts()
get_by_id_should_retrieve_same_object()
update_should_modify_object()
delete_should_remove_object()

print('All tests passed successfully!')
