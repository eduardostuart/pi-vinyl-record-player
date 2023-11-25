import os
import toml

class Config:

    def __init__(self, config_filename: str):
        self.config_path = os.path.join(os.getcwd(), config_filename);
        self._data = {}
        self.read_config()

    @property
    def cast(self):
        return self._data.get('cast', {})

    @property
    def albums(self):
        return self._data.get('albums', {})

    def read_config(self):
        try:
          with open(self.config_path, 'r') as file:
              self._data = toml.load(file)
        except FileNotFoundError:
          raise ValueError(f"Could not find config file: {self.config_path}")
        except toml.TomlDecodeError as e:
          raise ValueError(f"Could not parse config file: {e}")
        except Exception as e:
          raise ValueError(f"Could not read config file: {e} at {self.config_path}")
