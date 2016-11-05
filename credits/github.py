from github import Github
from django.conf import settings
import requests

BASE_URL = 'https://api.github.com'

gh = Github(settings.GITHUB_USERNAME, settings.GITHUB_PASSWORD)


def get_json_response_or_none(path):
    url = '{base_url}{path}'.format(base_url=BASE_URL, path=path)
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None


def get_contributors(repo='tutorial', owner='djangogirls'):
    return gh.get_repo('{owner}/{repo}'.format(owner=owner, repo=repo)).get_contributors()
