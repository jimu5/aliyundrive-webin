from sanic import Sanic
from api.base import BaseAligo


# 初始化服务
alidrive = BaseAligo()
app = Sanic("aliyundrive-webin-api")
app.static('/', './frontend/dist/index.html')
app.static('/', './frontend/dist')
