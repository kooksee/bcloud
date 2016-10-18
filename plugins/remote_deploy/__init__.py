# -*- coding:utf-8-*-
import getpass

import paramiko, base64

ips = ['192.168.101.237']

import paramiko


def ssh_cmd(ip, port, cmd, user, passwd):
    result = ""

    try:
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(ip, port, user, passwd, timeout=3)

        stdin, stdout, stderr = ssh.exec_command(cmd)

        result = stdout.read()

        ssh.close()

    except:

        print("ssh_cmd err.")

    return result


def test1():
    from rcontrol.ssh import SshSession, ssh_client
    from rcontrol.core import SessionManager

    node1 = ssh_client('192.168.101.237', 'barry', '123456')
    node2 = ssh_client('192.168.101.206', 'ubuntu', '123456')

    def log(task, line):
        print("%r: %s" % (task, line))

    def on_finished(task):
        print("finished (exit code: %d) !" % task.exit_code())

    def on_output(task, line):
        print line
        # print("output: %s" % line)

    with SshSession(node1) as session:
        a = session.execute("uname -a && sleep 3", on_stdout=on_output, on_finished=on_finished)
        b = session.execute("echo 123456 | sudo -S ls", on_stdout=on_output, on_finished=on_finished)
        print a.session
        print a.is_running()
        print a.error()
        print a.exit_code()
        # with SessionManager() as sessions:
        #     # create sessions on two hosts
        #     sessions.nazgul = SshSession(ssh_client('192.168.101.206', 'ubuntu', '123456'))
        #     sessions.nazgul1 = SshSession(ssh_client('192.168.101.206', 'ubuntu', '123456'))
        #
        #     # run commands in parallel
        #     sessions.nazgul1.execute("ls", on_stdout=on_output, on_finished=on_finished)
        #     sessions.nazgul1.execute("echo 123456 | sudo -S ls", on_stdout=on_output, on_finished=on_finished)


if __name__ == '__main__':
    pass

    # from rcontrol.ssh import SshSession, ssh_client
    # from rcontrol.core import SessionManager
    # from rcontrol.ssh import ssh_client, SshSession
    #
    #
    # def log(task, line):
    #     print("%r: %s" % (task, line))
    #
    #
    # sc = ssh_client('192.168.1.108', 'node1', '123456')
    #
    #
    # with SshSession(sc) as sessions:
    #     # create sessions on two hosts

    # run commands in parallel
    # sessions.execute("uname -a && sleep 3", on_stdout=log)
    # sessions.execute("uname -a && sleep 3", on_stdout=log)

    # password = getpass.getpass('Password for nide1@192.168.1.108')
    # print password

    # key = paramiko.RSAKey(data=base64.decodestring('AAA...'))

    # print key
    # print base64.decodestring('1111')


    # client = paramiko.SSHClient()
    # client.load_system_host_keys()
    # client.set_missing_host_key_policy(paramiko.WarningPolicy())
    #
    # # client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)
    # client.connect('192.168.1.108', username='node1', password='123456')
    # stdin, stdout, stderr = client.exec_command('ls')
    # for line in stdout:
    #     print '... ' + line.strip('\n')
    # client.close()

    # from openssh_wrapper import SSHConnection
    #
    # conn = SSHConnection('localhost', login='barry')
    # ret = conn.run('whoami')
    # # print ret
    # # print ret.returncode
    # # print conn.run('print "Hello world"', interpreter='python').stdout
    #
    # c = SSHConnection('192.168.101.237', login='barry')
    # print c.check_login('barry')
    # print c.run("whoami")
    # print c.run("echo 123456 | sudo -S ls")

    test1()
