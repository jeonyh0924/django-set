# utils/auto_schema.py

from drf_spectacular.openapi import AutoSchema


class HiddenSchema(AutoSchema):
    def get_operation(self, *args, **kwargs):
        return None
