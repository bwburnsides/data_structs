from abc import ABC, abstractmethod
from typing import Mapping, Union, Any

# Abstracts
class Expression(ABC):
    @abstractmethod
    def eval(self, env: Mapping[str, float]) -> float:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    def __add__(self, other: "Expression") -> "Expression":
        return Add(self, other)

    def __sub__(self, other: "Expression") -> "Expression":
        return Subtract(self, other)

    def __mul__(self, other: "Expression") -> "Expression":
        return Multiply(self, other)

    def __truediv__(self, other: "Expression") -> "Expression":
        return Divide(self, other)


class Operation(Expression, ABC):
    def __init__(self, *operands: Expression) -> None:
        self.operands = operands

    def eval(self, env: Mapping[str, float]) -> float:
        return self.operation(*[operand.eval(env) for operand in self.operands])  # type: ignore

    @property
    @abstractmethod
    def symbol(self):
        ...


class Binary(Operation, ABC):
    def __init__(self, operand1: Expression, operand2: Expression) -> None:
        super().__init__(operand1, operand2)
        self.operand1 = operand1
        self.operand2 = operand2

    def __repr__(self) -> str:
        return f"({self.operands[0]} {self.symbol} {self.operands[1]})"

    @staticmethod
    @abstractmethod
    def operation(op1, op2) -> float:
        ...


class Unary(Operation, ABC):
    def __init__(self, operand1: Expression) -> None:
        super().__init__(operand1)
        self.operand1 = operand1

    @staticmethod
    @abstractmethod
    def operation(op) -> float:
        ...


class Prefix(Unary, ABC):
    def __repr__(self) -> str:
        return f"{self.symbol}({self.operands[0]})"


class Postfix(Unary, ABC):
    def __repr__(self) -> str:
        return f"({self.operands[0]}){self.symbol}"


class Value(Expression, ABC):
    def __init__(self, value: Union[str, float]) -> None:
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


# Concretes
class Multiply(Binary):
    symbol = "*"

    @staticmethod
    def operation(op1, op2):
        return op1 * op2


class Divide(Binary):
    symbol = "/"

    @staticmethod
    def operation(op1, op2):
        return op1 / op2


class Add(Binary):
    symbol = "+"

    @staticmethod
    def operation(op1, op2):
        return op1 + op2


class Subtract(Binary):
    symbol = "-"

    @staticmethod
    def operation(op1, op2):
        return op1 - op2


class Exponent(Binary):
    symbol = "^"

    @staticmethod
    def operation(op1, op2):
        return op1 ** op2


class Negate(Prefix):
    symbol = "-"

    @staticmethod
    def operation(op1):
        return -op1


class Factorial(Postfix):
    symbol = "!"

    @staticmethod
    def operation(op1):
        if op1 in [0, 1]:
            return 1
        elif op1 > 1:
            return op1 * Factorial.operation(op1 - 1)
        raise ValueError


class Variable(Value, ABC):
    def eval(self, env):
        return env[self.value]


class Constant(Value, ABC):
    def eval(self, env):
        return self.value
