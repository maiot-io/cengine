# coding: utf-8

"""
    maiot Core Engine API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PipelineCreate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'pipeline_config': 'object',
        'workspace_id': 'str',
        'pipeline_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'pipeline_config': 'pipeline_config',
        'workspace_id': 'workspace_id',
        'pipeline_type': 'pipeline_type'
    }

    def __init__(self, name=None, pipeline_config=None, workspace_id=None, pipeline_type='normal'):  # noqa: E501
        """PipelineCreate - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._pipeline_config = None
        self._workspace_id = None
        self._pipeline_type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if pipeline_config is not None:
            self.pipeline_config = pipeline_config
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if pipeline_type is not None:
            self.pipeline_type = pipeline_type

    @property
    def name(self):
        """Gets the name of this PipelineCreate.  # noqa: E501


        :return: The name of this PipelineCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineCreate.


        :param name: The name of this PipelineCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pipeline_config(self):
        """Gets the pipeline_config of this PipelineCreate.  # noqa: E501


        :return: The pipeline_config of this PipelineCreate.  # noqa: E501
        :rtype: object
        """
        return self._pipeline_config

    @pipeline_config.setter
    def pipeline_config(self, pipeline_config):
        """Sets the pipeline_config of this PipelineCreate.


        :param pipeline_config: The pipeline_config of this PipelineCreate.  # noqa: E501
        :type: object
        """

        self._pipeline_config = pipeline_config

    @property
    def workspace_id(self):
        """Gets the workspace_id of this PipelineCreate.  # noqa: E501


        :return: The workspace_id of this PipelineCreate.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this PipelineCreate.


        :param workspace_id: The workspace_id of this PipelineCreate.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def pipeline_type(self):
        """Gets the pipeline_type of this PipelineCreate.  # noqa: E501


        :return: The pipeline_type of this PipelineCreate.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_type

    @pipeline_type.setter
    def pipeline_type(self, pipeline_type):
        """Sets the pipeline_type of this PipelineCreate.


        :param pipeline_type: The pipeline_type of this PipelineCreate.  # noqa: E501
        :type: str
        """

        self._pipeline_type = pipeline_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PipelineCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PipelineCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
