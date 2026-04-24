# Project Solarbank: Energy Data Monitoring & Analytics

## Project Overview
The objective of this project is to develop an automated monitoring solution for the **Anker Solix** solar power ecosystem (specifically targeting the Solarbank 2 series). 

By bypassing the limitations of the official mobile-only interface, this project aims to:
* **Extract real-time telemetry**: Capture live data from photovoltaic panels (input), battery storage (capacity/health), and home load (output).
* **Data Centralization**: Enable long-term logging for energy efficiency audits.
* **Smart Integration**: Prepare the data for export into custom dashboards or local home automation controllers.

## 🛠 Technical Challenge (The "Session Blocker")
We are currently facing a critical hurdle regarding **Session Management** and **Cloud Authentication** on Anker’s servers. 

### Symptoms & Observations:
1. **Intermittent Success**: Authentication works successfully on the first attempt but fails systematically on subsequent runs.
2. **Session Persistence Issues**: We frequently encounter `Login Failed` errors or `NoneType` exceptions, suggesting the internal `aiohttp` session is not being correctly maintained or closed.
3. **Bot Detection**: Even with a dedicated "Guest Account" and randomized User-Agents, the server appears to flag the IP address or the Account ID after a few requests.
4. **Environment Diversity**: The issue persists across different networks (Home Wi-Fi vs. 4G/LTE Hotspot), suggesting the lock is account-side rather than just IP-based.

## 📚 Credits and References
This project is built upon the Open Source community's reverse-engineering efforts of the Anker Solix protocol.

* **API Wrapper:** `anker-solix-api`
* **Original Author:** [thomluther](https://github.com/thomluther)
* **GitHub Repository:** [https://github.com/thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api)

## 🏗 Technical Stack
* **Language:** Python 3.x
* **Asynchronous Framework:** `asyncio` & `aiohttp`.
* **Configuration:** `python-dotenv` for secure credential management.
* **Architecture:** The client simulates a mobile device environment (Headers, User-Agent, App-Version) to communicate with Anker’s AWS-hosted endpoints (EU/DE regions).

---
*Project developed for personal uses - 2026*
