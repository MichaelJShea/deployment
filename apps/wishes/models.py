from django.db import models
from apps.login_register.models import User


class WishManager(models.Manager):

    def wish_validator(self, PostData):
        errors = {}

        is_valid = True

        if len(PostData['wish_item']) == 0:
            is_valid = False
            errors['wish_item'] = "Wish must not be empty"
        if len(PostData['wish_item']) != 0:
            if len(PostData['wish_item']) < 3:
                is_valid = False
                errors['wish_item'] = "Wish must be longer than 3 characters"

        if len(PostData['wish_description']) == 0:
            is_valid = False
            errors['wish_description'] = "Description must not be empty"
        if len(PostData['wish_description']) != 0:
            if len(PostData['wish_description']) < 3:
                is_valid = False
                errors['wish_description'] = "Description must be longer than 3 characters"

    
        if is_valid == False:
            return errors

    def update_validator(self, PostData):
        errors = {}

        is_valid = True

        if len(PostData['update_item']) == 0:
            is_valid = False
            errors['update_item'] = "Updated Wish must not be empty"
        if len(PostData['update_item']) != 0:
            if len(PostData['update_item']) < 3:
                is_valid = False
                errors['update_item'] = "Updated Wish must be longer than 3 characters"

        if len(PostData['update_description']) == 0:
            is_valid = False
            errors['update_description'] = "Updated Description must not be empty"
        if len(PostData['update_description']) != 0:
            if len(PostData['update_description']) < 3:
                is_valid = False
                errors['update_description'] = "Updated Description must be longer than 3 characters"

        

        if is_valid == False:
            return errors

class wishes(models.Model):
    item = models.CharField(max_length = 255)
    description = models.TextField()
    wisher = models.ForeignKey(User, related_name = 'made_wish')
    granted_at = models.DateField(null = True)
    likes = models.ManyToManyField(User, related_name='liked')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = WishManager()
