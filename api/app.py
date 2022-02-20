from sanic import Sanic
from aligo import Aligo


# 初始化服务
alidrive = Aligo()
app = Sanic("aliyundrive-webin-api")
