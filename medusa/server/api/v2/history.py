# coding=utf-8
"""Request handler for history."""
import json

from .base import BaseRequestHandler


class HistoryHandler(BaseRequestHandler):
    """History request handler."""

    def get(self, query):
        """Query history.

        :param query:
        """
        self.api_finish(data={})
