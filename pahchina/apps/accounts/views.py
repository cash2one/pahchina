#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render_to_response as r2r
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(generic.FormView):
    form_class = UserCreationForm
    template_name = 'register.html'


def pah_login(request):
    """ 网站登录
    根据不同身份用户跳转到不同的页面
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('admin-index'))
                else:
                    return HttpResponse('请定义页面')
            else:
                return HttpResponse('用户没有激活')
        else:
            return HttpResponse('用户名与密码不匹配')

    form = AuthenticationForm
    return r2r('login.html', locals(), context_instance = RequestContext(request))

def pah_logout(request):
    """ 网站登出
    """
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@user_passes_test(lambda u: u.is_superuser)
def admin_index(request):
    """ 网站后台首页
    """
    return r2r('admin-index.html', locals(),
               context_instance=RequestContext(request))

class ListUser(generic.ListView):
    """ 列出所有用户
    """
    model = User
    context_object_name = 'user_list'
    template_name = 'list-user.html'


class DetailUser(generic.DetailView):
    """ 查看用户详情
    """
    model = User
    context_object_name = 'object_user'
    template_name = 'detail-user.html'

class CreateUser(generic.CreateView):
    """ 创建用户
    """
    model = User
    success_url = reverse_lazy('list-user')
    template_name = 'update-user.html'

class UpdateUser(generic.UpdateView):
    """ 更新用户详情
    """
    model = User
    success_url = reverse_lazy('list-user')
    template_name = 'update-user.html'


class DeleteUser(generic.DeleteView):
    """ 删除用户
    """
    model = User
    template_name = 'user_confirm_delete.html'