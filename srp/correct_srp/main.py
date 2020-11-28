from github.client import GithubClient
from repo.parser import Parser

if __name__ == '__main__':
    username = 'daciolima'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        Parser.parse(response['body'])
    else:
        print(response['body'])
