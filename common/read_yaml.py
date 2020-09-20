import yaml
import os

def read_yaml_data(yaml_path):
    '''读取yaml文件'''
    f = open(yaml_path, "r", encoding="utf-8")
    cfg = f.read()
    # print(cfg)
    #转python dict
    d = yaml.load(cfg)
    return d

if __name__ == '__main__':
    from setting import basepath
    import os
    yamlpath = os.path.join(basepath, "testdatas", "test_cases.yml")
    print(yamlpath)
    d = read_yaml_data(yamlpath)
    print(d)