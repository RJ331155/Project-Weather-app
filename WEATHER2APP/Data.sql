-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: weather
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data` (
  `D_S_name` varchar(70) DEFAULT NULL,
  `temp` float DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `pressure` float DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  `description` varchar(30) DEFAULT NULL,
  `Predictions` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES ('Angul',26,2.68,1015,26,'clear sky','Clear'),('Balangir',24,1.66,1016,32,'clear sky','Clear'),('Bargarh',24,1.2,1016,34,'clear sky','Clear'),('Balasore',26,3.77,1015,24,'clear sky','Clear'),('Bhadrak',26,2.5,1015,24,'clear sky','Clear'),('Cuttack',25,2.73,1015,27,'clear sky','Clear'),('Deogarh',26,0.8,1015,27,'clear sky','Clear'),('Dhenkanal',26,2.01,1015,28,'clear sky','Clear'),('Ganjam',24,3.52,1015,50,'clear sky','Clear'),('Gajapati',24,4.12,1019,78,'mist','Mist'),('Jharsuguda',25,1.54,1016,41,'clear sky','Clear'),('Jaipur',23,1.54,1019,38,'haze','Haze'),('Jagatsinghapur',25,3.2,1015,25,'clear sky','Clear'),('Boudh',23,1.7,1014,23,'Rainy','Rain'),('Khordha',24,2.68,1015,28,'clear sky','Clear'),('Keonjhar',23,1.7,1014,23,'Rainy','Rain'),('Kalahandi',23,1.7,1014,23,'Rainy','Rain'),('Kandhamal',23,1.7,1014,23,'mist','Mist'),('Koraput',22,2.74,1015,45,'clear sky','Clear'),('Kendrapara',26,3.18,1015,24,'clear sky','Clear'),('Malkangiri',28,0.58,1015,46,'clear sky','Clear'),('Mayurbhanj',23,1.7,1014,23,'mist','Mist'),('Mayurbhanj',23,1.7,1014,23,'mist','Mist'),('Nabarangpur',23,1.7,1014,23,'clear sky','Clear'),('Nuapada',23,1.7,1014,23,'clear sky','Clear'),('Nayagarh',26,1.63,1013,27,'clear sky','Clear'),('Puri',25,3.15,1013,27,'clear sky','Clear'),('Rayagada',28,0.45,1013,41,'clear sky','Clear'),('Sambalpur',23,2.08,1014,36,'clear sky','Clear'),('Subarnapur',25,2.2,1014,32,'clear sky','Clear'),('Sundargarh',24,0.54,1014,27,'clear sky','Clear'),('Rourkela',25,1.05,1014,29,'clear sky','Clear'),('Andhra pradesh',23,2.25,1014,69,'overcast clouds','Clouds'),('Arunachal pradesh',22,1.28,1013,36,'clear sky','Clear'),('Assam',22,0.61,1013,60,'clear sky','Clear'),('Bihar',-1,3.6,1037,93,'clear sky','Clear'),('Chhattisgarh',26,0.52,1014,28,'clear sky','Clear'),('Goa',30,0.4,1010,42,'overcast clouds','Clouds'),('Gujarat',28,3.21,1014,32,'clear sky','Clear'),('Haryana',23,2.22,1015,20,'scattered clouds','Clouds'),('Himachal pradesh',17,2.5,1013,16,'broken clouds','Clouds'),('Jammu',20,1.62,1016,18,'clear sky','Clear'),('Jammu and Kashmir',-16,3.82,1020,57,'clear sky','Clear'),('Jharkhand',23,3.48,1014,24,'clear sky','Clear'),('Karnataka',27,4.57,1011,56,'overcast clouds','Clouds'),('Kerala',31,2.88,1009,59,'broken clouds','Clouds'),('Madhya pradesh',23,2.39,1015,33,'clear sky','Clear'),('Maharashtra',26,1.33,1014,33,'clear sky','Clear'),('Manipur',20,1.62,1013,44,'clear sky','Clear'),('Meghalaya',15,2.8,1013,60,'scattered clouds','Clouds'),('Mizoram',22,1.22,1012,22,'clear sky','Clear'),('Nagaland',17,2.09,1013,52,'clear sky','Clear'),('Orissa',25,2.74,1014,27,'clear sky','Clear'),('Punjab',23,2.06,1016,18,'broken clouds','Clouds'),('Rajasthan',25,3.63,1015,19,'clear sky','Clear'),('Sikkim',-4,1.68,1015,55,'clear sky','Clear'),('Tamil Nadu',29,1.47,1010,58,'overcast clouds','Clouds'),('Tripura',25,1.1,1013,42,'clear sky','Clear'),('Uttarakhand',23,1.94,1012,14,'overcast clouds','Clouds'),('Uttar pradesh',23,3.13,1015,22,'clear sky','Clear'),('West bengal',25,2.41,1014,23,'clear sky','Clear'),('Nepal',19,1.73,1013,41,'clear sky','Clear'),('Chandigarh',22,3.07,1015,18,'clear sky','Clear'),('Dadra and Nagar Haveli',30,2.04,1013,25,'clear sky','Clear'),('Dadra',30,2.28,1013,28,'clear sky','Clear'),('Daman and Diu',28,3.17,1013,38,'clear sky','Clear'),('Daman',28,3.45,1013,41,'clear sky','Clear'),('Diu',28,3.89,1013,44,'clear sky','Clear'),('Delhi',22,2.06,1017,33,'smoke','Smoke'),('Mumbai',30,2.06,1013,29,'smoke','Smoke'),('Japan',19,5.14,1001,68,'broken clouds','Clouds');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-16 21:01:24
