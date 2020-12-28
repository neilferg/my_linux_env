#!/usr/bin/python3

import sys, os
import configparser
import time

this_dir = os.path.dirname(os.path.realpath(__file__))

DIFFMERGE = '/opt/diffmerge/usr/bin/diffmerge'


def launch(args, cfgdir = None):
    if cfgdir is None:
        cfgdir = os.path.join(this_dir,'..','home','diffmerge')

    cfgdir = os.path.realpath(cfgdir)
    inifile = os.path.join(cfgdir, '.SourceGear DiffMerge')

    cfg = configparser.ConfigParser()
    cfg.read(inifile)

    ts = int(cfg['License']['Check'])

    T_MAX = 3600

    tNow = int(time.time())
    tDelta = tNow - ts
    #print(tDelta)
    if tDelta > T_MAX:
        #print("Refresh ts (tNow=%d)" % (tNow))
        cfg['License']['check'] = str(tNow)
        cfg['Revision']['check'] = str(tNow)
 
        with open(inifile, 'w') as fs:
            cfg.write(fs)

    os.environ['HOME'] = cfgdir
    args.insert(0, DIFFMERGE)
    os.execve(args[0], args, os.environ)


if __name__ == '__main__':
    args = sys.argv[1:]
    launch(args)

