print("[MAIN] Starting simulation...")

from core.resource_pool import ResourcePool
from core.agent_manager import AgentManager
from core.scheduler import RoundRobinScheduler
from core.sim_clock import SimulationClock
from core.ipc import MessageBus
from agents.base_agent import BaseAgent

# Setup
pool = ResourcePool(total_resources=5)
manager = AgentManager()
clock = SimulationClock(tick_duration=0.5)
ipc = MessageBus()

# Register agents
manager.register(BaseAgent(agent_id="A1", required_units=3))
manager.register(BaseAgent(agent_id="A2", required_units=2))

# Schedule & Run
scheduler = RoundRobinScheduler(manager, clock)
scheduler.run(resource_pool=pool, ipc=ipc, ticks=6)

ipc.print_log()
