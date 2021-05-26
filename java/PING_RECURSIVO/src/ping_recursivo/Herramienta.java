/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ping_recursivo;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author jose.lara
 */
public class Herramienta {

    private ArrayList<Tienda> tiendas;
    private int tamano;

    public int getTamano() {
        return tamano;
    }

    public void setTamano(int tamano) {
        this.tamano = tamano;
    }

    public Herramienta() {
    }
    PreparedStatement ps;
    ResultSet rs;
    Connection con;
    Conexion conectar = new Conexion();
    Tienda p = new Tienda();

    Statement st;


    public ArrayList<Tienda> listar_tiendas() {
        
        ArrayList<Tienda> datos = new ArrayList<>();
        PING be = new PING();
        try {
            con = conectar.getConnection();
            ps = con.prepareStatement("SELECT Tienda.Cod_ncr,NOMBRE,IP_SERVER FROM TIENDAS.Tienda where Abierta= 1;");
            rs = ps.executeQuery();
            while (rs.next()) {

                p.setCod_ncr(rs.getInt("Cod_ncr"));
                p.setNOMBRE(rs.getString("NOMBRE"));
                p.setIP_SERVER(rs.getString("IP_SERVER"));
                p.setEstado(be.ping(p.getIP_SERVER()));

                // System.out.print(p.toString());
                Cambiar_estado(p.getEstado(), p.getCod_ncr());
                datos.add(p);
            }
        } catch (Exception e) {
        }

        this.tamano = datos.size();
        return datos;

    }

    public String Cambiar_estado(String estado, int Cod_ncr) {
        String resultado = "FALLA CON " + Cod_ncr;
        

        Tienda p = new Tienda();

        String sql = "UPDATE TIENDAS.Tienda SET Estado = '" + estado + "' WHERE (`Cod_ncr` = " + Cod_ncr + ");";
        try {
            if (estado != null || Cod_ncr >= 0) {

                st = con.createStatement();
                st.executeUpdate(sql);
                resultado = "TIENDA " + Cod_ncr + "  Modificado";

            } else {
                resultado = "Error...!!!";
            }

        } catch (Exception e) {
        }

   //     System.out.println(resultado);
        return resultado;
    }
}
