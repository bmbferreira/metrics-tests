# -*- coding: utf-8 -*-
########################### Copyrights and license ############################
# ##############################################################################

import github.GithubObject

import github.Commit


class Branch(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Branchs. The reference can be found here http://developer.github.com/v3/repos/#list-branches
    """

    @property
    def commit(self):
        """
        :type: :class:`github.Commit.Commit`
        """
        return self._commit.value

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    @property
    def protected(self):
        """
        :type: bool
        """
        return self._protected.value

    @property
    def enforcement_level(self):
        """
        :type: string
        """
        return self._enforcement_level.value

    @property
    def contexts(self):
        """
        :type: list of strings
        """
        return self._contexts.value

    def _initAttributes(self):
	self._commit = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "commit" in attributes:  # pragma no branch
            self._commit = self._makeClassAttribute(github.Commit.Commit, attributes["commit"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "protection" in attributes:
            self._protected = self._makeBoolAttribute(attributes["protection"]["enabled"])
            self._enforcement_level = self._makeStringAttribute(attributes["protection"]["required_status_checks"]["enforcement_level"])
            self._contexts = self._makeListOfStringsAttribute(attributes["protection"]["required_status_checks"]["contexts"])
