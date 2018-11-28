# -*- coding: UTF-8 -*-

import time
import sched
import connent

def worker(msg, starttime):
    connent.run()
    print 'content', time.time(), "name", msg, 'time', starttime

def run():
    i = 1
    print 'stat time:', time.time()
    while (i < 90):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(30*60, 1, worker, ('第' + str(i) + "次", time.time()))
        s.run()
        i = i+1
    print 'end time:', time.time()

run()