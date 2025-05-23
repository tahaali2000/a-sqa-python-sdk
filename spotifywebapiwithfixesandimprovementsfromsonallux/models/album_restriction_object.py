# -*- coding: utf-8 -*-

"""
spotifywebapiwithfixesandimprovementsfromsonallux

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapiwithfixesandimprovementsfromsonallux.api_helper import APIHelper


class AlbumRestrictionObject(object):

    """Implementation of the 'AlbumRestrictionObject' model.

    Attributes:
        reason (ReasonEnum): The reason for the restriction. Albums may be
            restricted if the content is not available in a given market, to
            the user's subscription type, or when the user's account is set to
            not play explicit content. Additional reasons may be added in the
            future.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason": 'reason'
    }

    _optionals = [
        'reason',
    ]

    def __init__(self,
                 reason=APIHelper.SKIP):
        """Constructor for the AlbumRestrictionObject class"""

        # Initialize members of the class
        if reason is not APIHelper.SKIP:
            self.reason = reason 

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
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(reason)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'reason={(self.reason if hasattr(self, "reason") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'reason={(self.reason if hasattr(self, "reason") else None)!s})')
