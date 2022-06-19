import time
import numpy as np
import yaml
import logging
import logging.config


with open('utils/logging.yaml') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


class Statistics():
    
    def __init__(self, algorithm) -> None:
        self.algorithm = algorithm


    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}({self.algorithm!r})')


    def __str__(self) -> str:
        return f'Compute performance statistics for {self.algorithm.__class__.__name__}'


    def performance(self):
        logger.debug("Perfomance timers started")
        self._loopTimer()
        self._vectorisedTimer()


    def _loopTimer(self):
        times = np.zeros(100) 

        for n in range(times.shape[0]):
            begin = time.perf_counter()
            _ = self.algorithm.loop()
            end = time.perf_counter()
            times[n] = (end - begin)*1000
        
        self._statisticsPrinter(name = "loop", times = times)


    def _vectorisedTimer(self):
        times = np.zeros(100) 

        for n in range(times.shape[0]):
            begin = time.perf_counter()
            _ = self.algorithm.vectorised()
            end = time.perf_counter()
            times[n] = (end - begin)*1000
        
        self._statisticsPrinter(name = "vectorised", times = times)


    def _statisticsPrinter(self, name: str, times):
        print(
            "====================\n"
            f"| {name} \n"
            "==== Statistics ====\n\n" 
            f"Average: {np.mean(times):.4f} ms\n"
            f"Standard deviation: {np.std(times):.4f} ms\n"
            f"Maximum: {np.max(times):.4f} ms\n"
            f"Total (runs = {times.shape[0]}): {np.sum(times):.4f} ms\n"
        )

