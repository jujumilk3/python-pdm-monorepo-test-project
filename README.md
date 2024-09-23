# python-pdm-monorepo-test-project

## commands

```bash
# at ./common
pdm init
pdm add requests

# at ./projects/test_backend
pdm init
pdm add ../../common  # then "common @ file:///${PROJECT_ROOT}/../../common" line created in pyproject.toml
pdm install
```
