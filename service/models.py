from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class ColorBoard(models.Model):
    players_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)],
                                        verbose_name="Number of players")
    board = models.TextField(verbose_name="Sequence of characters on the board")
    cards = models.TextField(verbose_name="Cards in the deck")

    winner = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)],
                                 verbose_name="Winner of game", null=True)
    last_move = models.PositiveIntegerField(verbose_name="Number of last move in game")

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ColorBoard Game"
        verbose_name_plural = "ColorBoard Games"
        db_table = "service_game_color_board"
