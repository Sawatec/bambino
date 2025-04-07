from datetime import date
from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(
        blank=True,

    )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    class Meta:
        ordering = ['-timestamp', ]
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def datepublished(self):
        timestamp = self.timestamp.strftime('%A, %d.%m.%Y')
        datesplitted = timestamp.split(',')
        days = {
            "Monday": "Montag",
            "Tuesday": "Dienstag",
            "Wednesday": "Mittwoch",
            "Thursday": "Donnerstag",
            "Friday": "Freitag",
            "Saturday": "Samstag",
            "Sunday": "Sonntag"
        }

        return days.get(datesplitted[0]) + ', ' + datesplitted[1]
        # return self.date_published.strftime('%A, %d.%m.%Y')

    def get_full_title(self):
        return self.title

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='up',
                                      news=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='down',
                                        news=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, user, up_or_down):
        vote = Vote.objects.create(up_or_down=up_or_down,
                                   user=user,
                                   news=self
                                   )

    def __str__(self):
        return self.title + ' (' + self.user.username + ')'

    def __repr__(self):
        return self.get_full_title() + ' / ' + self.user.username + ' / '


class Vote(models.Model):
    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]

    up_or_down = models.CharField(max_length=1,
                                  choices=VOTE_TYPES,
                                  )
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.up_or_down + ' on ' + self.news.title + ' by ' + self.user.username


class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp',]
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def datepublished(self):
        date = self.timestamp.strftime('%A, %d.%m.%Y')
        datesplitted = date.split(',')
        days = {
            "Monday": "Montag",
            "Tuesday": "Dienstag",
            "Wednesday": "Mittwoch",
            "Thursday": "Donnerstag",
            "Friday": "Freitag",
            "Saturday": "Samstag",
            "Sunday": "Sonntag"
        }

        return days.get(datesplitted[0]) + ', ' + datesplitted[1]
        # return self.date_published.strftime('%A, %d.%m.%Y')

    def get_comment_prefix(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

    def __str__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ')'

    def __repr__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ' / ' + str(self.timestamp) + ')'
