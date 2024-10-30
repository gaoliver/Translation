import json
from googletrans import Translator

LANG_CODES = ['pt', 'en', 'es', 'fr', 'it', 'de', 'ru', 'ja', 'zh-CN', 'nl']

def extract_data():
    print('(1) Portuguese, (2) English, (3) Spanish, (4) French, (5) Italian, (6) German, (7) Russian, (8) Japanese, (9) Chinese, (10) Dutch\n\n')

    src_lang = LANG_CODES[int(input('Enter the original language: ')) - 1]
    dest_lang = LANG_CODES[int(input('Enter the destination language: ')) - 1]

    print('\n\n')

    original_file_path = 'draft_content.json'
    file_path = 'output/texts_list_copy.json'
    output_file = 'output/translated-list.json'

    def copy_texts():
        with open(original_file_path, 'r') as f:              
            data = json.load(f)

        with open(file_path, 'w') as file:
            json.dump(data['materials']['texts'], file, indent=4)

    def translate_text(text):
        translator = Translator()
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text

    def translate_content(json_string):
        try:
            data = json.loads(json_string)
            if 'text' in data:
                data['text'] = translate_text(data['text'])
                # Print the translated text
                print(data['text'])
                return json.dumps(data, separators=(',', ':'), ensure_ascii=True)
            else:
                return None
        except json.JSONDecodeError:
            return None
        
    copy_texts()

    with open(file_path, 'r') as file:
        data = json.load(file)

    new_list = []
    for obj in data:
        text = ' '.join(obj['words']['text'])

        try:
            new_text_list = translate_text(text).replace(' ', '/ /').split('/')
            new_content_text = translate_content(obj['content'])

            new_obj = {
                'id': obj['id'],
                'words.text': new_text_list,
                'content': new_content_text
            }
            new_list.append(new_obj)
        except:
            continue

    with open(output_file, 'w') as file:
        json.dump(new_list, file, indent=4)

extract_data()