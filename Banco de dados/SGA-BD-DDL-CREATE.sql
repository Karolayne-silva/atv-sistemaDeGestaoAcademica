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
  `titulacao` VARCHAR(45) NOT NULL,
  `area_formacao` VARCHAR(45) NOT NULL,
  `Funcionario_cpf` CHAR(11) NOT NULL,
  PRIMARY KEY (`Funcionario_cpf`),
  CONSTRAINT `fk_Professor_Funcionario`
    FOREIGN KEY (`Funcionario_cpf`)
    REFERENCES `SGA`.`Funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SGA`.`Tecnico_administrativo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Tecnico_administrativo` (
  `Funcionario_cpf` CHAR(11) NOT NULL,
  PRIMARY KEY (`Funcionario_cpf`),
  CONSTRAINT `fk_Tecnico_administrativo_Funcionario1`
    FOREIGN KEY (`Funcionario_cpf`)
    REFERENCES `SGA`.`Funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
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
-- Table `SGA`.`Disciplina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Disciplina` (
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
    REFERENCES `SGA`.`Professor` (`Funcionario_cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Disciplina_Curso1`
    FOREIGN KEY (`Curso_codigo`)
    REFERENCES `SGA`.`Curso` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
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
  UNIQUE INDEX `matricula_UNIQUE` (`matricula` ASC) VISIBLE,
  INDEX `fk_Aluno_Curso1_idx` (`Curso_codigo` ASC) VISIBLE,
  CONSTRAINT `fk_Aluno_Curso1`
    FOREIGN KEY (`Curso_codigo`)
    REFERENCES `SGA`.`Curso` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SGA`.`Periodo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SGA`.`Periodo` (
  `Disciplina_codigo` VARCHAR(8) NOT NULL,
  `Aluno_cpf` CHAR(11) NOT NULL,
  PRIMARY KEY (`Disciplina_codigo`, `Aluno_cpf`),
  INDEX `fk_Periodo_Aluno1_idx` (`Aluno_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_Periodo_Disciplina1`
    FOREIGN KEY (`Disciplina_codigo`)
    REFERENCES `SGA`.`Disciplina` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Periodo_Aluno1`
    FOREIGN KEY (`Aluno_cpf`)
    REFERENCES `SGA`.`Aluno` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `SGA`.`Funcionario`
-- -----------------------------------------------------
START TRANSACTION;
USE `SGA`;
INSERT INTO `SGA`.`Funcionario` (`cpf`, `nome`, `endereco`, `telefone`, `salario`) VALUES ('98765432154', 'Valdir Braz', 'Córrego do Tiro, 13, Santo Amaro', '81932281151', 1300.22);
INSERT INTO `SGA`.`Funcionario` (`cpf`, `nome`, `endereco`, `telefone`, `salario`) VALUES ('81956151654', 'Erika Maiara Menezes', 'Rua dos Bobos, nº 0, New Discovery', '81940028922', 1500.13);

COMMIT;


-- -----------------------------------------------------
-- Data for table `SGA`.`Professor`
-- -----------------------------------------------------
START TRANSACTION;
USE `SGA`;
INSERT INTO `SGA`.`Professor` (`titulacao`, `area_formacao`, `Funcionario_cpf`) VALUES ('Doutor', 'Ciência da Computação', '98765432154');

COMMIT;


-- -----------------------------------------------------
-- Data for table `SGA`.`Tecnico_administrativo`
-- -----------------------------------------------------
START TRANSACTION;
USE `SGA`;
INSERT INTO `SGA`.`Tecnico_administrativo` (`Funcionario_cpf`) VALUES ('81956151654');

COMMIT;


-- -----------------------------------------------------
-- Data for table `SGA`.`Curso`
-- -----------------------------------------------------
START TRANSACTION;
USE `SGA`;
INSERT INTO `SGA`.`Curso` (`codigo`, `nome`, `duracao`) VALUES (1, 'Análise e Desenvolvimento de Sistemas', 5);

COMMIT;


-- -----------------------------------------------------
-- Data for table `SGA`.`Disciplina`
-- -----------------------------------------------------
START TRANSACTION;
USE `SGA`;
INSERT INTO `SGA`.`Disciplina` (`codigo`, `nome`, `carga_horaria`, `Professor_Funcionario_cpf`, `Curso_codigo`) VALUES ('12345678', 'Coding II: Linguagens e técnicas', 60, '98765432154', 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `SGA`.`Aluno`
-- -----------------------------------------------------
START TRANSACTION;
USE `SGA`;
INSERT INTO `SGA`.`Aluno` (`cpf`, `nome`, `matricula`, `Curso_codigo`) VALUES ('21364598712', 'Antonieta Maria Gonzaga', 'ADS321654', 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `SGA`.`Periodo`
-- -----------------------------------------------------
START TRANSACTION;
USE `SGA`;
INSERT INTO `SGA`.`Periodo` (`Disciplina_codigo`, `Aluno_cpf`) VALUES ('12345678', '21364598712');

COMMIT;

