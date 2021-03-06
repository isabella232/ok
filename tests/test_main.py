from tests import OkTestCase

class TestMain(OkTestCase):
    def test_home(self):
        """Tests that the home page loads."""
        response = self.client.get('/')
        self.assert_200(response)
        self.assert_template_used('index.html')

    def test_health_check(self):
        """Tests that the health check is successful."""
        response = self.client.get('/healthz')
        self.assert_200(response)
