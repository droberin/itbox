#import requests
import logging
from configobj import ConfigObj
from os.path import isfile


def list_nodes(from_file='/var/lib/nova/itbox-nodes.ini'):
    try:
        with open(from_file, 'rb') as node_list_fp:
            pass
    except PermissionError or FileNotFoundError:
        pass
    finally:
        node_list_fp.close()


class ITBox:
    """"
    ITBox class will create a whole new Cloud for you
    """
    cloud_initiated = False
    provisioning_server = 'https://itbox.gradiant.org'

    def __init__(self, *args, **kwargs):
        """
        Initialiser
        :param args:
        :param kwargs:
        """
        super(ITBox, self).__init__(*args, **kwargs)

    def provision_server(self, url=None):
        if not url:
            logging.info("No URL requested. Using default provisioning server: " + self.provisioning_server)
        else:
            self.provisioning_server = url
