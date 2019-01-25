# to jest deklaracja wyjątków do zadania "Obiekty_Zad_7_bankomat_z_wyjatkami_moje"


class CashMachineError(Exception):
    pass


class BasketFullError(CashMachineError):
    pass


class EmptyError(CashMachineError):
    pass


class WrongAmountError(CashMachineError):
    pass
