# tests/test_ipc_protocol.py
import unittest
from core.ipc import MessageBus

class TestMessageFlow(unittest.TestCase):
    def test_sequence(self):
        ipc = MessageBus()
        ipc.send("A1", "A2", "Need access", "DATA_REQ", tick=1)
        msg = ipc.receive("A2")
        self.assertEqual(msg["type"], "DATA_REQ")
        ipc.send("A2", "A1", "OK", "ACK", tick=2)
        ack = ipc.receive("A1")
        self.assertEqual(ack["type"], "ACK")

if __name__ == "__main__":
    unittest.main()
