from django.db import models

# Create your models here.


from django.db import models
from user.models import User

class Post(models.Model):
    class Meta:
        db_table = 'post'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, null=False)
    postdate = models.DateTimeField(null=False)

    author = models.ForeignKey(User)


    def __repr__(self):
        return "<post {} {} {} >".format(
            self.id, self.title, self.author)

    __str__ = __repr__

class Content(models.Model):
    class Meta:
        db_table = 'content'
    post = models.OneToOneField(Post)
    content = models.TextField(null=False)
    def __repr__(self):
        return '<content {} {} >'.format(self.post.id, self.content[:20])

    __str__ = __repr__
