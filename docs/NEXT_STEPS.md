# Next Steps

1. Add a tiny curl-based API usage section (health + analyze examples) to README so first-time users can manually verify outputs quickly
2. Add example error payloads for `/analyze` in README (500/502/504) so client-side retry and UX flows can be implemented confidently
3. Add parser-level tests for malformed top-level OpenRouter envelopes (`choices` missing/wrong type) to complement route-level drift tests
