from sanic import Sanic
from aligo import Aligo
from sanic_cors import CORS


# 初始化服务
alidrive = Aligo()
app = Sanic("aliyundrive-webin-api")
app.static('/', './frontend/dist/index.html')
app.static('/', './frontend/dist')
CORS(app)
