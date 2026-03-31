// Minimal first-build bench air node packet emitter for ESP32-S3.
// This sketch intentionally avoids external sensor libraries so the
// serial JSON contract can be exercised before full sensor integration.

static const char* kSchemaVersion = "rhi.bench-air.v1";
static const char* kNodeId = "bench-air-01";
static const char* kFirmwareVersion = "0.1.0";
static const char* kLocationMode = "indoor";
static const char* kObservedAtPlaceholder = "1970-01-01T00:00:00Z";

static const int kI2cSdaPin = 8;
static const int kI2cSclPin = 9;
static const unsigned long kSampleIntervalMs = 5000;

struct Sht45Reading {
  bool present;
  float temperature_c;
  float relative_humidity_pct;
};

struct Bme680Reading {
  bool present;
  float temperature_c;
  float relative_humidity_pct;
  float pressure_hpa;
  float gas_resistance_ohm;
};

unsigned long last_sample_ms = 0;
unsigned long read_failures_total = 0;

Sht45Reading readSht45() {
  // Replace this placeholder with a real SHT45 library read.
  Sht45Reading reading;
  reading.present = true;
  reading.temperature_c = 23.4f;
  reading.relative_humidity_pct = 41.8f;
  return reading;
}

Bme680Reading readBme680() {
  // Replace this placeholder with a real BME680 library read.
  Bme680Reading reading;
  reading.present = true;
  reading.temperature_c = 24.1f;
  reading.relative_humidity_pct = 40.9f;
  reading.pressure_hpa = 1012.6f;
  reading.gas_resistance_ohm = 145230.0f;
  return reading;
}

void printFloat(float value, int digits = 1) {
  Serial.print(value, digits);
}

void emitPacket(const Sht45Reading& sht45, const Bme680Reading& bme680) {
  Serial.print("{\"schema_version\":\"");
  Serial.print(kSchemaVersion);
  Serial.print("\",\"node_id\":\"");
  Serial.print(kNodeId);
  Serial.print("\",\"observed_at\":\"");
  Serial.print(kObservedAtPlaceholder);
  Serial.print("\",\"firmware_version\":\"");
  Serial.print(kFirmwareVersion);
  Serial.print("\",\"location_mode\":\"");
  Serial.print(kLocationMode);
  Serial.print("\",\"sensors\":{\"sht45\":{\"present\":");
  Serial.print(sht45.present ? "true" : "false");
  Serial.print(",\"temperature_c\":");
  printFloat(sht45.temperature_c);
  Serial.print(",\"relative_humidity_pct\":");
  printFloat(sht45.relative_humidity_pct);
  Serial.print("},\"bme680\":{\"present\":");
  Serial.print(bme680.present ? "true" : "false");
  Serial.print(",\"temperature_c\":");
  printFloat(bme680.temperature_c);
  Serial.print(",\"relative_humidity_pct\":");
  printFloat(bme680.relative_humidity_pct);
  Serial.print(",\"pressure_hpa\":");
  printFloat(bme680.pressure_hpa);
  Serial.print(",\"gas_resistance_ohm\":");
  printFloat(bme680.gas_resistance_ohm, 0);
  Serial.print("}},\"derived\":{\"temperature_c_primary\":");
  printFloat(sht45.temperature_c);
  Serial.print(",\"relative_humidity_pct_primary\":");
  printFloat(sht45.relative_humidity_pct);
  Serial.print(",\"pressure_hpa\":");
  printFloat(bme680.pressure_hpa);
  Serial.print(",\"voc_trend_source\":\"gas_resistance_ohm\"},\"health\":{\"uptime_s\":");
  Serial.print(millis() / 1000UL);
  Serial.print(",\"wifi_connected\":false,\"free_heap_bytes\":");
#ifdef ESP32
  Serial.print(ESP.getFreeHeap());
#else
  Serial.print(0);
#endif
  Serial.print(",\"read_failures_total\":");
  Serial.print(read_failures_total);
  Serial.print(",\"last_error\":null}}");
  Serial.println();
}

void setup() {
  Serial.begin(115200);
  delay(250);

  Serial.println("# bench_air_node_serial_json");
  Serial.print("# I2C pin plan: SDA=GPIO");
  Serial.print(kI2cSdaPin);
  Serial.print(" SCL=GPIO");
  Serial.println(kI2cSclPin);
  Serial.println("# placeholder sensor values enabled");
}

void loop() {
  unsigned long now = millis();
  if (now - last_sample_ms < kSampleIntervalMs) {
    delay(50);
    return;
  }

  last_sample_ms = now;

  Sht45Reading sht45 = readSht45();
  Bme680Reading bme680 = readBme680();

  if (!sht45.present || !bme680.present) {
    read_failures_total++;
  }

  emitPacket(sht45, bme680);
}
