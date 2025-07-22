# core/agent_manager.py
from agents.base_agent import BaseAgent

class AgentManager:
    def __init__(self):
        self.agents = []

    def register(self, agent: BaseAgent):
        self.agents.append(agent)

    def run_all(self, resource_pool):
        for agent in self.agents:
            agent.run(resource_pool)
