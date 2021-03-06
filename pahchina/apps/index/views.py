#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render_to_response as r2r, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm

from ..news.models import News, Sorts
from ..website.models import Website


class Index(generic.TemplateView):
    """ 网站首页
    """
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['sort_is_index'] = Sorts.objects.filter(is_index=True).order_by("-weight")
        context['websites'] = Website.objects.all().order_by('id')
        return context

    template_name = 'index.html'

class ListNews(generic.DetailView):

    model = Sorts
    template_name = "index/list-news.html"

    #def __init__(self, *args, **kwargs):
    #    super(ListNews, self).__init__(*args, **kwargs)
    #    self._sort = get_object_or_404(Sorts, id=self.kwargs['sort_id'])

    def get_context_data(self, **kwargs):
        context = super(ListNews, self).get_context_data(**kwargs)
        context['sort_news_list'] = News.objects.filter(sort=self.object)
        context['sort'] = self.object
        return context


class About(generic.TemplateView):

    template_name = 'about.html'