from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Configuration using Flask's built-in config system
app.config['REDIS_HOST'] = os.getenv("REDIS_HOST", "localhost")
app.config['REDIS_PORT'] = int(os.getenv("REDIS_PORT", 6379))

def get_redis_client():
    try:
        redis_client = redis.StrictRedis(
            host=app.config['REDIS_HOST'], 
            port=app.config['REDIS_PORT'], 
            decode_responses=True
        )
        # Test Redis connection
        redis_client.ping()
        return redis_client
    except redis.ConnectionError as e:
        # Log or handle error here
        raise RuntimeError(f"Failed to connect to Redis: {e}")

# Instantiate Redis client
redis_client = get_redis_client()

@app.route('/')
def welcome():
    return "Welcome to Mo's CoderCo Containers Challenge using Flask and Redis!"

@app.route('/count')
def count():
    try:
        redis_client.incr('visit_count')
        count = redis_client.get('visit_count')
        return jsonify(visit_count=count)
    except redis.RedisError as e:
        return jsonify(error=f"Redis error: {e}"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
