from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200)

    short_description = models.TextField()

    technology = models.CharField(max_length=300)

    project_url = models.URLField(
        blank=True,
        null=True
    )

    github_url = models.URLField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Skill(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "name"]


class Service(models.Model):

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order", "title"]

class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"        

