import os, re


def get_text(file_path: str):
    txtFileObj = open(file_path, 'r')
    data = txtFileObj.read().replace('\n', '')
    return data


def filter_first_paragraph(content: str):
    return content.split('comparece')[-1].split('expone')[0]


base = 'sociedades-texto'
files = os.listdir('./%s' % base)

for file in files:
    print('-- %s --' % file)
    file_path = './%s/%s' % (base, file)

    # Se lee el archivo y se limita al primer parrafo con los que comparecen
    # para ahorrar memoria
    text = filter_first_paragraph(get_text(file_path))

    # Buscar con regex...
    # ref https://embed.ihateregex.io/make/JTVCJTVFJTQwJTIwJTVDJTVDdCU1QyU1Q3IlNUMlNUNuJTVEJTJCJTVDJTVDcyU1QiU1RSU0MCUyMCU1QyU1Q3QlNUMlNUNyJTVDJTVDbiU1RCUyQiU1QyU1Q3MlNUIlNUUlNDAlMjAlNUMlNUN0JTVDJTVDciU1QyU1Q24lNUQlMkIlMkMlMjBSdXQlNUMlNUNzJTJCJTVDJTVDZCU3QjElMkMyJTdEJTVDJTVDLiU1QyU1Q2QlN0IzJTdEJTVDJTVDLiU1QyU1Q2QlN0IzJTdEJTVCLSU1RCU1QjAtOWtLJTVEJTVDJTVDbg
    personas = re.findall('[^@ \t\r\n]+\s[^@ \t\r\n]+\s[^@ \t\r\n]+, Rut\s+\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]', text)

    for p in personas:
        print(p.replace(' Rut', ''))
