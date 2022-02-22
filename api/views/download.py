from sanic.response import json
from ..app import alidrive


async def get_download(requests):
    """
    获取下载链接

    :request param:
    file_id: [必选] 下载文件file_id
    """
    file_id = requests.args.get('file_id')
    if not file_id:
        return json({"error": "file_id"}, status=400)
    file = alidrive.get_file(file_id=file_id)
    return json({
        "download_url": file.download_url,
        "file_name": file.name,
        })
