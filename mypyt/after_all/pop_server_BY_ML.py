import poplib, getpass, sys

mailserver = 'There is need to get name mail server pop :)'
mailuser = 'There is need to get user\'s name :)'
mailpasswd = getpass.getpass('Password for %s?' % mailserver)

print('Connecting...')
server = poplib.POP3(mailserver)
server.user(mailuser)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    masgCount, mboxSize = server.stat()
    print('There are', msgCount, 'mail messages, size ', mboxSize)
    msginfo = server.list()
    print(msginfo)
    for i in range(msgCount):
        msgnum = i+1
        msgsize = msginfo[1][i].split()[1]
        resp, hdrlines, octets = server.top(msgnum, 0)
        print('-' * 80)
        print('[%d: octets = %d, size = %s]' % (msgnum, octets, msgsize))
        for line in hdrlines: print(line)

        if input('Print?(y)') in ['y', 'Y']:
            for line in server.retr(msgnum)[1]: print(line)
        if input('Delete?(y)') in ['y', 'Y']:
            print('deleting')
            server.dele(msgnum)
        else:
            print('skipping')
finally:
    server.quit()
raw_input('Bye.')
                 
