# Next Steps

1. Connect `/analyze` to OpenRouter behind the existing response contract, with mock fallback for local/dev mode
2. Add CI/devcontainer bootstrap so `make smoke` works in fresh environments without manual apt setup (`python3-pip`, `python3.12-venv`)
3. Add route-level error mapping for OpenRouter failures (config/request/timeout/parse) so API responses stay explicit and debuggable
