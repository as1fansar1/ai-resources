# Next Steps

1. Add OpenAPI error response docs for `/analyze` (codes + error payload schema) so client handling is contract-driven
2. Add a lightweight prompt/response contract test for OpenRouter mode to detect schema drift early (missing keys, empty arrays, non-JSON output)
3. Add a tiny curl-based API usage section (health + analyze examples) to README so first-time users can manually verify outputs quickly
