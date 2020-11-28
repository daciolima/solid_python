from models.repo import Repo


class Parser:

    @classmethod
    def parse(cls, reponse):
        for i in range(len(reponse)):
            repo = reponse[i]
            repo = Repo(repo["id"], repo["name"], repo["stargazers_count"])
            print(repo)

