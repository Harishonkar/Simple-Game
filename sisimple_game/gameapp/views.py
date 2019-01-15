from django.shortcuts import render
from .models import Hero
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CreateHero(APIView):

    def post(self, request, format=None):
        if request.method == 'POST':
            print("inside post if")

            new_hero=Hero.objects.create('alive','0')
            new_hero.save()
            data={
            'new_hero':new_hero.id,
            'status':new_hero.status,
            'win_score':new_hero.win_score,
            }
            return Response(data)
