#!/usr/bin/python3

import sys, os
import diffmerge

this_dir = os.path.dirname(os.path.realpath(__file__))

VIM = '/opt/vim/bin/vim'
if not os.path.exists(VIM):
    VIM = '/usr/bin/vim'


def launch(args):
    cfgdir = os.path.join(this_dir,'..','home','gvimdiff_dm')
    cfgdir = os.path.realpath(cfgdir)
    
    if (len(args) < 2) or (not (os.path.isfile(args[0]) and os.path.isfile(args[1]))):
        diffmerge.launch(args, cfgdir=cfgdir)
    else:
        _args = [ VIM, '-d', '-g' ]
        _args.extend(args)
        os.environ['HOME'] = cfgdir
        os.execve(_args[0], _args, os.environ)


if __name__ == '__main__':
    args = sys.argv[1:]
    launch(args)

