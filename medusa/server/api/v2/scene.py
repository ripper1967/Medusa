# coding=utf-8
"""Request handler for scene exceptions."""
from .base import BaseRequestHandler


class SceneHandler(BaseRequestHandler):
    """Scene exception request handler."""

    def get(self, query):
        """Query scene exceptions.

        :param query:
        """
        self.api_finish(data={})
