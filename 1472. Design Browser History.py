class BrowserHistory:
    class historyNode:
        def __init__(self, url, prev = None, next = None):
            self.url = url
            self.prev = prev
            self.next = next

    def __init__(self, homepage: str):
        self.history = self.historyNode(homepage)


    def visit(self, url: str) -> None:
        new = self.historyNode(url, self.history)
        self.history.next = new  
        new.prev = self.history  
        self.history = new
    

    def back(self, steps: int) -> str:
        while self.history.prev and steps > 0:
            self.history = self.history.prev
            steps -= 1
        return self.history.url
        

    def forward(self, steps: int) -> str:
        while self.history.next and steps > 0:
            self.history = self.history.next
            steps -= 1
        return self.history.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)