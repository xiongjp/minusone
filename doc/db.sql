
DROP DATABASE IF EXISTS `yagra`
CREATE DATABASE IF NOT EXISTS `yagra`;
USE `yagra`;

DROP TABLE IF EXISTS `yagra_user`;
DROP TABLE IF EXISTS `yagra_session`;
DROP TABLE IF EXISTS `yagra_avatar`;

CREATE TABLE `yagra_user` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(60) NOT NULL DEFAULT '',
    `passwd` varchar(64) NOT NULL DEFAULT '',
    `salt` varchar(64) NOT NULL DEFAULT '',
    PRIMARY KEY (`use_id`),
    KEY `username_key` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `yagra_session` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(60) NOT NULL DEFAULT '',
    `sid` varchar(32) NOT NULL DEFAULT '',
    `last_visit_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (`id`),
    KEY `username_key` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `yagra_avatar` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `user_id` bigint(20) unsigned NOT NULL,
    `path` varchar(32) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    KEY `path_key` (`path`),
    FOREIGN KEY (`user_id`) REFERENCES `yagra_user`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
