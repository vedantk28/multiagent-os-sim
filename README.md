# 🧠 Multi-Agent OS Simulation Project

A modular, agent-driven operating system simulator that teaches students core OS concepts through interactive resource management, inter-process communication (IPC), and multi-agent coordination protocols. Built with extensibility, clarity, and educational value in mind.

## 📌 Project Highlights

- 🧵 **Agent Lifecycle & Scheduling**
  - States: `READY`, `RUNNING`, `BLOCKED`, `RESPONDING`, `COMPLETED`
  - Round-Robin Scheduler with time-sliced execution

- ⚙️ **Resource Management**
  - Custom `ResourcePool` with dynamic allocation and release
  - Agents request and compete for CPU/RAM slots

- 📡 **Inter-Agent Messaging (IPC)**
  - Structured protocols: `DATA_REQ → ACK → EXEC`
  - Support for priority-based queues and broadcast coordination

- 🧠 **Agent Memory & Reasoning**
  - Agents track message history and conditionally respond
  - Enables adaptive behavior and negotiation patterns

- 🔎 **Simulation Clock & Ticking System**
  - Controls execution order with customizable tick duration

- 📊 **CLI-Based Message Logger**
  - Real-time trace of inter-agent communication per tick
  - Easy debugging, visualization, and teaching aid

## 🗂️ Folder Structure

```
multiagent_os_project/
├── agents/                 # Agent classes with logic and memory
│   ├── __init__.py
│   ├── base_agent.py      # Abstract base class for all agents
│   ├── worker_agent.py    # Example worker agent implementation
│   └── manager_agent.py   # Coordinator agent for resource management
├── core/                  # Scheduler, IPC, resource pool, clock
│   ├── __init__.py
│   ├── scheduler.py       # Round-robin scheduling logic
│   ├── message_bus.py     # IPC messaging system
│   ├── resource_pool.py   # Dynamic resource allocation
│   └── clock.py           # Simulation timing control
├── utils/                 # Message logger for CLI trace
│   ├── __init__.py
│   └── logger.py          # Real-time communication logging
├── tests/                 # Unit tests for messaging and scheduling
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_scheduler.py
│   └── test_messaging.py
├── main.py                # Simulation entry point
└── README.md              # This file
```

## 🚀 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/multiagent-os-sim.git
cd multiagent-os-sim

# Create virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install rich loguru

# Run the simulation
python main.py
```

## 🧪 How It Works

Each simulation tick proceeds as follows:

1. **Agent Selection**: The scheduler selects the next agent based on round-robin logic
2. **Message Processing**: Agent optionally receives a message and updates its state
3. **Agent Negotiation**: Agents send messages (e.g. `DATA_REQ`) and negotiate with peers
4. **Resource Allocation**: Resources are allocated or denied based on current availability
5. **Logging**: Message log tracks all interactions for review and testing

## 🏗️ System Architecture Overview

The Multi-Agent OS Simulator is structured around modular components that emulate operating system behavior through autonomous agents. Each layer is designed for clarity, extensibility, and real-time simulation.

```
┌────────────────────────────────────────────────────────────┐
│                      main.py (Entry Point)                │
└────────────────────────────────────────────────────────────┘
           │
           ▼
┌───────────────┐    Initializes core modules and agents
│ AgentManager  │◄────────────────────────────────┐
└───────────────┘                                 │
           │                                      │
           ▼                                      │
┌────────────────┐                                │
│ BaseAgent(s)   │──┐                             │
└────────────────┘  │                             │
                    ▼                             ▼
┌────────────────────────────────────────────────────────────┐
│              RoundRobinScheduler (core/scheduler.py)       │
└────────────────────────────────────────────────────────────┘
           │           ▲
           ▼           │
┌────────────────┐     │   Controlled execution by tick
│ SimulationClock│─────┘
└────────────────┘
           ▼
┌────────────────┐       Tracks available resources per tick
│ ResourcePool   │◄─────────────────────────────────────┐
└────────────────┘                                      │
           │                                            │
           ▼                                            │
┌────────────────┐   Agents request/release resources   │
│ MessageBus     │◄─────────────────────────────────────┘
└────────────────┘
           │
           ▼
┌────────────────┐
│ MessageLogger  │   Logs all communication events
└────────────────┘
           ▼
┌────────────────────────────────────────────────────────────┐
│                    CLI Output & Log Trace                  │
└────────────────────────────────────────────────────────────┘
```

## 📦 Module Responsibilities

- **`agents/`** → Defines agent behavior, messaging logic, memory tracking
- **`core/`** → Includes scheduler, clock, IPC layer, and resource pool
- **`utils/`** → Message logger for CLI-based protocol trace
- **`tests/`** → Validates sequencing, resource negotiation, and agent coordination
- **`main.py`** → Orchestrates setup and simulation loop

## 💡 Expandable Labs

This project supports easy academic expansion:

- ✨ **Plug-in alternate schedulers** (e.g. priority-based, shortest job first)
- 🧠 **Add ML-based policy agents** (reinforcement learning, supervised decisions)
- 🧩 **Simulate deadlock detection and recovery** mechanisms
- 🎛️ **Build GUI dashboard** with `Tkinter` or `Flask` for visualization
- 🧵 **Extend IPC protocols** to include reject, timeout, retry mechanisms
- 📈 **Performance metrics** and throughput analysis
- 🔐 **Security protocols** and access control simulation

## 🎓 Educational Utility

Designed as a hands-on teaching tool for:

- **Operating System Fundamentals** - Process scheduling, resource management, IPC
- **Multi-Agent Systems** - Coordination protocols, negotiation, distributed decision making
- **Concurrency & Synchronization** - Race conditions, mutual exclusion, deadlock prevention
- **System Architecture** - Modular design, event-driven programming, simulation techniques

## 🧠 Design Principles

- **Modularity** → Each component is cleanly separable and testable
- **Explainability** → Tick-by-tick logging allows debugging and teaching
- **Extensibility** → Easy to plug in new agents, message types, or schedulers
- **Pedagogical Focus** → Built for clarity, validation, and learning—not just output

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test modules
python -m pytest tests/test_agents.py
python -m pytest tests/test_scheduler.py -v
```

## 📝 Example Output

```
[Tick 1] Agent-001 (READY) → Agent-002: DATA_REQ {priority: HIGH}
[Tick 1] ResourcePool: CPU slots 3/4, RAM slots 7/8
[Tick 2] Agent-002 (RUNNING) → Agent-001: ACK {resource_granted: True}
[Tick 2] Agent-001 state: READY → RUNNING
[Tick 3] Agent-001 → Agent-002: EXEC {task_id: 'compute_matrix'}
...
```

## 🤝 Contributing

Contributions are welcome! Please feel free to:

- Submit bug reports and feature requests
- Fork the repository and create pull requests
- Improve documentation and add examples
- Extend the simulation with new agent types or protocols

## 👨‍💻 Author

Built by **Vedant** 

Passionate about modular, reviewable, and production-grade AI systems. Feel free to connect or fork the repo for your own classroom experiments or research demos!

## 📄 License

This project is open-source for educational use. For other purposes, please contact the author directly.

---

**Ready to simulate some OS magic?** 🚀 Start with `python main.py` and watch your agents come to life!
