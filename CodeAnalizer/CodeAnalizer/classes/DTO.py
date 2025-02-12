class DTO:

    @staticmethod
    def extract_sast_response(url, branch_name, tmp_repo, horusec_analysis, semgrep_analysis, repository):
        merged_results = []

        DTO.extract_horusec_analysis(url, branch_name, horusec_analysis, merged_results, repository)
        DTO.extract_semgrep_analysis(url, branch_name, semgrep_analysis, tmp_repo, merged_results, repository)

        sorted_results = sorted(merged_results, key=DTO.severity_impact_order, reverse=True)

        return sorted_results
    
    @staticmethod
    def extract_horusec_analysis(url, branch_name, horusec_analysis, merged_results, repository):
        if "analysisVulnerabilities" in horusec_analysis and horusec_analysis["analysisVulnerabilities"]:
            for result in horusec_analysis["analysisVulnerabilities"]:
                merged_results.append({
                    "file": result["vulnerabilities"]["file"],
                    "url": f"{url}/blob/{branch_name}/{result["vulnerabilities"]["file"]}#L{result["vulnerabilities"]["line"]}",
                    "line": result["vulnerabilities"]["line"],
                    "code": repository.get_line_code(f"{url}/blob/{branch_name}/{result["vulnerabilities"]["file"]}",
                                                    result["vulnerabilities"]["line"]),
                    "message": result["vulnerabilities"]["details"],
                    "severity": result["vulnerabilities"]["severity"],
                    "impact": None,  # Horusec doesn't use "impact"
                })

    @staticmethod
    def extract_semgrep_analysis(url, branch_name, semgrep_analysis, tmp_repo, merged_results, repository):
        if "results" in semgrep_analysis and semgrep_analysis["results"]:
            for result in semgrep_analysis["results"]:
                merged_results.append({
                    "file": result["path"].replace(f"{tmp_repo}/", ''),
                    "url": f"{url}/blob/{branch_name}/{result["path"].replace(f"{tmp_repo}/", '')}#L{result["start"]["line"]}",
                    "line": result["start"]["line"],
                    "code": repository.get_line_code(f"{url}/blob/{branch_name}/{result["path"].replace(f"{tmp_repo}/", '')}",
                                                    result["start"]["line"]),
                    "message": result["extra"]["message"],
                    "severity": None,  # Semgrep doesn't use "severity"
                    "impact": result["extra"]["metadata"]["impact"],
                })

    @staticmethod
    def severity_impact_order(result):
        severity_impact_map = {
            "CRITICAL": 4,
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1,
            None: 0
        }
        return max(severity_impact_map.get(result["severity"], 0), severity_impact_map.get(result["impact"], 0))
