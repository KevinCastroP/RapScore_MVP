-- MySQL dump 10.17  Distrib 10.3.22-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: rapscore_mvp
-- ------------------------------------------------------
-- Server version	10.3.22-MariaDB-1ubuntu1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `rapscore_mvp`
--

/*!40000 DROP DATABASE IF EXISTS `rapscore_mvp`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `rapscore_mvp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci */;

USE `rapscore_mvp`;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `id` int(3) NOT NULL,
  `person` int(11) NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `observations` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`,`person`),
  CONSTRAINT `address_FK` FOREIGN KEY (`id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_info`
--

DROP TABLE IF EXISTS `contact_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_info` (
  `person` int(11) NOT NULL,
  `type_contact` varchar(5) COLLATE utf8mb4_spanish_ci NOT NULL,
  `data_contact` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `description` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`person`,`type_contact`),
  CONSTRAINT `contact_info_FK` FOREIGN KEY (`person`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_info`
--

LOCK TABLES `contact_info` WRITE;
/*!40000 ALTER TABLE `contact_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `investment`
--

DROP TABLE IF EXISTS `investment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `investment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `investor` int(11) NOT NULL,
  `amount` float NOT NULL,
  `term_in_months` int(5) NOT NULL,
  `rentability` float NOT NULL,
  `status` varchar(15) COLLATE utf8mb4_spanish_ci NOT NULL,
  `investment_date` datetime DEFAULT NULL,
  `return_date` datetime NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `investment_FK` (`investor`),
  CONSTRAINT `investment_FK` FOREIGN KEY (`investor`) REFERENCES `investor` (`investor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `investment`
--

LOCK TABLES `investment` WRITE;
/*!40000 ALTER TABLE `investment` DISABLE KEYS */;
/*!40000 ALTER TABLE `investment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `investor`
--

DROP TABLE IF EXISTS `investor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `investor` (
  `investor` int(11) NOT NULL,
  `bank_name` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `type_account` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `number_account` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `date_incorporation` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`investor`),
  CONSTRAINT `investor_FK` FOREIGN KEY (`investor`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `investor`
--

LOCK TABLES `investor` WRITE;
/*!40000 ALTER TABLE `investor` DISABLE KEYS */;
/*!40000 ALTER TABLE `investor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number_request` int(11) NOT NULL,
  `amount_outlay` float NOT NULL,
  `term_in_months` int(5) NOT NULL,
  `interest_rate` float NOT NULL,
  `outlay_date` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `loan_FK` (`number_request`),
  CONSTRAINT `loan_FK` FOREIGN KEY (`number_request`) REFERENCES `request` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `type_id` varchar(5) COLLATE utf8mb4_spanish_ci NOT NULL,
  `number_identification` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `first_name` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `name_company` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `business_name` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `tradename` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `legal_status` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `legal_repre_type_id` varchar(5) COLLATE utf8mb4_spanish_ci NOT NULL,
  `legal_repre_number_id` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `legal_repre_full_name` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `born_date` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `person_FK` (`username`),
  CONSTRAINT `person_FK` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `worker` int(11) NOT NULL,
  `amount_request` float NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `type_loan` int(11) NOT NULL,
  `observations` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `request_date` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `request_FK` (`worker`),
  CONSTRAINT `request_FK` FOREIGN KEY (`worker`) REFERENCES `worker` (`worker`),
  CONSTRAINT `request_FK_1` FOREIGN KEY (`id`) REFERENCES `type_loan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_loan`
--

DROP TABLE IF EXISTS `type_loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `type_loan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `amount_min` float NOT NULL,
  `amount_max` float NOT NULL,
  `score_min` float NOT NULL,
  `interest_rate` float NOT NULL,
  `term_min` int(5) NOT NULL,
  `term_max` int(5) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_loan`
--

LOCK TABLES `type_loan` WRITE;
/*!40000 ALTER TABLE `type_loan` DISABLE KEYS */;
/*!40000 ALTER TABLE `type_loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `username` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `psswd` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `status` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `worker`
--

DROP TABLE IF EXISTS `worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `worker` (
  `worker` int(11) NOT NULL,
  `score` float NOT NULL,
  `type_vehicle` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `date_incorporation` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`worker`),
  CONSTRAINT `worker_FK` FOREIGN KEY (`worker`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `worker`
--

LOCK TABLES `worker` WRITE;
/*!40000 ALTER TABLE `worker` DISABLE KEYS */;
/*!40000 ALTER TABLE `worker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'rapscore_mvp'
--

--
-- Dumping routines for database 'rapscore_mvp'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-04  9:15:51
