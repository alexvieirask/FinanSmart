from System.Config import *

class SKCache:
    def get_user_cache(useremail):
        if useremail in user_caches:
            return user_caches[useremail]
        
        user_cache = Cache(app)
        user_caches[useremail] = user_cache
        return user_cache