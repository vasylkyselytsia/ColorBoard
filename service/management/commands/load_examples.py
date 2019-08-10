# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings

# Import View Only For Creation Example (bad practice, because helper or util creation needed)
from service.views import ColorBoardCreateView


class Command(BaseCommand):
    SEPARATOR = getattr(settings, "CARD_FORM_SEPARATOR", ",")

    EXAMPLE_DATA = [
        {
            "players_count": 2,
            "squares_count": 13,
            "cards_count": 8,
            "squares_board": list("RYGPBRYGBRPOP"),
            "cards_on_deck": "R,B,GG,Y,P,B,P,RR".split(SEPARATOR),
        },
        {
            "players_count": 2,
            "squares_count": 6,
            "cards_count": 5,
            "squares_board": list("RYGRYB"),
            "cards_on_deck": "R,YY,G,G,B".split(SEPARATOR),
        },
        {
            "players_count": 3,
            "squares_count": 9,
            "cards_count": 6,
            "squares_board": list("QQQQQQQQQ"),
            "cards_on_deck": "Q,QQ,Q,Q,QQ,Q".split(SEPARATOR),
        },
        {
            "players_count": 4,
            "squares_count": 13,
            "cards_count": 8,
            "squares_board": list("RYGPBRYGBRPOP"),
            "cards_on_deck": "R,B,GG,Y,P,B,P,RR".split(SEPARATOR),
        },
        {
            "players_count": 3,
            "squares_count": 79,
            "cards_count": 10,
            "squares_board": list("ABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNOPQRSTUVWXYABCD"),
            "cards_on_deck": "D,BB,CC,E,A,BB,EE,DD,CC,AA".split(SEPARATOR),
        },
        {
            "players_count": 1,
            "squares_count": 10,
            "cards_count": 5,
            "squares_board": list("ABCDEABCDE"),
            "cards_on_deck": "A,B,A,BB,E".split(SEPARATOR),
        },
        {
            "players_count": 4,
            "squares_count": 1,
            "cards_count": 1,
            "squares_board": ["Z"],
            "cards_on_deck": "X",
        },
        {
            "players_count": 4,
            "squares_count": 79,
            "cards_count": 200,
            "squares_board": list("ABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNOPQRSTUVWXYABCD"),
            "cards_on_deck": ("A,A,A,A,B,B,B,B,C,C,C,C,D,D,D,D,E,E,E,E,F,F,F,F,G,G,G,"
                              "G,H,H,H,H,I,I,I,I,J,J,J,J,K,K,K,K,L,L,L,L,M,M,M,M,N,N,N,N,O,O,O,O,P,P,"
                              "P,P,Q,Q,Q,Q,R,R,R,R,S,S,S,S,T,T,T,T,U,U,U,U,V,V,V,V,W,W,W,W,X,X,X,"
                              "X,Y,Y,Y,Y,A,A,A,A,B,B,B,B,C,C,C,C,D,D,D,D,E,E,E,E,F,F,F,F,G,G,G,G,H,"
                              "H,H,H,I,I,I,I,J,J,J,J,K,K,K,K,L,L,L,L,M,M,M,M,N,N,N,N,O,O,O,O,P,P,P,P,"
                              "Q,Q,Q,Q,R,R,R,R,S,S,S,S,T,T,T,T,U,U,U,U,V,V,V,V,W,W,W,W,X,X,X,X,Y,"
                              "Y,Y,Y").split(SEPARATOR),
        },
        {
            "players_count": 4,
            "squares_count": 79,
            "cards_count": 100,
            "squares_board": list("ABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNOPQRSTUVWXYABCD"),
            "cards_on_deck": ("A,A,A,A,B,B,B,B,C,C,C,C,D,D,D,D,E,E,E,E,F,F,F,F,G,G,G,"
                              "G,H,H,H,H,I,I,I,I,J,J,J,J,K,K,K,K,L,L,L,L,M,M,M,M,N,N,N,N,O,O,O,O,P,P,"
                              "P,P,Q,Q,Q,Q,R,R,R,R,S,S,S,S,T,T,T,T,U,U,U,U,V,V,V,V,W,W,W,W,X,X,X,"
                              "X,Y,Y,Y,Z").split(SEPARATOR),
        },

    ]

    def handle(self, *args, **kwargs):
        for data in self.EXAMPLE_DATA:
            ColorBoardCreateView.save_game(data, ColorBoardCreateView.solve(data))
