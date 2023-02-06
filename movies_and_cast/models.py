from django.db import models

from generics.generics import CreatedUpdatedMixin


class Movie(CreatedUpdatedMixin):
    title = models.CharField(max_length=50)
    runtime = models.IntegerField()
    language = models.CharField(max_length=15)
    tagline = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Cast(CreatedUpdatedMixin):

    GENDER_CHOICE = (("M", "Male"), ("F", "Female"), ("O", "Other"))

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    dob = models.DateField(help_text="Date of birth")
    movie = models.ForeignKey(
        Movie, on_delete=models.DO_NOTHING, related_name="movie_casts"
    )

    def __str__(self):
        return self.name
