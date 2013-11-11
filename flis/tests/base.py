from django.db.models import Model
from django.core.urlresolvers import reverse
from django.template.base import TemplateDoesNotExist

from mock import Mock
from django_webtest import WebTest
from webtest.forms import Select, MultipleSelect
from webtest import AppError


USER_ADMIN_DATA = {'user_id': 'admin', 'user_roles': ['Administrator'],
                   'groups': []}
user_admin_mock = Mock(status_code=200, json=USER_ADMIN_DATA)


class BaseWebTest(WebTest):

    csrf_checks = False

    def __init__(self, *args, **kwargs):
        self.AppError = AppError
        super(BaseWebTest, self).__init__(*args, **kwargs)

    def populate_fields(self, form, data):
        for field_name, field in form.field_order:
            if field_name in data:
                value = data[field_name]
                if isinstance(value, Model):
                    value = value.pk
                if isinstance(field, MultipleSelect):
                    if not isinstance(value, list):
                        value = [value]
                if isinstance(field, (Select, MultipleSelect)):
                    field.force_value(value)
                else:
                    field.value = value
        return form

    def normalize_data(self, data):
        for k, v in data.items():
            if isinstance(v, Model):
                data[k] = v.pk
        return data

    def reverse(self, view_name, *args, **kwargs):
        return reverse(view_name, args=args, kwargs=kwargs)


