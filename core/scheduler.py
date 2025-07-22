from core.sim_clock import SimulationClock
from core.ipc import MessageBus

class RoundRobinScheduler:
    def __init__(self, agent_manager, clock: SimulationClock):
        self.agents = agent_manager.agents
        self.clock = clock

    def run(self, resource_pool, ipc: MessageBus, ticks=10):
        index = 0
        for _ in range(ticks):
            tick = self.clock.tick()
            print(f"\n=== Tick {tick} ===")

            agent = self.agents[index % len(self.agents)]
            print(f"[Scheduler] Tick {tick}: Selected Agent {agent.agent_id} (State: {agent.state})")

            if agent.state in ["READY", "BLOCKED"]:
                agent.run(resource_pool, ipc, tick)
            else:
                print(f"[Scheduler] Agent {agent.agent_id} already completed.")

            index += 1
