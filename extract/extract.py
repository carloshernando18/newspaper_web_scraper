import argparse
import yaml

__config = None

def config():
    global __config
    if not __config:
        with open('../config.yml', mode='r') as config_file:
            __config = yaml.load(config_file, Loader=yaml.FullLoader)
    return __config

def main():
    parser = argparse.ArgumentParser()
    news_sites = list(config()['news_sites'].keys())
    print(news_sites)


main()
