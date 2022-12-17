-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SGA
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SGA
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SGA` ;
USE `SGA` ;

-- -----------------------------------------------------
-- Table `SGA`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Funcionario` (
  `cpf` CHAR(11) NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `endereco` VARCHAR(120) NULL,
  `telefone` VARCHAR(11) NULL,
  `salario` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`cpf`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SGA`.`Professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Professor` (
  `cpf` CHAR(11) NOT NULL,
  `titulacao` VARCHAR(45) NOT NULL,
  `area_formacao` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `endereco` VARCHAR(120) NULL,
  `telefone` VARCHAR(11) NULL,
  `salario` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`cpf`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SGA`.`Tecnico_administrativo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Tecnico_administrativo` (
  `cpf` CHAR(11) NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `endereco` VARCHAR(120) NULL,
  `telefone` VARCHAR(11) NULL,
  `salario` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`cpf`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SGA`.`Disciplina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Disciplina` (
  `codigo` VARCHAR(8) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `carga_horaria` INT NOT NULL,
  `Curso_codigo` INT NOT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SGA`.`Curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Curso` (
  `codigo` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `duracao` INT NOT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SGA`.`Aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Aluno` (
  `cpf` CHAR(11) NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `matricula` VARCHAR(15) NOT NULL,
  `Curso_codigo` INT NOT NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE INDEX `matricula_UNIQUE` (`matricula` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
