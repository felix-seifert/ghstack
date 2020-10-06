#!/usr/bin/env python3

import re
from typing import Dict, Any
try:
    from mypy_extensions import TypedDict
except ImportError:
    # Avoid the dependency on the mypy_extensions package.
    # It is required, however, for type checking.
    def TypedDict(name, attrs, total=True):  # type: ignore
        return Dict[Any, Any]


RE_PR_URL = re.compile(
    r'^https://(?P<github_url>[^/]+)/(?P<owner>[^/]+)/(?P<name>[^/]+)/pull/(?P<number>[0-9]+)/?$')

GitHubPullRequestParams = TypedDict('GitHubPullRequestParams', {
    'github_url': str
    'owner': str,
    'name': str,
    'number': int,
})


def parse_pull_request(pull_request: str) -> GitHubPullRequestParams:
    m = RE_PR_URL.match(pull_request)
    if not m:
        raise RuntimeError("Did not understand PR argument.  PR must be URL")

    github_url = m.group("github_url")
    owner = m.group("owner")
    name = m.group("name")
    number = int(m.group("number"))
    return {'github_url': github_url, 'owner': owner, 'name': name, 'number': number}
