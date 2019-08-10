from django.conf import settings
from django.forms import forms, fields, widgets


class ColorBoardForm(forms.Form):
    players_count = fields.IntegerField(min_value=1, max_value=4, initial=2,
                                        label="Number of players")
    squares_count = fields.IntegerField(min_value=1, max_value=79, initial=1,
                                        label="Number of squares on the board")
    cards_count = fields.IntegerField(min_value=1, max_value=200, initial=1,
                                      label="Number of cards in the deck")
    squares_board = fields.CharField(label="Characters representing the colored squares on the board",
                                     widget=widgets.Textarea(attrs={"rows": 2}))

    cards_on_deck = fields.CharField(
        label="Cards in the deck",
        widget=widgets.Textarea(attrs={
            "rows": 2,
            "title": "as a comma separated string."
        })
    )

    error_messages = {
        "invalid_form": "Check form and fix form errors.",
        "invalid_squares_board": (
            "Please enter a correct characters representing the colored squares on the board.\n"
            "Note that '%(squares_board)s' length must be equals to '%(squares_count)s'."
        ),
        "invalid_cards_on_deck": (
            "Please enter a correct cards in the deck.\n"
            "Note that '%(cards_on_deck)s' length must be equals to '%(cards_count)s',\n"
            "and length every cards must be 1 or 2."
        ),
    }

    global_validation_error = forms.ValidationError(error_messages['invalid_form'], code='invalid_form')

    def clean(self):

        cards_separator = getattr(settings, "CARD_FORM_SEPARATOR", ",")

        # Trim input data (remove spaces from input)
        self.cleaned_data["cards_on_deck"] = [
            x.strip() for x in self.cleaned_data.get("cards_on_deck", "").split(cards_separator)
        ]
        self.cleaned_data["squares_board"] = list(filter(lambda x: x, self.cleaned_data.get("squares_board", "")))

        # Check if all params valid
        if self.cleaned_data.get("squares_count") != len(self.cleaned_data["squares_board"]):
            self.add_error("squares_board", forms.ValidationError(
                self.error_messages['invalid_squares_board'],
                code='invalid_squares_board',
                params={'squares_board': self.fields["squares_board"].label,
                        'squares_count': self.fields["squares_count"].label},
            ))
            raise self.global_validation_error

        if any((
                self.cleaned_data.get("cards_count") != len(self.cleaned_data["cards_on_deck"]),
                not all((map(lambda x: 0 < len(x) < 3, self.cleaned_data["cards_on_deck"])))
        )):
            self.add_error("cards_on_deck", forms.ValidationError(
                self.error_messages['invalid_cards_on_deck'],
                code='invalid_cards_on_deck',
                params={'cards_on_deck': self.fields["cards_on_deck"].label,
                        'cards_count': self.fields["cards_count"].label},
            ))
            raise self.global_validation_error

        return self.cleaned_data
