# from django.shortcuts import render, redirect, render_to_response, HttpResponse, RequestContext
from django.shortcuts import render, redirect, HttpResponse     #, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import Http404, JsonResponse
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.views import generic
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import News, ReadLater, NewsWithRead, FollowNew, MediaInterest
from apps.media.models import Media
from apps.base import views


# def home(request):
#     return render(request, 'news/home.html')
    
def home(request):
    return render(request, 'news/home.html')
    # template = 'home.html'
    # template = 'news/home.html'
#     msg = ''
#     if request.user.is_authenticated():

#         follows = FollowNew.objects.filter(user=request.user, marked=True).order_by('timestamp')[:10:0]
#         follownews_menu = []
#         for follow in follows:
#             x = News.objects.get(id=follow.news.id)
#             follownews_menu.append(x)

#         reads = ReadLater.objects.filter(user=request.user, marked=True).order_by('timestamp')[:10:0]
#         readnews_menu = []
#         for read in reads:
#             x = News.objects.get(id=read.news.id)
#             readnews_menu.append(x)

#         interests = MediaInterest.objects.filter(user=request.user, marked=True)
#         if interests:
#             newsformedia = []
#             medias = []
#             news_list = []
#             for interest in interests:
#                 medias.append(interest.media)
#                 newsfrommedia = News.objects.filter(media=interest.media).order_by('-timestamp')
#                 for news in newsfrommedia:
#                     #newsformedia.append(news)
#                     r1 = ReadLater.objects.filter(user=request.user, news_id=news.pk, marked=True)
#                     f1 = FollowNew.objects.filter(user=request.user, news_id=news.pk, marked=True)
#                     if r1.exists():
#                         if f1.exists():
#                             newsformedia.append({'news': news, 'pk': news.pk, 'r1': True, 'f1':True})
#                         else:
#                             newsformedia.append({'news': news, 'pk': news.pk, 'r1': True, 'f1': False})
#                     else:
#                         if f1.exists():
#                             newsformedia.append({'news': news, 'pk': news.pk, 'r1': False, 'f1':True})
#                         else:
#                             newsformedia.append({'news': news, 'pk': news.pk, 'r1': False, 'f1': False})
#             medias = medias
#             news = newsformedia
#             msg = "none"
#         else:
#            msg = "block"
#            medias = Media.objects.all().order_by('name')
#            news = News.objects.all().order_by('-timestamp')
#            newsformedia = []
#            for news in news:
#                r1 = ReadLater.objects.filter(user=request.user, news_id=news.pk, marked=True)
#                f1 = FollowNew.objects.filter(user=request.user, news_id=news.pk, marked=True)
#                if r1.exists():
#                    if f1.exists():
#                        newsformedia.append({'news': news, 'pk': news.pk, 'r1': True, 'f1': True})
#                    else:
#                        newsformedia.append({'news': news, 'pk': news.pk, 'r1': True, 'f1': False})
#                else:
#                    if f1.exists():
#                        newsformedia.append({'news': news, 'pk': news.pk, 'r1': False, 'f1': True})
#                    else:
#                        newsformedia.append({'news': news, 'pk': news.pk, 'r1': False, 'f1': False})
#         if request.is_ajax():
#             template = 'entry_list_page.html'
#         # return render(
#         #     template, {'msg': msg, 'medias': medias, 'news': newsformedia, 'follownews_menu':follownews_menu, 'readnews_menu':readnews_menu}, context_instance=RequestContext(request))
#         return render(request, template, {'msg': msg, 'medias': medias, 'news': newsformedia, 'follownews_menu':follownews_menu, 'readnews_menu':readnews_menu})
#     else:
#         # medias = Media.objects.all()
#         medias = Media.objects.all().order_by('name')
#         # news = News.objects.all()
#         news = News.objects.all().order_by('-timestamp')
#         if request.is_ajax():
#             template = 'entry_list_page.html'
#         # return render(
#         #     template, {'msg': msg, 'medias': medias, 'news': news}, context_instance=RequestContext(request))
#         return render(request, template, {'msg': msg, 'medias': medias, 'news': news})





#     #return render_to_response("home.html", {'msg':msg, 'medias':medias, 'news':news}, context_instance=RequestContext(request))


