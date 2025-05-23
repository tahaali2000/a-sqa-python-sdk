# -*- coding: utf-8 -*-

"""
spotifywebapiwithfixesandimprovementsfromsonallux

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapiwithfixesandimprovementsfromsonallux.api_helper import APIHelper


class ImageObject(object):

    """Implementation of the 'ImageObject' model.

    Attributes:
        url (str): The source URL of the image.
        height (int): The image height in pixels.
        width (int): The image width in pixels.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url',
        "height": 'height',
        "width": 'width'
    }

    _nullables = [
        'height',
        'width',
    ]

    def __init__(self,
                 url=None,
                 height=None,
                 width=None):
        """Constructor for the ImageObject class"""

        # Initialize members of the class
        self.url = url 
        self.height = height 
        self.width = width 

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
        url = dictionary.get("url") if dictionary.get("url") else None
        height = dictionary.get("height") if dictionary.get("height") else None
        width = dictionary.get("width") if dictionary.get("width") else None
        # Return an object of this model
        return cls(url,
                   height,
                   width)

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
            return APIHelper.is_valid_type(value=dictionary.url,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.height,
                                            type_callable=lambda value: isinstance(value, int),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.width,
                                            type_callable=lambda value: isinstance(value, int),
                                            is_value_nullable=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('url'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('height'),
                                        type_callable=lambda value: isinstance(value, int),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('width'),
                                        type_callable=lambda value: isinstance(value, int),
                                        is_value_nullable=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'url={self.url!r}, '
                f'height={self.height!r}, '
                f'width={self.width!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'url={self.url!s}, '
                f'height={self.height!s}, '
                f'width={self.width!s})')
