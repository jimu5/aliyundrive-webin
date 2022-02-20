from sanic.response import json
from typing import List
from aligo.types import BaseFile

from ..app import alidrive


async def search_file(request):
    """
    搜索文件

    :request param:
    file_name: [必选] 搜索的文件名
    file_category:[可选] 搜索的文件类型
    """
    file_name = request.args.get("file_name")
    file_category = request.args.get("file_category")
    result = alidrive.search_file(name=file_name, category=file_category)
    # 处理搜索结果
    result = handle_search_result(result)
    return json(body=result)


def handle_search_result(result: List[BaseFile]) -> list:
    handle_list = []
    for file in result:
        file_info = {
            'name': file.name,
            'file_id': file.file_id,
            'type': file.type
        }
        handle_list.append(file_info)
    return handle_list