# def media(request, slug):
#     msg = ''
#     template = 'mediawithnews.html'

#     if request.user.is_authenticated():

#         follows = FollowNew.objects.filter(user=request.user, marked=True).order_by('timestamp')[:10:0]
#         follownews_menu = []
#         for follow in follows:
#             x = News.objects.get(id=follow.news.id)
#             follownews_menu.append(x)

#         reads = ReadLater.objects.filter(user=request.user, marked=True).order_by('timestamp')[:10:0]
#         readnews_menu = []
#         for read in reads:
#             x = News.objects.get(id=read.news.id)
#             readnews_menu.append(x)

#         newsformedia = []
#         newsfrommedia = News.objects.filter(media__slug=slug).order_by('-timestamp')
#         #newsfrommedia = News.objects.filter(media=interest.media)
#         for news in newsfrommedia:
#             # newsformedia.append(news)
#             r1 = ReadLater.objects.filter(user=request.user, news_id=news.pk, marked=True)
#             f1 = FollowNew.objects.filter(user=request.user, news_id=news.pk, marked=True)
#             if r1.exists():
#                 if f1.exists():
#                     newsformedia.append({'news': news, 'pk': news.pk, 'r1': True, 'f1': True})
#                 else:
#                     newsformedia.append({'news': news, 'pk': news.pk, 'r1': True, 'f1': False})
#             else:
#                 if f1.exists():
#                     newsformedia.append({'news': news, 'pk': news.pk, 'r1': False, 'f1': True})
#                 else:
#                     newsformedia.append({'news': news, 'pk': news.pk, 'r1': False, 'f1': False})
#         media = Media.objects.get(slug=slug)
#         interests = MediaInterest.objects.filter(user=request.user, marked=True)
#         if interests:
#             medias = []
#             for interest in interests:
#                 medias.append(interest.media)
#         else:
#             media = Media.objects.get(slug=slug)
#             # medias = Media.objects.all()
#             medias = Media.objects.all().order_by('name')
#             news = News.objects.filter(media__slug=slug).order_by('-timestamp')
#         if request.is_ajax():
#             template = 'entry_list_page.html'
#         # return render(
#         #     template, {'msg': msg, 'medias': medias, 'media': media, 'news': newsformedia, 'follownews_menu':follownews_menu, 'readnews_menu':readnews_menu},
#         #     context_instance=RequestContext(request))
#         return render(request, template, {'msg': msg, 'medias': medias, 'media': media, 'news': newsformedia, 'follownews_menu':follownews_menu, 'readnews_menu':readnews_menu})
#     else:
#         media = Media.objects.get(slug=slug)
#         # medias = Media.objects.all()
#         medias = Media.objects.all().order_by('name')
#         # news = News.objects.filter(media__slug=slug)
#         news = News.objects.filter(media__slug=slug).order_by('-timestamp')
#         if request.is_ajax():
#             template = 'entry_list_page.html'
#         # return render(
#         #     template, {'msg':msg, 'medias':medias, 'media':media,'news':news}, context_instance=RequestContext(request))
#         return render(request, template, {'msg':msg, 'medias':medias, 'media':media,'news':news})


# class NewsListView(views.AddMediaMixin,
#                    generic.ListView):
#     model = News
#     queryset = News.objects.all().order_by("order", "timestamp")
#     #paginate_by = 8
#     # queryset = News.objects.exclude(delete=True)
#     context_object_name = "news_list"
#     template_name = "starter.html"

#     def get_queryset(self):
#         media = None
#         slug = slug = self._get_slug()
#         if slug:
#             media = Media.objects.get(slug=slug)
#         if self.request.user.is_authenticated():
#             queryset = NewsWithRead.objects.with_user(self.request.user, media)
#         else:
#             queryset = super().get_queryset()
#             if media:
#                 queryset = queryset.filter(media=media)
#         return queryset

#     def _get_slug(self):
#         if self.kwargs.get("slug", None):
#             return self.kwargs.get("slug")


# class NewsView(generic.ListView):
#     model = News
#     #paginate_by = 8
#     template_name = "news2.html"
#     context_object_name = "news_list"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         slug = self._get_slug()
#         if self.request.user.is_authenticated():
#             queryset = queryset.filter(Q(news_readlater_news__isnull=True) | Q(news_readlater_news__user=self.request.user ))
#         if slug:
#             queryset = queryset.filter(media__slug=slug)
#         return queryset

