# -*- coding: utf-8 -*-

"""
spotifywebapiwithfixesandimprovementsfromsonallux

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapiwithfixesandimprovementsfromsonallux.api_helper import APIHelper


class TimeIntervalObject(object):

    """Implementation of the 'TimeIntervalObject' model.

    Attributes:
        start (float): The starting point (in seconds) of the time interval.
        duration (float): The duration (in seconds) of the time interval.
        confidence (float): The confidence, from 0.0 to 1.0, of the
            reliability of the interval.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start": 'start',
        "duration": 'duration',
        "confidence": 'confidence'
    }

    _optionals = [
        'start',
        'duration',
        'confidence',
    ]

    def __init__(self,
                 start=APIHelper.SKIP,
                 duration=APIHelper.SKIP,
                 confidence=APIHelper.SKIP):
        """Constructor for the TimeIntervalObject class"""

        # Initialize members of the class
        if start is not APIHelper.SKIP:
            self.start = start 
        if duration is not APIHelper.SKIP:
            self.duration = duration 
        if confidence is not APIHelper.SKIP:
            self.confidence = confidence 

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
        start = dictionary.get("start") if dictionary.get("start") else APIHelper.SKIP
        duration = dictionary.get("duration") if dictionary.get("duration") else APIHelper.SKIP
        confidence = dictionary.get("confidence") if dictionary.get("confidence") else APIHelper.SKIP
        # Return an object of this model
        return cls(start,
                   duration,
                   confidence)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'start={(self.start if hasattr(self, "start") else None)!r}, '
                f'duration={(self.duration if hasattr(self, "duration") else None)!r}, '
                f'confidence={(self.confidence if hasattr(self, "confidence") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'start={(self.start if hasattr(self, "start") else None)!s}, '
                f'duration={(self.duration if hasattr(self, "duration") else None)!s}, '
                f'confidence={(self.confidence if hasattr(self, "confidence") else None)!s})')
