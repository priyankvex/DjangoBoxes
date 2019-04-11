from django.contrib.auth.models import User
from django.db import models


class CreateUpdateAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class Box(CreateUpdateAbstractModel):
    length = models.PositiveIntegerField(help_text="Length of the cuboid")
    breadth = models.PositiveIntegerField(help_text="Breadth of the cuboid")
    height = models.PositiveIntegerField(help_text="Height of the cuboid")
    created_by = models.ForeignKey(
        User, help_text="Creator of the box. This will never change once it's set.",
        on_delete=models.CASCADE, related_name="created_by"
    )
