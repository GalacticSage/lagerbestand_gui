from lagerbestand_core import lagerbestand_core as core
import json

class Util:
    def loadTranslations(language):
        try:
            with open(f'locales/{language}.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file doesn't exist

    def translate(translations, key):
        return translations.get(key, key)  # Return the key itself if translation not found

    def loadData(self, json_path):
        # Load data
        data = core.read_json(json_path)
        return data

    @staticmethod
    def loadDataAndOptions(self, json_path, loadKey):
        # Load data
        data = core.read_json(json_path)
        if loadKey:
            options = list(data.keys())
        else:
            options = list(data.values())
        return data, options