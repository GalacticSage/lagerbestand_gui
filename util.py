from lagerbestand_core import core
import json

class Util:
    def load_translations(language):
        try:
            with open(f'locales/{language}.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file doesn't exist

    def translate(translations, key):
        return translations.get(key, key)  # Return the key itself if translation not found

    @staticmethod
    def loadDataAndOptions(self, json_path):
        # Load data
        data = core.read_json(json_path)
        options = list(data.keys())
        return data, options