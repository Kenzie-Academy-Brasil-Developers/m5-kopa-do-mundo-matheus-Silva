from urllib import request, response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError, data_processing
from teams.models import Team
from django.forms.models import model_to_dict


class TeamView(APIView):
    def post(self, request):
        team_data = request.data
        if team_data["titles"] < 0:
            return Response({"error": "titles cannot be negative"}, status =400)

        year_cup = int(team_data["first_cup"][0:4])

        if (year_cup - 1930) % 4 != 0 or year_cup < 1930:
            return Response({"error": "there was no world cup this year"}, status =400)

        if year_cup > 2020:
            return Response({"error": "impossible to have more titles than disputed cups"}, status =400)

        new_data = Team.objects.create(**team_data)
        return Response(model_to_dict(new_data), 201)

    def get(self, request):
        team = list(Team.objects.values())
        return Response(team)

class TeamDetailsView(APIView):

    def get(self, request, team_id):
        try:
            list_id = Team.objects.get(id = team_id)
            return Response(model_to_dict(list_id), status=200)    
        except(Team.DoesNotExist):
            return Response({"message": "Team not found"}, status=404)

    def delete(self , request, team_id):
        try:
            delete_id = Team.objects.get(id = team_id)
            delete_id.delete()
            return Response (status=204)
        except(Team.DoesNotExist):
            return Response({"message": "Team not found"}, status=404)

    def patch(self , request, team_id):
        try:
            items = request.data.items()
            team = Team.objects.get(id = team_id)
            for key,value in items:
                setattr(team ,key,value)     
            team.save()
            return Response(model_to_dict(team), status=200)       
        except(Team.DoesNotExist):
            return Response({"message": "Team not found"}, status=404)
