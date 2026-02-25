# Next Steps

1. Add a lightweight prompt/response contract test for OpenRouter mode to detect schema drift early (missing keys, empty arrays, non-JSON output)
2. Add a tiny curl-based API usage section (health + analyze examples) to README so first-time users can manually verify outputs quickly
3. Add example error payloads for `/analyze` in README (500/502/504) so client-side retry and UX flows can be implemented confidently
