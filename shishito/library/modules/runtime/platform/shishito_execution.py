# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
@summary: Selenium Webdriver Python test runner
"""

import os
import ConfigParser


class ShishitoExecution(object):
    """ """

    def __init__(self, shishito_support, test_timestamp):
        self.current_folder = os.path.dirname(os.path.abspath(__file__))

        self.shishito_support = shishito_support
        self.platform_name = self.shishito_support.gid('test_platform')
        self.environment_name = self.shishito_support.gid('test_environment')

        environment_class = self.shishito_support.get_modules(module='test_environment')
        self.environment = environment_class(shishito_support)

        # TODO: this may not work well if runner is not used
        self.project_root = os.getcwd()

        self.result_folder = os.path.join(self.project_root, 'results', test_timestamp)
        self.config_file = os.path.join(
            self.project_root, 'config', self.platform_name,
            '%s.properties' % self.environment_name
        )

        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.config_file)

    def run_tests(self):
        """ Triggers PyTest runner locally or on BrowserStack.
        It runs PyTest for each BS combination, taken from either versioned .properties file or environment variable """
        pass

    def trigger_pytest(self, config_section):
        """ Runs PyTest runner on specific configuration """
        pass
