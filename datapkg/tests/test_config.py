import datapkg
import datapkg.config

class TestConfig:
    def test_make_default_config(self):
        cfg = datapkg.config.make_default_config()
        assert cfg.get('DEFAULT', 'version') == datapkg.__version__
        assert cfg.get('DEFAULT', 'ckan.url') == 'http://ckan.net/api/'

    def test_dictget(self):
        cfg = datapkg.config.Config()
        default = 'ZZZZZZ'
        out = cfg.dictget('DEFAULT', 'xyz', default)
        assert out == default
