from send_to_mongo import send_to_mongo, update

__author__ = 'evangelie'
import requests
import json
from django.shortcuts import render, redirect, render_to_response
from social_auth.db.django_models import UserSocialAuth
from pymongo import MongoClient


# Home page
def index(request):
    if request.method == 'GET':
        if not request.user:
            return redirect('/accounts/login')
        #social_user = request.user.social_auth.filter(provider='facebook',).first()
        try:
            social_user = request.user.social_auth.filter(provider='facebook',).first()
             #Get user likes
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
            #Get user photos
            url2= u'https://graph.facebook.com/{0}/' \
                  u'photos?fields=source&limit=1000&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url2
            res2 = requests.get(url2)
            print json.loads(res2.text)
            photos = json.loads(res2.text)
            #Get user posts
            url3= u'https://graph.facebook.com/{0}/' \
                  u'feed?limit=10000&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url3
            res3 = requests.get(url3)
            print json.loads(res3.text)
            posts = json.loads(res3.text)
            #Get friends
            url4 = u'https://graph.facebook.com/{0}/' \
                  u'friends?fields=id,name,location,picture' \
                  u'&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url4
            res4 = requests.get(url4)
            print json.loads(res4.text)
            friends_info = json.loads(res4.text)
            #Ger user_info
            url5 = u'https://graph.facebook.com/me?fields=name,email,about,gender,age_range,birthday,education,favorite_athletes,' \
                  u'favorite_teams,hometown,location,interested_in,relationship_status&access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url5
            res5 = requests.get(url5)
            print json.loads(res5.text)
            user_info = json.loads(res5.text)
            #Ger user_events
            url6 = u'https://graph.facebook.com/{0}/events?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url6
            res6 = requests.get(url6)
            print json.loads(res6.text)
            events = json.loads(res6.text)
            #Ger user_tagged_places
            url7 = u'https://graph.facebook.com/{0}?' \
                   u'tagged_places?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url7
            res7 = requests.get(url7)
            print json.loads(res7.text)
            tagged_places = json.loads(res7.text)
            #Ger user_books
            url8 = u'https://graph.facebook.com/{0}/' \
                   u'books?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url8
            res8 = requests.get(url8)
            print json.loads(res8.text)
            books = json.loads(res8.text)
            #Ger user_family
            url9 = u'https://graph.facebook.com/{0}/family?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url9
            res9 = requests.get(url9)
            print json.loads(res9.text)
            family = json.loads(res9.text)
             #Ger music
            url10 = u'https://graph.facebook.com/{0}/music?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )
            print url10
            res10 = requests.get(url10)
            print json.loads(res10.text)
            music = json.loads(res10.text)
             #Ger movies
            url11 = u'https://graph.facebook.com/{0}/movies?access_token={1}'.format(
                      social_user.uid,
                      social_user.extra_data['access_token'],
                  )

            res11 = requests.get(url11)
            movies = json.loads(res11.text)
            mongo_conn = MongoClient('mongodb://euprojects.net:3368')
            mongo_db = mongo_conn.Optimum
            cols = mongo_db.collection_names()
            optimum_users = mongo_db["OptimumUsers"]
            user_facebook = optimum_users.find({"uuid": social_user.uid})
            #user_facebook = UserFacebookData.objects.filter(user=social_user)
            print user_facebook
            #send_messages_to_mongo()
            if not user_facebook:
                send_to_mongo(social_user.id, social_user.provider, social_user.uid, social_user.extra_data['access_token'], likes, photos, {},posts,friends_info,user_info, events, tagged_places,books,family,music,movies)
            else:
                field = {"facebook_data": {"likes" : likes, "photos" : photos,"posts" : posts, "friends_info": friends_info,
                                            "user_info":user_info, "events": events, "tagged_places": tagged_places,
                                            "books": books, "family": family, "music": music, "movies": movies}}
                update(social_user.id, field)

        except:
            print('not auth')
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
