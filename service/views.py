from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from django.http.response import HttpResponseRedirect

from .models import ColorBoard
from .forms import ColorBoardForm


class ColorBoardCreateView(View):

    def get(self, request):
        return render(request, "game-create.html", {"form": ColorBoardForm()})

    def post(self, request):
        form = ColorBoardForm(request.POST)

        if not form.is_valid():
            return render(request, "game-create.html", {"form": form})

        validated_data = form.cleaned_data
        result = self.solve(validated_data)
        game = self.save_game(validated_data, result)

        return HttpResponseRedirect(reverse("color-board-view", kwargs={"pk": game.pk}))

    @classmethod
    def solve(cls, validated_data):
        player_start_positions = [-1] * validated_data["players_count"]

        for idx, card in enumerate(validated_data["cards_on_deck"]):
            cur_player = idx % validated_data["players_count"]
            cur_position = player_start_positions[cur_player] + 1

            for symbol in card:
                try:
                    cur_position = validated_data["squares_board"].index(symbol, cur_position + (len(card) - 1))
                except ValueError:  # not found index after start position
                    return {"player": cur_player + 1, "cards": idx + 1}

            if cur_position == validated_data["squares_count"] - 1:  # Last step
                return {"player": cur_player + 1, "cards": idx + 1}

            player_start_positions[cur_player] = cur_position

        return {"player": None, "cards": validated_data["cards_count"]}

    @classmethod
    def save_game(cls, validated_data, game_result):
        return ColorBoard.objects.create(
            players_count=validated_data["players_count"],
            board=",".join(validated_data["squares_board"]),
            cards=",".join(validated_data["cards_on_deck"]),
            winner=game_result['player'],
            last_move=game_result["cards"]
        )


class ColorBoardListView(ListView):
    context_object_name = "games_list"
    template_name = "game-list.html"
    queryset = ColorBoard.objects.all()


class ColorBoardDetailView(DetailView):
    context_object_name = "game"
    template_name = "game-view.html"
    queryset = ColorBoard.objects.all()
