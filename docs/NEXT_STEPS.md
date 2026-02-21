# Next Steps

1. Add CI/devcontainer bootstrap so `make smoke` works in fresh environments without manual apt setup (`python3-pip`, `python3.12-venv`)
2. Add route-level error mapping for OpenRouter failures (config/request/timeout/parse) so API responses stay explicit and debuggable
3. Parse structured OpenRouter output (themes/opportunities/experiments) into first-class response fields instead of mock-derived placeholders
