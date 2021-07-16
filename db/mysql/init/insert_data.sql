
-- SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
-- START TRANSACTION;
-- SET time_zone = "+00:00";

-- Create table

CREATE TABLE `users` (
    `id` bigint UNSIGNED NOT NULL,
    `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'ユーザの表示名',
    `age` int UNSIGNED NOT NULL COMMENT 'ユーザーの年齢',
    `gender` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'ユーザの性別'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert sample datas

INSERT INTO `users` (`id`, `name`, `age`, `gender`) VALUES
(1, 'user1', '20', '男'),
(2, 'user2', '20', '女'),
(3, 'user3', '20', '男'),
(4, 'user4', '20', '女');