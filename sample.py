from enum import Enum, auto
class HitBlowResult(Enum):
        HIT = auto()
        BLOW = auto()
        NONE = auto()
p_num = [HitBlowResult.NONE, HitBlowResult.NONE, HitBlowResult.NONE]
p_num[0] = (HitBlowResult.HIT)
print(p_num)