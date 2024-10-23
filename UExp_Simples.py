
import numpy as np

class UG_simples:

    def __init__(
    
        self,

        Dados: np.ndarray,
        
        chi_0: float

    ) -> None:
        
        self.X = Dados

        self.N = self.X.shape[0]

        self.m_X_eta = np.zeros(shape = (self.N))

        self.chi_0 = chi_0

        self.chi = 0

        self.eta = 0

    def inicializa_modelo(self) -> None:

        self.eta = np.random.uniform(low = self.X.min(), high = self.X.max())

    def atualiza_m_X_eta(self) -> None:

        self.m_X_eta = self.X

    def atualiza_chi(self) -> None:

        self.chi = self.chi_0 + self.m_X_eta.sum()

    def atualiza_m_eta_X(self) -> None:

        self.eta = np.random.exponential(scale = self.chi, size = 100)

        self.eta = self.eta.mean()

    def atualiza_modelo(self) -> None:

        self.atualiza_m_X_eta()

        self.atualiza_chi()

        self.atualiza_m_eta_X()

    def estima_modelo(self, max: int) -> None:

        self.inicializa_modelo()

        self.atualiza_modelo()

        for i in range(max):

            self.atualiza_modelo()