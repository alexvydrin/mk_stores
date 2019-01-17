from django.shortcuts import render
from .models import Oper
from django.shortcuts import render, get_object_or_404

def oper_list(request):
    #opers = Oper.objects.filter(date__gte=0).order_by('date')
    opers = Oper.objects.all().order_by('date')
    sum_debet_total = 0
    sum_credit_total = 0
    for oper in opers:
        sum_debet_total += oper.sum_debet
        sum_credit_total += oper.sum_credit
    context = {
        'opers': opers,
        'sum_debet_total': sum_debet_total,
        'sum_credit_total': sum_credit_total}
    return render(request, 'operkassa/oper_list.html', context=context)

def oper_detail(request, pk):
    oper = get_object_or_404(Oper, pk=pk)
    return render(request, 'operkassa/oper_detail.html', {'oper': oper})