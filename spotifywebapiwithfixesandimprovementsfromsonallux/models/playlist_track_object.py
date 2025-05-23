# -*- coding: utf-8 -*-

"""
spotifywebapiwithfixesandimprovementsfromsonallux

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapiwithfixesandimprovementsfromsonallux.api_helper import APIHelper
from spotifywebapiwithfixesandimprovementsfromsonallux.models.playlist_user_object import PlaylistUserObject


class PlaylistTrackObject(object):

    """Implementation of the 'PlaylistTrackObject' model.

    Attributes:
        added_at (datetime): The date and time the track or episode was added.
            _**Note**: some very old playlists may return `null` in this
            field._
        added_by (PlaylistUserObject): The Spotify user who added the track or
            episode. _**Note**: some very old playlists may return `null` in
            this field._
        is_local (bool): Whether this track or episode is a [local
            file](/documentation/web-api/concepts/playlists/#local-files) or
            not.
        track (TrackObject | EpisodeObject | None): Information about the
            track or episode.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "added_at": 'added_at',
        "added_by": 'added_by',
        "is_local": 'is_local',
        "track": 'track'
    }

    _optionals = [
        'added_at',
        'added_by',
        'is_local',
        'track',
    ]

    def __init__(self,
                 added_at=APIHelper.SKIP,
                 added_by=APIHelper.SKIP,
                 is_local=APIHelper.SKIP,
                 track=APIHelper.SKIP):
        """Constructor for the PlaylistTrackObject class"""

        # Initialize members of the class
        if added_at is not APIHelper.SKIP:
            self.added_at = APIHelper.apply_datetime_converter(added_at, APIHelper.RFC3339DateTime) if added_at else None 
        if added_by is not APIHelper.SKIP:
            self.added_by = added_by 
        if is_local is not APIHelper.SKIP:
            self.is_local = is_local 
        if track is not APIHelper.SKIP:
            self.track = track 

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
        from spotifywebapiwithfixesandimprovementsfromsonallux.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        added_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("added_at")).datetime if dictionary.get("added_at") else APIHelper.SKIP
        added_by = PlaylistUserObject.from_dictionary(dictionary.get('added_by')) if 'added_by' in dictionary.keys() else APIHelper.SKIP
        is_local = dictionary.get("is_local") if "is_local" in dictionary.keys() else APIHelper.SKIP
        track = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PlaylistTrackObjectTrack'), dictionary.get('track'), False) if dictionary.get('track') is not None else APIHelper.SKIP
        # Return an object of this model
        return cls(added_at,
                   added_by,
                   is_local,
                   track)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'added_at={(self.added_at if hasattr(self, "added_at") else None)!r}, '
                f'added_by={(self.added_by if hasattr(self, "added_by") else None)!r}, '
                f'is_local={(self.is_local if hasattr(self, "is_local") else None)!r}, '
                f'track={(self.track if hasattr(self, "track") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'added_at={(self.added_at if hasattr(self, "added_at") else None)!s}, '
                f'added_by={(self.added_by if hasattr(self, "added_by") else None)!s}, '
                f'is_local={(self.is_local if hasattr(self, "is_local") else None)!s}, '
                f'track={(self.track if hasattr(self, "track") else None)!s})')
