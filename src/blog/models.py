from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return "blog/{}/{}".format(instance.author.id, filename)

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category_name
    
class Post(models.Model):
    OPTIONS = (
        ("d", "Draft"),
        ("p", "Published")
    )
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to=user_directory_path)
    post_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status =  models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.post_title
    @property
    def comment_count(self):
        return self.comment_set.all().count()

    @property
    def view_count(self):
        return self.postview_set.all().count()

    @property
    def like_count(self):
        return self.like_set.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_added_date = models.DateField(auto_now_add=True)
    comment_content = models.TextField()

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    postview_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username