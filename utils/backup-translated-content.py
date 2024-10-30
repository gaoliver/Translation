import json
import os

def backup_translated_content():
    original_file_path = 'output/texts_list_copy.json'
    translated_file_path = 'output/translated-list.json'
    output_file_path = 'output/translated-draft_content.json'

    with open(translated_file_path, 'r') as f:
        translated_list = json.load(f)

    with open(original_file_path, 'r') as f:
        test_json = json.load(f)

    translated_data = []

    for translated_obj in translated_list:
        test_obj = next((obj for obj in test_json if obj['id'] == translated_obj['id']), None)
        if test_obj:
            test_obj['words']['text'] = translated_obj['words.text']
            test_obj['content'] = translated_obj['content']
            translated_data.append(test_obj)

    with open(output_file_path, 'w') as f:
        json.dump(translated_data, f, indent=4)

backup_translated_content()