# core/resource_pool.py
class ResourcePool:
    def __init__(self, total_resources):
        self.total = total_resources
        self.available = total_resources

    def request(self, agent_id, units):
        if units <= self.available:
            self.available -= units
            print(f"[POOL] Granted {units} units to Agent {agent_id}")
            return True
        print(f"[POOL] Denied {units} units to Agent {agent_id}")
        return False

    def release(self, agent_id, units):
        self.available += units
        print(f"[POOL] Agent {agent_id} released {units} units")
