from django.shortcuts import render
from .models import Hero
from rest_framework.views import APIView
from rest_framework.response import Response
from random import sample,randint
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class CreateHero(APIView):

    def post(self, request, format=None):
        print("entered post function")
        if request.method == 'POST':
            print("inside post if")

            new_hero=Hero.objects.create(status='alive',win_score=0)
            new_hero.save()
            data={
            'new_hero':new_hero.id,
            'status':new_hero.status,
            'win_score':new_hero.win_score,
            }
            return Response(data)




class FightToDeath(APIView):
    def post(self, request, format=None):

        print("entered FIGHT TO DEATH post function")
        if request.method == 'POST':
            print("inside post if")

            new_hero=Hero.objects.filter(status='alive').values_list('id',flat=True)
            print("object ",new_hero)
            if len(new_hero)>=2:
            #names = ["Conor", "Esther", "Jonty", "Elwin", "Elise"]
                print("entedred ifffffff")
                chosen = sample(list(new_hero), 2)
                print("chosen",chosen)
                index = sample(chosen,1)
                print("index",index,"..............................")
                get_hero=Hero.objects.get(id=index[0])

                print("get_hero", get_hero)
                get_hero.status='dead'

                get_hero.save()
                print("saved,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                if  chosen[0] != index[0]:
                    print("if ======================")
                    get_hero=Hero.objects.get(id=chosen[0])
                    score=get_hero.win_score
                    print(type(score))
                    get_hero.win_score=int(score)+1
                    get_hero.save()
                else:
                    print("else------------------------------")
                    get_hero=Hero.objects.get(id=chosen[1])
                    get_hero.win_score=get_hero.win_score+1
                    get_hero.save()

                print("********************************************")
                data={
                'new_hero':get_hero.id,
                'status':get_hero.status,
                'win_score':get_hero.win_score,
                }
        return Response(data)
