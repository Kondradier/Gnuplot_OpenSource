import MapStatistic


class MapStatistic:
    def __init__(self, iter: int, f_C: float, f_C_corr: float, av_pay: float, f_cr0: float, f_cr_1: float, f_allC: float, f_allD: float, f_Kd: float, f_Kc: float, f_Kdc: float, fstrat_ch: float) -> None:
        self.iter = iter
        self.f_C = f_C
        self.f_C_corr = f_C_corr
        self.av_pay = av_pay
        self.f_cr0 = f_cr0
        self.f_cr_1 = f_cr_1
        self.f_allC = f_allC
        self.f_allD = f_allD
        self.f_Kd = f_Kd
        self.f_Kc = f_Kc
        self.f_Kdc = f_Kdc
        self.fstrat_ch = fstrat_ch

    def getTestData() -> MapStatistic:
        return MapStatistic(
            0, 0.48, 0.01, 0.2, 0, 1, 0.2, 0.2, 0.2, 0.2, 0.2, 0
        )

    def __str__(self) -> str:
        width = 10
        return f"{self.iter:>{width}} {self.f_C:>{width}} {self.f_C_corr:>{width}} {self.av_pay:>{width}} {self.f_cr0:>{width}} {self.f_cr_1:>{width}} {self.f_allC:>{width}} {self.f_allD:>{width}} {self.f_Kd:>{width}} {self.f_Kc:>{width}} {self.f_Kdc:>{width}} {self.fstrat_ch:>{width}}"

    def __repr__(self) -> str:
        return self.__str__()