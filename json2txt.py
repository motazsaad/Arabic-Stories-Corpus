import os
import json
import glob

directory = 'qisasse.com/json/'
out_dir = 'qisasse.com/text/'
json_files = glob.glob(directory + '*.json')
for json_file in json_files:
    doc = json.loads(open(json_file, encoding='utf-8').read())
    outfile_name = json_file.split('/')[-1].replace('.html.json', '.txt')
    outfile_name = os.path.join(out_dir + outfile_name)
    title = doc.get('title')
    text = doc.get('text')
    if title and text:
        with open(outfile_name, encoding='utf-8', mode='w') as writer:
            writer.write(title + '\n')
            writer.write(text)
    else:
        print('error in', json_file)
