#
# Copyright 2018 Eduardo A. Paris Penas <edward2a@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import argparse
import logging
import os
import yaml

default_config = os.path.dirname(os.path.abspath(__file__)) + '/../../config/config.yml'
logger = logging.getLogger(__name__)

def load_args():
    """Parse command line arguments and return namespace object."""
    p = argparse.ArgumentParser()
    p.add_argument('-c', '--config', default=default_config, required=False)
    return p.parse_args()


def load_config(cfg_file):
    """Load configuration from file in YAML format and return dict."""
    with open(cfg_file) as f:
        return yaml.load(f)

def load_env(cfg_obj):
    """Parse cfg_obj for env: strings and load them from process env."""
    for key, value in cfg_obj.items():

        if isinstance(value, dict):
            load_env(value)

        elif isinstance(value, str) and value.startswith('env:'):

            try:
                # String handler
                if value.startswith('env:str:'):
                    cfg_obj[key] = os.environ[value.lstrip('env:str:')]

                # List (array) handler
                elif value.startswith('env:list:'):
                    cfg_obj[key] = os.environ[value.lstrip('env:list:')].split(',')

                # Bool handler
                elif value.startswith('env:bool:'):
                    cfg_obj[key] = bool(os.environ[value.lstrip('env:bool:')])


            except KeyError:
                logger.error('Configuration missing in process environment: ' + value)

