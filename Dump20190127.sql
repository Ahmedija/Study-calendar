-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: studycalendar
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `calendar`
--

DROP TABLE IF EXISTS `calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `calendar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `category` varchar(45) NOT NULL,
  `description` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendar`
--

LOCK TABLES `calendar` WRITE;
/*!40000 ALTER TABLE `calendar` DISABLE KEYS */;
INSERT INTO `calendar` VALUES (1,'2018-12-01','Cooking','Today I learned how to make apple pie.'),(3,'2019-01-18','IT','Danas sam naucio kako unjeti nesto u bazu'),(4,'2019-01-18','Music','New song from Saban Saulic'),(5,'2019-01-18','Cars','Today I learne how to change tirres on car.'),(6,'2019-01-23','Driving','Today I learned how to drive a bike.'),(7,'2019-01-23','WordPress','I learned how to use elementor in WordPress.'),(9,'2018-12-29','Fishing','Learned how to catch a fish.'),(10,'2019-01-12','Programming','Learned how to connect Python with Mysql database.'),(11,'2019-01-01','GYM','Learned how to exercise.'),(12,'2019-01-25','Games','Mastered how to play GTA5'),(13,'2017-02-01','Cooking','How to make tortilas with delicious taste.'),(14,'2019-01-01','Programming','Learned how to make GUI for Java.'),(15,'2018-01-04','Driving','Learned how to drive snow bike.'),(16,'2019-01-26','Eating','Eggs'),(18,'2019-01-26','Gaming','Learned how to play Paladins.'),(19,'2019-01-19','Health','Learned on youtube how to exercise.'),(20,'2018-01-02','Skydiving','My first skydive jump.'),(21,'2019-01-27','Crafting','Learned how to make table from wood.'),(22,'2019-01-11','Mechanic','Now I konw how to change filters from air and oil in car.');
/*!40000 ALTER TABLE `calendar` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-27 15:13:16
