# 如果Http请求失败，实现"重试"功能
import requests


def retry(attempt):
    """使用装饰器实现重试"""
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            att = 0
            while att < attempt:
                print(att)
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    att += 1
        
        return wrapper
    
    return decorator


@retry(attempt=3)
def get_response(url):
    r = requests.get(url)
    return r


URL = 'http://www.1631212.com'
r = get_response(URL)
print(r)
# 将内容转成GBK
# print(r.content.decode('gbk'))
