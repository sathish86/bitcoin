# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from poloniex import Poloniex

# Create your views here.


def index(request):
    polo = Poloniex()
    records = polo.returnTicker()
    return render(request, 'bc_api/home.html', {'latest_usdt_btc': records['USDT_BTC'],  'records': records})
