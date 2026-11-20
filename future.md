# DustVision: Architectural Review & Urban Environmental AI Roadmap (future.md)

---

## 1. Architectural Code Review & Current State Analysis

DustVision is an urban environmental IoT and computer vision intelligence engine engineered to tackle micro-particulate pollution ($PM_{10} / PM_{2.5}$) in construction corridors and industrial quadrants. By fusing physical air quality sensor spikes with spatial camera event triggers across a $\pm 2$-minute temporal window and validating against the $50^\circ\text{--}140^\circ$ critical wind transport corridor, DustVision drives an ultra-low latency Random Forest regressor to forecast pollution 30 minutes into the future and actuate smart water-mist cannons before threshold breaches occur.

### Architectural Strengths
- **Sub-5ms Edge Inference:** The trained Random Forest model runs with sub-millisecond execution times, requiring $<45\text{MB}$ RAM and allowing single municipal servers to monitor hundreds of quadrants.
- **Physical Corridor Grounding:** Prevents false alarms by checking wind vector alignment; sensor spikes without matching wind directions or visual plumes are treated as local anomalies rather than actionable dust clouds.
- **Closed-Loop Mitigation Governance:** Automatically maps predicted severity ($150\text{--}250\ \mu\text{g/m}^3$) to tiered mitigation responses (60% spray vs 100% spray with contractor violation logging).

### Identified Bottlenecks & Modernization Needs
1. **Camera Image Pre-Processing:** Computer vision detection currently ingests pre-computed camera event logs rather than running real-time deep optical flow or optical density estimation directly on RTSP video streams.
2. **Tabular vs Spatio-Temporal Graph Modeling:** Random Forest treats temporal lag features well, but lacks spatial graph awareness to model how dust plumes disperse downwind across interconnected city street canyons.
3. **Hardware Gateway Coupling:** Spray actuation logic emits simulated API payloads rather than integrating with standard industrial IoT protocols (Modbus TCP, BACnet, MQTT Sparkplug B).

---

## 2. Strategic Engineering Roadmap

```mermaid
flowchart TD
    subgraph Phase 1: Real-Time Edge Video Optical Density
        P1A[RTSP CCTV Stream Ingestion] --> P1B[YOLOv8-Dust Optical Opacity Estimator]
        P1B --> P1C[Real-Time Plume Velocity Vectors]
    end

    subgraph Phase 2: Urban Street-Canyon CFD Modeling
        P2A[3D City GML Building Mesh] --> P2B[Physics-Informed Neural Network PINN]
        P2B --> P2C[Micro-Climate Air Dispersion Forecast]
    end

    subgraph Phase 3: Autonomous Drone & Industrial Mist Cannons
        P3A[Modbus / MQTT Hardware Actuation Broker] --> P3B[Autonomous Tethered Drone Mist Deployer]
        P3B --> P3C[Automated Mist Droplet Size Optimization]
    end

    subgraph Phase 4: Municipal Carbon & Penalty Blockchain Ledger
        P4A[Cryptographic Sensor Hash Verification] --> P4B[Municipal Contractor Penalty Smart Contract]
        P4B --> P4C[Public Real-Time Air Cleanliness Portal]
    end

    Phase 1 --> Phase 2
    Phase 2 --> Phase 3
    Phase 3 --> Phase 4
```

---

## 3. Detailed Milestone Execution Plan

### Milestone 1: Edge Computer Vision Optical Density on RTSP Streams
- [ ] **Real-Time Plume Segmentation:** Deploy an edge TensorRT-accelerated segmentation model directly on municipal CCTV cameras to measure visual optical extinction ($\beta_{ext}$) in real time.
- [ ] **Background Subtraction & Optical Flow:** Track plume dispersion trajectory to calculate wind velocity independently of sparse anemometer stations.

### Milestone 2: Physics-Informed Neural Network (PINN) Dispersion
- [ ] **Urban Street Canyon PINN:** Train a physics-informed surrogate neural model to predict turbulent particulate dispersion around high-rise buildings in $<20\text{ms}$.
- [ ] **Spatio-Temporal Graph Neural Network (ST-GNN):** Model urban sensor networks as dynamic graphs, propagating pollution risks downwind to neighboring schools and hospitals.

### Milestone 3: Industrial IoT Hardware Actuation (MQTT / Modbus)
- [ ] **Industrial Protocol Drivers:** Implement Modbus TCP and MQTT Sparkplug B drivers to command physical high-pressure atomizing mist cannons and solenoid valves directly.
- [ ] **Droplet Size Aerodynamics:** Adjust nozzle pressure dynamically based on relative humidity to ensure water droplet diameters ($10\text{--}50\mu\text{m}$) match particulate size for maximum scavenging efficiency.

### Milestone 4: Cryptographic Evidence Ledger for Environmental Compliance
- [ ] **Tamper-Proof Audit Logging:** Hash all sensor readings, camera frames, and contractor violation notices into an append-only cryptographic ledger.
- [ ] **Automated Environmental Fines:** Generate automated PDF violation citations with embedded satellite/CCTV photo proof for municipal pollution control boards.
