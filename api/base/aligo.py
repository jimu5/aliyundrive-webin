from typing import Callable, Iterator, List

from aligo import Aligo
from aligo.core.Config import V2_FILE_SEARCH
from aligo.request import SearchFileRequest
from aligo.response import SearchFileResponse
from aligo.types import DataClass, Null, BaseFile
from aligo.types.Enum import SearchCategory
from aligo.types.DataClass import DataType


class BaseAligo(Aligo):
    def _list_file(self, PATH: str, body: DataClass, ResponseType: Callable, **kwargs) -> Iterator[DataType]:
        response = self._post(PATH, body=body)
        file_list = self._result(response, ResponseType)
        if isinstance(file_list, Null):
            yield file_list
            return
        for item in file_list.items:
            yield item
        if file_list.next_marker != '':
            body.marker = file_list.next_marker
            yield from self._list_file(PATH=PATH, body=body, ResponseType=ResponseType)

    def _list_file_by_pagination(self, PATH: str, body: DataClass, ResponseType: Callable, **kwargs) -> Iterator[DataType]:
        """如果有下一页的话，列表的最后一个是下一页的marker"""
        if kwargs.get('page_marker'):
            body.marker = kwargs.pop('page_marker')
        response = self._post(PATH, body=body)
        file_list = self._result(response, ResponseType)
        result = file_list.items
        if file_list.next_marker != '':
            result.append(file_list.next_marker)
        return result

    def _core_search_file(self, body: SearchFileRequest, **kwargs) -> Iterator[BaseFile]:
        if kwargs.get('pagination'):
            return self._list_file_by_pagination(V2_FILE_SEARCH, body, SearchFileResponse, **kwargs)
        else:
            return super()._core_search_file(body)

    def search_file(self, name: str = None, category: SearchCategory = None, drive_id: str = None,
                    body: SearchFileRequest = None, **kwargs) -> List[BaseFile]:
        """search_file"""
        pagination = kwargs.pop('pagination')
        page_marker = kwargs.pop('page_marker')
        if body is None:
            query = f'name match "{name}"'
            if category is not None:
                query += f' and category = "{category}"'
            body = SearchFileRequest(query=query, drive_id=drive_id, **kwargs)
        if pagination:
            return self._core_search_file(body, pagination=pagination, page_marker=page_marker)
        result = self._core_search_file(body)
        return [i for i in result]
