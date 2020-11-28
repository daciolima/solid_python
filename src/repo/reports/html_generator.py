

class HtmlGenerator:

    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'<strong>ID: </strong>{repo.id} <strong>Name: </strong>{repo.name}  <strong>Stars: </strong>{repo.stars}\n'
            for repo in repos)
        return f'<p>{items}</p>'
