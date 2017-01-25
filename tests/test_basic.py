class TestBasic:

    def test_root_page_opens(self, client):
        """
        A very basic unit test to check if the overall setup works
        """
        response = client.get('/')
        assert response.status_code
