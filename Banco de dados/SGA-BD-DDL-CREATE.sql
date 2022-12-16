-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Funcionario` (
  `cpf` CHAR(11) NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `endereco` VARCHAR(120) NULL,
  `telefone` VARCHAR(11) NULL,
  `salario` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`cpf`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Professor` (
  `titulacao` VARCHAR(45) NULL,
  `area_formacao` VARCHAR(45) NULL,
  `Funcionario_cpf` CHAR(11) NOT NULL,
  PRIMARY KEY (`Funcionario_cpf`),
  CONSTRAINT `fk_Professor_Funcionario`
    FOREIGN KEY (`Funcionario_cpf`)
    REFERENCES `mydb`.`Funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`Tecnico_administrativo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Tecnico_administrativo` (
  `Funcionario_cpf` CHAR(11) NOT NULL,
  PRIMARY KEY (`Funcionario_cpf`),
  CONSTRAINT `fk_Tecnico_administrativo_Funcionario1`
    FOREIGN KEY (`Funcionario_cpf`)
    REFERENCES `mydb`.`Funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Curso` (
  `codigo` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `duracao` INT NOT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Disciplina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Disciplina` (
  `codigo` VARCHAR(8) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `carga_horaria` INT NOT NULL,
  `Professor_Funcionario_cpf` CHAR(11) NOT NULL,
  `Curso_codigo` INT NOT NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_Disciplina_Professor1_idx` (`Professor_Funcionario_cpf` ASC) VISIBLE,
  INDEX `fk_Disciplina_Curso1_idx` (`Curso_codigo` ASC) VISIBLE,
  CONSTRAINT `fk_Disciplina_Professor1`
    FOREIGN KEY (`Professor_Funcionario_cpf`)
    REFERENCES `mydb`.`Professor` (`Funcionario_cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Disciplina_Curso1`
    FOREIGN KEY (`Curso_codigo`)
    REFERENCES `mydb`.`Curso` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Aluno` (
  `cpf` CHAR(11) NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `matricula` VARCHAR(15) NOT NULL,
  `Curso_codigo` INT NOT NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE INDEX `matricula_UNIQUE` (`matricula` ASC) VISIBLE,
  INDEX `fk_Aluno_Curso1_idx` (`Curso_codigo` ASC) VISIBLE,
  CONSTRAINT `fk_Aluno_Curso1`
    FOREIGN KEY (`Curso_codigo`)
    REFERENCES `mydb`.`Curso` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
