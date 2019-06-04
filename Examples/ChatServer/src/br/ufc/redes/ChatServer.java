package br.ufc.redes;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ChatServer {

    private int port;

    public ChatServer(int port){
        this.port = port;
    }

    public void start(){

        try {

            ServerSocket serverSocket = new ServerSocket(this.port);
            System.out.println("Iniciano o servidor no endereço "
                    + serverSocket.getInetAddress().getHostAddress()
                    + ":"
                    + serverSocket.getLocalPort());

            while(true){

                System.out.println("Aguardando conexões...");
                Socket clientSocket = serverSocket.accept();

                if(clientSocket.isConnected()){

                    System.out.println("Cliente "
                            + clientSocket.getRemoteSocketAddress()
                            + " está conectado");

                    byte[] buffer = new byte[100];
                    clientSocket.getInputStream().read(buffer);

                    String msg = new String(buffer);
                    System.out.println("Mensagem recebida: " + msg.trim());

                    clientSocket.getOutputStream().write(buffer);

                }


            }



        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
