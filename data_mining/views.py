from send_to_mongo import send_to_mongo
__author__ = 'evangelie'
import requests
import json
from django.shortcuts import render, redirect, render_to_response
from social_auth.db.django_models import UserSocialAuth


# Home page
def index(request):
    if request.method == 'GET':
        return render(request, "mainPage.html",)

def get_facebook_data(request):
    social_user = request.user.social_auth.filter(provider='facebook',).first()
    if social_user:

        url = u'https://graph.facebook.com/{0}/' \
              u'likes?access_token={1}&limit=1000'.format(
                  social_user.uid,
                  social_user.extra_data['access_token'],
              )
        #url = 'https://graph.facebook.com/v2.5/me/friends?access_token='+social_user.extra_data['access_token']
        print url
        res = requests.get(url)
        print res.text
        likes=json.loads(res.text)

    return render(request, "data.html", {'result': json.loads(res.text)})


def thanks(request):
     if request.method == 'GET':

        social_user = request.user.social_auth.filter(provider='facebook',).first()
        #Get user likes
        url = u'https://graph.facebook.com/{0}/' \
                  u'likes?access_token={1}&limit=1000'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        #url = 'https://graph.facebook.com/v2.5/me/friends?access_token='+social_user.extra_data['access_token']
        print url
        try:
            res = requests.get(url)
            print res.text
            like=json.loads(res.text)
        except:
            like={}
        try:
            likes = [like]
            while like['paging']['next'] == True:
                url = u'https://graph.facebook.com/{0}/' \
                  u'likes?access_token={1}&limit=100&after={2}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                      like['paging']['cursor']['after']
                  )
                response = requests.get(url)
                like=json.loads(response.text)
                likes.append(like)
        except:
            likes=like

        #Get user photos
        url2= u'https://graph.facebook.com/{0}/' \
                  u'photos?fields=source&limit=1000&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url2
        try:
            res2 = requests.get(url2)
            print json.loads(res2.text)
            photo = json.loads(res2.text)
        except:
            photo = {}
        try:

            next_page = photo['paging']['next']
            photos = [photo]
            while next_page == True:
                url = u'https://graph.facebook.com/{0}/' \
                      u'photos?access_token={1}&limit=100&after={2}'.format(
                          social_user.uid,
                          social_user.extra_data['access_token'],
                          photo['paging']['cursor']['after']
                      )
                response = requests.get(url)
                photo=json.loads(response.text)
                photos.append(photo)
        except:
                photos= photo
        #Get user posts
        url3= u'https://graph.facebook.com/{0}/' \
                  u'feed?limit=10000&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url3
        try:
            res3 = requests.get(url3)
            print json.loads(res3.text)
            post = json.loads(res3.text)
        except:
            post={}

        try:

            posts = [post]
            while post['paging']['next'] == True:
                url = u'https://graph.facebook.com/{0}/' \
                      u'feed?access_token={1}&limit=100&after={2}'.format(
                          social_user.uid,
                          social_user.extra_data['access_token'],
                          post['paging']['cursor']['after']
                      )
                response = requests.get(url)
                post=json.loads(response.text)
                posts.append(post)
        except:
                posts=post
        #Get friends
        url4 = u'https://graph.facebook.com/{0}/' \
                  u'friends?fields=id,name,location,picture' \
                  u'&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url4
        try:
            res4 = requests.get(url4)
            print json.loads(res4.text)
            friends = json.loads(res4.text)
        except:
            friends={}
        try:

            friends_info = [friends]
            while friends['paging']['next'] == True:
                url = u'https://graph.facebook.com/{0}/' \
                      u'friends?access_token={1}&limit=100&after={2}'.format(
                          social_user.uid,
                          social_user.extra_data['access_token'],
                          friends['paging']['cursor']['after']
                      )
                response = requests.get(url)
                friends=json.loads(response.text)
                friends_info.append(friends)
        except:
            friends_info = friends
        #Ger user_info
        url5 = u'https://graph.facebook.com/me?fields=name,email,about,gender,age_range,birthday,education,favorite_athletes,' \
                  u'favorite_teams,hometown,location,interested_in,relationship_status&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url5
        try:
            res5 = requests.get(url5)
            print json.loads(res5.text)
            user_info = json.loads(res5.text)
        except:
            user_info={}
        #Ger user_events
        url6 = u'https://graph.facebook.com/{0}/events?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url6
        try:
            res6 = requests.get(url6)
            print json.loads(res6.text)
            events = json.loads(res6.text)
        except:
            events={}
        #Ger user_tagged_places
        url7 = u'https://graph.facebook.com/{0}?' \
                   u'tagged_places?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url7
        try:
            res7 = requests.get(url7)
            print json.loads(res7.text)
            tagged_places = json.loads(res7.text)
        except:
            tagged_places={}
        #Ger user_books
        url8 = u'https://graph.facebook.com/{0}/' \
                   u'books?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url8
        try:
            res8 = requests.get(url8)
            print json.loads(res8.text)
            book = json.loads(res8.text)
        except:
            book={}

        try:
            book = json.loads(res8.text)
            books = [book]
            while book['paging']['next'] == True:
                url = u'https://graph.facebook.com/{0}/' \
                      u'books?access_token={1}&limit=100&after={2}'.format(
                          social_user.uid,
                          social_user.extra_data['access_token'],
                          book['paging']['cursor']['after']
                      )
                response = requests.get(url)
                book=json.loads(response.text)
                books.append(book)
        except:
                books=book
        #Ger user_family
        url9 = u'https://graph.facebook.com/{0}/family?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url9
        try:
            res9 = requests.get(url9)
            print json.loads(res9.text)
            family = json.loads(res9.text)
        except:
            family={}
        #Ger music
        url10 = u'https://graph.facebook.com/{0}/music?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        print url10
        try:
            res10 = requests.get(url10)
            print json.loads(res10.text)
            music_page = json.loads(res10.text)
        except:
            music_page={}
        try:

            music = [music_page]
            while music_page['paging']['next'] == True:
                url = u'https://graph.facebook.com/{0}/' \
                      u'music?access_token={1}&limit=100&after={2}'.format(
                          social_user.uid,
                          social_user.extra_data['access_token'],
                          music_page['paging']['cursor']['after']
                      )
                response = requests.get(url)
                music_page=json.loads(response.text)
                music.append(music_page)
        except:
            music= music_page
        #Ger movies
        url11 = u'https://graph.facebook.com/{0}/movies?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
        try:
            res11 = requests.get(url11)
            movie = json.loads(res11.text)
        except:
            movie={}
        try:
            movies = [movie]
            while movie['paging']['next'] == True:
                url = u'https://graph.facebook.com/{0}/' \
                      u'movies?access_token={1}&limit=100&after={2}'.format(
                          social_user.uid,
                          social_user.extra_data['access_token'],
                          movie['paging']['cursor']['after']
                      )
                response = requests.get(url)
                movie=json.loads(response.text)
                movies.append(movie)
        except:
                movies=movie
        send_to_mongo(social_user.id, social_user.provider, social_user.uid, social_user.extra_data['access_token'], likes, photos, {},posts,friends_info,user_info, events, tagged_places,books,family,music,movies)

     return render(request, "thanks.html")