#     def _get_slug(self):
#         if self.kwargs.get("slug", None):
#             return self.kwargs.get("slug")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = self._get_slug()
#         if slug:
#             context["media_name"] = Media.objects.get(slug=slug).name
#         return context

#     def render_to_response(self, context, **response_kwargs):
#         response = super().render_to_response(context, **response_kwargs)
#         return JsonResponse({"html": response.rendered_content})


# class ReadLaterDetailView(generic.DetailView):
#     model = ReadLater
#     template_name = "readlater.html"
#     slug_field = "news_id"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user=self.request.user)

#     def render_to_response(self, context, **response_kwargs):
#         response = super().render_to_response(context, **response_kwargs)
#         if self.request.is_ajax():
#             return JsonResponse({"html": response.rendered_content})
#         return response


# def view_read_later(request, pk):
#     if not request.user.is_authenticated():
#         raise Http404
#     r1 = ReadLater.objects.filter(user=request.user, news_id=pk)
#     if r1.exists():
#         r1 = r1.get()
#     else:
#         r1, created = ReadLater.objects.get_or_create(user=request.user, news_id=pk)
#     r1.marked = not r1.marked
#     r1.save()

#     if request.is_ajax():
#         return JsonResponse({"html": render_to_string("readlater.html", context={"readlater": r1.marked, "pk":pk}, request=request)})
#     return render(request, "readlater.html", {"readlaters": r1.marked, "pk":pk})


# class FollowNewDetailView(generic.DetailView):
#     model = FollowNew
#     template_name = "follownew.html"
#     slug_field = "news_id"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user=self.request.user)

#     def render_to_response(self, context, **response_kwargs):
#         response = super().render_to_response(context, **response_kwargs)
#         if self.request.is_ajax():
#             return JsonResponse({"html": response.rendered_content})
#         return response


# def view_follow_new(request, pk):
#     if not request.user.is_authenticated():
#         raise Http404
#     r1 = FollowNew.objects.filter(user=request.user, news_id=pk)
#     if r1.exists():
#         r1 = r1.get()
#     else:
#         r1, created = FollowNew.objects.get_or_create(user=request.user, news_id=pk)
#     r1.marked = not r1.marked
#     r1.save()

#     if request.is_ajax():
#         return JsonResponse({"html": render_to_string("follownew.html", context={"follownew": r1.marked, "pk":pk}, request=request)})
#     return render(request, "follownew.html", {"follownew": r1.marked, "pk":pk})


# @login_required
# def medias(request):
#     medias = Media.objects.all().order_by('name')
#     u = request.user
#     medias_list = []
#     for x in medias:
#         try:
#             m = MediaInterest.objects.get(user=u, media=x.pk)
#             if m.marked == True:
#                 medias_list.append({'name':x, 'pk': x.pk, 'marked':True})
#             elif m.marked == False:
#                 medias_list.append({'name': x, 'pk': x.pk, 'marked': False})
#         except ObjectDoesNotExist:
#             medias_list.append({'name': x, 'pk': x.pk, 'marked': False})
#             pass
#     if request.is_ajax():
#         # return render("media.html", {'medias': medias_list}, context_instance=RequestContext(request))
#         return render(request, "media.html", {'medias': medias_list})
#     else:
#         # return render("media.html", {'medias': medias_list}, context_instance=RequestContext(request))
#         return render(request, "media.html", {'medias': medias_list})

# @login_required
# def mediaswithnews(request):
#     intereses = MediaInterest.objects.filter(user=request.user, marked=True)
#     noticiasxmedio = []
#     for medio in intereses:
#         noticias = News.objects.filter(media=medio.media)
#         for noticia in noticias:
#             noticiasxmedio.append(noticia)
#     # return render("mediawithnews.html", {'noticiasxmedio': noticiasxmedio}, context_instance=RequestContext(request))
#     return render(request, "mediawithnews.html", {'noticiasxmedio': noticiasxmedio})

# @login_required
# class FollowMediaDetailView(generic.DetailView):
#     model = MediaInterest
#     template_name = "mediafollow.html"
#     slug_field = "media"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user=self.request.user)

