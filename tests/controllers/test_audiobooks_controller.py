# -*- coding: utf-8 -*-

"""
spotifywebapiwithfixesandimprovementsfromsonallux

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from spotifywebapiwithfixesandimprovementsfromsonallux.api_helper import APIHelper


class AudiobooksControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(AudiobooksControllerTests, cls).setUpClass()
        cls.controller = cls.client.audiobooks
        cls.response_catcher = cls.controller.http_call_back

    # Get Spotify catalog information for a single audiobook. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.
    #
    def test_get_an_audiobook(self):
        # Parameters for the API call
        id = '7iHfbu1YPACw6oZPAFJtqe'
        market = 'ES'

        # Perform the API call through the SDK function
        result = self.controller.get_an_audiobook(id, market)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get Spotify catalog information for several audiobooks identified by their Spotify IDs. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.
    #
    def test_get_multiple_audiobooks(self):
        # Parameters for the API call
        ids = '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe'
        market = 'ES'

        # Perform the API call through the SDK function
        result = self.controller.get_multiple_audiobooks(ids, market)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.
    #
    def test_get_audiobook_chapters(self):
        # Parameters for the API call
        id = '7iHfbu1YPACw6oZPAFJtqe'
        market = 'ES'
        limit = 20
        offset = 0

        # Perform the API call through the SDK function
        result = self.controller.get_audiobook_chapters(id, market, limit, offset)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.
    #
    def test_get_users_saved_audiobooks(self):
        # Parameters for the API call
        limit = 20
        offset = 0

        # Perform the API call through the SDK function
        result = self.controller.get_users_saved_audiobooks(limit, offset)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Save one or more audiobooks to the current Spotify user's library.
    #
    def test_save_audiobooks_user(self):
        # Parameters for the API call
        ids = '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe'

        # Perform the API call through the SDK function
        self.controller.save_audiobooks_user(ids)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Remove one or more audiobooks from the Spotify user's library.
    #
    def test_remove_audiobooks_user(self):
        # Parameters for the API call
        ids = '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe'

        # Perform the API call through the SDK function
        self.controller.remove_audiobooks_user(ids)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Check if one or more audiobooks are already saved in the current Spotify user's library.
    #
    def test_check_users_saved_audiobooks(self):
        # Parameters for the API call
        ids = '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe'

        # Perform the API call through the SDK function
        result = self.controller.check_users_saved_audiobooks(ids)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        assert '[\r\n  false,\r\n  true\r\n]' == self.response_catcher.response.text

