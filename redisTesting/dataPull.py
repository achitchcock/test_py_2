import redis

r = redis.Redis()

while True:
    try:
        msg = r.lpop("msg_q")
    except Exception as e:
        print e
    if msg:
        print(msg)
