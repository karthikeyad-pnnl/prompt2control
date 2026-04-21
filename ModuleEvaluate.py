import os
import json
import difflib
from typing import Dict, List

class ModelicaModuleComparator:
    def __init__(self, file1_path=None, file2_path=None):
        self.file1_path = file1_path
        self.file2_path = file2_path
    def load_file(self):
        self.code1 = self._load_file(self.file1_path)
        self.code2 = self._load_file(self.file2_path)
    def _load_file(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    def compare_code_similarity(self) -> float:
        """Return a ratio from 0.0 (no match) to 1.0 (identical)."""
        return difflib.SequenceMatcher(None, self.code1, self.code2).ratio()


    @staticmethod
    def load_json_metadata(json_path: str) -> List[Dict[str, str]]:
        """Load JSON and extract 'title', 'path', 'prompt' from top-level entries."""
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        results = []
        for key in data:
            entry = data[key]
            if all(k in entry for k in ("title", "path", "prompt")):
                results.append({
                    "id": key,
                    "title": entry["title"],
                    "path": entry["path"],
                    "prompt": entry["prompt"]
                })
        return results

    def github_url_to_local_path(self,github_url: str, local_base: str, prefix = "https://github.com/lbl-srg/modelica-buildings/raw/master/Buildings/") -> str:
        if not github_url.startswith(prefix):
            raise ValueError("URL does not match expected GitHub raw prefix.")
        relative_path = github_url[len(prefix):]  # Extract the relative model path
        local_path = os.path.join(local_base, relative_path)
        return os.path.normpath(local_path)
    
    def load_file_content(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

# Example usage:
# comp = ModelicaModuleComparator("model1.mo", "model2.mo")
# print("Code similarity:", comp.compare_code_similarity())
# print("Parameter comparison:", comp.compare_parameters())
# meta = ModelicaModuleComparator.load_json_metadata("modules.json")
# for item in meta:
#     print(item)
