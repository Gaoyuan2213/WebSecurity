# WebSecurity Project – IT Help Desk & Packet Capture

## Project Overview

This project is a simple **IT Help Desk system** combined with network packet capture and logging. It allows users to submit support tickets and supports analyzing PCAP/PCAPNG files using Python for network monitoring tasks.

Key features:

* Employee/IT/Admin roles for ticket submission and management.
* Packet capture logging and JSONL export.
* Basic packet analysis and Mini-SIEM style alerts (Milestone 2).
* Example PCAPs included for DNS and HTTP traffic.

## Folder Structure

```
Course Project/
├─ agent/              # Agent code for packet capture & CLI
├─ detectors/          # DNS, ICMP, ARP, HTTP detectors
├─ siem/               # Mini-SIEM: ingest, alerts, CLI views
├─ scripts/            # Run tests scripts
├─ pcaps/              # Sample PCAP/PCAPNG files
├─ logs/               # JSONL output: detections.jsonl, ops.jsonl, alerts.jsonl
├─ capture_logger.py   # Milestone 1 packet capture & JSONL export
├─ config.yaml         # Config file for thresholds & logging
├─ README.md           # Project documentation
├─ requirements.txt    # Python dependencies
```

## Setup

1. Create virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

2. Make sure Npcap is installed if using Windows live capture.

## Usage

### 1. Capture and export PCAP to JSON

```bash
python capture_logger.py --pcap pcaps/basic_http.pcapng --out logs/out_basic.jsonl --overwrite
python capture_logger.py --pcap pcaps/dns_examples.pcapng --out logs/out_dns.jsonl --overwrite
```

### 2. Mini-SIEM CLI

Run analysis on `detections.jsonl`:

```bash
# Timeline view
python -m siem.mini_siem --timeline

# Top talkers
python -m siem.mini_siem --top

# Rule stats
python -m siem.mini_siem --rule-stats
```

### 3. Run visible tests

```bash
python scripts/run_tests.py
```

## JSONL Output Format

### Detections (`logs/detections.jsonl`)

```json
{
  "ts": "2025-10-20T12:34:56+00:00",
  "schema_version": "1.0",
  "src": "192.168.1.10:12345",
  "dst": "8.8.8.8:53",
  "proto": "DNS",
  "rule_id": "DNS_SUSPICIOUS",
  "severity": "high",
  "summary": "Suspicious DNS query detected",
  "metadata": { "query": "longlabel.example.com", "entropy": 4.2 }
}
```

### Ops log (`logs/ops.jsonl`)

```json
{
  "ts": "2025-10-20T12:35:00",
  "level": "INFO",
  "component": "capture",
  "msg": "start_pcap",
  "kv": { "file": "pcaps/basic_http.pcapng" }
}
```

### Alerts (`logs/alerts.jsonl`)

```json
{
  "ts": "2025-10-20T12:36:00",
  "alert_id": "ALERT_ICMP_FLOOD",
  "severity": "high",
  "summary": "High volume ICMP events",
  "entities": { "src": "192.168.1.10", "rule_id": "ICMP_RATE" },
  "evidence_count": 42
}
```

## Notes

* Ensure PCAP files exist in `pcaps/` before running capture scripts.
* Thresholds for detections are configurable in `config.yaml`.
* For live capture on Windows, Npcap must be installed.
* This README serves for both Milestone 1 and Milestone 2 combined.

## References

* [Scapy Documentation](https://scapy.net) – Python packet manipulation library
* [JSON Lines Format](http
