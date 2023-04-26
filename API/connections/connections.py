import redis

# create connection to redis
redis = redis.Redis(host='localhost', port=6379,db=0)
# create connection to postgres