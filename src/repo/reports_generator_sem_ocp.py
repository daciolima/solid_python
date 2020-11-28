from .reports.html_generator import HtmlGenerator
from .reports.markdown_generator import MarkdownGenerator


class ReportGenerator:

    @classmethod
    def build(cls, type, repos):
        if type == 'HTML':
            return HtmlGenerator.build(repos)
        elif type == 'MARKDOWN':
            return MarkdownGenerator.build(repos)
        else:
            return "Tipo de report inválido"
