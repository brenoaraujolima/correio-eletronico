import socket
import ssl


CR = b'\r'
LF = b'\n'
CRLF = CR+LF
MAX = 2048
PORT = '995'

class error_invalid(Exception): pass

class POP3:

    cod = 'UTF-8'

    def __init__(self, host, port, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.mySocket = self.createConnection(timeout)
        self.file = self.mySocket.makefile('rb')

    def createConnection(self,timeout):
        sock = socket.create_connection((self.host, self.port), timeout)
        return sock

    def user(self,user):
        return self.reducedCommand('USER %s' % user)

    def pass_(self, password):
        return self.reducedCommand('PASS %s' % password)

    def stat(self):
        returnedValue = self.reducedCommand('STAT')
        returnedString = returnedValue.split()
        print('*stat', repr(rets))
        numMsg = int (returnedString[1])
        sizeMsg = int(returnedString[2])
        return (numMsg, sizeMsg)

    def list(self, id):
        if id is not None:
            return self.reducedCommand('LIST %s' % id)
        return self.command('LIST')

    def retr(self, id):
        return self.command('RETR %s' % id)

    def dele(self, id):
        return self.reducedCommand('DELE %s' % id)

    def noop(self):
        return self.reducedCommand('NOOP')

    def quit(self):
        answer = self.reducedCommand('QUIT')
        self.close()
        return answer

    def close(self):
        try:
            file = self.file
            self.file = None
            if file is not None:
                file.close()
        finally:
            mySocket = self.mySocket
            self.mySocket = None
            if mySocket is not None:
                try:
                    mySocket.shutdown(socket.SHUT_RDWR)
                except:
                    print("Erro: Invalid Operation ")
                    return "Invalid Operation"
                finally:
                    mySocket.close()

    #Auxiliar Commands to the Server
    def reducedCommand(self, line):
        self.writeCommand(line)
        return self.answerByServer()

    def command(self, line):
        self.writeCommand(line)
        return self.textByServer()

    def writeLine(self, line):
        print('*put', repr(line))
        self.mySocket.sendall(line + CRLF)

    def writeCommand(self, line):
        print('*cmd', repr(line))
        line = bytes(line, self.cod)
        self.writeLine(line)

    def answerByServer(self):
        answer, o = self.getLine()
        print('*resp*', repr(answer))
        if not answer.startswith(b'+'):
            print ("Error: Invalid Answer")
            raise error_invalid(answer)
        return answer

    def textByServer(self):
        answer = self.answerByServer()
        list = []; octets = 0
        line, o = self.getLine()

        while line != b'.':
            if line.startswith(b'..'):
                o = o-1
                line = line[1:]
            octets = octets + o
            list.append(line)
            line, o = self.getLine()
        return answer, list, octets
    
    def getLine(self):
        line = self.file.readline(MAX + 1)
        if len(line) > MAX:
            raise error_invalid('linha excedida')

        print('*get*', repr(line))
        if not line: raise error_invalid('-ERR EOF')
        octets = len(line)
        
        if line[-2:] == CRLF:
            return line[:-2], octets
        if line[:1] == CR:
            return line[1:-1], octets
        return line[:-1], octets

class POP3_SSL(POP3):

    def __init__(self, host, port="995", keyfile=None, certfile=None,timeout=socket._GLOBAL_DEFAULT_TIMEOUT, context=None):
            if context is not None and keyfile is not None:
                raise ValueError("context and keyfile arguments are mutually exclusive")
            if context is not None and certfile is not None:
                raise ValueError("context and certfile arguments are mutually exclusive")
            if keyfile is not None or certfile is not None:
                import warnings
                warnings.warn("keyfile and certfile are deprecated, use a custom context instead", DeprecationWarning, 2)
           
            self.keyfile = keyfile
            self.certfile = certfile

            if context is None:
                context = ssl._create_stdlib_context(certfile=certfile, keyfile=keyfile)
            self.context = context
            POP3.__init__(self, host, port, timeout)

    def createConnection(self, timeout):
        sock = POP3.createConnection(self, timeout)
        sock = self.context.wrap_socket(sock,server_hostname=self.host)
        return sock

"""if __name__ == "__main__":
    user = 'breno.bal.araujo@gmail.com' 
    Mailbox = myPOP3('pop.googlemail.com', '995')
    Mailbox.user(user) 
    Mailbox.pass_("m749cob35lk") 
    (numMsgs, totalSize) = Mailbox.stat()

    for i in range(1, numMsgs + 1):
        (header, msg, octets) = Mailbox.retr(i)
        print("Message %d:" % i)
        for line in msg:
            print('   ' + line)
        print('-----------------------')
    a.quit()"""