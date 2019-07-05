class Storage:
    """Класс для хранения метрик в памяти процесса"""

    def __init__(self):
        # используем словарь для хранения метрик
        self._data = {}

    def put(self, key, value, timestamp):
        if key not in self._data:
            self._data[key] = {}

        self._data[key][timestamp] = value

    def get(self, key):
        data = self._data

        # вовзращаем нужную метрику если это не *
        if key != "*":
            data = {
                key: data.get(key, {})
            }

        # для простоты мы храним метрики в обычном словаре и сортируем значения
        # при каждом запросе, в реальном приложении следует выбрать другую
        # структуру данных
        result = {}
        for key, timestamp_data in data.items():
            result[key] = sorted(timestamp_data.items())

        return result


class Loader:
    """"""
    def __init__(self):
        pass