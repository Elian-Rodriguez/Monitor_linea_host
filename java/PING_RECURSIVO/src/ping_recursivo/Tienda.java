/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ping_recursivo;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
//import Conexion_bd;
/**
 *
 * @author jose.lara
 */
public class Tienda {
    public int Cod_ncr;
    public ArrayList<Tienda> Tiendas;
    public String NOMBRE,CODIGO_SAP,IP_SERVER,IP_PC,IP_CAMARAS,Abierta,Estado;

    public Tienda(String CODIGO_SAP, String IP_SERVER) {
        this.Tiendas = new ArrayList<>();
        this.CODIGO_SAP = CODIGO_SAP;
        this.IP_SERVER = IP_SERVER;
    }

    @Override
    public String toString() {
        return "" + "Cod_ncr=" + Cod_ncr + ", NOMBRE=" + NOMBRE + ", IP_SERVER=" + IP_SERVER + ", Estado = "+ Estado +'\n';
    }

    public Tienda() {
    }

    public int getCod_ncr() {
        return Cod_ncr;
    }

    public void setCod_ncr(int Cod_ncr) {
        this.Cod_ncr = Cod_ncr;
    }

    public String getNOMBRE() {
        return NOMBRE;
    }

    public void setNOMBRE(String NOMBRE) {
        this.NOMBRE = NOMBRE;
    }

    public String getCODIGO_SAP() {
        return CODIGO_SAP;
    }

    public void setCODIGO_SAP(String CODIGO_SAP) {
        this.CODIGO_SAP = CODIGO_SAP;
    }

    public String getIP_SERVER() {
        return IP_SERVER;
    }

    public void setIP_SERVER(String IP_SERVER) {
        this.IP_SERVER = IP_SERVER;
    }

    public String getIP_PC() {
        return IP_PC;
    }

    public void setIP_PC(String IP_PC) {
        this.IP_PC = IP_PC;
    }

    public String getIP_CAMARAS() {
        return IP_CAMARAS;
    }

    public void setIP_CAMARAS(String IP_CAMARAS) {
        this.IP_CAMARAS = IP_CAMARAS;
    }

    public String getAbierta() {
        return Abierta;
    }

    public void setAbierta(String Abierta) {
        this.Abierta = Abierta;
    }

    public String getEstado() {
        return Estado;
    }

    public void setEstado(String Estado) {
        this.Estado = Estado;
    }
   
}
