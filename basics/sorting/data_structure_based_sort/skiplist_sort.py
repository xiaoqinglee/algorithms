def skiplist_sort(nums: list[int]) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    sorted_ = []
    import random
    from basics.data_structure.RedisZset import ZSet
    zset: ZSet = ZSet(elem_to_score={
        random.random().hex(): score for score in nums
    })
    list_node = zset.skiplist.dummy_header.levels[0].forward
    while list_node is not None:
        sorted_.append(list_node.score)
        list_node = list_node.levels[0].forward
    return sorted_


# 浮点数与随机数话题：


# 虽然计算机科可表示的浮点数在数轴上分布不均匀，但是各个语言所提供的随机数标准库包生成的随机数在数轴上是分布均匀的。
# python random 包提供了两个随机数生成器，一个默认的，一个操作系统的。
# 用户权衡待解决的问题对于计算性能和密码学安全性的要求选择合适的生成器。
#
# https://docs.python.org/zh-cn/3/library/random.html
# 几乎所有模块函数都依赖于基本函数 random() ，它在半开放区间 [0.0,1.0) 内均匀生成随机浮点数。
# Python 使用 Mersenne Twister 作为核心生成器。
# 它产生 53 位精度浮点数，周期为 2**19937-1 ，其在 C 中的底层实现既快又线程安全。
# Mersenne Twister 是现存最广泛测试的随机数发生器之一。
# 但是，因为完全确定性，它不适用于所有目的，并且完全不适合加密目的。
#
#
# 以下函数生成特定的实值分布。
# 如常用数学实践中所使用的那样，函数形参以分布方程中的相应变量命名，大多数这些方程都可以在任何统计学教材中找到。
#
# random.random()
#
#     返回 [0.0, 1.0) 范围内的下一个随机浮点数。
#
# random.uniform(a, b)
#
#     返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a 。
#     取决于等式 a + (b-a) * random() 中的浮点舍入，终点 b 可以包括或不包括在该范围内。
#
#
# # 注意：
# 如果我的问题只对随机性有要求，对值分布区间的长度、左边界和右边界没有要求，那么没有必要使用uniform。
# 回想计算机可表示的浮点数在数轴上的分布特点，
# [0, 1)内可表示的浮点数个数约等于[1, +Inf)内可表示的浮点数个数，越远离零点数值的分布越稀疏。
# 增加[a, b]区间的长度不但不能获得更大的随机数空间，而且会降低结果的随机性。
# 例如：
# 将random.random()更改为random.uniform(0, 1亿)不但不会获得更多随机数，而且会让产生的随机数存在更高概率的碰撞。
# 因为结果中值为0-1的元素个数是x，值为1-1亿的元素个数约为1亿x，我们知道越是远离零点的地方，有效的浮点数分布越稀疏，
# 这意味着：
# 1.要在更小的浮点数集合中选择更多的浮点数，结果会产生大量的近似舍入，出现更多的碰撞事件。
# 2.很大的浮点数集合中只选择零星几个值， 庞大的取值空间被浪费。


# https://docs.python.org/zh-cn/3/library/random.html
#
# >>> import random
# >>> random.random()
# 0.9133595450439957
# >>> random.random()
# 0.9818857598853842
# >>> random.random()
# 0.20618389899602974
# >>> random.random()
# 0.6956792424560458
# >>> random.random()
# 0.9463295021100163
# >>> random.random()
# 0.7059505312944383
# >>> random.random()
# 0.0394860910721595
# >>> random.random()
# 0.3913427241583629
# >>> random.random()
# 0.5397926906917183
# >>>
# >>> import sys
# >>> sys.float_info.max
# 1.7976931348623157e+308
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
#
# >>> # 不使用默认生成器, 把生成随机数这个任务交给操作系统, 结果随机性质量最高, 适用于密码学领域
# >>> sr = random.SystemRandom()
# >>> sr.random()
# 0.9517785977887042
# >>> sr.random()
# 0.6291729114590532
# >>> sr.random()
# 0.6096667374496195
# >>> sr.random()
# 0.5331073643219107
# >>>
# >>> sr.uniform(0, 42)
# 16.54355851565242
# >>> sr.uniform(0, 42)
# 16.108215553099065
# >>> sr.uniform(0, 42)
# 28.984643708408
# >>> sr.uniform(0, 42)
# 16.28344691477766
# >>> sr.uniform(0, 42)
# 10.982167030390404
# >>> sr.uniform(0, 42)
# 35.469516517443594
# >>>


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
