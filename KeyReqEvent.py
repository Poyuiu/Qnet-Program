from qcompute_qnet.core.des import DESEnv, EventHandler, Entity


class KeyReqEvent(Entity):
    def __init__(self, name: str, env=None):
        super().__init__(name, env)
        self.key_request_queue = []
        self.waiting_time = []

    def init(self):
        self.scheduler.schedule_now(EventHandler(self, "key_request_start"))

    def key_request_start(self):
        self.key_request_queue.append(KeyReqEvent(self.env.now))
        self.env.logger.debug(f"Key request {self.env.now}")
        if len(self.key_request_queue) == 1:
            self.scheduler.schedule_now(EventHandler(self, "key_request_end"))
        self.scheduler.schedule_after(20, EventHandler(self, "key_request_start"))
