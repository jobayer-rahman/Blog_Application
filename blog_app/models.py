from django.db import models


class Author(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    userName = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    authorIntro = models.CharField(max_length=250)
    image = models.ImageField()
    registered_at = models.DateField()
    updated_at = models.DateField()
    last_login = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        self.userName

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=120)
    summery = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=False)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        self.title

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-body']

    def __str__(self):
        self.body




