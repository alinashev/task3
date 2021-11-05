import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from Reader import Reader

path = 'res/osmi.json'

def counting(jsonString, startValue, endValue):
    number = 0
    for i in range(startValue, endValue):
        if jsonString['questions'][i]['id'] != "":
            number += 1
    return number

def runExecutor(jsonString, executorClass):
    executor = executorClass(max_workers=2)
    startTimeThread = time.time()
    fututres1 = executor.submit(counting, jsonString = jsonString,
                                startValue = 0,
                                endValue = int(len(jsonString['questions'])/2))
    fututres2 = executor.submit(counting, jsonString = jsonString,
                                startValue = int(len(jsonString['questions'])/2),
                                endValue = len(jsonString['questions']))

    result = fututres2.result() + fututres1.result()
    print("Results: {result}. Ececutor: {executor}. Time:{spentTime}".format(
        result = result,
        executor = executorClass.__name__,
        spentTime = time.time() - startTimeThread
    ))

def main():
    reader = Reader()
    jsonString = reader.openJSONFile(path)
    runExecutor(jsonString, ThreadPoolExecutor)
    runExecutor(jsonString, ProcessPoolExecutor)

if __name__ == '__main__':
    main()