import requests


class GithubClient:

    API_BASE_URL = "https://api.github.com"

    @classmethod
    def get_repos_by_user(cls, user):
        response = requests.get(f'{cls.API_BASE_URL}/users/{user}/repos')
        print(response.json())
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "erro ao tentar localizar os repositórios"}
