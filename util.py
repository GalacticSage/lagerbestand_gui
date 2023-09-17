from lagerbestand_core import core

class Util:
    @staticmethod
    def loadDataAndOptions(self, json_path):
        # Load data
        data = core.read_json(json_path)
        options = list(data.keys())
        return data, options