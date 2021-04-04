#-*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from mailer.models import Company, Contact
from django.db.models import Sum, Count, Prefetch


class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100
    
    def get_queryset(self, **kwargs):
        queryset = super(IndexView, self).get_queryset()
        queryset = Company.objects.prefetch_related('orders').prefetch_related(Prefetch('contacts',queryset=Contact.objects.annotate(order_count=Count('orders')))).annotate(order_count=Count('orders'),total_sum=Sum('orders__total'))
        return queryset