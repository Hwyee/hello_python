# async
"""
python 现在目前由于GIL 限制,python只能是单线程顺序,但是在等待时候，会切换到其他任务，这就是异步编程

eventloop : eventloop只能执行task
    来控制所有任务，循环任务，控制任务执行

异步编程：
    1. 协程
    2. 异步IO


"""

import asyncio
import time


async def test():
    """
    这是个协程函数，函数执行只会返回一个协程object
    """
    await asyncio.sleep(1)
    print("test")
    return "return test"


async def test2():
    await asyncio.sleep(2)
    print("test2")
    return "return test2"


async def main():
    print(f"started at {time.strftime('%X')}")
    # await做了什么？
    # 1.
    #   1.1如果await的是coroutine，就像调用了一个生成器会等待他执行完毕，不交换控制权，没有异步
    #   1.2如果await的是task，则会等待他执行完毕，并且交换控制权，然后由eventloop完成调用，异步
    #   1.3future，future是task的父类
    # 2. 获取task的返回值，异常等信息，等这个task执行完成，再继续执行下面的代码（不用await是拿不到返回值的）
    res1 = await test()
    res2 = await test2()
    print(f"finished at {time.strftime('%X')} {res1} {res2}")


corouObj = main()  # 不会运行函数代码，而是获取写成对象
asyncio.run(
    corouObj
)  # 进入async模式，让event loop控制函数执行，把协程对象转换成 evetloop的第一个task

"""
以上代码执行了三秒：输出
started at 01:56:34
test
test2
finished at 01:56:37 return test return test2
因为在等待test1的sleep任务是,test2的任务,await还没有创建,只能等test1完成才能执行test2
event loop拿回控制权:不能制动拿
1. await 创建任务
2. 获取任务结果 (task执行结束,即函数执行完成)
"""


# 如何让 sleep的时候，协程去执行其他task呢
async def test3():
    await asyncio.sleep(1)
    print("test3")
    return "return test3"


async def test4():
    await asyncio.sleep(2)
    print("test4")
    return "return test4"


async def main1():
    print(f"started at {time.strftime('%X')}")
    # 先创建任务 注册到event loop，不交还控制权
    task1 = asyncio.create_task(test3())
    task2 = asyncio.create_task(test4())
    # 这时await就不用把coroutine对象转换成task了，直接将控制权给eventloop，要等待task完成
    # res1 = await task1
    # res2 = await task2
    # gather() 可以是coroutin对象，也可以是task对象，甚至可以是gather的返回值，可以继续gather，gather返回的是一个futuer
    # 然后await 就是等待gather中的每个task都执行完成
    res = await asyncio.gather(task1, task2)
    print(f"finished at {time.strftime('%X')} {res}")


asyncio.run(main1())
"""
函数输出
started at 02:09:27
test3
test4
finished at 02:09:29 return test3 return test4
gather把返回值包装成了列表
started at 02:13:10
test3
test4
finished at 02:13:12 ['return test3', 'return test4']
"""
