from django.db import models


class Promotion(models.Model):
    graduation_year = models.PositiveIntegerField(default=0)
    FOND = 'FOND'
    APP = 'APP'
    MAR = 'MAR'
    MAP = 'MAP'
    TYPE_OF_STUDY = [
        (FOND, 'Licence Fondamentale'),
        (APP, 'Licence Appliquée'),
        (MAR, 'Master de Recherche'),
        (MAP, 'Master Professionel'),
    ]
    year_in_school = models.CharField(
        max_length=5,
        choices=TYPE_OF_STUDY,
        default=FOND,
    )
