from typing import Tuple
from pathlib import Path
from importlib.resources import files
import virtue
import softworks


@virtue.hookimpl
def virtue_python_package_name() -> str:
    return "softworks"

@virtue.hookimpl
def virtue_skill_package_name() -> str:
    return "Softworks"

@virtue.hookimpl
def virtue_skill_initialization_paths() -> Tuple[Path]:
    return (files(softworks) / "softworks.cdsinit.ils"),

@virtue.hookimpl
def virtue_cdslibmgr_paths() -> Tuple[Path]:
    return (files(softworks) / "softworks.cdsLibMgr.il"),

@virtue.hookimpl
def virtue_data_reg_paths() -> Tuple[Path]:
    return (
        files(softworks) / "python" / "SdmPy.data.reg",
        files(softworks) / "skill" / "SdmSkill.data.reg",
        files(softworks) / "pptx" / "SdmPptx.data.reg",
        files(softworks) / "xlsx" / "SdmXlsx.data.reg",
        files(softworks) / "pdf" / "SdmPdf.data.reg",
        files(softworks) / "html" / "SdmHtml.data.reg",
        )