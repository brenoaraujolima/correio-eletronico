package br.ufc.redes;

public class Application {

    public static void main(String[] args) {


        ChatClient chatClient = new ChatClient("127.0.0.1", 2345);
        chatClient.start();

    }

}
