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
        data={
        'fail':'fail'
        }
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
                    score=get_hero.win_score
                    print(type(score))
                    get_hero.win_score=int(score)+1
                    get_hero.save()

                print("********************************************")
                data={
                'new_hero':get_hero.id,
                'status':get_hero.status,
                'win_score':get_hero.win_score,
                }
            return Response(data)

        return Response(data)




class become_champion(APIView):

    def post(self, request, format=None):

        print("entered become Chanpion get function")
        if request.method == 'POST':
            print("inside get if")
            get_alive_list=Hero.objects.filter(status='alive').order_by('-win_score')
            get_champion=get_alive_list[0]
            print("champ======================",get_champion.status)
            for alive_obj in get_alive_list:
                if alive_obj.id != get_champion.id:
                    alive_obj.status='dead'
                    alive_obj.save()
            data={
            'new_hero':get_champion.id,
            'status':get_champion.status,
            'win_score':get_champion.win_score,
            }
        return Response(data)
