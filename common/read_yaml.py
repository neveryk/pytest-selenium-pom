import yaml


class ReadYaml():
    def load_yaml(self,file_path):
        with open(file_path,encoding = 'utf-8')as f:
            data=yaml.safe_load(f)
            return data

yaml_data=ReadYaml()