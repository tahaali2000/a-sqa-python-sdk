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
from spotifywebapiwithfixesandimprovementsfromsonallux.models.playlists_followers_request import PlaylistsFollowersRequest
from spotifywebapiwithfixesandimprovementsfromsonallux.models.me_following_request import MeFollowingRequest
from spotifywebapiwithfixesandimprovementsfromsonallux.models.me_following_request_1 import MeFollowingRequest1


class UsersControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(UsersControllerTests, cls).setUpClass()
        cls.controller = cls.client.users
        cls.response_catcher = cls.controller.http_call_back

    # Get detailed profile information about the current user (including the
    #current user's username).
    #
    def test_get_current_users_profile(self):

        # Perform the API call through the SDK function
        result = self.controller.get_current_users_profile()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get public profile information about a Spotify user.
    #
    def test_get_users_profile(self):
        # Parameters for the API call
        user_id = 'smedjan'

        # Perform the API call through the SDK function
        result = self.controller.get_users_profile(user_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Add the current user as a follower of a playlist.
    #
    def test_follow_playlist(self):
        # Parameters for the API call
        playlist_id = '3cEYpjA9oz9GiPac4AsH4n'
        body = None

        # Perform the API call through the SDK function
        self.controller.follow_playlist(playlist_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Remove the current user as a follower of a playlist.
    #
    def test_unfollow_playlist(self):
        # Parameters for the API call
        playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

        # Perform the API call through the SDK function
        self.controller.unfollow_playlist(playlist_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Get the current user's followed artists.
    #
    def test_get_followed(self):
        # Parameters for the API call
        mtype = 'artist'
        after = '0I2XqVXqHScXjHhk6AYYRe'
        limit = 20

        # Perform the API call through the SDK function
        result = self.controller.get_followed(mtype, after, limit)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Add the current user as a follower of one or more artists or other Spotify users.
    #
    def test_follow_artists_users(self):
        # Parameters for the API call
        mtype = 'artist'
        ids = '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6'
        body = None

        # Perform the API call through the SDK function
        self.controller.follow_artists_users(mtype, ids, body)

        # Test response code
        assert self.response_catcher.response.status_code == 204

    # Remove the current user as a follower of one or more artists or other Spotify users.
    #
    def test_unfollow_artists_users(self):
        # Parameters for the API call
        mtype = 'artist'
        ids = '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6'
        body = None

        # Perform the API call through the SDK function
        self.controller.unfollow_artists_users(mtype, ids, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Check to see if the current user is following one or more artists or other Spotify users.
    #
    def test_check_current_user_follows(self):
        # Parameters for the API call
        mtype = 'artist'
        ids = '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6'

        # Perform the API call through the SDK function
        result = self.controller.check_current_user_follows(mtype, ids)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        assert '[\r\n  false,\r\n  true\r\n]' == self.response_catcher.response.text

    # Check to see if one or more Spotify users are following a specified playlist.
    #
    def test_check_if_user_follows_playlist(self):
        # Parameters for the API call
        playlist_id = '3cEYpjA9oz9GiPac4AsH4n'
        ids = 'jmperezperez,thelinmichael,wizzler'

        # Perform the API call through the SDK function
        result = self.controller.check_if_user_follows_playlist(playlist_id, ids)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        assert '[\r\n  false,\r\n  true\r\n]' == self.response_catcher.response.text

    # Get the current user's top artists based on calculated affinity.
    #
    def test_get_users_top_artists(self):
        # Parameters for the API call
        time_range = 'medium_term'
        limit = 20
        offset = 0

        # Perform the API call through the SDK function
        result = self.controller.get_users_top_artists(time_range, limit, offset)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get the current user's top tracks based on calculated affinity.
    #
    def test_get_users_top_tracks(self):
        # Parameters for the API call
        time_range = 'medium_term'
        limit = 20
        offset = 0

        # Perform the API call through the SDK function
        result = self.controller.get_users_top_tracks(time_range, limit, offset)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


