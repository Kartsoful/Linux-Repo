-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: exampledb
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `highscores`
--

DROP TABLE IF EXISTS `highscores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `highscores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nickname` varchar(32) NOT NULL,
  `score` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `highscores`
--

LOCK TABLES `highscores` WRITE;
/*!40000 ALTER TABLE `highscores` DISABLE KEYS */;
INSERT INTO `highscores` VALUES (1,'testi',42,'2025-11-11 11:19:23'),(2,'Kartso',3,'2025-11-11 11:29:42'),(3,'Kartso',173,'2025-11-11 11:31:10'),(4,'Kartso',12,'2025-11-11 11:33:11'),(5,'anon',7,'2025-11-11 11:35:17'),(6,'anon',36,'2025-11-11 11:35:58'),(7,'anon',57,'2025-11-11 11:37:07'),(8,'Kartso',159,'2025-11-11 11:37:41'),(9,'tyhäm peli :(',39,'2025-11-11 11:37:53'),(10,'anon',86,'2025-11-11 11:39:15'),(11,'anon',60,'2025-11-11 11:40:08'),(12,'anon',3,'2025-11-11 11:40:18'),(13,'anon',8,'2025-11-11 11:40:31'),(14,'anon',23,'2025-11-11 11:40:59'),(15,'anon',13,'2025-11-11 11:41:18'),(16,'anon',34,'2025-11-11 11:41:53'),(17,'anon',9,'2025-11-11 11:42:07'),(18,'anon',1,'2025-11-11 11:42:10'),(19,'anon',5,'2025-11-11 11:42:18'),(20,'anon',80,'2025-11-11 11:43:21'),(21,'anon',33,'2025-11-11 11:43:55'),(22,'anon',9,'2025-11-11 11:44:07'),(23,'anon',56,'2025-11-11 11:44:55'),(24,'anon',16,'2025-11-11 11:45:14'),(25,'anon',14,'2025-11-11 11:45:32'),(26,'anon',16,'2025-11-11 11:45:58'),(27,'anon',17,'2025-11-11 11:46:17'),(28,'anon',45,'2025-11-11 11:46:57'),(29,'anon',3,'2025-11-11 11:47:05'),(30,'anon',25,'2025-11-11 11:47:30'),(31,'anon',3,'2025-11-11 11:47:42'),(32,'anon',6,'2025-11-11 11:47:50'),(33,'anon',8,'2025-11-11 11:48:08'),(34,'anon',4,'2025-11-11 11:48:19'),(35,'anon',77,'2025-11-11 11:48:28'),(36,'anon',0,'2025-11-11 11:48:50'),(37,'Kartso',198,'2025-11-11 11:50:38'),(38,'anon',15,'2025-11-11 11:51:04'),(39,'anon',0,'2025-11-11 11:53:51'),(40,'anon',0,'2025-11-11 11:54:02'),(41,'anon',12,'2025-11-11 11:54:17'),(42,'Sam',0,'2025-11-11 12:00:25'),(43,'Sam',134,'2025-11-11 12:01:47'),(44,'anon',11,'2025-11-11 12:06:55'),(45,'anon',0,'2025-11-11 12:57:49'),(46,'anon',0,'2025-11-11 13:15:00'),(47,'anon',4,'2025-11-11 13:15:07'),(48,'anon',5,'2025-11-11 13:15:14'),(49,'anon',75,'2025-11-11 13:16:18'),(50,'anon',0,'2025-11-11 13:18:12'),(51,'anon',0,'2025-11-11 16:26:44'),(52,'anon',0,'2025-11-11 16:31:21'),(53,'anon',0,'2025-11-11 19:31:11'),(54,'anon',4,'2025-11-11 19:31:18'),(55,'anon',58,'2025-11-12 10:31:40'),(56,'anon',1,'2025-11-13 14:21:55'),(57,'anon',1,'2025-11-13 14:31:54'),(58,'anon',1000,'2025-11-13 14:33:06'),(59,'anon',0,'2025-11-13 16:30:14'),(60,'anon',0,'2025-11-13 16:31:02'),(61,'anon',0,'2025-11-13 16:31:09'),(62,'anon',0,'2025-11-13 16:31:15'),(63,'anon',1,'2025-11-13 16:42:33'),(64,'Täällä haisee palaneen käry',10000,'2025-11-13 16:43:10'),(65,'anon',6,'2025-11-13 23:20:21'),(66,'anon',26,'2025-11-13 23:20:50'),(67,'anon',150,'2025-11-13 23:22:50'),(68,'anon',202,'2025-11-13 23:25:41'),(69,'anon',0,'2025-11-14 12:10:24'),(70,'anon',1,'2025-11-14 12:10:26'),(71,'anon',1,'2025-11-14 12:10:29'),(72,'anon',1,'2025-11-14 12:10:36'),(73,'anon',0,'2025-11-14 12:10:38'),(74,'anon',3,'2025-11-14 12:11:03'),(75,'anon',0,'2025-11-14 12:13:04'),(76,'anon',0,'2025-11-14 12:14:29'),(77,'anon',5,'2025-11-14 12:14:47'),(78,'hax',99999,'2025-11-14 12:31:56'),(79,'Ei ole reilu peli tämä',100000,'2025-11-14 12:33:35'),(80,'anon',0,'2025-11-14 12:33:57');
/*!40000 ALTER TABLE `highscores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-14 14:30:11
