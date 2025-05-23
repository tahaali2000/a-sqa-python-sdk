# -*- coding: utf-8 -*-

"""
spotifywebapiwithfixesandimprovementsfromsonallux

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapiwithfixesandimprovementsfromsonallux.models.cursor_paging_simplified_artist_object import CursorPagingSimplifiedArtistObject


class CursorPagedArtists(object):

    """Implementation of the 'CursorPagedArtists' model.

    Attributes:
        artists (CursorPagingSimplifiedArtistObject): The model property of
            type CursorPagingSimplifiedArtistObject.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "artists": 'artists'
    }

    def __init__(self,
                 artists=None):
        """Constructor for the CursorPagedArtists class"""

        # Initialize members of the class
        self.artists = artists 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        artists = CursorPagingSimplifiedArtistObject.from_dictionary(dictionary.get('artists')) if dictionary.get('artists') else None
        # Return an object of this model
        return cls(artists)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'artists={self.artists!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'artists={self.artists!s})')
