package br.ufc.redes;

public class Application {

    public static void main(String[] args) {

        ChatServer server = new ChatServer(2345);
        server.start();


    }

}
