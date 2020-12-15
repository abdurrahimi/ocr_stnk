-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 29, 2020 at 03:45 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mayasari_bakti`
--

-- --------------------------------------------------------

--
-- Table structure for table `log_user`
--

CREATE TABLE `log_user` (
  `id_log` int(10) NOT NULL,
  `id_admin` int(10) NOT NULL,
  `nama_pengguna` varchar(30) NOT NULL,
  `tanggal_login` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `log_user`
--

INSERT INTO `log_user` (`id_log`, `id_admin`, `nama_pengguna`, `tanggal_login`) VALUES
(1, 1, 'Rivita', '2020-05-01'),
(2, 1, 'Rivita', '2020-04-01');

-- --------------------------------------------------------

--
-- Table structure for table `setup_admin`
--

CREATE TABLE `setup_admin` (
  `id_admin` int(10) NOT NULL,
  `id_role` int(10) NOT NULL,
  `nama_pengguna` varchar(30) NOT NULL,
  `kata_sandi` varchar(30) NOT NULL,
  `nama_lengkap` varchar(30) NOT NULL,
  `dibuat_oleh` int(10) NOT NULL,
  `dibuat_tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `setup_admin`
--

INSERT INTO `setup_admin` (`id_admin`, `id_role`, `nama_pengguna`, `kata_sandi`, `nama_lengkap`, `dibuat_oleh`, `dibuat_tanggal`) VALUES
(1, 1, 'Rivita', '123', 'Rivita Anggun Octaviani', 1, '2020-04-03');

-- --------------------------------------------------------

--
-- Table structure for table `setup_role`
--

CREATE TABLE `setup_role` (
  `id_role` int(10) NOT NULL,
  `nama_role` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `setup_role`
--

INSERT INTO `setup_role` (`id_role`, `nama_role`) VALUES
(1, 'Super Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `stnk`
--

CREATE TABLE `stnk` (
  `id_stnk` int(10) NOT NULL,
  `nomor_registrasi` varchar(8) NOT NULL,
  `nama_pemilik` varchar(30) NOT NULL,
  `masa_berlaku` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stnk`
--

INSERT INTO `stnk` (`id_stnk`, `nomor_registrasi`, `nama_pemilik`, `masa_berlaku`) VALUES
(1, 'B4670TIQ', 'ABDUL CHOLIK', '2020-12-28'),
(2, 'B452H78G', 'SUPARMAN', '2020-05-30'),
(3, 'BUU23HUY', 'SUKIJAH', '2020-10-28');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `log_user`
--
ALTER TABLE `log_user`
  ADD PRIMARY KEY (`id_log`),
  ADD KEY `id_admin` (`id_admin`);

--
-- Indexes for table `setup_admin`
--
ALTER TABLE `setup_admin`
  ADD PRIMARY KEY (`id_admin`),
  ADD KEY `id_role` (`id_role`);

--
-- Indexes for table `setup_role`
--
ALTER TABLE `setup_role`
  ADD PRIMARY KEY (`id_role`);

--
-- Indexes for table `stnk`
--
ALTER TABLE `stnk`
  ADD PRIMARY KEY (`id_stnk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `log_user`
--
ALTER TABLE `log_user`
  MODIFY `id_log` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `setup_admin`
--
ALTER TABLE `setup_admin`
  MODIFY `id_admin` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `setup_role`
--
ALTER TABLE `setup_role`
  MODIFY `id_role` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `stnk`
--
ALTER TABLE `stnk`
  MODIFY `id_stnk` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `log_user`
--
ALTER TABLE `log_user`
  ADD CONSTRAINT `log_user_ibfk_1` FOREIGN KEY (`id_admin`) REFERENCES `setup_admin` (`id_admin`);

--
-- Constraints for table `setup_admin`
--
ALTER TABLE `setup_admin`
  ADD CONSTRAINT `setup_admin_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `setup_role` (`id_role`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
