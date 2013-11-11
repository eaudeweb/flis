from mock import patch
from .base import BaseWebTest
from .base import user_admin_mock
from .factories import CountryFactory


__all__ = ('InterlinksPermTests', )


class InterlinksPermTests(BaseWebTest):

    def setUp(self):
        CountryFactory()
        super(InterlinksPermTests, self).setUp()

    @patch('flis.frame.requests')
    def test_interlinks_edit_perm(self, mock_requests):
        mock_requests.get.return_value = user_admin_mock
        url = self.reverse('interlink_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
