from django.db import models


class TodoListItem(models.Model):
    content = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content + ' | ' + str(self.completed)
