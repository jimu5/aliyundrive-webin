from sanic import Sanic
from aligo import Aligo


# 初始化服务
app = Sanic("aliyundrive-webin-api")
alidrive = Aligo()
