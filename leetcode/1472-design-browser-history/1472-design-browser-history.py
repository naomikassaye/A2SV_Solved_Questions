class BrowserHistory:
    def __init__(self, homepage: str):
        self.h = [homepage]
        self.curr = 0
        self.end = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr < len(self.h):
            self.h[self.curr] = url
        else:
            self.h.append(url)
        self.end = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.h[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.end, self.curr + steps)
        return self.h[self.curr]