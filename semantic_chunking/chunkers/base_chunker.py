from abc import ABC, abstractmethod
from typing import List, Dict

class BaseChunker(ABC):
    """
    Abstract base class for all chunkers
    """

    @abstractmethod
    def chunk(self, document: Dict) -> List[Dict]:
        """
        Input: document {text, metadata}
        Output: list of chunks with metadata
        """
        pass
