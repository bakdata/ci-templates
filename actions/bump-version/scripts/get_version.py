from configparser import ConfigParser


cfg = ConfigParser()
cfg.read('.bumpversion.cfg')
print(cfg['bumpversion']['current_version'])
