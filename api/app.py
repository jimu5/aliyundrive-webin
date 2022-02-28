from sanic import Sanic
from aligo import Aligo
from sanic_cors import CORS


# 初始化服务
alidrive = Aligo()
app = Sanic("aliyundrive-webin-api")
CORS(app)
