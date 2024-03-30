-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: suyuan
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add mineral development model',7,'add_mineraldevelopmentmodel'),(26,'Can change mineral development model',7,'change_mineraldevelopmentmodel'),(27,'Can delete mineral development model',7,'delete_mineraldevelopmentmodel'),(28,'Can view mineral development model',7,'view_mineraldevelopmentmodel'),(29,'Can add regional resource facilities model',8,'add_regionalresourcefacilitiesmodel'),(30,'Can change regional resource facilities model',8,'change_regionalresourcefacilitiesmodel'),(31,'Can delete regional resource facilities model',8,'delete_regionalresourcefacilitiesmodel'),(32,'Can view regional resource facilities model',8,'view_regionalresourcefacilitiesmodel'),(33,'Can add national energy import and export model',9,'add_nationalenergyimportandexportmodel'),(34,'Can change national energy import and export model',9,'change_nationalenergyimportandexportmodel'),(35,'Can delete national energy import and export model',9,'delete_nationalenergyimportandexportmodel'),(36,'Can view national energy import and export model',9,'view_nationalenergyimportandexportmodel'),(37,'Can add national power generation installed capacity model',10,'add_nationalpowergenerationinstalledcapacitymodel'),(38,'Can change national power generation installed capacity model',10,'change_nationalpowergenerationinstalledcapacitymodel'),(39,'Can delete national power generation installed capacity model',10,'delete_nationalpowergenerationinstalledcapacitymodel'),(40,'Can view national power generation installed capacity model',10,'view_nationalpowergenerationinstalledcapacitymodel'),(41,'Can add national energy production and inventory',11,'add_nationalenergyproductionandinventory'),(42,'Can change national energy production and inventory',11,'change_nationalenergyproductionandinventory'),(43,'Can delete national energy production and inventory',11,'delete_nationalenergyproductionandinventory'),(44,'Can view national energy production and inventory',11,'view_nationalenergyproductionandinventory'),(45,'Can add national energy production and inventory model',12,'add_nationalenergyproductionandinventorymodel'),(46,'Can change national energy production and inventory model',12,'change_nationalenergyproductionandinventorymodel'),(47,'Can delete national energy production and inventory model',12,'delete_nationalenergyproductionandinventorymodel'),(48,'Can view national energy production and inventory model',12,'view_nationalenergyproductionandinventorymodel'),(49,'Can add energy import and export model',9,'add_energyimportandexportmodel'),(50,'Can change energy import and export model',9,'change_energyimportandexportmodel'),(51,'Can delete energy import and export model',9,'delete_energyimportandexportmodel'),(52,'Can view energy import and export model',9,'view_energyimportandexportmodel'),(53,'Can add energy production and inventory model',12,'add_energyproductionandinventorymodel'),(54,'Can change energy production and inventory model',12,'change_energyproductionandinventorymodel'),(55,'Can delete energy production and inventory model',12,'delete_energyproductionandinventorymodel'),(56,'Can view energy production and inventory model',12,'view_energyproductionandinventorymodel'),(57,'Can add power generation installed capacity model',10,'add_powergenerationinstalledcapacitymodel'),(58,'Can change power generation installed capacity model',10,'change_powergenerationinstalledcapacitymodel'),(59,'Can delete power generation installed capacity model',10,'delete_powergenerationinstalledcapacitymodel'),(60,'Can view power generation installed capacity model',10,'view_powergenerationinstalledcapacitymodel'),(61,'Can add api request',13,'add_apirequest'),(62,'Can change api request',13,'change_apirequest'),(63,'Can delete api request',13,'delete_apirequest'),(64,'Can view api request',13,'view_apirequest'),(65,'Can add energy consumption model',14,'add_energyconsumptionmodel'),(66,'Can change energy consumption model',14,'change_energyconsumptionmodel'),(67,'Can delete energy consumption model',14,'delete_energyconsumptionmodel'),(68,'Can view energy consumption model',14,'view_energyconsumptionmodel'),(69,'Can add main energy production',15,'add_mainenergyproduction'),(70,'Can change main energy production',15,'change_mainenergyproduction'),(71,'Can delete main energy production',15,'delete_mainenergyproduction'),(72,'Can view main energy production',15,'view_mainenergyproduction'),(73,'Can add main energy production model',15,'add_mainenergyproductionmodel'),(74,'Can change main energy production model',15,'change_mainenergyproductionmodel'),(75,'Can delete main energy production model',15,'delete_mainenergyproductionmodel'),(76,'Can view main energy production model',15,'view_mainenergyproductionmodel'),(77,'Can add electric field fault model',16,'add_electricfieldfaultmodel'),(78,'Can change electric field fault model',16,'change_electricfieldfaultmodel'),(79,'Can delete electric field fault model',16,'delete_electricfieldfaultmodel'),(80,'Can view electric field fault model',16,'view_electricfieldfaultmodel'),(81,'Can add electric field model',17,'add_electricfieldmodel'),(82,'Can change electric field model',17,'change_electricfieldmodel'),(83,'Can delete electric field model',17,'delete_electricfieldmodel'),(84,'Can view electric field model',17,'view_electricfieldmodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$ziwDfjBKQCF6meW0T9rvLU$AoEYxn+3FEOI1wS/spwc4TGwFphWcrsN6GcXuVSCH/U=','2024-03-26 23:20:54.692642',1,'Li','','','',1,1,'2024-03-17 13:19:00.000000'),(2,'pbkdf2_sha256$720000$nwysS9Seg3e5UtOBbMTvua$4pynNa9NVQH47PQIMl6zTYbmvZDAlivDbLB9L94l2Uo=','2024-03-25 20:52:14.545035',1,'admin','','','',1,1,'2024-03-25 17:36:55.004381');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-03-17 13:40:36.873475','1','2010',1,'[{\"added\": {}}]',9,1),(2,'2024-03-17 13:40:53.444160','2','2015',1,'[{\"added\": {}}]',9,1),(3,'2024-03-17 13:41:08.911785','3','2019',1,'[{\"added\": {}}]',9,1),(4,'2024-03-17 13:41:21.057546','4','2020',1,'[{\"added\": {}}]',9,1),(5,'2024-03-17 13:41:37.034824','5','2021',1,'[{\"added\": {}}]',9,1),(6,'2024-03-17 13:41:44.429358','4','2020',2,'[{\"changed\": {\"fields\": [\"\\u53ef\\u4f9b\\u6d88\\u8d39\\u7684\\u80fd\\u6e90\\u603b\\u91cf\"]}}]',9,1),(7,'2024-03-17 13:42:10.342572','1','2010',2,'[{\"changed\": {\"fields\": [\"\\u77f3\\u6cb9\", \"\\u7164\\u70ad\"]}}]',9,1),(8,'2024-03-17 13:42:34.188989','2','2015',2,'[{\"changed\": {\"fields\": [\"\\u77f3\\u6cb9\", \"\\u77f3\\u6cb9\"]}}]',9,1),(9,'2024-03-17 13:42:39.798254','1','2010',2,'[{\"changed\": {\"fields\": [\"\\u7164\\u70ad\", \"\\u77f3\\u6cb9\"]}}]',9,1),(10,'2024-03-17 13:42:53.583130','3','2019',2,'[{\"changed\": {\"fields\": [\"\\u77f3\\u6cb9\", \"\\u77f3\\u6cb9\"]}}]',9,1),(11,'2024-03-17 13:43:11.374963','4','2020',2,'[{\"changed\": {\"fields\": [\"\\u77f3\\u6cb9\", \"\\u77f3\\u6cb9\"]}}]',9,1),(12,'2024-03-17 13:43:22.827483','5','2021',2,'[{\"changed\": {\"fields\": [\"\\u77f3\\u6cb9\", \"\\u77f3\\u6cb9\"]}}]',9,1),(13,'2024-03-17 13:44:00.372134','1','2010',2,'[{\"changed\": {\"fields\": [\"\\u7164\\u70ad\", \"\\u7164\\u70ad\"]}}]',9,1),(14,'2024-03-17 13:44:10.028496','2','2015',2,'[{\"changed\": {\"fields\": [\"\\u7164\\u70ad\", \"\\u7164\\u70ad\"]}}]',9,1),(15,'2024-03-17 13:44:18.567364','3','2019',2,'[{\"changed\": {\"fields\": [\"\\u7164\\u70ad\", \"\\u7164\\u70ad\"]}}]',9,1),(16,'2024-03-17 13:44:27.629045','4','2020',2,'[{\"changed\": {\"fields\": [\"\\u7164\\u70ad\", \"\\u7164\\u70ad\"]}}]',9,1),(17,'2024-03-17 13:44:30.856161','4','2020',2,'[]',9,1),(18,'2024-03-17 13:44:41.937279','5','2021',2,'[{\"changed\": {\"fields\": [\"\\u7164\\u70ad\", \"\\u7164\\u70ad\"]}}]',9,1),(19,'2024-03-17 13:45:12.141392','1','2010',2,'[{\"changed\": {\"fields\": [\"\\u7535\\u529b\", \"\\u7535\\u529b\"]}}]',9,1),(20,'2024-03-17 13:45:19.563332','2','2015',2,'[{\"changed\": {\"fields\": [\"\\u7535\\u529b\", \"\\u7535\\u529b\"]}}]',9,1),(21,'2024-03-17 13:45:26.808569','3','2019',2,'[{\"changed\": {\"fields\": [\"\\u7535\\u529b\", \"\\u7535\\u529b\"]}}]',9,1),(22,'2024-03-17 13:45:33.796274','4','2020',2,'[{\"changed\": {\"fields\": [\"\\u7535\\u529b\", \"\\u7535\\u529b\"]}}]',9,1),(23,'2024-03-17 13:45:41.467384','5','2021',2,'[{\"changed\": {\"fields\": [\"\\u7535\\u529b\", \"\\u7535\\u529b\"]}}]',9,1),(24,'2024-03-18 12:40:53.995842','1','2018年发电装机容量',1,'[{\"added\": {}}]',10,1),(25,'2024-03-18 12:57:11.633998','2','2019年发电装机容量',1,'[{\"added\": {}}]',10,1),(26,'2024-03-18 12:57:41.070817','3','2020年发电装机容量',1,'[{\"added\": {}}]',10,1),(27,'2024-03-18 12:58:07.268353','4','2021年发电装机容量',1,'[{\"added\": {}}]',10,1),(28,'2024-03-18 12:58:36.775024','5','2022年发电装机容量',1,'[{\"added\": {}}]',10,1),(29,'2024-03-21 08:48:24.146628','1','2010年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(30,'2024-03-21 08:48:38.160007','2','2015年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(31,'2024-03-21 08:48:53.924222','3','2019年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(32,'2024-03-21 08:49:11.357779','4','2020年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(33,'2024-03-21 08:49:24.507928','5','2021年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(34,'2024-03-25 19:06:59.277324','6','2018年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(35,'2024-03-25 19:07:06.154682','6','2018年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(36,'2024-03-25 19:07:10.983185','7','2017年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(37,'2024-03-25 19:07:15.823406','7','2017年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u53ef\\u4f9b\\u6d88\\u8d39\\u7684\\u80fd\\u6e90\\u603b\\u91cf\"]}}]',12,1),(38,'2024-03-25 19:10:22.287202','6','2018年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u53ef\\u4f9b\\u6d88\\u8d39\\u7684\\u80fd\\u6e90\\u603b\\u91cf\", \"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(39,'2024-03-25 19:12:20.715886','7','2017年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u53ef\\u4f9b\\u6d88\\u8d39\\u7684\\u80fd\\u6e90\\u603b\\u91cf\", \"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(40,'2024-03-25 19:13:54.696980','5','2021年 - 能源平衡总和',2,'[]',12,1),(41,'2024-03-25 19:13:58.326570','8','2022年 - 能源平衡总和',1,'[{\"added\": {}}]',12,1),(42,'2024-03-25 19:14:09.251530','8','2022年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(43,'2024-03-25 19:20:26.227679','8','2022年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u53ef\\u4f9b\\u6d88\\u8d39\\u7684\\u80fd\\u6e90\\u603b\\u91cf\", \"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(44,'2024-03-25 19:21:37.366038','8','2022年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(45,'2024-03-25 19:23:15.663947','6','2018年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(46,'2024-03-25 19:24:13.227591','5','2021年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(47,'2024-03-25 19:24:45.302187','5','2021年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(48,'2024-03-25 19:25:03.769833','8','2022年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(49,'2024-03-25 19:25:35.222042','8','2022年 - 能源平衡总和',2,'[]',12,1),(50,'2024-03-25 19:25:54.125716','5','2021年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(51,'2024-03-25 19:26:43.282263','7','2017年 - 能源平衡总和',2,'[{\"changed\": {\"fields\": [\"\\u4e00\\u6b21\\u80fd\\u6e90\\u751f\\u4ea7\\u603b\\u91cf\"]}}]',12,1),(52,'2024-03-25 20:02:04.166945','1','2000年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(53,'2024-03-25 20:02:22.056808','2','2001年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(54,'2024-03-25 20:02:40.272588','3','2002年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(55,'2024-03-25 20:02:59.072305','4','2003年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(56,'2024-03-25 20:03:12.168150','5','2004年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(57,'2024-03-25 20:03:36.169105','6','2005年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(58,'2024-03-25 20:03:55.273509','7','2006年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(59,'2024-03-25 20:04:08.468155','8','2007年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(60,'2024-03-25 20:04:26.381455','9','2008年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(61,'2024-03-25 20:04:41.856831','10','2009年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(62,'2024-03-25 20:05:01.292437','11','2010年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(63,'2024-03-25 20:05:24.035463','12','2011年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(64,'2024-03-25 20:05:50.683132','13','2012年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(65,'2024-03-25 20:06:08.947252','14','2013年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(66,'2024-03-25 20:06:40.115976','15','2014年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(67,'2024-03-25 20:07:02.383439','16','2015年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(68,'2024-03-25 20:07:20.676803','17','2016年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(69,'2024-03-25 20:07:42.065258','18','2017年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(70,'2024-03-25 20:07:56.851773','19','2018年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(71,'2024-03-25 20:08:19.522558','20','2019年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(72,'2024-03-25 20:08:39.983064','21','2020年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(73,'2024-03-25 20:09:10.851748','22','2021年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(74,'2024-03-25 20:09:33.918755','23','2022年 - 能源消耗水平',1,'[{\"added\": {}}]',14,1),(75,'2024-03-25 20:50:08.798804','1','Li',2,'[{\"changed\": {\"fields\": [\"Superuser status\", \"Last login\"]}}]',4,1),(76,'2024-03-25 20:52:23.315820','1','Li',2,'[{\"changed\": {\"fields\": [\"Superuser status\"]}}]',4,2),(77,'2024-03-26 21:42:07.075630','1','安徽 - 2023 - 规模以上企业主要能源产量',1,'[{\"added\": {}}]',15,1),(78,'2024-03-26 21:50:03.098448','1','安徽 - 2023 - 规模以上企业主要能源产量',2,'[{\"changed\": {\"fields\": [\"\\u539f\\u7164\", \"\\u539f\\u6cb9\"]}}]',15,1),(79,'2024-03-26 21:50:14.625351','1','安徽 - 2023 - 规模以上企业主要能源产量',2,'[]',15,1),(80,'2024-03-26 22:09:21.714832','2','安徽 - 2022 - 规模以上企业主要能源产量',1,'[{\"added\": {}}]',15,1),(81,'2024-03-26 22:15:57.352398','2','安徽 - 2022 - 规模以上企业主要能源产量',2,'[]',15,1),(82,'2024-03-27 01:17:15.480061','2','安徽 - 2022 - 规模以上企业主要能源产量',2,'[{\"changed\": {\"fields\": [\"\\u539f\\u6cb9\"]}}]',15,1),(83,'2024-03-27 01:55:00.045736','3','安徽 - 2021 - 规模以上企业主要能源产量',1,'[{\"added\": {}}]',15,1),(84,'2024-03-27 01:57:46.116892','3','安徽 - 2021 - 规模以上企业主要能源产量',2,'[{\"changed\": {\"fields\": [\"\\u706b\\u529b\\u53d1\\u7535\\u91cf\", \"\\u6c34\\u529b\\u53d1\\u7535\\u91cf\", \"\\u98ce\\u529b\\u53d1\\u7535\\u91cf\", \"\\u592a\\u9633\\u80fd\\u53d1\\u7535\\u91cf\", \"\\u6838\\u80fd\\u53d1\\u7535\\u91cf\", \"\\u603b\\u53d1\\u7535\\u91cf\"]}}]',15,1),(85,'2024-03-27 02:01:26.113702','4','安徽 - 2020 - 规模以上企业主要能源产量',1,'[{\"added\": {}}]',15,1),(86,'2024-03-27 02:09:24.892314','5','安徽 - 2019 - 规模以上企业主要能源产量',1,'[{\"added\": {}}]',15,1),(87,'2024-03-27 02:11:17.775549','6','安徽 - 2018 - 规模以上企业主要能源产量',1,'[{\"added\": {}}]',15,1),(88,'2024-03-27 22:14:05.216885','1','淮南市 - 2024-03-27 22:14:05.215886 - 潘集发电 - 故障信息',1,'[{\"added\": {}}]',16,1),(89,'2024-03-27 22:15:31.477383','1','淮南市 - 2024-03-27 22:15:31.477383 - 潘集发电',1,'[{\"added\": {}}]',17,1),(90,'2024-03-27 22:16:52.962466','2','合肥市 - 皖能电力 - 2024-03-27 22:16:52.962466',1,'[{\"added\": {}}]',17,1),(91,'2024-03-27 22:19:19.733705','3','安庆市 - 中节股份 - 2024-03-27 22:19:19.733705',1,'[{\"added\": {}}]',17,1),(92,'2024-03-27 22:21:42.253293','4','马鞍山市 - 马鞍山经纬回转支承 - 2024-03-27 22:21:42.253293',1,'[{\"added\": {}}]',17,1),(93,'2024-03-27 22:22:09.493367','5','合肥市 - 阳光电源 - 2024-03-27 22:22:09.492367',1,'[{\"added\": {}}]',17,1),(94,'2024-03-27 22:23:20.424792','6','合肥市 - 森永新能源 - 2024-03-27 22:23:20.423792',1,'[{\"added\": {}}]',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(16,'renew','electricfieldfaultmodel'),(17,'renew','electricfieldmodel'),(15,'renew','mainenergyproductionmodel'),(6,'sessions','session'),(13,'SuYuanApplication','apirequest'),(14,'SuYuanApplication','energyconsumptionmodel'),(9,'SuYuanApplication','energyimportandexportmodel'),(12,'SuYuanApplication','energyproductionandinventorymodel'),(7,'SuYuanApplication','mineraldevelopmentmodel'),(11,'SuYuanApplication','nationalenergyproductionandinventory'),(10,'SuYuanApplication','powergenerationinstalledcapacitymodel'),(8,'SuYuanApplication','regionalresourcefacilitiesmodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'SuYuanApplication','0001_initial','2024-03-17 13:18:28.880800'),(2,'SuYuanApplication','0002_nationalenergyimportandexportmodel_delete_filemodel_and_more','2024-03-17 13:18:29.029798'),(3,'contenttypes','0001_initial','2024-03-17 13:18:29.091799'),(4,'auth','0001_initial','2024-03-17 13:18:30.138797'),(5,'admin','0001_initial','2024-03-17 13:18:30.398799'),(6,'admin','0002_logentry_remove_auto_add','2024-03-17 13:18:30.414799'),(7,'admin','0003_logentry_add_action_flag_choices','2024-03-17 13:18:30.422797'),(8,'contenttypes','0002_remove_content_type_name','2024-03-17 13:18:30.532800'),(9,'auth','0002_alter_permission_name_max_length','2024-03-17 13:18:30.642798'),(10,'auth','0003_alter_user_email_max_length','2024-03-17 13:18:30.668797'),(11,'auth','0004_alter_user_username_opts','2024-03-17 13:18:30.676797'),(12,'auth','0005_alter_user_last_login_null','2024-03-17 13:18:30.757797'),(13,'auth','0006_require_contenttypes_0002','2024-03-17 13:18:30.761797'),(14,'auth','0007_alter_validators_add_error_messages','2024-03-17 13:18:30.776799'),(15,'auth','0008_alter_user_username_max_length','2024-03-17 13:18:30.859797'),(16,'auth','0009_alter_user_last_name_max_length','2024-03-17 13:18:30.981797'),(17,'auth','0010_alter_group_name_max_length','2024-03-17 13:18:31.005797'),(18,'auth','0011_update_proxy_permissions','2024-03-17 13:18:31.015797'),(19,'auth','0012_alter_user_first_name_max_length','2024-03-17 13:18:31.109797'),(20,'sessions','0001_initial','2024-03-17 13:18:31.167797'),(21,'SuYuanApplication','0003_nationalenergyimportandexportmodel_coal_and_more','2024-03-17 13:30:41.729781'),(22,'SuYuanApplication','0004_alter_nationalenergyimportandexportmodel_options_and_more','2024-03-17 13:37:17.563232'),(23,'SuYuanApplication','0005_nationalenergyimportandexportmodel_all_e_and_more','2024-03-17 13:39:48.486421'),(24,'SuYuanApplication','0006_alter_nationalenergyimportandexportmodel_all_i','2024-03-17 13:40:01.454859'),(25,'SuYuanApplication','0007_nationalpowergenerationinstalledcapacitymodel_and_more','2024-03-18 12:29:22.531936'),(26,'SuYuanApplication','0008_nationalenergyproductionandinventory','2024-03-21 08:11:03.634106'),(27,'SuYuanApplication','0009_nationalenergyproductionandinventorymodel_and_more','2024-03-21 08:30:40.213855'),(28,'SuYuanApplication','0010_remove_nationalenergyproductionandinventorymodel_thermal_power_and_more','2024-03-21 08:39:50.464827'),(29,'SuYuanApplication','0011_alter_mineraldevelopmentmodel_year_and_more','2024-03-21 08:40:53.150116'),(30,'SuYuanApplication','0012_rename_nationalenergyimportandexportmodel_energyimportandexportmodel_and_more','2024-03-21 08:43:56.034795'),(31,'SuYuanApplication','0013_apirequest','2024-03-24 12:13:39.013309'),(32,'SuYuanApplication','0014_alter_apirequest_request_time','2024-03-25 05:20:33.666214'),(33,'SuYuanApplication','0015_energyimportandexportmodel_created_at_and_more','2024-03-25 15:52:25.449512'),(34,'SuYuanApplication','0016_rename_request_time_apirequest_created_at','2024-03-25 15:53:22.335181'),(35,'SuYuanApplication','0017_rename_created_at_apirequest_request_time','2024-03-25 15:59:45.054387'),(36,'SuYuanApplication','0002_energyconsumptionmodel','2024-03-25 19:57:24.527435'),(37,'SuYuanApplication','0003_energyconsumptionmodel_power_and_other','2024-03-25 20:00:48.707356'),(38,'SuYuanApplication','0004_rename_total_energy_available_for_consumption_energyconsumptionmodel_total_energy_consumption','2024-03-25 20:21:52.112807'),(39,'renew','0001_initial','2024-03-26 18:54:41.818881'),(40,'renew','0002_rename_mainenergyproduction_mainenergyproductionmodel','2024-03-26 18:55:31.540763'),(41,'renew','0003_alter_mainenergyproductionmodel_options_and_more','2024-03-26 21:39:31.590701'),(42,'SuYuanApplication','0005_alter_mineraldevelopmentmodel_region_and_more','2024-03-27 22:01:40.906573'),(43,'renew','0002_electricfieldmodel_delete_electricfieldfaultmodel','2024-03-27 22:15:15.862710'),(44,'renew','0003_alter_electricfieldmodel_station_type','2024-03-27 22:16:35.284154');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2k7o5jy5pks5nf25vxeta3f445m7he80','.eJxVjDsOwjAQRO_iGln-LcGU9DmDtfaucQDZUpxUiLuTSCmgG817M28RcF1KWDvPYSJxFUacfruI6cl1B_TAem8ytbrMU5S7Ig_a5diIX7fD_Tso2Mu2TvaibOaz1y4m0JiNJZc9ZE3WKCZw1mmDPGRPHr2HYcvaKIiKmS2Izxfg5TfT:1rohSU:FJ-RpsLHpqLWz3okTIY64QPpZqvHWznq9AKbhnJa3aw','2024-04-08 18:21:38.705475'),('j55sweqvve7x2re5csvuv58ogjae0i6b','.eJxVjDsOwyAQRO9CHSGw-KZMnzOghWWDkwgkY1dW7h4juUiqkWbevJ0F2NYStp6XMCO7Mskuv12E9Mp1DPiE-mg8tbouc-QD4efa-b1hft9O9k9QoJfjTUJbTCgFOaPRT2BIoU82SSFR6UOkSGorZI4EZoSzzpPTHiBNFNnnC_QHOJI:1rohVu:RlMreOOTMtW7hzoJVjPQqBojX_qhBwXKGfnHTZtPNVI','2024-04-08 18:25:10.945841'),('nc6mvz7cv5x1qcdpaqvl6u5mo1voahog','.eJxVjDsOwyAQRO9CHSGw-KZMnzOghWWDkwgkY1dW7h4juUiqkWbevJ0F2NYStp6XMCO7Mskuv12E9Mp1DPiE-mg8tbouc-QD4efa-b1hft9O9k9QoJfjTUJbTCgFOaPRT2BIoU82SSFR6UOkSGorZI4EZoSzzpPTHiBNFNnnC_QHOJI:1rojo0:zdHCPxjg4MWIpWaGb3cho_ZSVpsY0LED4zBkZF-MMh0','2024-04-08 20:52:00.843228'),('r0v4xjgcutoa8km5x2c7juoesroj7a1j','.eJxVjDsOwyAQRO9CHSGw-KZMnzOghWWDkwgkY1dW7h4juUiqkWbevJ0F2NYStp6XMCO7Mskuv12E9Mp1DPiE-mg8tbouc-QD4efa-b1hft9O9k9QoJfjTUJbTCgFOaPRT2BIoU82SSFR6UOkSGorZI4EZoSzzpPTHiBNFNnnC_QHOJI:1rp8be:AkLCPYkcqnEOf7xCEKTzDnYmI6W7vaX75jCrr6BVt7k','2024-04-09 23:20:54.701618'),('tily80h5utw3h3t9ymj40e51zdbfm7sw','.eJxVjDsOwyAQRO9CHSGw-KZMnzOghWWDkwgkY1dW7h4juUiqkWbevJ0F2NYStp6XMCO7Mskuv12E9Mp1DPiE-mg8tbouc-QD4efa-b1hft9O9k9QoJfjTUJbTCgFOaPRT2BIoU82SSFR6UOkSGorZI4EZoSzzpPTHiBNFNnnC_QHOJI:1rojoW:z09cZRpkMjCG-Wmj1wc-jXAlDFnhe6Q3CESEgoNVMA8','2024-04-08 20:52:32.997960');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renew_electricfieldmodel`
--

DROP TABLE IF EXISTS `renew_electricfieldmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renew_electricfieldmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `province` varchar(100) DEFAULT NULL,
  `station_type` varchar(100) NOT NULL,
  `station_name` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renew_electricfieldmodel`
--

LOCK TABLES `renew_electricfieldmodel` WRITE;
/*!40000 ALTER TABLE `renew_electricfieldmodel` DISABLE KEYS */;
INSERT INTO `renew_electricfieldmodel` VALUES (1,'淮南','火力发电','潘集发电','2024-03-27 22:15:31.477383'),(2,'合肥','综合性发电','皖能电力','2024-03-27 22:16:52.962466'),(3,'安庆','火力发电','中节股份','2024-03-27 22:19:19.733705'),(4,'马鞍山','风力发电','马鞍山经纬回转支承','2024-03-27 22:21:42.253293'),(5,'合肥','综合性发电','阳光电源','2024-03-27 22:22:09.492367'),(6,'合肥','太阳能发电','森永新能源','2024-03-27 22:23:20.423792');
/*!40000 ALTER TABLE `renew_electricfieldmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renew_mainenergyproductionmodel`
--

DROP TABLE IF EXISTS `renew_mainenergyproductionmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renew_mainenergyproductionmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `region` varchar(100) NOT NULL,
  `year` int NOT NULL,
  `raw_coal` decimal(10,1) NOT NULL,
  `crude_oil` decimal(10,1) NOT NULL,
  `fire_power` decimal(10,1) NOT NULL,
  `water_power` decimal(10,1) NOT NULL,
  `wind_power` decimal(10,1) NOT NULL,
  `sun_power` decimal(10,1) NOT NULL,
  `all_power` decimal(10,1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `nuclear_power` decimal(10,1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `year` (`year`),
  UNIQUE KEY `renew_mainenergyproduction_year_region_efbe7d90_uniq` (`year`,`region`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renew_mainenergyproductionmodel`
--

LOCK TABLES `renew_mainenergyproductionmodel` WRITE;
/*!40000 ALTER TABLE `renew_mainenergyproductionmodel` DISABLE KEYS */;
INSERT INTO `renew_mainenergyproductionmodel` VALUES (1,'安徽',2023,11285.8,773.4,3033.0,68.0,123.4,111.2,3335.6,'2024-03-26 21:42:07.075630',0.0),(2,'安徽',2022,11176.9,579.0,2882.9,52.8,101.9,97.3,3134.9,'2024-03-26 22:09:21.714832',0.0),(3,'安徽',2021,11274.1,752.0,2690.3,55.7,85.6,80.3,2911.9,'2024-03-27 01:55:00.044738',0.0),(4,'安徽',2020,11084.4,330.7,2527.3,40.7,47.0,66.7,2681.6,'2024-03-27 02:01:26.113191',0.0),(5,'安徽',2019,10988.4,658.1,2637.2,30.0,42.4,59.8,2769.4,'2024-03-27 02:09:24.892314',0.0),(6,'安徽',2018,11529.1,727.6,2491.3,35.2,45.2,51.1,2622.8,'2024-03-27 02:11:17.774551',0.0);
/*!40000 ALTER TABLE `renew_mainenergyproductionmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renew_powergenerationmodel`
--

DROP TABLE IF EXISTS `renew_powergenerationmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renew_powergenerationmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `region` varchar(100) NOT NULL,
  `year` int NOT NULL,
  `fire` decimal(8,1) NOT NULL,
  `wind` decimal(8,1) NOT NULL,
  `water` decimal(8,1) NOT NULL,
  `solar` decimal(8,1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `all` decimal(8,1) NOT NULL,
  `all_increase` decimal(3,1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `year` (`year`),
  UNIQUE KEY `renew_powergenerationmodel_region_year_d81d2154_uniq` (`region`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renew_powergenerationmodel`
--

LOCK TABLES `renew_powergenerationmodel` WRITE;
/*!40000 ALTER TABLE `renew_powergenerationmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `renew_powergenerationmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suyuanapplication_apirequest`
--

DROP TABLE IF EXISTS `suyuanapplication_apirequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suyuanapplication_apirequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `path` varchar(255) NOT NULL,
  `request_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=988 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suyuanapplication_apirequest`
--

LOCK TABLES `suyuanapplication_apirequest` WRITE;
/*!40000 ALTER TABLE `suyuanapplication_apirequest` DISABLE KEYS */;
INSERT INTO `suyuanapplication_apirequest` VALUES (605,'/api/energyproandinvnt/','2024-03-25 18:45:07.498601'),(606,'/api/rscefacilt/13/','2024-03-25 18:45:10.948827'),(607,'/api/energyproandinvnt/','2024-03-25 18:45:57.652432'),(608,'/api/rscefacilt/13/','2024-03-25 18:46:46.720613'),(609,'/api/energyproandinvnt/','2024-03-25 18:49:25.224831'),(610,'/api/rscefacilt/13/','2024-03-25 18:51:29.178482'),(611,'/api/rscefacilt/13/','2024-03-25 18:51:32.612204'),(612,'/api/energyproandinvnt/','2024-03-25 18:51:33.365704'),(613,'/api/rscefacilt/13/','2024-03-25 18:57:03.362701'),(614,'/api/rscefacilt/13/','2024-03-25 19:01:31.533914'),(615,'/api/rscefacilt/13/','2024-03-25 19:01:47.527224'),(616,'/api/energyproandinvnt/','2024-03-25 19:02:58.296589'),(617,'/api/energyproandinvnt/','2024-03-25 19:03:25.574617'),(618,'/api/energyproandinvnt/','2024-03-25 19:05:34.076915'),(619,'/api/energyproandinvnt/','2024-03-25 19:05:57.361741'),(620,'/api/energyproandinvnt/','2024-03-25 19:06:06.074991'),(621,'/api/energyproandinvnt/','2024-03-25 19:06:20.958599'),(622,'/api/energyproandinvnt/','2024-03-25 19:07:18.833507'),(623,'/api/energyproandinvnt/','2024-03-25 19:08:26.429723'),(624,'/api/energyproandinvnt/','2024-03-25 19:10:24.891373'),(625,'/api/energyproandinvnt/','2024-03-25 19:10:57.963706'),(626,'/api/energyproandinvnt/','2024-03-25 19:11:19.878289'),(627,'/api/energyproandinvnt/','2024-03-25 19:11:20.422356'),(628,'/api/energyproandinvnt/','2024-03-25 19:11:20.953836'),(629,'/api/energyproandinvnt/','2024-03-25 19:11:21.214731'),(630,'/api/energyproandinvnt/','2024-03-25 19:11:21.968739'),(631,'/api/energyproandinvnt/','2024-03-25 19:11:22.144813'),(632,'/api/energyproandinvnt/','2024-03-25 19:11:22.507522'),(633,'/api/energyproandinvnt/','2024-03-25 19:11:22.681574'),(634,'/api/energyproandinvnt/','2024-03-25 19:11:22.835574'),(635,'/api/rscefacilt/13/','2024-03-25 19:11:44.281037'),(636,'/api/energyproandinvnt/','2024-03-25 19:11:46.766480'),(637,'/api/energyproandinvnt/','2024-03-25 19:12:25.832490'),(638,'/api/energyproandinvnt/','2024-03-25 19:12:49.692444'),(639,'/api/energyproandinvnt/','2024-03-25 19:12:50.117062'),(640,'/api/energyproandinvnt/','2024-03-25 19:12:50.513274'),(641,'/api/energyproandinvnt/','2024-03-25 19:12:50.858854'),(642,'/api/energyproandinvnt/','2024-03-25 19:12:51.069855'),(643,'/api/energyproandinvnt/','2024-03-25 19:12:51.261854'),(644,'/api/energyproandinvnt/','2024-03-25 19:12:51.415854'),(645,'/api/energyproandinvnt/','2024-03-25 19:12:51.563440'),(646,'/api/rscefacilt/13/','2024-03-25 19:12:54.294793'),(647,'/api/energyproandinvnt/','2024-03-25 19:12:56.660830'),(648,'/api/energyproandinvnt/','2024-03-25 19:13:02.810383'),(649,'/api/energyproandinvnt/','2024-03-25 19:13:10.841004'),(650,'/api/energyproandinvnt/','2024-03-25 19:13:20.203302'),(651,'/api/energyproandinvnt/','2024-03-25 19:13:22.311866'),(652,'/api/energyproandinvnt/','2024-03-25 19:13:23.658127'),(653,'/api/energyproandinvnt/','2024-03-25 19:13:26.451445'),(654,'/api/energyproandinvnt/','2024-03-25 19:13:29.405347'),(655,'/api/energyproandinvnt/','2024-03-25 19:14:35.669773'),(656,'/api/energyproandinvnt/','2024-03-25 19:14:40.014125'),(657,'/api/energyproandinvnt/','2024-03-25 19:14:42.237799'),(658,'/api/energyproandinvnt/','2024-03-25 19:14:44.520458'),(659,'/api/energyproandinvnt/','2024-03-25 19:14:46.465316'),(660,'/api/energyproandinvnt/','2024-03-25 19:14:48.182905'),(661,'/api/energyproandinvnt/','2024-03-25 19:15:13.342905'),(662,'/api/energyproandinvnt/','2024-03-25 19:15:20.201382'),(663,'/api/energyproandinvnt/','2024-03-25 19:15:56.500522'),(664,'/api/energyproandinvnt/','2024-03-25 19:15:58.374040'),(665,'/api/energyproandinvnt/','2024-03-25 19:16:14.673036'),(666,'/api/energyproandinvnt/','2024-03-25 19:16:20.642992'),(667,'/api/energyproandinvnt/','2024-03-25 19:16:48.104646'),(668,'/api/energyproandinvnt/','2024-03-25 19:17:21.595981'),(669,'/api/energyproandinvnt/','2024-03-25 19:17:21.827981'),(670,'/api/rscefacilt/13/','2024-03-25 19:17:26.116519'),(671,'/api/energyproandinvnt/','2024-03-25 19:20:28.706057'),(672,'/api/energyproandinvnt/','2024-03-25 19:20:32.005565'),(673,'/api/energyproandinvnt/','2024-03-25 19:20:34.224019'),(674,'/api/energyproandinvnt/','2024-03-25 19:21:39.955108'),(675,'/api/energyproandinvnt/','2024-03-25 19:24:47.911079'),(676,'/api/energyproandinvnt/','2024-03-25 19:24:50.895797'),(677,'/api/energyproandinvnt/','2024-03-25 19:25:06.825221'),(678,'/api/energyproandinvnt/','2024-03-25 19:25:08.562770'),(679,'/api/energyproandinvnt/','2024-03-25 19:25:56.724531'),(680,'/api/energyproandinvnt/','2024-03-25 19:26:46.667580'),(681,'/api/rscefacilt/1/','2024-03-25 19:28:05.463315'),(682,'/api/powergenerationcapcty/','2024-03-25 19:28:10.686489'),(683,'/api/powergenerationcapcty/','2024-03-25 19:28:18.773784'),(684,'/api/powergenerationcapcty/','2024-03-25 19:29:20.626114'),(685,'/api/powergenerationcapcty/','2024-03-25 19:30:02.195342'),(686,'/api/powergenerationcapcty/','2024-03-25 19:30:28.947130'),(687,'/api/energyiae/','2024-03-25 19:30:41.584337'),(688,'/api/powergenerationcapcty/','2024-03-25 19:30:53.598540'),(689,'/api/powergenerationcapcty/','2024-03-25 19:31:39.273815'),(690,'/api/energyiae/','2024-03-25 19:34:13.633280'),(691,'/api/energyproandinvnt/','2024-03-25 19:34:18.257576'),(692,'/api/energyproandinvnt/','2024-03-25 19:35:56.392386'),(693,'/api/rscefacilt/13','2024-03-25 19:36:50.960954'),(694,'/api/rscefacilt/13/','2024-03-25 19:36:51.022539'),(695,'/api/powergenerationcapcty/','2024-03-25 19:37:23.144907'),(696,'/api/rscefacilt/13/','2024-03-25 19:37:51.023364'),(697,'/api/powergenerationcapcty/','2024-03-25 19:37:51.373180'),(698,'/api/energyproandinvnt/','2024-03-25 19:37:53.857345'),(699,'/api/rscefacilt/13/','2024-03-25 19:37:55.905538'),(700,'/api/rscefacilt/13/','2024-03-25 19:38:45.018353'),(701,'/api/energyproandinvnt/','2024-03-25 19:38:46.612074'),(702,'/api/energyproandinvnt/','2024-03-25 19:39:35.112486'),(703,'/api/energyproandinvnt/','2024-03-25 19:39:38.174395'),(704,'/api/rscefacilt/13/','2024-03-25 19:40:33.806857'),(705,'/api/rscefacilt/13/','2024-03-25 19:40:43.521514'),(706,'/api/energyproandinvnt/','2024-03-25 19:41:40.390328'),(707,'/api/rscefacilt/13/','2024-03-25 19:42:20.525492'),(708,'/api/rscefacilt/13/','2024-03-25 19:42:27.757162'),(709,'/api/rscefacilt/13/','2024-03-25 19:42:30.051119'),(710,'/api/rscefacilt/13/','2024-03-25 19:48:24.911479'),(711,'/api/energyproandinvnt/','2024-03-25 19:49:01.670552'),(712,'/api/energyiae/','2024-03-25 19:49:10.977580'),(713,'/api/energyiae/','2024-03-25 19:49:20.032702'),(714,'/api/energyiae/','2024-03-25 19:49:34.969512'),(715,'/api/energyiae/','2024-03-25 19:50:04.932469'),(716,'/api/energyiae/','2024-03-25 19:50:22.811579'),(717,'/api/rscefacilt/13/','2024-03-25 19:51:14.363483'),(718,'/api/energyproandinvnt/','2024-03-25 19:52:16.697953'),(719,'/api/energyproandinvnt/','2024-03-25 19:55:44.266543'),(720,'/api/rscefacilt/13/','2024-03-25 19:58:58.571976'),(721,'/api/energyproandinvnt/','2024-03-25 19:59:03.721883'),(722,'/api/energyproandinvnt/','2024-03-25 20:00:47.548212'),(723,'/api/energyproandinvnt/','2024-03-25 20:06:19.665008'),(724,'/api/energyproandinvnt/','2024-03-25 20:06:20.519672'),(725,'/api/energyproandinvnt/','2024-03-25 20:06:20.597671'),(726,'/api/rscefacilt/13/','2024-03-25 20:06:50.738243'),(727,'/api/energyproandinvnt/','2024-03-25 20:07:01.687593'),(728,'/api/energyproandinvnt/','2024-03-25 20:07:01.798591'),(729,'/api/energyproandinvnt/','2024-03-25 20:07:02.104593'),(730,'/api/energyproandinvnt/','2024-03-25 20:07:21.328207'),(731,'/api/energyproandinvnt/','2024-03-25 20:07:21.641625'),(732,'/api/energyproandinvnt/','2024-03-25 20:07:40.728094'),(733,'/api/energyproandinvnt/','2024-03-25 20:07:40.732093'),(734,'/api/energyproandinvnt/','2024-03-25 20:08:02.655865'),(735,'/api/energyproandinvnt/','2024-03-25 20:08:02.908018'),(736,'/api/energyproandinvnt/','2024-03-25 20:08:20.465410'),(737,'/api/energyproandinvnt/','2024-03-25 20:08:20.471922'),(738,'/api/rscefacilt/13/','2024-03-25 20:08:56.082057'),(739,'/api/energyproandinvnt/','2024-03-25 20:10:57.124118'),(740,'/api/energyproandinvnt/','2024-03-25 20:16:33.902788'),(741,'/api/energy_consumption/','2024-03-25 20:26:19.463797'),(742,'/api/energy_consumption/','2024-03-25 20:27:16.983325'),(743,'/api/energy_consumption/','2024-03-25 20:27:18.330582'),(744,'/api/energy_consumption/','2024-03-25 20:28:37.601402'),(745,'/api/energy_consumption/','2024-03-25 20:30:39.470161'),(746,'/api/energy_consumption/','2024-03-25 20:31:22.371043'),(747,'/api/energy_consumption/','2024-03-25 20:31:23.773647'),(748,'/api/energy_consumption/','2024-03-25 20:31:46.363341'),(749,'/api/energy_consumption/','2024-03-25 20:31:47.098901'),(750,'/api/energy_consumption/','2024-03-25 20:31:47.674164'),(751,'/api/energy_consumption/','2024-03-25 20:32:24.981153'),(752,'/api/energy_consumption/','2024-03-25 20:35:54.974222'),(753,'/api/energy_consumption/','2024-03-25 20:38:47.446010'),(754,'/api/energy_consumption/','2024-03-25 20:38:57.144265'),(755,'/api/energy_consumption/','2024-03-25 20:39:00.355861'),(756,'/api/energy_consumption/','2024-03-25 20:39:11.700787'),(757,'/api/energyproandinvnt/','2024-03-25 20:42:01.242483'),(758,'/api/energyproandinvnt/','2024-03-25 20:47:48.154290'),(759,'/api/rscefacilt/13/','2024-03-25 20:47:50.303089'),(760,'/api/energyproandinvnt/','2024-03-25 20:49:11.368807'),(761,'/api/energyproandinvnt/','2024-03-25 20:49:33.960298'),(762,'/api/rscefacilt/13/','2024-03-25 20:52:49.987112'),(763,'/api/rscefacilt/13/','2024-03-25 20:53:02.731310'),(764,'/api/rscefacilt/13/','2024-03-25 20:53:04.655171'),(765,'/api/energyproandinvnt/','2024-03-25 20:53:06.091929'),(766,'/api/rscefacilt/13/','2024-03-25 20:53:06.976176'),(767,'/api/energyproandinvnt/','2024-03-25 20:53:28.855508'),(768,'/api/rscefacilt/13/','2024-03-25 20:53:37.755684'),(769,'/api/rscefacilt/13/','2024-03-25 20:53:47.395035'),(770,'/api/rscefacilt/13/','2024-03-25 20:53:50.862156'),(771,'/api/rscefacilt/13/','2024-03-25 20:53:53.439486'),(772,'/api/rscefacilt/13/','2024-03-25 20:53:54.667724'),(773,'/api/rscefacilt/13/','2024-03-25 20:53:55.752952'),(774,'/api/rscefacilt/13/','2024-03-25 20:53:57.089508'),(775,'/api/energyproandinvnt/','2024-03-25 20:54:50.916111'),(776,'/api/rscefacilt/13/','2024-03-25 20:54:52.182341'),(777,'/api/rscefacilt/13/','2024-03-25 20:56:41.803932'),(778,'/api/rscefacilt/13/','2024-03-25 20:56:56.325254'),(779,'/api/rscefacilt/13/','2024-03-25 21:00:25.063909'),(780,'/api/rscefacilt/13/','2024-03-25 21:00:26.390543'),(781,'/api/rscefacilt/13/','2024-03-25 21:00:29.115160'),(782,'/api/energyproandinvnt/','2024-03-25 21:00:34.962702'),(783,'/api/energyproandinvnt/','2024-03-25 21:01:12.404281'),(784,'/api/rscefacilt/13/','2024-03-25 21:01:18.721317'),(785,'/api/rscefacilt/13/','2024-03-25 21:02:10.648947'),(786,'/api/rscefacilt/13/','2024-03-25 21:04:03.773380'),(787,'/api/energyproandinvnt/','2024-03-25 21:04:07.870418'),(788,'/api/rscefacilt/13/','2024-03-25 21:10:28.031373'),(789,'/api/rscefacilt/13/','2024-03-25 21:10:30.913351'),(790,'/api/energyproandinvnt/','2024-03-25 21:10:33.094535'),(791,'/api/energyproandinvnt/','2024-03-25 21:12:43.858554'),(792,'/api/rscefacilt/13/','2024-03-25 21:12:56.327225'),(793,'/api/rscefacilt/13/','2024-03-25 21:14:40.552133'),(794,'/api/energyproandinvnt/','2024-03-25 21:15:13.878365'),(795,'/api/rscefacilt/13/','2024-03-25 21:17:02.657705'),(796,'/api/rscefacilt/13/','2024-03-25 21:17:17.615508'),(797,'/api/energyproandinvnt/','2024-03-25 21:19:54.165719'),(798,'/api/energyproandinvnt/','2024-03-25 21:21:57.083330'),(799,'/api/rscefacilt/13/','2024-03-25 21:22:13.647544'),(800,'/api/rscefacilt/13/','2024-03-25 21:22:37.779311'),(801,'/api/energyproandinvnt/','2024-03-25 21:23:00.404094'),(802,'/api/rscefacilt/13/','2024-03-25 21:23:05.719529'),(803,'/api/energyproandinvnt/','2024-03-25 21:23:29.051462'),(804,'/api/rscefacilt/13/','2024-03-25 21:23:29.956636'),(805,'/api/energyproandinvnt/','2024-03-25 21:23:40.549173'),(806,'/api/rscefacilt/13/','2024-03-25 21:24:32.293025'),(807,'/api/rscefacilt/13/','2024-03-25 21:24:39.422975'),(808,'/api/rscefacilt/13/','2024-03-25 21:24:42.303243'),(809,'/api/energyproandinvnt/','2024-03-25 21:25:35.454373'),(810,'/api/rscefacilt/13/','2024-03-25 21:25:36.371381'),(811,'/api/energyproandinvnt/','2024-03-25 21:25:39.682129'),(812,'/api/rscefacilt/13/','2024-03-25 21:26:04.834128'),(813,'/api/rscefacilt/13/','2024-03-25 21:26:10.749212'),(814,'/api/energyproandinvnt/','2024-03-25 21:26:11.869289'),(815,'/api/rscefacilt/13/','2024-03-25 21:26:37.775546'),(816,'/api/energyproandinvnt/','2024-03-25 21:26:48.514053'),(817,'/api/rscefacilt/13/','2024-03-25 21:26:49.581519'),(818,'/api/rscefacilt/13/','2024-03-25 21:26:55.856812'),(819,'/api/rscefacilt/13/','2024-03-25 21:27:29.418936'),(820,'/api/rscefacilt/13/','2024-03-25 21:27:32.131350'),(821,'/api/rscefacilt/13/','2024-03-25 21:27:34.115635'),(822,'/api/rscefacilt/13/','2024-03-25 21:27:35.977081'),(823,'/api/rscefacilt/13/','2024-03-25 21:27:37.054752'),(824,'/api/rscefacilt/13/','2024-03-25 21:27:38.525629'),(825,'/api/energyproandinvnt/','2024-03-25 21:28:10.677727'),(826,'/api/rscefacilt/13/','2024-03-25 21:29:23.581298'),(827,'/api/energyproandinvnt/','2024-03-25 21:29:30.190762'),(828,'/api/rscefacilt/13/','2024-03-25 21:29:31.316891'),(829,'/api/rscefacilt/13/','2024-03-25 21:30:29.425826'),(830,'/api/energyproandinvnt/','2024-03-25 21:32:22.217550'),(831,'/api/rscefacilt/13/','2024-03-25 21:33:41.821439'),(832,'/api/energyproandinvnt/','2024-03-25 21:34:10.292546'),(833,'/api/rscefacilt/13/','2024-03-25 21:34:10.932759'),(834,'/api/energyproandinvnt/','2024-03-25 21:35:21.074799'),(835,'/api/rscefacilt/13/','2024-03-25 21:35:40.118694'),(836,'/api/energyproandinvnt/','2024-03-25 21:36:26.522301'),(837,'/api/rscefacilt/13/','2024-03-25 21:36:47.170876'),(838,'/api/energyproandinvnt/','2024-03-25 21:37:31.743177'),(839,'/api/rscefacilt/13/','2024-03-25 21:37:35.258093'),(840,'/api/rscefacilt/13/','2024-03-25 21:39:20.649477'),(841,'/api/rscefacilt/13/','2024-03-25 21:39:25.791805'),(842,'/api/rscefacilt/13/','2024-03-25 21:40:44.239256'),(843,'/api/rscefacilt/13/','2024-03-25 21:43:27.648315'),(844,'/api/energyproandinvnt/','2024-03-25 21:43:29.548796'),(845,'/api/rscefacilt/13/','2024-03-25 21:43:30.313306'),(846,'/api/rscefacilt/13/','2024-03-25 21:44:20.714561'),(847,'/api/rscefacilt/13/','2024-03-25 21:49:08.484905'),(848,'/api/rscefacilt/13/','2024-03-25 21:50:20.972557'),(849,'/api/rscefacilt/13/','2024-03-25 21:50:24.368565'),(850,'/api/rscefacilt/13/','2024-03-25 21:50:45.520434'),(851,'/api/rscefacilt/13/','2024-03-25 21:50:48.024404'),(852,'/api/rscefacilt/13/','2024-03-25 21:50:51.265366'),(853,'/api/energyproandinvnt/','2024-03-25 21:51:22.467883'),(854,'/api/rscefacilt/13/','2024-03-25 21:51:26.600418'),(855,'/api/rscefacilt/13/','2024-03-25 21:51:33.465059'),(856,'/api/rscefacilt/13/','2024-03-25 21:52:24.533190'),(857,'/api/energyproandinvnt/','2024-03-25 21:52:28.298393'),(858,'/api/rscefacilt/13/','2024-03-25 21:52:29.847403'),(859,'/api/rscefacilt/13/','2024-03-25 21:52:33.516692'),(860,'/api/rscefacilt/13/','2024-03-25 21:54:38.338601'),(861,'/api/rscefacilt/13/','2024-03-25 21:54:42.944459'),(862,'/api/rscefacilt/13/','2024-03-25 21:59:20.705701'),(863,'/api/rscefacilt/13/','2024-03-25 22:03:28.943405'),(864,'/api/rscefacilt/13/','2024-03-25 22:09:35.185511'),(865,'/api/rscefacilt/13/','2024-03-25 22:10:37.838882'),(866,'/api/rscefacilt/13/','2024-03-25 22:17:10.525910'),(867,'/api/rscefacilt/13/','2024-03-25 22:17:37.315635'),(868,'/api/rscefacilt/13/','2024-03-25 22:18:04.982790'),(869,'/api/energyproandinvnt/','2024-03-26 17:47:41.291583'),(870,'/api/rscefacilt/13/','2024-03-26 17:47:47.755133'),(871,'/api/rscefacilt/13','2024-03-26 17:50:00.028829'),(872,'/api/rscefacilt/13/','2024-03-26 17:50:00.171833'),(873,'/api/rscefacilt/13/','2024-03-26 17:50:02.098552'),(874,'/api/rscefacilt/13/','2024-03-26 18:09:45.362345'),(875,'/api/energyproandinvnt/','2024-03-26 18:09:48.588950'),(876,'/api/rscefacilt/13/','2024-03-26 18:09:52.742219'),(877,'/api/rscefacilt/13/','2024-03-26 18:11:18.721778'),(878,'/api/rscefacilt/13/','2024-03-26 18:26:51.773733'),(879,'/api/energyproandinvnt/','2024-03-26 18:30:25.232154'),(880,'/api/energyproandinvnt/','2024-03-26 18:30:26.648158'),(881,'/api/energyproandinvnt/','2024-03-26 18:30:27.730159'),(882,'/api/rscefacilt/13/','2024-03-26 18:30:30.904161'),(883,'/api/rscefacilt/13/','2024-03-26 18:39:09.820826'),(884,'/api/energyproandinvnt/','2024-03-26 18:45:16.372312'),(885,'/api/rscefacilt/13/','2024-03-26 18:48:47.606692'),(886,'/api/energyproandinvnt/','2024-03-26 19:12:08.079287'),(887,'/api/renew/','2024-03-26 19:15:29.049996'),(888,'/api/renew/get_electricity_generation/13/','2024-03-26 19:19:18.036479'),(889,'/api/get_energy_consumption/','2024-03-26 19:25:14.041146'),(890,'/api/get_energy_import_and_export/','2024-03-26 19:25:29.882597'),(891,'/api/get_mineral_develop/1/','2024-03-26 19:26:23.716869'),(892,'/api/get_mineral_develop/2/','2024-03-26 19:26:28.080210'),(893,'/api/get_mineral_develop/13/','2024-03-26 19:26:31.142041'),(894,'/api/get_mineral_develop/1/','2024-03-26 19:26:33.585114'),(895,'/api/rscefacilt/13/','2024-03-26 19:26:54.283030'),(896,'/api/energyproandinvnt/','2024-03-26 19:27:02.780781'),(897,'/api/energyproandinvnt/','2024-03-26 19:27:52.421038'),(898,'/api/rscefacilt/13/','2024-03-26 19:28:10.337219'),(899,'/api/rscefacilt/13/','2024-03-26 19:28:10.400971'),(900,'/api/rscefacilt/13/','2024-03-26 19:28:41.055708'),(901,'/api/get_regional_resource_facilities/1/','2024-03-26 19:28:56.103233'),(902,'/api/get_regional_resource_facilities/1/','2024-03-26 19:29:09.285548'),(903,'/api/get_power_generation_installed_capacity/','2024-03-26 19:29:15.888208'),(904,'/api/energyproandinvnt/','2024-03-26 19:29:25.931903'),(905,'/api/energyproandinvnt/','2024-03-26 19:29:47.592001'),(906,'/api/renew/get_electricity_generation/1/','2024-03-26 19:29:53.699209'),(907,'/api/renew/get_electricity_generation/2/','2024-03-26 19:29:59.543471'),(908,'/api/renew/get_electricity_generation/3/','2024-03-26 19:30:01.516680'),(909,'/api/get_energy_consumption/','2024-03-26 19:30:22.665602'),(910,'/api/renew/get_electricity_generation/13/','2024-03-26 19:30:39.648596'),(911,'/api/renew/get_electricity_generation/13/','2024-03-26 19:30:53.225541'),(912,'/api/get_regional_resource_facilities/1/','2024-03-26 19:30:54.614347'),(913,'/api/energyproandinvnt/','2024-03-26 19:30:55.854562'),(914,'/api/get_energy_production_and_inventory/','2024-03-26 19:31:57.688967'),(915,'/api/energyproandinvnt/','2024-03-26 19:32:12.313875'),(916,'/api/energyproandinvnt/','2024-03-26 19:32:19.221158'),(917,'/api/get_energy_import_and_export/','2024-03-26 19:32:22.911050'),(918,'/api/get_energy_production_and_inventory/','2024-03-26 19:32:30.955195'),(919,'/api/get_energy_production_and_inventory/','2024-03-26 19:32:42.778882'),(920,'/api/get_energy_consumption/','2024-03-26 19:32:49.685310'),(921,'/api/get_energy_production_and_inventory/','2024-03-26 19:32:56.513210'),(922,'/api/get_regional_resource_facilities/1/','2024-03-26 19:32:58.651957'),(923,'/api/get_energy_production_and_inventory/','2024-03-26 19:33:14.997912'),(924,'/api/get_energy_production_and_inventory/','2024-03-26 19:33:17.382414'),(925,'/api/get_regional_resource_facilities/1/','2024-03-26 19:33:18.540755'),(926,'/api/get_regional_resource_facilities/1/','2024-03-26 19:33:36.758173'),(927,'/api/get_energy_production_and_inventory/','2024-03-26 19:34:12.352391'),(928,'/api/get_energy_production_and_inventory/','2024-03-26 19:36:01.033491'),(929,'/api/get_regional_resource_facilities/1/','2024-03-26 19:36:33.609060'),(930,'/api/get_energy_production_and_inventory/','2024-03-26 19:36:35.121403'),(931,'/api/get_regional_resource_facilities/1/','2024-03-26 19:36:38.697781'),(932,'/api/get_regional_resource_facilities/1/','2024-03-26 19:37:38.135356'),(933,'/api/get_energy_production_and_inventory/','2024-03-26 19:37:39.809354'),(934,'/api/get_regional_resource_facilities/1/','2024-03-26 19:39:11.906948'),(935,'/api/get_regional_resource_facilities/1/','2024-03-26 20:06:39.850922'),(936,'/api/get_regional_resource_facilities/1/','2024-03-26 21:20:08.759587'),(937,'/api/get_regional_resource_facilities/1/','2024-03-26 21:20:12.404375'),(938,'/api/get_regional_resource_facilities/1/','2024-03-26 21:20:15.931833'),(939,'/api/get_regional_resource_facilities/1/','2024-03-26 21:29:17.807881'),(940,'/api/get_regional_resource_facilities/1/','2024-03-26 21:31:55.404724'),(941,'/api/get_regional_resource_facilities/1/','2024-03-26 21:33:14.260657'),(942,'/api/get_regional_resource_facilities/1/','2024-03-26 21:33:54.295020'),(943,'/api/get_energy_production_and_inventory/','2024-03-26 21:34:14.090225'),(944,'/api/get_regional_resource_facilities/1/','2024-03-26 21:41:44.264389'),(945,'/api/get_regional_resource_facilities/1/','2024-03-26 21:42:55.308582'),(946,'/api/get_regional_resource_facilities/1/','2024-03-26 21:43:06.390305'),(947,'/api/get_energy_production_and_inventory/','2024-03-26 21:43:08.789943'),(948,'/api/get_energy_consumption/','2024-03-26 21:47:40.733881'),(949,'/api/get_energy_consumption/','2024-03-26 21:47:40.858881'),(950,'/api/get_energy_consumption/','2024-03-26 21:47:40.985880'),(951,'/api/get_energy_consumption/','2024-03-26 21:47:41.124289'),(952,'/api/get_energy_consumption/','2024-03-26 21:47:41.253104'),(953,'/api/get_energy_consumption/','2024-03-26 21:47:41.380104'),(954,'/api/get_energy_consumption/','2024-03-26 21:47:41.520495'),(955,'/api/get_energy_consumption/','2024-03-26 21:47:41.655836'),(956,'/api/get_energy_consumption/','2024-03-26 21:47:41.810836'),(957,'/api/get_energy_consumption/','2024-03-26 21:47:41.954836'),(958,'/api/get_energy_consumption/','2024-03-26 21:47:42.119836'),(959,'/api/get_energy_consumption/','2024-03-26 21:47:42.258837'),(960,'/api/get_energy_consumption/','2024-03-26 21:47:42.403836'),(961,'/api/get_energy_consumption/','2024-03-26 21:47:42.538837'),(962,'/api/get_energy_consumption/','2024-03-26 21:47:42.674836'),(963,'/api/get_regional_resource_facilities/1/','2024-03-26 21:53:34.497727'),(964,'/api/get_regional_resource_facilities/1/','2024-03-26 21:53:39.296668'),(965,'/api/get_regional_resource_facilities/1/','2024-03-26 21:53:41.326614'),(966,'/api/get_regional_resource_facilities/1/','2024-03-26 21:58:05.282113'),(967,'/api/get_energy_production_and_inventory/','2024-03-26 22:03:00.227211'),(968,'/api/get_regional_resource_facilities/1/','2024-03-26 22:03:06.241142'),(969,'/api/get_regional_resource_facilities/1/','2024-03-26 22:03:10.405890'),(970,'/api/get_regional_resource_facilities/1/','2024-03-26 22:04:48.576084'),(971,'/api/get_regional_resource_facilities/1/','2024-03-26 22:05:36.360838'),(972,'/api/get_regional_resource_facilities/1/','2024-03-26 22:07:42.438979'),(973,'/api/get_regional_resource_facilities/1/','2024-03-26 22:08:18.091550'),(974,'/api/get_energy_production_and_inventory/','2024-03-26 22:16:28.616228'),(975,'/api/get_regional_resource_facilities/1/','2024-03-26 22:16:29.394805'),(976,'/api/get_regional_resource_facilities/1/','2024-03-26 22:16:30.341996'),(977,'/api/renew/get_electricity_generation/9/','2024-03-27 02:24:43.775768'),(978,'/api/renew/get_electricity_generation/9/','2024-03-27 02:24:44.884336'),(979,'/api/renew/get_electricity_generation/9/','2024-03-27 02:24:51.703442'),(980,'/api/get_regional_resource_facilities/1/','2024-03-27 22:25:55.688971'),(981,'/api/get_regional_resource_facilities/1/','2024-03-27 22:26:00.189508'),(982,'/api/get_energy_production_and_inventory/','2024-03-27 22:26:02.060888'),(983,'/api/get_regional_resource_facilities/1/','2024-03-27 22:26:03.836376'),(984,'/api/get_energy_production_and_inventory/','2024-03-27 22:26:12.306497'),(985,'/api/get_energy_production_and_inventory/','2024-03-27 22:27:10.426713'),(986,'/api/get_regional_resource_facilities/1/','2024-03-27 22:27:21.874264'),(987,'/api/get_energy_production_and_inventory/','2024-03-27 22:28:26.740203');
/*!40000 ALTER TABLE `suyuanapplication_apirequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suyuanapplication_energyconsumptionmodel`
--

DROP TABLE IF EXISTS `suyuanapplication_energyconsumptionmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suyuanapplication_energyconsumptionmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `total_energy_consumption` decimal(10,2) NOT NULL,
  `coal` decimal(3,1) NOT NULL,
  `petroleum` decimal(3,1) NOT NULL,
  `natural_gas` decimal(3,1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `power_and_other` decimal(3,1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `year` (`year`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suyuanapplication_energyconsumptionmodel`
--

LOCK TABLES `suyuanapplication_energyconsumptionmodel` WRITE;
/*!40000 ALTER TABLE `suyuanapplication_energyconsumptionmodel` DISABLE KEYS */;
INSERT INTO `suyuanapplication_energyconsumptionmodel` VALUES (1,2000,146964.00,68.5,22.0,2.2,'2024-03-25 20:02:04.166426',7.3),(2,2001,155547.00,68.0,21.2,2.4,'2024-03-25 20:02:22.056808',8.4),(3,2002,169577.00,68.5,21.0,2.3,'2024-03-25 20:02:40.272588',8.2),(4,2003,197083.00,70.2,20.1,2.3,'2024-03-25 20:02:59.072305',7.4),(5,2004,230281.00,70.2,19.9,2.3,'2024-03-25 20:03:12.167633',7.6),(6,2005,261369.00,72.4,17.8,2.4,'2024-03-25 20:03:36.168104',7.4),(7,2006,286467.00,72.4,17.5,2.7,'2024-03-25 20:03:55.272509',7.4),(8,2007,311442.00,72.5,17.0,3.0,'2024-03-25 20:04:08.468155',7.5),(9,2008,320611.00,71.5,16.7,3.4,'2024-03-25 20:04:26.380939',8.4),(10,2009,336126.00,71.6,16.4,3.5,'2024-03-25 20:04:41.855831',8.5),(11,2010,360648.00,69.2,17.4,4.0,'2024-03-25 20:05:01.292437',9.4),(12,2011,387043.00,70.2,16.8,4.6,'2024-03-25 20:05:24.035463',8.4),(13,2012,402138.00,68.5,17.0,4.8,'2024-03-25 20:05:50.682606',9.7),(14,2013,416913.00,67.4,17.1,5.3,'2024-03-25 20:06:08.946251',10.2),(15,2014,428334.00,65.8,17.3,5.6,'2024-03-25 20:06:40.114976',11.3),(16,2015,434113.00,63.8,18.4,5.8,'2024-03-25 20:07:02.383439',12.0),(17,2016,441492.00,62.2,18.7,6.1,'2024-03-25 20:07:20.676803',13.0),(18,2017,455827.00,60.6,18.9,6.9,'2024-03-25 20:07:42.065258',13.6),(19,2018,471925.00,59.0,18.9,7.6,'2024-03-25 20:07:56.850773',14.5),(20,2019,487488.00,57.7,19.0,8.0,'2024-03-25 20:08:19.522045',15.3),(21,2020,498314.00,56.9,18.8,8.4,'2024-03-25 20:08:39.982064',15.9),(22,2021,525896.00,55.9,18.6,8.8,'2024-03-25 20:09:10.851748',16.7),(23,2022,541000.00,56.2,17.9,8.4,'2024-03-25 20:09:33.918238',17.5);
/*!40000 ALTER TABLE `suyuanapplication_energyconsumptionmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suyuanapplication_energyimportandexportmodel`
--

DROP TABLE IF EXISTS `suyuanapplication_energyimportandexportmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suyuanapplication_energyimportandexportmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `coal_e` decimal(10,2) NOT NULL,
  `coal_i` decimal(10,2) NOT NULL,
  `petroleum_e` decimal(10,2) NOT NULL,
  `petroleum_i` decimal(10,2) NOT NULL,
  `power_e` decimal(10,2) NOT NULL,
  `power_i` decimal(10,2) NOT NULL,
  `all_e` decimal(10,2) NOT NULL,
  `all_i` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SuYuanApplication_nation_year_cf1bd179_uniq` (`year`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suyuanapplication_energyimportandexportmodel`
--

LOCK TABLES `suyuanapplication_energyimportandexportmodel` WRITE;
/*!40000 ALTER TABLE `suyuanapplication_energyimportandexportmodel` DISABLE KEYS */;
INSERT INTO `suyuanapplication_energyimportandexportmodel` VALUES (1,2010,1911.00,18307.00,4079.00,29437.00,191.00,55.00,8803.00,57671.00,'2024-03-25 15:52:09.022149'),(2,2015,534.00,20406.00,5128.00,39749.00,187.00,62.00,9785.00,77695.00,'2024-03-25 15:52:09.022149'),(3,2019,603.00,29977.00,8211.00,58102.00,217.00,49.00,14151.00,119064.00,'2024-03-25 15:52:09.022149'),(4,2020,319.00,30361.00,7551.00,61272.00,218.00,48.00,12838.00,124805.00,'2024-03-25 15:52:09.022149'),(5,2021,261.00,32327.00,7617.00,58820.00,202.00,59.00,13122.00,214807.00,'2024-03-25 15:52:09.022149');
/*!40000 ALTER TABLE `suyuanapplication_energyimportandexportmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suyuanapplication_energyproductionandinventorymodel`
--

DROP TABLE IF EXISTS `suyuanapplication_energyproductionandinventorymodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suyuanapplication_energyproductionandinventorymodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `total_energy_available_for_consumption` decimal(10,2) NOT NULL,
  `total_production_of_primary_energy` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SuYuanApplication_nation_year_2575435f_uniq` (`year`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suyuanapplication_energyproductionandinventorymodel`
--

LOCK TABLES `suyuanapplication_energyproductionandinventorymodel` WRITE;
/*!40000 ALTER TABLE `suyuanapplication_energyproductionandinventorymodel` DISABLE KEYS */;
INSERT INTO `suyuanapplication_energyproductionandinventorymodel` VALUES (1,2010,365588.00,312125.00,'2024-03-25 15:52:13.464224'),(2,2015,431636.00,362193.00,'2024-03-25 15:52:13.464224'),(3,2019,493178.00,397317.00,'2024-03-25 15:52:13.464224'),(4,2020,507479.00,407295.00,'2024-03-25 15:52:13.464224'),(5,2021,533841.00,432547.29,'2024-03-25 15:52:13.464224'),(6,2018,481420.64,377033.20,'2024-03-25 19:06:59.276324'),(7,2017,478284.03,359371.69,'2024-03-25 19:07:10.982172'),(8,2022,549322.39,472961.58,'2024-03-25 19:13:58.325570');
/*!40000 ALTER TABLE `suyuanapplication_energyproductionandinventorymodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suyuanapplication_mineraldevelopmentmodel`
--

DROP TABLE IF EXISTS `suyuanapplication_mineraldevelopmentmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suyuanapplication_mineraldevelopmentmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `region` varchar(100) NOT NULL,
  `year` int NOT NULL,
  `coal` decimal(10,2) NOT NULL,
  `petroleum` decimal(10,2) NOT NULL,
  `gas` decimal(10,2) NOT NULL,
  `coalbed_methane` decimal(10,2) NOT NULL,
  `shale_gas` decimal(10,2) NOT NULL,
  `iron` decimal(10,2) NOT NULL,
  `manganese` decimal(10,2) NOT NULL,
  `ferrochrome` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SuYuanApplication_minera_year_region_4fcaaabb_uniq` (`year`,`region`),
  UNIQUE KEY `SuYuanApplication_mineraldevelopmentmodel_year_8b7344a6_uniq` (`year`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suyuanapplication_mineraldevelopmentmodel`
--

LOCK TABLES `suyuanapplication_mineraldevelopmentmodel` WRITE;
/*!40000 ALTER TABLE `suyuanapplication_mineraldevelopmentmodel` DISABLE KEYS */;
INSERT INTO `suyuanapplication_mineraldevelopmentmodel` VALUES (1,'全国',2022,2070.12,38.06,65690.12,3659.69,5605.59,162.46,27561.45,279.47,'2024-03-25 15:52:14.421474'),(2,'全国',2021,2078.85,36.89,63392.67,3659.68,5440.62,161.24,28168.78,308.60,'2024-03-25 15:52:14.421474'),(3,'全国',2020,1622.88,36.19,62665.78,3315.54,4026.17,108.78,21295.69,276.97,'2024-03-25 15:52:14.421474'),(4,'全国',2018,17085.73,35.73,57936.08,3046.30,2160.20,852.19,18.16,1193.27,'2024-03-25 15:52:14.421474'),(5,'全国',2017,16666.73,35.42,55220.96,3025.36,1982.88,848.88,18.46,1220.24,'2024-03-25 15:52:14.421474'),(6,'全国',2016,15980.01,35.01,54365.47,3344.04,1224.13,840.63,15.51,1233.19,'2024-03-25 15:52:14.421474'),(7,'全国',2019,17385.83,46.93,66026.98,3110.40,9804.40,857.49,19.16,1166.24,'2024-03-25 15:52:14.421474');
/*!40000 ALTER TABLE `suyuanapplication_mineraldevelopmentmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suyuanapplication_powergenerationinstalledcapacitymodel`
--

DROP TABLE IF EXISTS `suyuanapplication_powergenerationinstalledcapacitymodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suyuanapplication_powergenerationinstalledcapacitymodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `thermal_power` decimal(10,2) NOT NULL,
  `hydropower` decimal(10,2) NOT NULL,
  `nuclear_power` decimal(10,2) NOT NULL,
  `wind_power` decimal(10,2) NOT NULL,
  `solar_power_generation` decimal(10,2) NOT NULL,
  `other_power` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SuYuanApplication_nation_year_b368136c_uniq` (`year`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suyuanapplication_powergenerationinstalledcapacitymodel`
--

LOCK TABLES `suyuanapplication_powergenerationinstalledcapacitymodel` WRITE;
/*!40000 ALTER TABLE `suyuanapplication_powergenerationinstalledcapacitymodel` DISABLE KEYS */;
INSERT INTO `suyuanapplication_powergenerationinstalledcapacitymodel` VALUES (1,2018,114408.00,35259.00,4466.00,18427.00,17433.00,19.00,'2024-03-25 15:52:15.251991'),(2,2019,118957.00,35804.00,4874.00,20915.00,20418.00,37.00,'2024-03-25 15:52:15.251991'),(3,2020,124624.00,37028.00,4989.00,28165.00,25356.00,41.00,'2024-03-25 15:52:15.251991'),(4,2021,129739.00,39094.00,5326.00,32871.00,30654.00,94.00,'2024-03-25 15:52:15.251991'),(5,2022,133329.00,41406.00,5553.00,36564.00,39268.00,675.00,'2024-03-25 15:52:15.251991');
/*!40000 ALTER TABLE `suyuanapplication_powergenerationinstalledcapacitymodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suyuanapplication_regionalresourcefacilitiesmodel`
--

DROP TABLE IF EXISTS `suyuanapplication_regionalresourcefacilitiesmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suyuanapplication_regionalresourcefacilitiesmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `region` varchar(100) NOT NULL,
  `name` varchar(30) NOT NULL,
  `do` varchar(30) NOT NULL,
  `number` decimal(7,2) NOT NULL,
  `up` varchar(10) NOT NULL,
  `when` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SuYuanApplication_region_region_name_1cfeef21_uniq` (`region`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suyuanapplication_regionalresourcefacilitiesmodel`
--

LOCK TABLES `suyuanapplication_regionalresourcefacilitiesmodel` WRITE;
/*!40000 ALTER TABLE `suyuanapplication_regionalresourcefacilitiesmodel` DISABLE KEYS */;
INSERT INTO `suyuanapplication_regionalresourcefacilitiesmodel` VALUES (1,'安徽','铜陵矿业','产铜',12.10,'万吨','1999-12-31','2024-03-25 15:52:16.138171'),(2,'安徽','淮南矿业','采煤',5100.54,'万吨','1999-12-31','2024-03-25 15:52:16.138171'),(3,'安徽','高邮湖风','发电',81.22,'亿千瓦时','2024-08-06','2024-03-25 15:52:16.138171'),(4,'安徽','绩溪电站','发电',40.12,'亿千瓦时','2021-07-23','2024-03-25 15:52:16.138171'),(5,'安徽','芜湖电厂','发电',15.36,'亿千瓦时','2011-03-01','2024-03-25 15:52:16.138171'),(6,'安徽','恒源煤电','产煤',702.40,'万吨','2023-10-12','2024-03-25 15:52:16.138171'),(7,'安徽','淮河能源','产电',49.10,'亿千瓦时','2024-02-02','2024-03-25 15:52:16.138171'),(8,'安徽','铜陵有色','加工铜',40.02,'万吨','2022-11-18','2024-03-25 15:52:16.138171');
/*!40000 ALTER TABLE `suyuanapplication_regionalresourcefacilitiesmodel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-27 22:28:55
