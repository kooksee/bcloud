# encoding=utf-8

'''
简化版本报告部署脚本
'''

import datetime
from fabric.api import local, env, run, cd, execute
from fabric.contrib.files import exists, parallel, roles, put
from fabric.operations import sudo

# 操作一致的服务器可以放在一组，同一组的执行同一套操作
env.roledefs = {
    'test': [
        'barry@192.168.101.237'
    ]
}

env.password = '123456'
env.colorize_errors = True
env.warn_only = True

env.pty = False
env.port = 22
env.parallel = True


# env.skip_bad_hosts = True
# env.timeout = 3


# 升级python包
@roles("test")
def pip_update():
    run(
        '''
        pwd;
        ls /;
        rm -rf fabric;
        rm -rf fabricd;
        rm -rf tests;

        git clone https://github.com/fabric/fabric.git --depth=1;
        ls fabric;
        pwd
        mv fabric fabricd;
        pwd
        cp -r $(pwd)/fabricd/tests .;
        ls tests
        pwd
        sudo ls
        ls
        '''
    )


# 升级python包
@roles("test")
def task2():
    run(
        '''
        echo 123456 | sudo -S ls
        pwd;
        sudo ls
        sudo ll
        ls /;
        rm -rf fabric;
        rm -rf fabricd;
        rm -rf tests;
        ls

        pwd
        sudo touch kkkk
        ls | grep kkkk
        '''
    )


if __name__ == '__main__':
    # execute(pip_update)
    execute(task2)
