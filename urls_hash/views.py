# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from urls_hash.forms import HashUrlForm
from urls_hash.models import HashedUrl


class UrlHashView(View):

    def post(self, request):
        form = HashUrlForm(data=request.POST)

        if form.is_valid():
            form.save()
            path = reverse('hashed_url', args=[form.cleaned_data['hash_value']])
            url = request.build_absolute_uri(path)

            return render(request, 'result.html', {'hashed_url': url})

        return render(request, 'hash-form.html', {'form': form})

    def get(self, request):
        form = HashUrlForm()

        return render(request, 'hash-form.html', {'form': form})


class HashedUrlView(View):

    def get(self, request, hash_value):
        hashed_url = get_object_or_404(HashedUrl, hash_value=hash_value)

        return redirect(hashed_url.url)
