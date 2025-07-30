from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='hr').exists():
                return redirect('hr-view')
        return render(request, 'vue_index.html')

class HrView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.groups.filter(name='hr').exists():
            return render(request, 'vue_index.html')
        return render(request, 'unauthorized.html')
        