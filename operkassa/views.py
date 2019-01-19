from .models import Oper
from .forms import OperForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


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


def oper_new(request):
    if request.method == "POST":
        form = OperForm(request.POST)
        if form.is_valid():
            oper = form.save(commit=False)
            oper.author = request.user
            oper.save()
            return redirect('oper_detail', pk=oper.pk)
    else:
        form = OperForm()
    return render(request, 'operkassa/oper_edit.html', {'form': form})


def oper_edit(request, pk):
    oper = get_object_or_404(Oper, pk=pk)
    if request.method == "POST":
        form = OperForm(request.POST, instance=oper)
        if form.is_valid():
            oper = form.save(commit=False)
            oper.author = request.user
            oper.save()
            return redirect('oper_detail', pk=oper.pk)
    else:
        form = OperForm(instance=oper)
    return render(request, 'operkassa/oper_edit.html', {'form': form})