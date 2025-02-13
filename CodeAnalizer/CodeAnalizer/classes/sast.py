import subprocess, json, os, sys
from django.conf import settings
from CodeAnalizer.classes.DTO import DTO

class SAST:

    @staticmethod
    def analyze(repository, branch_name, repo_path):

        url = repository.url.rstrip(".git")

        try:
            semgrep = SAST.run_semgrep(repo_path)
            horusec = SAST.run_horusec(repo_path)
            
            return DTO.extract_sast_response(url, branch_name, repo_path, horusec, semgrep, repository)

        except subprocess.CalledProcessError as e:
            error_message = f"Error running Horusec:\n{e.stderr}"
            print(error_message)  # Log the error details
            raise Exception(error_message) from e
        
        finally:
            if f"{repo_path}.json":
                os.remove(f"{repo_path}.json")
    
    @staticmethod
    def run_semgrep(repo_path):
        semgrep = subprocess.run(
            ["semgrep", "--config=auto", repo_path, "--json"],
            capture_output=True,
            text=True,
            check=True  # Automatically raises CalledProcessError on non-zero return code
        )
        return json.loads(semgrep.stdout)
    
    @staticmethod
    def run_horusec(repo_path):
        horusec = subprocess.run(
            [
                "horusec","start",
                "-p",repo_path,
                "-o=json",f"-O={repo_path}.json",
                "-D"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        with open(f"{repo_path}.json", "r") as json_file:
                return json.load(json_file)
