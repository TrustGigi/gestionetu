-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : sam. 14 nov. 2026 à 06:43
-- Version du serveur :  10.4.13-MariaDB
-- Version de PHP : 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestionetudiant_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `etudiant`
--

CREATE TABLE `etudiant` (
  `id` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `adresse` varchar(50) DEFAULT NULL,
  `nationalite` varchar(50) DEFAULT NULL,
  `tel` varchar(50) DEFAULT NULL,
  `sexe` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `etudiant`
--

INSERT INTO `etudiant` (`id`, `nom`, `prenom`, `adresse`, `nationalite`, `tel`, `sexe`, `age`) VALUES
(6, 'Kaneza', 'Danny', 'Kibenga', 'Francaise', '67928044', 'M', 33),
(7, 'Dusabe', 'Guillaume', 'Avenue 2 Gasekebuye', 'Burundaise', '71258963', 'M', 29),
(8, 'kakunze', 'Betina', 'Carama', 'Francaise', '65258741', 'F', 23),
(9, 'MANIRAKIZA', 'Hermes', 'Kajondi', 'Rwandaise', '71456258', 'M', 28),
(10, 'IRIHO', 'Brianna', 'Kanyosha', 'Burundaise', '71528963', 'F', 25),
(11, 'BUTOYI', 'Danny', 'Kinanira', 'Congolaise', '71565789', 'M', 28),
(12, 'IRAKOZE', 'Hope', 'Musaga', 'Congolaise', '71258963', 'F', 20),
(13, 'KANEZA', 'Ariella', 'Carama', 'Francaise', '61258741', 'F', 25),
(14, 'IRAKOZE', 'Fiston', 'Mutakura', 'Congolaise', '77582149', 'M', 34),
(15, 'BURIKUKIYE', 'Leonard', 'Bwiza', 'Burundaise', '77425693', 'M', 29),
(16, 'INEZA', 'Ange', 'Kirimiro', 'Burundaise', '64258369', 'F', 25),
(17, 'IRADUKUNDA', 'Bertrand', 'Kibenga', 'Francaise', '62456321', 'M', 20);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`) VALUES
(1, 'Dusabe', 'trustlord86@gmail.com', 'scrypt:32768:8:1$EoUMuDlEyITHa6iD$27381762b93116b84e031a13cef72d6bc77814ee289a88306c1d6879e4877a5635c4d923cdb5148a1d96ddc3e24d3433e567817f01b003977aa9993b3227bcb7'),
(2, 'Ciza', 'ci21@gmail.com', 'scrypt:32768:8:1$4AgnJaVsAgcjeJoT$dba15aeb9d063079339e4c782c7f604db06447ce9d254ce129a56290296f50af55ae9b7691c0a21b0d94a677eb48b19cf7fd9f37f55bf6e1435be53ca9df5ccb'),
(3, 'kiki', 'trustlord25@gmail.com', 'scrypt:32768:8:1$HmVNOslXcy302JrA$ae61d248b34981f924635a6aeb757b40288734baabe850b786287757312319be249cd32cc917d5114d99c67981dc8d462e57468acab8b7bc955e8aacec5a9ed5'),
(4, 'toto', 'toto@gmail.com', 'scrypt:32768:8:1$U5QV46L1fjOETdCE$39142b3225551e5f2441a1770d9fe14cbf6a13790a442cb28849080d7e13f412a2633a5c44f1db92e24d1b58faa32aefe54fa07dfb26718b44a43cda85298ccb'),
(6, 'lolo', 'lolo@gmail.com', 'scrypt:32768:8:1$VGtSmCKvfWvdDeMl$80d2a1bbff88f1b431c0429ba0d4122b08f4f896607824641c0c1ff2490c96bb508dba88efc659c5e8ac177fe661063bd544d50ed8258b49bb3337e16ac92e2f'),
(7, 'Kelly', 'keke@gmail.com', 'scrypt:32768:8:1$NVgjJMsMD7JfqfuA$12257893fd5ce4e81b68b1edf7fd73836d0ffe033ef92d0bb929ce963497c702ae4c9f09ee29a522eb13bfdf6f0ef02c6b6a7ec4742d16893645cecc2b979312'),
(8, 'kakunze', '', 'scrypt:32768:8:1$7uhCKJJOJSmd1ZS8$f8f1dd35b499573ea4c69723faf87a022f38e6f1a9501be556f6333a8c6842d8849888eff5abe778eb1dd726dc8a591f4f3c8a929663388344c6123196dfd9e5'),
(9, 'kakunze', 'kakunze@gmail.com', 'scrypt:32768:8:1$EWvPoeYt9XzMILXG$1bc2c21de6eb797c3f23f655ba9d51e68f0cb6bf3fa06490f2cddd3a321c6e357c14766d4eb392249e00b68326e703c57f47799a0a8c22beda073c4911930d23'),
(11, 'kiki', 't86@gmail.com', 'scrypt:32768:8:1$VR7UDh9GfetuOCLU$0f4240bf4fb5751bb9ba23a53a2c3cbe695e1e3ca33cd555b83cd412424411ce5b681533a4045ac74ac3a74d35b4ce5f6572c903879c3ad8336ea847724c301a'),
(14, 'nina', 'nina@gmail.com', 'scrypt:32768:8:1$zTpMx4Of4XdbMPoN$08e34eefa87e278bec203dfec7fa104633d52a942cb2fef57c40f9b4f40af2b25653c2a58a10f3f89d7048ac80e33920ce0ada1b6dd07dd6fd03cee99af9091b'),
(16, 'fjhfhhf', 'trustlordkkkkk86@gmail.com', 'scrypt:32768:8:1$fRLP7eagcBmPD7qz$d22c92c06c93a045c6591500d93e330498196e08ccb216d8306935aad6a24469d49d5ac26ea39004be4cb7f206491d874cb3eaf40a9f1be105b1d3916dabca80'),
(17, 'IRAKOZE', 'kelly12@gmail.com', 'scrypt:32768:8:1$R31EO95KisTkKJnS$7603c24d866e3da56fe138a9a35893d875b652c47c34a973d8096964999a8e791e0212dc45569063d5408de8d6689644dd9778bf56b4e3845a5aa4424faa5b0c'),
(18, 'kana', 'nana@gmail.com', 'scrypt:32768:8:1$KyP7NjXkZV5Gy2kB$3107af003cf9cb38d79f5a4a480f93b448765a514fabcbf9b2ce6267cd61e3d36a22f4dcf4c45dcc059920f4b5ee7dca3a876ba432b89b931619a6382f21cd85'),
(19, 'Ciza', 'ciza@gmail.com', 'scrypt:32768:8:1$vhxLdSpYFe1Bb1yz$8f5a927011753481bf5533bf98032a7caf85b798d8e5c674e6a16772e7b89bd2f5bf7cf2272cf3d3f326623cb0274992b962bc6b299e2fa667f85244d42a36d1'),
(20, 'dodo', 'dodo@gmail.com', 'scrypt:32768:8:1$MQv6Mi5t1wA55Wbi$8b8a34e79566371c01e89d2362f3bfac095347e4a86364466ae9e42b172dfc29b71be8efe44802d93f75a2a38b762a4de59f9e6b13c62193189d9195fc4e8759'),
(21, 'Hope', 'hope@gmail.com', 'scrypt:32768:8:1$FHoLhrjSvqTO6I4T$c720f3bf1e329ab24145ad96a79bb345e5f73f5c3e16a855533b5ad32320612b1be6b0a379edca03b091bdb96aecd7469837e5df37789fe148d5e9080c00a8b4');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `etudiant`
--
ALTER TABLE `etudiant`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `etudiant`
--
ALTER TABLE `etudiant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
