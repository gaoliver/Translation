import json

def replace_original():
    draft_content_path = 'draft_content.json'
    translated_file_path = 'output/translated-draft_content.json'

    with open(draft_content_path, 'r') as f:
        draft_content = json.load(f)

    with open(translated_file_path, 'r') as f:
        translated_test = json.load(f)

    draft_content['materials']['texts'] = []

    with open(draft_content_path, 'w') as f:
        json.dump(draft_content, f, indent=4)

    draft_content['materials']['texts'] = translated_test

    with open(draft_content_path, 'w') as f:
        json.dump(draft_content, f, indent=4)

replace_original()