#     def render_to_response(self, context, **response_kwargs):
#         response = super().render_to_response(context, **response_kwargs)
#         if self.request.is_ajax():
#             return JsonResponse({"html": response.rendered_content})
#         return response

# @login_required
# def view_follow_media(request, pk):
#     if not request.user.is_authenticated():
#         raise Http404
#     r1 = MediaInterest.objects.filter(user=request.user, media_id=pk)
#     if r1.exists():
#         r1 = r1.get()
#     else:
#         r1, created = MediaInterest.objects.get_or_create(user=request.user, media_id=pk)
#     r1.marked = not r1.marked
#     r1.save()

#     if request.is_ajax():
#         return JsonResponse({"html": render_to_string("mediafollow.html", context={"mediofollow": r1.marked, "pk":pk}, request=request)})
#     return render(request, "mediafollow.html", {"mediofollow": r1.marked, "pk":pk})

# @login_required
# def myfollownews(request):

#     if not request.user.is_authenticated():
#         raise Http404

#     follows_m = FollowNew.objects.filter(user=request.user, marked=True).order_by('timestamp')[:10:0]
#     follownews_menu = []
#     for follow in follows_m:
#         x = News.objects.get(id=follow.news.id)
#         follownews_menu.append(x)

#     reads_m = ReadLater.objects.filter(user=request.user, marked=True).order_by('timestamp')[:10:0]
#     readnews_menu = []
#     for read in reads_m:
#         x = News.objects.get(id=read.news.id)
#         readnews_menu.append(x)

#     follows = FollowNew.objects.filter(user=request.user, marked=True)
#     news = []
#     for follow in follows:
#         x = News.objects.get(id=follow.news.id)
#         news.append({'news': x, 'pk': x.pk, 'r1': True, 'f1': True, 'follow':follow})

#     return render(request, "myfollownews.html", {"news": news, "follownews_menu":follownews_menu, "readnews_menu": readnews_menu})

# @login_required
# def myreadlaternews(request):
#     if not request.user.is_authenticated():
#         raise Http404

#     reads = ReadLater.objects.filter(user=request.user)
#     news = []
#     for read in reads:
#         x = News.objects.get(id=read.news.id)
#         news.append(x)

#     follows_m = FollowNew.objects.filter(user=request.user).order_by('timestamp')[:10:0]
#     follownews_menu = []
#     for follow in follows_m:
#         x = News.objects.get(id=follow.news.id)
#         follownews_menu.append(x)

#     reads_m = ReadLater.objects.filter(user=request.user).order_by('timestamp')[:10:0]
#     readnews_menu = []
#     for read in reads_m:
#         x = News.objects.get(id=read.news.id)
#         readnews_menu.append(x)

#     return render(request, "myreadlaternews.html", {"news": news, "follownews_menu":follownews_menu, "readnews_menu": readnews_menu})

# def busqueda(new, list):
#     import operator
#     import functools
#     from django.db.models import Q
#     noticia= new
#     q = list
#     enlace = "http://ynews.co/myfollownews/#"+str(noticia.pk)
#     query = functools.reduce(operator.and_, (Q(short_desc__contains=item) or Q(title__contains=item) for item in q))
#     result = News.objects.filter(query)

#     from django.core.mail import send_mail

#     mensaje = "Hemos encontrado la siguientes relaciones a la noticia seguida por usted el día "+str(noticia.timestamp)+\
#               " titulada: '"+str(noticia.title)+"'. Para ir a la noticia da clic en el siguiente enlace: \n \n"+\
#               enlace+"\n \n Atentamente, \n \n ynews.co"

#     send_mail(
#         'Nueva noticia encontrada',
#         mensaje,
#         'davidburneo@xinternet.co',
#         ['davidburneo@gmail.com'],
#         fail_silently=False,
#     )

#     # send_mail(
#     #     'Nueva noticia encontrada',
#     #     mensaje,
#     #     'cdelaossapabon@gmail.com',
#     #     ['cdelaossa@ideasinnovadoras.co'],
#     #     fail_silently=False,
#     # )

#     print(result)
#     #for n in result:
#         #print(n.title+": "+n.short_desc)
#     #return result
