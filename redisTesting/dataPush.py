import redis

r = redis.Redis()

while True:
    msg = raw_input("Enter message: ")
    r.lpush("msg_q", msg)
