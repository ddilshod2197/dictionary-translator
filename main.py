class Lugat:
    def __init__(self):
        self.lugat = {}

    def qo'sh(self, so'z, tarjima):
        self.lugat[so'z] = tarjima

    def o'chir(self, so'z):
        if so'z in self.lugat:
            del self.lugat[so'z]
        else:
            print("So'z lug'atda mavjud emas.")

    def tarjima(self, so'z):
        return self.lugat.get(so'z, "So'z lug'atda mavjud emas.")

class Translator:
    def __init__(self):
        self.lugat = Lugat()

    def qo'sh(self, so'z, tarjima):
        self.lugat.qo'sh(so'z, tarjima)

    def o'chir(self, so'z):
        self.lugat.o'chir(so'z)

    def tarjima(self, so'z):
        return self.lugat.tarjima(so'z)

    def yangi_lugat(self, lugat):
        self.lugat.lugat.update(lugat)

    def lugatni_yuklash(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    so'z, tarjima = line.strip().split(',')
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_json(self, file_name):
        import json
        try:
            with open(file_name, 'r') as file:
                lugat = json.load(file)
                for so'z, tarjima in lugat.items():
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_csv(self, file_name):
        try:
            import csv
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        self.qo'sh(row[0], row[1])
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_txt(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    so'z, tarjima = line.strip().split(',')
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_xml(self, file_name):
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(file_name)
            root = tree.getroot()
            for element in root:
                so'z = element.find('soz').text
                tarjima = element.find('tarjima').text
                self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_yaml(self, file_name):
        try:
            import yaml
            with open(file_name, 'r') as file:
                lugat = yaml.safe_load(file)
                for so'z, tarjima in lugat.items():
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_jsonl(self, file_name):
        try:
            import json
            with open(file_name, 'r') as file:
                for line in file:
                    lugat = json.loads(line)
                    self.qo'sh(lugat['soz'], lugat['tarjima'])
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_csvl(self, file_name):
        try:
            import csv
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        self.qo'sh(row[0], row[1])
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_txtl(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    so'z, tarjima = line.strip().split(',')
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_xml(self, file_name):
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(file_name)
            root = tree.getroot()
            for element in root:
                so'z = element.find('soz').text
                tarjima = element.find('tarjima').text
                self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_yaml(self, file_name):
        try:
            import yaml
            with open(file_name, 'r') as file:
                lugat = yaml.safe_load(file)
                for so'z, tarjima in lugat.items():
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_jsonl(self, file_name):
        try:
            import json
            with open(file_name, 'r') as file:
                for line in file:
                    lugat = json.loads(line)
                    self.qo'sh(lugat['soz'], lugat['tarjima'])
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_csvl(self, file_name):
        try:
            import csv
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        self.qo'sh(row[0], row[1])
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_txtl(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    so'z, tarjima = line.strip().split(',')
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_xml(self, file_name):
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(file_name)
            root = tree.getroot()
            for element in root:
                so'z = element.find('soz').text
                tarjima = element.find('tarjima').text
                self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_yaml(self, file_name):
        try:
            import yaml
            with open(file_name, 'r') as file:
                lugat = yaml.safe_load(file)
                for so'z, tarjima in lugat.items():
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_jsonl(self, file_name):
        try:
            import json
            with open(file_name, 'r') as file:
                for line in file:
                    lugat = json.loads(line)
                    self.qo'sh(lugat['soz'], lugat['tarjima'])
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_csvl(self, file_name):
        try:
            import csv
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        self.qo'sh(row[0], row[1])
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_txtl(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    so'z, tarjima = line.strip().split(',')
                    self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_xml(self, file_name):
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(file_name)
            root = tree.getroot()
            for element in root:
                so'z = element.find('soz').text
                tarjima = element.find('tarjima').text
                self.qo'sh(so'z, tarjima)
        except FileNotFoundError:
            print("Fayl mavjud emas.")

    def lugatni_yuklash_yaml(self, file_name):
        try:
            import yaml
            with open(file_name, 'r') as file:
                lugat = yaml.safe_load(file)
                for so'z,
