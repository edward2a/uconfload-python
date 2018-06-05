#!/usr/bin/env python3


import uconfload


args = uconfload.load_args()
config = uconfload.load_config(args.config)
uconfload.load_env(config)
print(args)
print(config)
