import yaml

def dictionary_print(m_dict):
    print(yaml.dump(m_dict, default_flow_style=False))