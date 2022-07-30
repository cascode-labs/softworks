"""
Updates or create's the specified user's project code workspace

The workspace is located at:
   /prj/${PROJ_ID}/work_libs/${USER}/${PROJ_ID}_code

Example using it as a script:
   python3 code_workspace.py ${PROJ_ID} ${USER}

"""
from importlib.resources import path
from shutil import copyfile
import sys
from pathlib import Path

import workspace_files.dotvscode


class CodeWorkspace:
    def __init__(self, prj_id, user) -> None:
        self.prj_id = prj_id
        self.user = user
        self.user_worklib = f"/prj/{self.prj_id}/work_libs/{self.user}"
        self.user_code_workspace = f"{self.user_worklib}/{self.prj_id}_code"

    def update(self):
        self._create_workspace()
        self._update_library_links()
        self._create_dotvscode_dir()
        self._create_readme()

    def _create_workspace(self):
        user_worklib_path = Path(self.user_worklib)
        if user_worklib_path.is_dir():
            user_code_workspace_path = Path(self.user_code_workspace)
            user_code_workspace_path.mkdir(exist_ok=True)
            print(f"creating user code workspace at: '{self.user_code_workspace}'")
        else:
            print(f"user work library not found: '{self.user_worklib}'")
            exit(1)

    def _update_library_links(self):
        """Updates or creates the project's library symbolic links"""
        cds_root = f"/prj/{self.prj_id}/work_libs/{self.user}/cds"
        sym_links = {
            f"{self.prj_id}_work": Path(f"{cds_root}/design_controlled/{self.prj_id}_work"),
            f"{self.prj_id}_sim": Path(f"{cds_root}/design_controlled/{self.prj_id}_sim"),
            f"{self.prj_id}_{self.user}": Path(f"{cds_root}/design")
        }

        for name, path in sym_links.items():
            link_path = Path(f"{self.user_code_workspace}/{name}")
            if not link_path.is_symlink() and not link_path.exists() and path.is_dir():
                link_path.symlink_to(path, target_is_directory=True)            

    def _create_dotvscode_dir(self):
        dotvscode = f"{self.user_code_workspace}/.vscode"
        dotvscode_path = Path(dotvscode)
        if dotvscode_path.is_dir():
            print(f"\tdirectory already exists at: {dotvscode}")
            return
        dotvscode_path.mkdir()
        print(f"\tcreated {dotvscode}")
        with path(workspace_files.dotvscode, "extensions.json") as extensions_json_path: 
            dst = f"{dotvscode}/extensions.json"
            if not Path(dst).exists():
                copyfile(src=extensions_json_path, dst=dst)
                print(f"\t\tcreated {dst}")
            else:
                print(f"\t\tfile already exists at: {dst}")

        with path(workspace_files.dotvscode, "settings.json") as settings_json_path: 
            dst = f"{dotvscode}/settings.json"
            if not Path(dst).exists():
                copyfile(src=settings_json_path, dst=dst)
                print(f"\tcreated {dst}")
            else:
                print(f"file already exists at: {dst}")


    def _create_readme(self):
        with path(workspace_files, "README.md") as readme_path: 
            dst = f"{self.user_code_workspace}/README.md"
            if not Path(dst).exists():
                copyfile(src=readme_path, dst=dst)
                print(f"\tcreated {dst}")
            else:
                print(f"\tfile already exists at: {dst}")

if __name__ == "__main__":
    code_work_space = CodeWorkspace(prj_id=sys.argv[1], user=sys.argv[2])
    code_work_space.update()
