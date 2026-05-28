import requests


class NewsAPIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url.rstrip('/')

        self.session = requests.Session()

        if token:
            self.session.headers.update({
                'Authorization': f'Token {token}'
            })

    def register(self, username, email, password):
        response = self.session.post(
            f"{self.base_url}/api/users/",
            json={
                'username': username,
                'email': email,
                'password': password
            }
        )

        return response.json()

    def get_news(self, news_id=None):
        if news_id:
            url = f"{self.base_url}/api/news/{news_id}/"
        else:
            url = f"{self.base_url}/api/news/"

        response = self.session.get(url)

        return response.json()

    def create_news(self, title, content, summary=""):
        response = self.session.post(
            f"{self.base_url}/api/news/",
            json={
                'title': title,
                'content': content,
                'summary': summary
            }
        )

        return response.json()

    def update_news(self, news_id, **kwargs):
        response = self.session.patch(
            f"{self.base_url}/api/news/{news_id}/",
            json=kwargs
        )

        return response.json()

    def delete_news(self, news_id):
        response = self.session.delete(
            f"{self.base_url}/api/news/{news_id}/"
        )

        return response.status_code