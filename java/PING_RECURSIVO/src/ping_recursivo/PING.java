/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ping_recursivo;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author jose.lara
 */
public class PING {

    public String host;

    public PING() {
    }

    public String ping(String host) {
        String HOST = host;
        String estado = "OFLINE";
        boolean alcanzable;
        try {

            InetAddress direccion = InetAddress.getByName(HOST);

            alcanzable = direccion.isReachable(10000);

            // System.out.println("¿El host es alcanzable?: " + alcanzable);
            if (alcanzable == true) {
                estado = "ONLINE";
            }
        } catch (IOException e) {

            estado = ("Ocurrió un error de entrada/salida: " + e.getMessage());
        }
        return estado;
    }
}
