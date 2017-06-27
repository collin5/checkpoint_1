# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 27.06.2017
# Last Modified: 27.06.2017

import json
import os


class FileIO(object):

    def __init__(self):
        super(FileIO, self).__init__()

    @staticmethod
    def generate_pk_with_file(func):
        def wrap(*args, **kwargs):
            # Get PK from config file, create one if not exists
            config_file = None
            CONFIG, kwargs['ID'] = {}, 0

            try:
                if not os.path.exists('config.json'):
                    with open('config.json', 'w'):
                        pass
                config_file = open('config.json', 'r')
            except Exception as ex:
                raise

            fstring = config_file.read()
            config_file.close()

            if len(fstring.strip()) > 0:
                CONFIG = json.loads(fstring)
                if 'people_pk' in CONFIG:
                    kwargs['ID'] = CONFIG['people_pk'] + 1

                else:
                    CONFIG['people_pk'] = 0

            CONFIG['people_pk'] = kwargs['ID']
            config_file = open('config.json', 'w')

            config_file.write(json.dumps(CONFIG))
            config_file.close()

            return func(*args, {'PK': CONFIG['people_pk']})

        return wrap
