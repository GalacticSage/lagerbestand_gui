from lagerbestand_core import lagerbestand_core as core
import json

class Util:

    def setLanguage(self, language_name):
        available_languages = core.read_json("locales/available_languages.json")
        selected_language_code = available_languages.get(language_name)

        if selected_language_code is not None:
            settings_data = core.read_json("settings.json")
            settings_data['Language'] = selected_language_code
            core.write_json(settings_data, "settings.json")
        else:
            print(f"The language '{language_name}' is not available.")

        
    
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
    
    def filter_values_under_five(self, input_dict):
        new_dict = {}

        for key, value in input_dict.items():
            try:
                value_as_int = int(value)
                if value_as_int < 5:
                    new_dict[key] = value_as_int
            except ValueError:
                pass

        return new_dict
