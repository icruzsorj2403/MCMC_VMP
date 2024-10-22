
import numpy as np

class UG_simples:

    def __init__(
            
        self,

        Dados: np.ndarray,

        sigma: float, mu_0: float, kappa_0: float

    ) -> None:
        
        self.X = Dados

        self.sigma = sigma

        self.mu_0 = mu_0

        self.kappa_0 = kappa_0

        self.mu = 0

    def inicializa_modelo(self) -> None:

        pass
