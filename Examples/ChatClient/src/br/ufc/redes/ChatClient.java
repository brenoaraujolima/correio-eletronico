package br.ufc.redes;

import java.io.IOException;
import java.net.Socket;

public class ChatClient {

    private String host;
    private int port;

    public ChatClient(String host, int port){
        this.host = host;
        this.port = port;
    }

    public void start(){

        try {

            Socket socket = new Socket(this.host, this.port);
            System.out.println("Iniciado a conexão com o servidor" +
                    socket.getRemoteSocketAddress());

            if(socket.isConnected()){

                socket.getOutputStream().write("Hello World!".getBytes());

            }


        } catch (IOException e) {
            e.printStackTrace();
        }

    }


}
