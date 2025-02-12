import urllib.request
from urllib.parse import urlparse
from django.conf import settings
from git import Repo
import tempfile, re, os, requests
from CodeAnalizer.classes.abstract import Abstract
from CodeAnalizer.classes.sast import SAST

class Repository(Abstract):

    def __init__(self, request):
        raw_url = self.post_param(request, "repo")

        self.url = self.clean_url(raw_url)
        self.branch = self.extract_branch(raw_url)

    def get_repo_name(url):
        if url:
            return url.split('/')[-1].replace('.git', '') 
        
    def clone_repository(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            if self.branch:
                repo = Repo.clone_from(self.url, tmpdir, branch=f'{self.branch}')
            else:
                repo = Repo.clone_from(self.url, tmpdir)
            branch_name = repo.active_branch.name
            result = SAST.analyze(self, branch_name, tmpdir)
            return result
        
    def extract_branch(self, url):
        match = re.search(r"/tree/([^/]+)", url)
        return match.group(1).split('?')[0] if match else None

    def clean_url(self, url):
        base_url = url.split('?')[0]

        base_url = base_url.replace("/-/", "/")
        base_url = base_url.split('/tree/')[0]
        base_url = base_url.rstrip('/')

        if not base_url.endswith('.git'):
            base_url += '.git'

        return base_url
    
    def get_line_code(self, raw_url, line_number):
        line_number = int(line_number)
        # Parse the URL to get the domain and path
        parsed_url = urlparse(raw_url)
        
        # Check if the URL is for GitHub or GitLab
        if "github.com" in parsed_url.netloc:
            # GitHub: Convert to raw URL
            url = raw_url.replace("github.com", "raw.githubusercontent.com").replace("/blob", "")
        elif "gitlab.com" in parsed_url.netloc:
            # GitLab: Convert to raw URL
            url = raw_url.replace("gitlab.com", "gitlab.com").replace("/blob", "/raw")
        else:
            return None

        # Fetch the raw content of the file
        response = requests.get(url)
        
        if response.status_code == 200:
            # Split the content into lines
            lines = response.text.splitlines()
            
            # Check if the line number is valid
            if 0 < line_number <= len(lines):
                return lines[line_number - 1]
        else:
            return None