from pymongo import MongoClient


def send_to_mongo(user_id, provider, uuid, extra_data, likes, photos, posts, gps_trace, friends,info, events, places,books,family,music,movies):

    user = {"id": user_id,
         "provider": provider,
         "uuid": uuid,
         "extra_data": extra_data,
         "access_token" : "access_token",
         "facebook_data": {
             "likes" : likes,
             "photos" : photos,
             "posts" : posts,
             "friends_info": friends,
             "user_info":info,
             "events": events,
             "tagged_places": places,
             "books": books,
             "family": family,
             "music": music,
             "movies": movies
          },
          "gps_traces" : [
               {
                  "trace_id" : 1,
                  "timestamp" : "01/12/12",
                  "trace" : gps_trace
               }
            ]
        }

    mongo_conn = MongoClient('mongodb://euprojects.net:3368')
    mongo_db = mongo_conn.Optimum
    cols = mongo_db.collection_names()
    print cols
    print user
    optimum_users = mongo_db["OptimumUsers"]

    result = optimum_users.update({"id": user_id},{"$set": user},True,True)
    '''for messages in optimum_users.find():
            print messages'''

def send_messages_to_mongo():
    mongo_conn = MongoClient('mongodb://euprojects.net:3368')
    mongo_db = mongo_conn.Optimum
    cols = mongo_db.collection_names()
    print cols
    optimum_messages = mongo_db["OptimumMessages"]
    message1 = {
                "id": 1,
                "message_text": "It's not too far. You get 30 points for walking.",
                "persuasive_strategy": "Reward",
                "context": "WalkingDistance",
                "number_of_times_sent": 0,
                "number_of_successes": 0,
            }
    message2 = {
                "id": 2,
                "message_text": "Great job! Your emissions are decreasing!",
                "persuasive_strategy": "Praise",
                "context": "emissionsIncreasing",
                "number_of_times_sent": 0,
                "number_of_successes": 0,
            }

    message3 = {
                "id": 3,
                "message_text": "Take public transport to reduce your emissions. Last week you caused 2000 kg of CO2 emissions.",
                "persuasive_strategy": "Self-monitoring",
                "context": "noContext",
                "number_of_times_sent": 0,
                "number_of_successes": 0,
            }
    #result = optimum_messages.insert_one(message3)
    for messages in optimum_messages.find():
            print messages