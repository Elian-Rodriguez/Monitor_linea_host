/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ping_recursivo;

import java.io.IOException;
import java.net.InetAddress;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author jose.lara
 */
public class PING_RECURSIVO {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        PING be = new PING();
        be.ping("10.26.1.161");
        String val = (be.ping("10.26.1.161"));
        if (val.equals("ONLINE"))
        {
        Herramienta beta = new Herramienta();
        beta.listar_tiendas();
        System.out.println("Finalizo , TIENDAS CONSULTADAS "+beta.getTamano());
        }
        else{
            System.out.println("No se tiene conexion al SRV MYSQL");
        }
    }
}
/*
CREATE USER 'bart'@'%' IDENTIFIED BY 'Linux-1234';
CREATE USER 'lisa'@'%'  IDENTIFIED BY 'Linux-1234';
CREATE USER 'homero'@'%' IDENTIFIED BY 'Linux-1234';

GRANT ALL PRIVILEGES ON * . * TO 'lisa'@'%';
GRANT ALL PRIVILEGES ON * . * TO 'bart'@'%';
FLUSH PRIVILEGES ON * . * TO 'homero'@'%';
FLUSH PRIVILEGES;
Koba06

ALTER USER 'bart'@'%' IDENTIFIED WITH mysql_native_password BY 'Linux-1234';
ALTER USER 'lisa'@'%' IDENTIFIED WITH mysql_native_password BY 'Linux-1234';
ALTER USER 'homero'@'%' IDENTIFIED WITH mysql_native_password BY 'Linux-1234';
*/

/*
UPDATE `TIENDAS`.`Tienda` SET `Estado` = 'Online' WHERE (`Cod_ncr` = '1');
*/