from django.shortcuts import render


def oper_list(request):
    return render(request, 'operkassa/oper_list.html', {})