from django.views import View
from django.shortcuts import render, redirect

class Login(View):
    def get(self, request):

        return render(request, 'vue_index.html')