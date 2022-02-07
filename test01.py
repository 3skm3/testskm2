import requests
from 接口自动化.public.common import *

url_toutiao = 'https://www.toutiao.com/article/v2/tab_comments/?aid=24&app_name=toutiao_web&offset=0&count=20&group_id=7019248919704076832&item_id=7019248919704076832&_signature=_02B4Z6wo00f015Ty0AwAAIDDFPAqTsU11g-U1tSAAIRdZiUExMCqpSEmavuC-MLDoBuSEX4qV9NAxCVlflF5GHMVFktvTmsG2qIVSpwQuMoHsMFE.FBZa.VrNQ0ZfJB7PDVJiiWF2yWDiN1l05'
result = requests.get(url_toutiao)

print(result.json()['data'][0]['comment']['text']) #字典或列表