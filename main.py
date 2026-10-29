from pathlib import Path
import runpy


PROJECT_ROOT = Path(__file__).parent


def run_project(path: Path) -> None:
    runpy.run_path(str(path), run_name="__main__")


if __name__ == "__main__":
    # run_project(PROJECT_ROOT / "1" / "stars.py")
    run_project(PROJECT_ROOT / "1" / "trajectory.py")
