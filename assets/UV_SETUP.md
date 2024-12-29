# Instruction to setup `uv`

#### Install uv [uv](https://github.com/astral-sh/uv)

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, from [PyPI](https://pypi.org/project/uv/):

```bash
# With pip.
pip install uv
```

```bash
# Or pipx.
pipx install uv
```

If installed via the standalone installer, uv can update itself to the latest version:

```bash
uv self update
```

#### Install packages

```bash
uv sync
```

#### Activate the virtual environment

```bash
source .venv/bin/activate
```

### Run server

```bash
fastapi dev app/main.py --port 8001 --host 0.0.0.0
```

## Modify

### Version management

Current version is in file `version.txt`
Increment version

```bash
./version_increment.sh
```

This will also create a new git tag and push to remote to trigger the CI/CD pipeline build new image and deploy to staging server.
