## TERRA: IoT-Based Smart Agriculture System 🌱

TERRA is an IoT-based smart agriculture project designed to automate and optimize farming practices. By integrating real-time ground sensor data with large-scale satellite imagery, TERRA delivers actionable insights for efficient and sustainable agriculture.

## Features

Hybrid Data Monitoring: Combines hyper-local data from on-ground sensors with large-scale satellite imagery to provide a complete and accurate picture of your farm's health.

Real-Time Ground Truth: Get live updates on critical soil and atmospheric conditions, including soil moisture, NPK levels, temperature, humidity, light intensity, and UV index.

Satellite-Powered Insights: Leverage satellite data to monitor vegetation health (NDVI, NDWI, EVI) across your entire field and receive predictive alerts for potential pest outbreaks.

Remote Access & Control: Monitor your farm's conditions and manually override automated systems from anywhere in the world using a responsive web dashboard on your phone or laptop.

Customized Crop Reporting: Select your crop type and generate detailed, actionable reports that fuse both ground and satellite data for tailored recommendations.

Historical Trend Analysis: View and analyze historical data through interactive charts to identify patterns, track crop performance, and optimize your farming strategies for future seasons.

Scalable & Modular Design: The system is built to grow with your farm. Easily expand your network from a single module to cover entire fields with our modular hardware and software architecture.

## Project Structure

/
├── hardware/
│   ├── arduino_transmitter/    # Firmware for the Arduino UNO sensor and actuator node.
│   └── esp32_receiver/         # Firmware for the ESP32 gateway that sends data to the cloud.
│
├── software/
│   ├── backend/                # Source code for the API server that processes and stores data.
│   └── frontend/               # Source code for the web dashboard user interface.
│
└── docs/
    ├── schematics/             # Circuit diagrams, PCB layouts, and hardware connection guides.
    └── reports/                # Project reports, presentations, and other supporting materials.

## Getting Started

1. Clone the repository:

git clone https://github.com/AadityaChaturvedy/TERRA_CODE_MERGE.git

## Hardware Requirements

Microcontrollers:Arduino UNO R3, ESP32 Dev Module
Communication	NRF24L01 Modules
Capacitive Soil Moisture Sensor
AHT10 Sensor (Temperature & Humidity)
BH1750 Sensor (Light Intensity)
GUVA-S12SD UV Sensor
NPK Sensor
Actuators	5V Single Channel Relay Module
Common Cathode RGB LED

## Software Requirements

Firmware:	Arduino IDE or PlatformIO
Backend	Python (3.8+) or Node.js
Database:	Supabase Account
Cloud API	
Sentinel Hub Account
Version Control	Git

## Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.

---

Developed by Team Wunderkinds for Code Merge, 2025.
