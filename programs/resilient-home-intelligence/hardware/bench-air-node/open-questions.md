# Open Questions

- Should the MVP publish over serial only, or require Wi-Fi delivery to the ingest service before the subsystem counts as complete?
- What enclosure standard should be used for sheltered deployments so airflow remains useful without inviting dust or splashes?
- Should the node compute any local anomaly hints, or stay strictly evidence-only and leave all interpretation to downstream services?
- Which sensor should be canonical for temperature and humidity when SHT45 and BME680 disagree?
- Do we want a persistent local ring buffer for offline periods in the first hardware iteration, or is continuous power plus upstream ingest enough?
- What node identity scheme should be used before any secure provisioning workflow exists?
