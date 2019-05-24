DROP DATABASE IF EXISTS `logindb`;
CREATE DATABASE `logindb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `logindb`;
CREATE TABLE `usertab` (
  `login` varchar(50) NOT NULL COLLATE UTF8_bin,
  `pass` varchar(50) NOT NULL,
  PRIMARY KEY (`login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `logindb`.`usertab`
(`login`,`pass`)
VALUES ('Admin',md5('123')),('User',md5('456')),('Paul',md5('abc'));
