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
from spotifywebapiwithfixesandimprovementsfromsonallux.models.me_albums_request import MeAlbumsRequest


class AlbumsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(AlbumsControllerTests, cls).setUpClass()
        cls.controller = cls.client.albums
        cls.response_catcher = cls.controller.http_call_back

    # Get Spotify catalog information for a single album.
    #
    def test_get_an_album(self):
        # Parameters for the API call
        id = '4aawyAB9vmqN3uQ7FjRGTy'
        market = 'ES'

        # Perform the API call through the SDK function
        result = self.controller.get_an_album(id, market)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get Spotify catalog information for multiple albums identified by their Spotify IDs.
    #
    def test_get_multiple_albums(self):
        # Parameters for the API call
        ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'
        market = 'ES'

        # Perform the API call through the SDK function
        result = self.controller.get_multiple_albums(ids, market)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get Spotify catalog information about an album’s tracks.
    #Optional parameters can be used to limit the number of tracks returned.
    #
    def test_get_an_albums_tracks(self):
        # Parameters for the API call
        id = '4aawyAB9vmqN3uQ7FjRGTy'
        market = 'ES'
        limit = 20
        offset = 0

        # Perform the API call through the SDK function
        result = self.controller.get_an_albums_tracks(id, market, limit, offset)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get a list of the albums saved in the current Spotify user's 'Your Music' library.
    #
    def test_get_users_saved_albums(self):
        # Parameters for the API call
        limit = 20
        offset = 0
        market = 'ES'

        # Perform the API call through the SDK function
        result = self.controller.get_users_saved_albums(limit, offset, market)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Save one or more albums to the current user's 'Your Music' library.
    #
    def test_save_albums_user(self):
        # Parameters for the API call
        ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'
        body = None

        # Perform the API call through the SDK function
        self.controller.save_albums_user(ids, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Remove one or more albums from the current user's 'Your Music' library.
    #
    def test_remove_albums_user(self):
        # Parameters for the API call
        ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'
        body = None

        # Perform the API call through the SDK function
        self.controller.remove_albums_user(ids, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.
    #
    def test_check_users_saved_albums(self):
        # Parameters for the API call
        ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'

        # Perform the API call through the SDK function
        result = self.controller.check_users_saved_albums(ids)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        assert '[\r\n  false,\r\n  true\r\n]' == self.response_catcher.response.text

    # Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).
    #
    def test_get_new_releases(self):
        # Parameters for the API call
        limit = 20
        offset = 0

        # Perform the API call through the SDK function
        result = self.controller.get_new_releases(limit, offset)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


