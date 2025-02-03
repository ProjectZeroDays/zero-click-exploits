import redis

cache = redis.Redis(host="localhost", port=6379, db=0)

def get_cached_response(key):
    cached_response = cache.get(key)
    return cached_response.decode("utf-8") if cached_response else None

def cache_response(key, response, ttl=300):
    cache.set(key, response, ex=ttl)

# Example usage
response = get_cached_response("ai_response_123")
if not response:
    response = "AI-generated response"
    cache_response("ai_response_123", response)
