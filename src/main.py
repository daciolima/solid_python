from src.github.client import GithubClient
from src.repo.parser import Parser
from src.repo.reports.html_generator import HtmlGenerator
from src.repo.reports.markdown_generator import MarkdownGenerator

from src.repo.reports_generator_com_ocp import ReportGenerator

if __name__ == '__main__':
    username = 'daciolima'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = Parser.parse(response['body'])
        markdown_report = ReportGenerator.build(MarkdownGenerator, repos)
        html_report = ReportGenerator.build(HtmlGenerator, repos)

        print(markdown_report)
        print(html_report)
    else:
        print(response['body'])
