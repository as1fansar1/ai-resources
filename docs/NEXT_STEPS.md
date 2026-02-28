# Next Steps

1. Add parser-level tests for malformed top-level OpenRouter envelopes (`choices` missing/wrong type) to complement route-level drift tests
2. Add a tiny `scripts/smoke_api.sh` wrapper that runs health + analyze curl checks for users without `jq`
3. Add a short client-handling note in README mapping `/analyze` error codes to retry behavior (retry `openrouter_timeout`/`openrouter_request_error`, fail-fast on config/parse)
