
DROP DATABASE IF EXISTS `yagra`;
CREATE DATABASE IF NOT EXISTS `yagra`;
USE `yagra`;

DROP TABLE IF EXISTS `yagra_user`;
DROP TABLE IF EXISTS `yagra_session`;
DROP TABLE IF EXISTS `yagra_avatar`;

CREATE TABLE `yagra_user` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(60) NOT NULL DEFAULT '',
    `password` varchar(64) NOT NULL DEFAULT '',
    `salt` varchar(64) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    KEY `username_key` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `yagra_session` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(60) NOT NULL DEFAULT '',
    `sid` varchar(32) NOT NULL DEFAULT '',
    `last_visit_time` double unsigned NOT NULL,
    PRIMARY KEY (`id`),
    KEY `username_key` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `yagra_avatar` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `md5` varchar(32) NOT NULL DEFAULT '',
    `ext` varchar(10) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    KEY `md5_key` (`md5`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
