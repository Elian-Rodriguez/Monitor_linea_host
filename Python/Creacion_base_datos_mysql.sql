CREATE SCHEMA IF NOT EXISTS `TIENDAS` DEFAULT CHARACTER SET utf8 ;
USE `TIENDAS` ;

-- -----------------------------------------------------
-- Table `TIENDAS`.`Tienda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TIENDAS`.`Tienda` ;

CREATE TABLE IF NOT EXISTS `TIENDAS`.`Tienda` (
  `Cod_ncr` INT UNSIGNED NOT NULL,
  `NOMBRE` VARCHAR(45) NOT NULL,
  `CODIGO_SAP` VARCHAR(45) NOT NULL,
  `IP_SERVER` VARCHAR(45) NOT NULL,
  `IP_PC` VARCHAR(45) NOT NULL,
  `IP_CAMARAS` VARCHAR(45) NOT NULL,
  `Abierta` TINYINT NOT NULL DEFAULT '1',
  `Estado` VARCHAR(45) NULL DEFAULT 'Ofline',
  PRIMARY KEY (`Cod_ncr`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

