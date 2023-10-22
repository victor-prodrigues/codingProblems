from abc import ABC, abstractmethod 


class TestResults(ABC): 
        
    @abstractmethod
    def test(self) -> bool:
        raise NotImplementedError()

    
    def run_tests(self) -> None:
        if self.test():
            print("All test passed!")
            return

        print("You have failed test cases!")
        

    