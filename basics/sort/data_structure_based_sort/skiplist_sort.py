import random
import sys


def skiplist_sort(nums: list[int]) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    sorted_ = []
    random_gen = random.SystemRandom()
    from basics.data_structure.RedisZset import ZSet
    zset: ZSet = ZSet(elem_to_score={
        random_gen.uniform(0, sys.float_info.max).hex(): score for score in nums
    })
    list_node = zset.skiplist.dummy_header.levels[0].forward
    while list_node is not None:
        sorted_.append(list_node.score)
        list_node = list_node.levels[0].forward
    return sorted_


# python 随机数话题：

# https://docs.python.org/zh-cn/3/library/uuid.html
#
# >>> import uuid
# >>> id_ = uuid.uuid4()
# >>> id_
# UUID('a0c09603-ef93-4ab1-bd54-aecea2601749')
# >>> id_ = uuid.uuid4()
# >>> id_
# UUID('b2ceaa68-a7d5-4079-a176-28ce2159654b')
# >>> id_ = uuid.uuid4()
# >>> id_
# UUID('84b385a9-7270-4e78-8ec8-252687a80936')
# >>> id_.is_safe
# <SafeUUID.unknown: None>
# >>>
#
#
# https://docs.python.org/zh-cn/3/library/random.html
#
# >>> import random
# >>> import sys
# >>> random.uniform(0, sys.float_info.max)
# 9.745031097917195e+307
# >>> random.uniform(0, sys.float_info.max)
# 4.119436108857729e+307
# >>> random.uniform(0, sys.float_info.max)
# 1.5213122541189402e+308
# >>> random.uniform(0, sys.float_info.max)
# 1.5629380990396959e+308
# >>> random.uniform(0, sys.float_info.max)
# 1.0413440219678448e+308
# >>> random.uniform(0, sys.float_info.max)
# 1.604028197066278e+308
# >>> random.uniform(0, sys.float_info.max)
# 9.41111841426963e+307
# >>> random.uniform(0, sys.float_info.max)
# 1.1177842081577284e+308
# >>> random.uniform(0, sys.float_info.max)
# 1.7337338824336913e+308
# >>> random.uniform(0, sys.float_info.max)
# 9.977245523929174e+305
# >>> random.uniform(0, sys.float_info.max)
# 7.007798948467095e+307
# >>> random.uniform(0, sys.float_info.max)
# 1.1867780741608513e+308
# >>>
#
# # 不使用默认生成器, 把生成随机数这个任务交给操作系统, 结果随机性质量最高, 适用于密码学领域
# >>> sr = random.SystemRandom()
# >>> sr
# <random.SystemRandom object at 0x0000025D00EF5890>
# >>> sr.uniform(0, sys.float_info.max)
# 1.089354218051575e+308
# >>> sr.uniform(0, sys.float_info.max)
# 2.905038765594629e+306
# >>> sr.uniform(0, sys.float_info.max)
# 1.3366399530296536e+308
# >>> sr.uniform(0, sys.float_info.max)
# 9.700863670412488e+307
# >>> sr.uniform(0, sys.float_info.max)
# 1.1304857385237975e+308
# >>> sr.uniform(0, sys.float_info.max)
# 2.4229820342472017e+307
# >>>
#
#
#
# https://docs.python.org/zh-cn/3/library/secrets.html
#
# >>> import secrets
# >>> sr2 = secrets.SystemRandom()
# >>> sr2
# <random.SystemRandom object at 0x0000025D01211AC0>
# >>>
#
# >>> secrets.token_hex(32)
# '8d69dbac1bc70649cd3d6975c3e8c960a266f611e3288c8e10c4a145f4d0aa5f'
# >>> secrets.token_hex(32)
# 'ba56685b48ce32d2b3633d3bb035ec3f17235f28f378b6a604c0dde21e8603df'
# >>> secrets.token_hex(32)
# '7afb7d3cd3702bef5df4973874ef0bc7fea4fe311f439d336467b1d628ba7d52'
# >>> secrets.token_hex(32)
# '73ee2c59f8241d065c3cd215c1231430cf738af410aab5e883367a87a3710132'
# >>>
