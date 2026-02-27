# Next Steps

1. Add example error payloads for `/analyze` in README (500/502/504) so client-side retry and UX flows can be implemented confidently
2. Add parser-level tests for malformed top-level OpenRouter envelopes (`choices` missing/wrong type) to complement route-level drift tests
3. Add a tiny `scripts/smoke_api.sh` wrapper that runs health + analyze curl checks for users without `jq`
