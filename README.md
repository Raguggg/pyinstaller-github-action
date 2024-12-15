# Generate EXE with GitHub Actions and PyInstaller

This repository contains a GitHub Actions workflow to package a Python application into a Windows executable (`.exe`) using [PyInstaller](https://pyinstaller.org/).

## Blog
[https://ragug.medium.com/ci-cd-pipeline-for-pyinstaller-on-github-actions-for-windows-7f8274349278](https://ragug.medium.com/ci-cd-pipeline-for-pyinstaller-on-github-actions-for-windows-7f8274349278)

## Workflow Overview

The GitHub Actions workflow:
1. **Checks out** the repository.
2. **Sets up** Python 3.10.
3. **Installs dependencies** for the Python project.
4. **Packages the application** using PyInstaller.
5. **Uploads the executable** as an artifact for download.

## Setup Instructions

### Prerequisites

Before running the workflow:
1. Ensure you have a `pyinstaller.spec` file in your repository. This file defines how PyInstaller packages your application.
2. If you're using a `requirements.txt`, make sure it's included in your repository.

### Folder Structure Example

```plaintext
pyinstaller-github-action/
├── assets
│   ├── c1.png
│   ├── c2.png
│   └── icon.ico
├── main.py
├── pyinstaller.spec
├── pyproject.toml # PyInstaller configuration
├── README.md
├── src
│   ├── first_screen.py
│   ├── __init__.py
│   ├── loading.py
│   └── utils.py
├── uv.lock
└── .github/
    └── workflows/
        └── get_windows_exe.yml  # GitHub Actions workflow
```

### Workflow Configuration

The workflow file (`package.yml`) is located in `.github/workflows/` and is triggered on every push to the `main` branch. Modify the branch name as needed.

### Key Sections of the Workflow

1. **Set Up Python:**
   The workflow sets up Python 3.10. Update the `python-version` field to your desired Python version.

2. **Install Dependencies:**
   Adjust the command to install your dependencies:
   - If using `setup.py`: `pip install .`
   - If using `requirements.txt`: `pip install -r requirements.txt`

3. **Package Application:**
   The workflow uses `pyinstaller.spec` to create the `.exe`. Ensure the `pyinstaller.spec` file correctly references your Python project.

4. **Upload Artifact:**
   The final `.exe` is uploaded as an artifact named `Windows-exe` for download.

## How to Run the Workflow

1. Push your code to the `main` branch (or the branch configured in the workflow).
2. Navigate to the **Actions** tab in your GitHub repository.
3. Select the **Package Application with PyInstaller** workflow.
4. Monitor the workflow execution. Upon completion, the `.exe` will be available for download as an artifact.

## Downloading the Executable

1. After the workflow completes, navigate to the **Actions** tab.
2. Select the workflow run and scroll down to the **Artifacts** section.
3. Download the `Windows-exe.zip` file.

## Notes

- Test the generated `.exe` thoroughly to ensure it works as expected.
- If you encounter issues with packaging, review your `pyinstaller.spec` file and ensure all dependencies are installed correctly.

## References

- [PyInstaller Documentation](https://pyinstaller.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
```

This `README.md` explains the workflow process, its setup, and how to use it to package a Python application into an executable. You can modify the instructions as per your specific requirements or use cases.