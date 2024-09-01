/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema DnD_Database
--

CREATE DATABASE IF NOT EXISTS DnD_Database;
USE DnD_Database;

--
-- Homebrew
--

--
-- Definition of table `DnD_Database`.`potions`
--

DROP TABLE IF EXISTS `DnD_Database`.`potions`;
CREATE TABLE  `DnD_Database`.`potions` (
  `potion_id` bigint(20) unsigned NOT NULL auto_increment,
  `potion_name` varchar(255) default NULL,
  `potion_descr` text,
  `potion_rarity` char(20) default NULL,
  `homebrew_id` bigint(20) unsigned NOT NULL,
  `oname` char(20) default NULL,
  PRIMARY KEY  (`potion_id`),
  UNIQUE KEY `potion_id` (`potion_id`),
  KEY `FK_potions_organization` (`oname`),
  KEY `FK_homebrew_potions` (`homebrew_id`),
  CONSTRAINT `FK_potions_organization` FOREIGN KEY (`oname`) REFERENCES `organization` (`oname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DnD_Database`.`potions`
--
/*!40000 ALTER TABLE `potions` DISABLE KEYS */;
LOCK TABLES `potions` WRITE;
INSERT INTO `DnD_Database`.`potions` VALUES  (10001, 'Potion of Restoration', 'when used, grants same benefits as revivify on dead target and greater restoration on alive target', 'very rare', 111, 'The Outcast Guild'),
(10002, 'Potion of Wildmagic', 'when consumed, user gets advantage on the next saving throw, attack role, or ability check of their choice within an hour; when adv. is used, it triggers a wild magic surge', 'uncommon', 112, 'The Outcast Guild'),
(10003, 'Hydra Lotion', 'apply this to yourslef or ally for healing (2D6) at the start of each round; fire damage supresses the healing', 'rare', 113, 'The Outcast Guild'),
(10004, 'Divina-Tea', 'when consumed, potion tastes like herbal tea and has no affect unless consumed by a monk; when consumed in such a way, they regain key points', 'varies', 114, 'The Outcast Guild'),
(10005, 'Mages Restoration Potion', 'this allows the user to regain spell slots equal to or less than the combined level rolled; die is determined by rarity and only one can be consumed per day (or wild magic surge happens)', 'varies', 115, 'The Outcast Guild'),
(10006, 'Solar Flare Potion', 'when the object is thrown, it reupts and sunlight is centered on that point; it lasts for a minute', 'rare', 116, 'The Outcast Guild'),
(10007, 'Potion of DaWizard', 'when consumed, all attacks a creature makes are considered magical for overcoming resistance and immunity', 'uncommon', 117, 'The Outcast Guild'),
(10008, 'Essential Oils', 'can coat a weapon or ammo, it deals 2D6 damage; damage type determined by potion', 'rare variety', 118, 'The Outcast Guild'),
(10009, 'Potion of Polymorph', 'when consumed, creature is under the effects of polymorph', 'rare variety', 119, 'The Outcast Guild'),
(100010, 'Potion of Disguise', 'when consumed, the users space is malleable and allows them to alter their appearance; this lasts for an hour and the stat block stays the same', 'uncommon', 120, 'The Outcast Guild'),
(100011, 'Draught of Rejuvinating Slumber', 'when consumed, a wave of tranquility washes over you and your weariness melts away', 'rare', 121, 'Happy Beholder'),
(100012, 'Elixr of the Hero Feast', 'when consumed, you feel an immediate surge of vitality and well-being', 'very rare', 122, 'Happy Beholder'),
(100013, 'Potion of Arcane Insight', 'when consumed, you gain a temporary boost to your magical abilities; lasts an hour (save DC and spell bonus increase by 2, adv on intelligence (Arcana) checks, cast one 1st level spell without expanding spell slot)', 'uncommon', 123, 'Happy Beholder'),
(100014, 'Brew of the Iron Will', 'when consumed, you gain the following benefits for the next 8 hours: (immunity to being charmed or freightened, adv on wisdom and charisma saving throws, can reroll one saving throw during potion effect)', 'rare', 124, 'Happy Beholder'),
(100015, 'Tonic of Swift Reflixes', 'when consumed, you gain these benefits for an hour: (movement speed inc. by 10, adv. on dexterity saving throws, you gain +2 to AC)', 'uncommon', 125, 'Happy Beholder'),
(100016, 'Potion of Shadow Morph', 'once ingested, it will turn creature into opaque image of themself and give: (adv. on stealth check, movement speed halved in bright environment, ability to hop from shadow to shadow)', 'uncommon', 126, 'StarFrost');
UNLOCK TABLES;
/*!40000 ALTER TABLE `potions` ENABLE KEYS */;

--
-- Definition of table `DnD_Database`.`shops`
--
DROP TABLE IF EXISTS `DnD_Database`.`shops`;
CREATE TABLE  `DnD_Database`.`shops` (
  `shop_id` bigint(20) unsigned NOT NULL,
  `shop_name` varchar(255) default NULL,
  `shop_location` varchar(255) default NULL,
  `shop_owner` varchar(255) default NULL,
  `location_id` bigint(20) unsigned NOT NULL,
  `npc_id` bigint(20) unsigned NOT NULL,
  `oname` char(20) default NULL,
  PRIMARY KEY  (`shop_id`),
  UNIQUE KEY `shop_id` (`shop_id`),
  KEY `FK_npcs_shops` (`npc_id`),
  KEY `FK_shops_npcs` (`shop_id`),
  KEY `FK_shops_locations` (`shop_id`),
  KEY `FK_shops_organization` (`oname`),
  KEY `FK_locations_shops` (`location_id`),
  CONSTRAINT `FK_shops_npcs` FOREIGN KEY (`shop_id`) REFERENCES `npcs` (`shop_id`),
  CONSTRAINT `FK_shops_locations` FOREIGN KEY (`shop_id`) REFERENCES `locations` (`shop_id`),
  CONSTRAINT `FK_shops_organization` FOREIGN KEY (`oname`) REFERENCES `organization` (`oname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DnD_Database`.`shops`
--
/*!40000 ALTER TABLE `shops` DISABLE KEYS */;
LOCK TABLES `shops` WRITE;
INSERT INTO `DnD_Database`.`shops` VALUES (500, 'Alor Magically Discounted Wares', 'Riven', 'Alor', 400, 300, 'Happy Beholder'),
(501, 'The Happy Beholder', 'Voros', 'Large Luigi', 401, 301, 'Happy Beholder'),
(502, 'Falling Tavern', 'Fey Wild', 'Blom', 402, 302, 'StarFrost'),
(503, 'Dwarf-R-Us', 'Crystal Meadows', 'Stephe', 403, 303, 'StarFrost'),
(504, 'Dwarvington Forge', 'Outcast Guild', 'Domar Dwarvington the Third', 404, 304, 'The Outcast Guild'),
(505, 'Broken Horn', 'varies', 'Bang', 405, 305, 'The Outcast Guild'),
(506, 'The Leaky Quill', 'Shaven', 'Tazlint', 406, 306, 'The Outcast Guild'),
(507, 'The Cracked Cauldren', 'Drakkenfizzer', 'Egan The Great', 407, 307, 'The Outcast Guild'),
(508, 'Doa Hammer', 'Yukigawa', 'Sunny D. Andesine', 408, 308, 'The Outcast Guild'),
(509, 'Gear Forge Enterprises', 'Alatos', 'Marcus Flintlock', 409, 309, 'The Outcast Guild'),
(510, 'Mystical Menagerie', 'Great Forest of Hewrt', 'Magnus Moonshadow', 410, 310, 'The Outcast Guild'),
(511, 'Kranky Forge', 'Krezk', 'Kranky', 411, 311, 'The Outcast Guild');
UNLOCK TABLES;
/*!40000 ALTER TABLE `shops` ENABLE KEYS */;


--
-- Definition of table `DnD_Database`.`npcs`
--
DROP TABLE IF EXISTS `DnD_Database`.`npcs`;
CREATE TABLE  `DnD_Database`.`npcs` (
  `npc_id` bigint(20) unsigned NOT NULL auto_increment,
  `npc_first` varchar(255) default NULL,
  `npc_last` varchar(255) default NULL,
  `npc_class` varchar(255) default NULL,
  `npc_race` varchar(255) default NULL,
  `npc_occupation` varchar(255) default NULL,
  `npc_realm` varchar(255) default NULL,
  `shop_id` bigint(20) unsigned NOT NULL,
  `oname` char(20) default NULL,
  PRIMARY KEY  (`npc_id`),
  UNIQUE KEY `npc_id` (`npc_id`),
  KEY `FK_npcs_organization` (`oname`),
  KEY `FK_shops_npcs` (`shop_id`),
  KEY `FK_npcs_shops` (`npc_id`),
  CONSTRAINT `FK_npcs_shops` FOREIGN KEY (`npc_id`) REFERENCES `shops` (`npc_id`),
  CONSTRAINT `FK_npcs_organization` FOREIGN KEY (`oname`) REFERENCES `organization` (`oname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DnD_Database`.`npcs`
--
/*!40000 ALTER TABLE `npcs` DISABLE KEYS */;
LOCK TABLES `npcs` WRITE;
INSERT INTO `DnD_Database`.`npcs` VALUES (300, 'Alor', NULL, 'wizard', 'elf', 'Magic Item Scavenger', 'The Land Between', 500, 'Happy Beholder'),
(301, 'Large', 'Luigi', 'god', 'Beholder', 'Tavern Owner', 'The Land Between', 501, 'Happy Beholder'),
(302, 'Blom', NULL, NULL, 'Eladrin', 'Tavern Owner', NULL, 502, 'StarFrost'),
(303, 'Stephe', NULL, 'artificer', 'dwarf', 'Shopkeep', NULL, 503, 'StarFrost'),
(304, 'Domar', 'Dwarvington', 'cleric', 'goliath', 'Forge Master', 'Idreal', 504, 'The Outcast Guild'),
(305, 'Bang', NULL, 'artificier', 'tiefling', 'alchemist', 'Idreal', 505, 'The Outcast Guild'),
(306, 'Tazlint', NULL, 'wizard', 'kalashtar', 'mage', 'Idreal', 506, 'The Outcast Guild'),
(307, 'Egan', NULL, 'wizard', 'kobold', 'mage', 'Idreal', 507, 'The Outcast Guild'),
(308, 'Sunny', 'Andesine', 'artificier', 'dragonborn', 'alchemist', 'Idreal', 508, 'The Outcast Guild'),
(309, 'Marcus', 'Flintlock', 'artificier', 'tiefling', 'inventor', 'Prismatic Falls', 509, 'The Outcast Guild'),
(310, 'Mangus', 'Moonshadow', NULL, 'fairy', 'beast guardian', 'Fey Wild', 510, 'The Outcast Guild'),
(311, 'Kranky', NULL, NULL, 'goliath', 'retired', 'Barovia', 511, 'The Outcast Guild');
UNLOCK TABLES;
/*!40000 ALTER TABLE `npcs` ENABLE KEYS */;

--
-- Definition of table `DnD_Database`.`locations`
--
DROP TABLE IF EXISTS `DnD_Database`.`locations`;
CREATE TABLE  `DnD_Database`.`locations` (
  `location_id` bigint(20) unsigned NOT NULL auto_increment,
  `loc_name` varchar(255) default NULL,
  `loc_environemnt` varchar(255) default NULL,
  `loc_realm` varchar(255) default NULL,
  `location_descr` text,
  `shop_id` bigint(20) unsigned NOT NULL,
  `oname` char(20) default NULL,
  PRIMARY KEY  (`location_id`),
  UNIQUE KEY `location_id` (`location_id`),
  KEY `FK_locations_organization` (`oname`),
  KEY `FK_locations_shops` (`location_id`),
  KEY `FK_shops_locations` (`shop_id`),
  CONSTRAINT `FK_locations_shops` FOREIGN KEY (`location_id`) REFERENCES `shops` (`location_id`),
  CONSTRAINT `FK_locations_organization` FOREIGN KEY (`oname`) REFERENCES `organization` (`oname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 

--
-- Dumping data for table `DnD_Database`.`locations`
--
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
LOCK TABLES `locations` WRITE;
INSERT INTO `DnD_Database`.`locations` VALUES (400, 'Riven', 'urban', 'The Land Between', 'a town owned by the Crimson Court and is a part of the Ostoyan Empire', 500, 'Happy Beholder'),
(401, 'Voros', 'urban', 'The Land Between', 'a town in the Charneault Kingdom, the Kingdom of the Elves', 501, 'Happy Beholder'),
(402, 'Fey Wild', 'rural', 'Fey Wild', 'the chaotic realm of the fey', 502, 'StarFrost'),
(403, 'Crystal Meadows', 'urban', NULL, 'a city located in the Amethyst mountain range', 503, 'StarFrost'),
(404, 'Outcast Guild', 'floating islands', 'realm of possibilities', 'a two story oak building resting upon a floating island in a sey of possibility', 504, 'The Outcast Guild'),
(405, 'varies', 'varies', 'varies', 'varies', 505, 'The Outcast Guild'),
(406, 'Shaven', 'urban', 'Idreal', 'advanced arcane city that wishes to lead Atlanther into a brighter future', 506, 'The Outcast Guild'),
(407, 'Drakkenfizzer', 'arcane wasteland', 'Idreal', 'a remnant from a city from a world long destroyed', 507, 'The Outcast Guild'),
(408, 'Yukigawa', 'elemental', 'Idreal', 'a hotspring city', 508, 'The Outcast Guild'),
(409, 'Alatos', 'urban', 'Idreal', 'the capital of the province of Silver and the origin point on artificery', 509, 'The Outcast Guild'),
(410, 'Great Forest of Hewrt', 'forest', 'Idreal', 'the point in Idreal where the Fey Wild and the prime material cross over greatly', 510, 'The Outcast Guild'),
(411, 'Crezk', 'rural', 'Barovia', 'small mountain villiage', 511, 'The Outcast Guild');
UNLOCK TABLES;
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;

--
-- Definition of table `DnD_Database`.`homebrew_items`
--
DROP TABLE IF EXISTS `DnD_Database`.`homebrew_items`;
CREATE TABLE  `DnD_Database`.`homebrew_items` (
  `homebrew_id` bigint(20) unsigned NOT NULL auto_increment,
  `hb_name` varchar(255) default NULL,
  `homebrew_descr` text,
  `hb_rarity` char(20) default NULL,
  `oname` char(20) default NULL,
  PRIMARY KEY  (`homebrew_id`),
  UNIQUE KEY `homebrew_id` (`homebrew_id`),
  KEY `FK_homebrew_potions` (`homebrew_id`),
  CONSTRAINT `FK_homebrew_potions` FOREIGN KEY (`homebrew_id`) REFERENCES `potions` (`homebrew_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 

--
-- Dumping data for table `DnD_Database`.`homebrew items`
--
/*!40000 ALTER TABLE `homebrew_items` DISABLE KEYS */;
LOCK TABLES `homebrew_items` WRITE;
INSERT INTO `DnD_Database`.`homebrew_items` VALUES (111, 'Potion of Restoration', 'when used, grants same benefits as revivify on dead target and greater restoration on alive target', 'very rare', 'The Outcast Guild'),
(112, 'Potion of Wildmagic', 'when consumed, user gets advantage on the next saving throw, attack role, or ability check of their choice within an hour; when adv. is used, it triggers a wild magic surge', 'uncommon','The Outcast Guild'),
(113, 'Hydra Lotion', 'apply this to yourslef or ally for healing (2D6) at the start of each round; fire damage supresses the healing', 'rare', 'The Outcast Guild'),
(114, 'Divina-Tea', 'when consumed, potion tastes like herbal tea and has no affect unless consumed by a monk; when consumed in such a way, they regain key points', 'varies', 'The Outcast Guild'),
(115, 'Mages Restoration Potion', 'this allows the user to regain spell slots equal to or less than the combined level rolled; die is determined by rarity and only one can be consumed per day (or wild magic surge happens)', 'varies', 'The Outcast Guild'),
(116, 'Solar Flare Potion', 'when the object is thrown, it reupts and sunlight is centered on that point; it lasts for a minute', 'rare', 'The Outcast Guild'),
(117, 'Potion of DaWizard', 'when consumed, all attacks a creature makes are considered magical for overcoming resistance and immunity', 'uncommon', 'The Outcast Guild'),
(118, 'Essential Oils', 'can coat a weapon or ammo, it deals 2D6 damage; damage type determined by potion', 'rare variety', 'The Outcast Guild'),
(119, 'Potion of Polymorph', 'when consumed, creature is under the effects of polymorph', 'rare variety', 'The Outcast Guild'),
(120, 'Potion of Disguise', 'when consumed, the users space is malleable and allows them to alter their appearance; this lasts for an hour and the stat block stays the same', 'uncommon', 'The Outcast Guild'),
(121, 'Draught of Rejuvinating Slumber', 'when consumed, a wave of tranquility washes over you and your weariness melts away', 'rare', 'Happy Beholder'),
(122, 'Elixr of the Hero Feast', 'when consumed, you feel an immediate surge of vitality and well-being', 'very rare', 'Happy Beholder'),
(123, 'Potion of Arcane Insight', 'when consumed, you gain a temporary boost to your magical abilities; lasts an hour (save DC and spell bonus increase by 2, adv on intelligence (Arcana) checks, cast one 1st level spell without expanding spell slot)', 'uncommon', 'Happy Beholder'),
(124, 'Brew of the Iron Will', 'when consumed, you gain the following benefits for the next 8 hours: (immunity to being charmed or freightened, adv on wisdom and charisma saving throws, can reroll one saving throw during potion effect)', 'rare', 'Happy Beholder'),
(125, 'Tonic of Swift Reflixes', 'when consumed, you gain these benefits for an hour: (movement speed inc. by 10, adv. on dexterity saving throws, you gain +2 to AC)', 'uncommon', 'Happy Beholder'),
(126, 'Potion of Shadow Morph', 'once ingested, it will turn creature into opaque image of themself and give: (adv. on stealth check, movement speed halved in bright environment, ability to hop from shadow to shadow)', 'uncommon', 'StarFrost'),
(127, 'Shield of Throwing', 'when worn gives a +1 to armor class. When attuned, the shield gains a +1 to attack and damage rolls along with the thrown property at a range of 30ft', 'very rare', 'The Outcast Guild'),
(128, 'Ban Hammer', 'takes the form of a comidicaly large wooden mallet with a crudly drawn angry face; +3 to attack and Damage rolls aditionaly whenever you score a critical hit with this weapon, you can force the target to make a DC 16 Charisma saving throw', 'very rare', 'The Outcast Guild'),
(129, 'Mask of Charming', 'the mask of charming comes in the form of a full porcelain mask and is said to hold the essence of beauty while wearing this mask Your Charisma score is 19; In addition, you have advantage on all Charisma (persuasion) and Charisma (deception) checks when wearing the mask.', 'uncommon', 'The Outcast Guild'),
(130, 'Skepticals', 'while wearing these glasses Your wisdom score is 19; In addition, you have advantage on all wisdom (insight) checks when wearing the glasses.', 'uncommon', 'The Outcast Guild'),
(131, 'The Boomstick', 'while attuned to this +1 weapon you deal an additional d6 thunder damage whenever you hit a creature and the weapon gains 6 charges regaining 1d4+2 charges each dawn. Spending a charge you can cast one of the following spells, each with a save DC of 15; Spending 1 charge cast thunder wave with the spell’s level increasing by one for every additional charge spent. Spending 2 charges allows you to cast thunderous smite without requiring concentration', 'very rare', 'The Outcast Guild'),
(132, 'Ki Bands', 'while Wearing these silver hand wraps, you gain a bonus to your unarmed strikes attack and damage rolls determined by the band’s rarity. In addition, when you land a critical hit on a creature you regain a number of ki points equal to your proficiency + the bands’ bonus to attack rolls.', 'varies', 'The Outcast Guild'),
(133, 'Blades of Redemption', 'you have a +1 bonus to attack and damage rolls made with this magic weapon', 'rare', 'Happy Beholder'),
(134, 'Selys-Lyann', 'a Scimitar infused with frost. The wielder can expend one of 3 of its charges to throw a ray of frost at a target. Target must succeed a CON saving throw of 17, on success freezes in place and take 3d6 frost damage', 'uncommon', 'Happy Beholder'),
(135, 'The Book Of Shadows', 'a book that was used by a powerful demon to gain contact with the mortal plain', 'very rare', 'StarFrost'),
(136, 'Shadow Tendril Blade', 'this sword acts as a normal +1 sword aside from the grapple ability: upon a hit the wielder can choose to make the sword grapple the creature DC STR+6 check for the person to resist the grapple ', 'very rare', 'StarFrost'),
(137, 'Black Void', 'a cantrip; The user absorbs shadows from around them and conjoins with them. This allows them to move freely inside the shadows; This cantrip breaks once they make an attack action', 'very rare', 'StarFrost'),
(138, 'Shadow Shot', 'the caster can shoot one person in sight with a shadow-binding arrow. The creature must pass a Strength saving throw. If they are successful they will take 1D4+4 piercing damage and 1 D8 necrotic. On a fail, they take 2 D4+4 and 2 D8. At higher levels, you add an additional D8', 'very rare', 'StarFrost');
UNLOCK TABLES;
/*!40000 ALTER TABLE `homebrew_items` ENABLE KEYS */;

--
-- Definition of table `DnD_Database`.`monsters`
--
DROP TABLE IF EXISTS `DnD_Database`.`monsters`;
CREATE TABLE  `DnD_Database`.`monsters` (
  `monster_id` bigint(20) unsigned NOT NULL auto_increment,
  `monster_name` varchar(255) default NULL,
  `monster_descr` text,
  `monster_cr` smallint(6) default NULL,
  `monster_type` varchar(255) default NULL,
  `oname` char(20) default NULL,
  PRIMARY KEY  (`monster_id`),
  UNIQUE KEY `monster_id` (`monster_id`),
  KEY `FK_monster_organization` (`oname`),
  CONSTRAINT `FK_homebrew_organization` FOREIGN KEY (`oname`) REFERENCES `organization` (`oname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DnD_Database`.`monsters`
--
/*!40000 ALTER TABLE `monsters` DISABLE KEYS */;
LOCK TABLES `monsters` WRITE;
INSERT INTO `DnD_Database`.`monsters` VALUES (800, 'Capyhorror', 'a creature that conceals its true nature beneath the innocent guise of a capybara.', 0.5, 'beast', 'Leo Lebrón'),
(801, 'H.A.L. Draco', 'Also known as the Hallucination-inducing Automated Locomotive Dragon, this is a variant on the SPD01-036. This is a nightmarish entity that strikes fear into the hearts of adventurers brave enough to challenge its dominion.', 16, 'construct', 'Leo Lebrón'),
(802, 'Phrump', 'The Phrump is a truly extraordinary creature, a whimsical creation born from the mystical energies of the Rift. It is a charming amalgamation of a sheep, a goat, and a balloon, resulting in a sight that defies conventional logic. The most remarkable aspect of the Phrump is its ability to effortlessly float above the ground, never making contact with the earth below.', 0.5, 'beast', 'Leo Lebrón'),
(803, 'Fate Weaver Scarab', 'The Fate Weaver Scarab is a mesmerizing creature that exudes an aura of mystery and power.', 10, 'monstrosity', 'Leo Lebrón'),
(804, 'The GFW', 'a magical abomination that should never have existed', 17, 'monstrosity', 'The Outcast Guild'),
(805, 'Duskfallen Eternal Loneliness', 'the emboddiment of depression', 8, 'fey', 'The Outcast Guild'),
(806, 'Umbral Stalker', 'make your players afraid of the dark', 8, 'construct', 'The Outcast Guild'),
(807, 'Umbral Infiltrator', 'the perfect spy', 9, 'construct', 'The Outcast Guild'),
(808, 'Umbral Slayer', 'a mages worst enemy', 9, 'construct', 'The Outcast Guild'),
(809, 'Umbral Dreadnaut', 'the monster under the bed', 12, 'construct', 'The Outcast Guild'),
(810, 'Knight Stalker', 'a tall bird-looking creature with four arms', 10, 'monstrosity', 'StarFrost'),
(811, 'Shadow Golem', 'a 13-foot tall creature built of shadow and darkness this Golem is able to lift creatures of large sizes and smaller', 0, 'construct', 'StarFrost');
UNLOCK TABLES;
/*!40000 ALTER TABLE `monsters` ENABLE KEYS */;

--
-- Definition of table `DnD_Database`.`organization`
--
DROP TABLE IF EXISTS `DnD_Database`.`organization`;
CREATE TABLE  `DnD_Database`.`organization` (
  `organization_id` bigint(20) unsigned NOT NULL auto_increment,
  `oname` char(20) default NULL,
  `org_owner` varchar(255) default NULL,
  PRIMARY KEY  (`organization_id`),
  UNIQUE KEY `organization_id` (`organization_id`),
  KEY `FK_locations_organization` (`oname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DnD_Database`.`organization`
--
/*!40000 ALTER TABLE `organization` DISABLE KEYS */;
LOCK TABLES `organization` WRITE;
INSERT INTO `DnD_Database`.`organization` VALUES (600, 'The Outcast Guild', 'Geeks'),
(601, 'Happy Beholder', 'Luna'),
(602, 'StarFrost', 'Dani'),
(604, 'Leo Lebrón', 'Leo');
UNLOCK TABLES;
/*!40000 ALTER TABLE `organization` ENABLE KEYS */;

--
-- Non-homebrew
--

-- define dnd classes and synergistic races
DROP TABLE IF EXISTS `DnD_Database`.`class`;
CREATE TABLE  `DnD_Database`.`class` (
  `class_id` bigint(20) unsigned NOT NULL auto_increment,
  `class_name` varchar(255) default NULL,
  `synergy_1` varchar(255) default NULL,
  `synergy_2` varchar(255) default NULL,
  `synergy_3` varchar(255) default NULL,
  PRIMARY KEY  (`class_id`),
  UNIQUE KEY `class_id` (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DnD_Database`.`class`
--
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
LOCK TABLES `class` WRITE;
INSERT INTO `DnD_Database`.`class` (`class_name`, `synergy_1`, `synergy_2`, `synergy_3`) VALUES 
  ('Barbarian', 'Dragonborn', 'Half-Orc', 'Goliath'),
  ('Bard', 'Elf', 'Half-Elf', 'Tiefling'),
  ('Cleric', 'Dwarf', 'Human', 'Aasimar'),
  ('Druid', 'Elf', 'Halfling', 'Firbolg'),
  ('Fighter', 'Human', 'Dwarf', 'Half-Orc'),
  ('Monk', 'Human', 'Aarakocra', 'Elf'),
  ('Paladin', 'Human', 'Dragonborn', 'Half-Elf'),
  ('Ranger', 'Elf', 'Halfling', 'Human'),
  ('Rogue', 'Halfling', 'Half-Elf', 'Tiefling'),
  ('Sorcerer', 'Dragonborn', 'Tiefling', 'Aasimar'),
  ('Warlock', 'Tiefling', 'Half-Elf', 'Human'),
  ('Wizard', 'Elf', 'Human', 'Gnome'),
  ('Artificer', 'Gnome', 'Human', 'Dwarf'),
  ('Blood Hunter', 'Human', 'Half-Elf', 'Tiefling');
UNLOCK TABLES;
/*!40000 ALTER TABLE `class` ENABLE KEYS */;


-- define dnd race table
DROP TABLE IF EXISTS `DnD_Database`.`race`;
CREATE TABLE  `DnD_Database`.`race` (
  `race_id` bigint(20) unsigned NOT NULL auto_increment,
  `race_name` varchar(255) default NULL,
  PRIMARY KEY  (`race_id`),
  UNIQUE KEY `race_id` (`race_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DnD_Database`.`race`
--

/*!40000 ALTER TABLE `race` DISABLE KEYS */;
LOCK TABLES `race` WRITE;
INSERT INTO `DnD_Database`.`race` (`race_name`) VALUES 
  ('Dragonborn'),
  ('Dwarf'),
  ('Elf'),
  ('Gnome'),
  ('Half-Elf'),
  ('Half-Orc'),
  ('Halfling'),
  ('Human'),
  ('Tiefling'),
  ('Aarakocra'),
  ('Genasi'),
  ('Goliath'),
  ('Aasimar'),
  ('Bugbear'),
  ('Firbolg'),
  ('Goblin'),
  ('Hobgoblin'),
  ('Kenku'),
  ('Kobold'),
  ('Lizardfolk'),
  ('Orc'),
  ('Tabaxi'),
  ('Triton'),
  ('Yuan-ti Pureblood');
UNLOCK TABLES;
/*!40000 ALTER TABLE `race` ENABLE KEYS */;

-- Create items table without foreign keys
DROP TABLE IF EXISTS `DnD_Database`.`items`;
CREATE TABLE `DnD_Database`.`items` (
  `item_id` bigint(20) unsigned NOT NULL auto_increment,
  `weapon_id` bigint(20) unsigned default NULL,
  `armor_id` bigint(20) unsigned default NULL,
  `spell_id` bigint(20) unsigned default NULL,
  `magic_id` bigint(20) unsigned default NULL,
  `iname` varchar(255) default NULL,
  `itype` varchar(255) default NULL,
  `irarity` varchar(255) default NULL,
  PRIMARY KEY (`item_id`),
  UNIQUE KEY `item_id` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- dump weapons into items table
/*!40000 ALTER TABLE `DnD_Database`.`items` DISABLE KEYS */;
LOCK TABLES `DnD_Database`.`items` WRITE;

INSERT INTO `DnD_Database`.`items` (`weapon_id`,`iname`, `itype`, `irarity`) VALUES 
  (1, 'Club', 'Weapon', 'Common'),
  (2, 'Dagger', 'Weapon', 'Common'),
  (3, 'Greatclub', 'Weapon', 'Common'),
  (4, 'Handaxe', 'Weapon', 'Common'),
  (5, 'Javelin', 'Weapon', 'Common'),
  (6, 'Light Hammer', 'Weapon', 'Common'),
  (7, 'Mace', 'Weapon', 'Common'),
  (8, 'Quarterstaff', 'Weapon', 'Common'),
  (9, 'Sickle', 'Weapon', 'Common'),
  (10, 'Spear', 'Weapon', 'Common'),
  (11, 'Crossbow, Light', 'Weapon', 'Common'),
  (12, 'Dart', 'Weapon', 'Common'),
  (13, 'Shortbow', 'Weapon', 'Common'),
  (14, 'Sling', 'Weapon', 'Common'),
  (15, 'Battleaxe', 'Weapon', 'Common'),
  (16, 'Flail', 'Weapon', 'Common'),
  (17, 'Glaive', 'Weapon', 'Common'),
  (18, 'Greataxe', 'Weapon', 'Common'),
  (19, 'Greatsword', 'Weapon', 'Common'),
  (20, 'Halberd', 'Weapon', 'Common');

UNLOCK TABLES;
/*!40000 ALTER TABLE `DnD_Database`.`items` ENABLE KEYS */;

-- dump armor into items
/*!40000 ALTER TABLE `DnD_Database`.`items` DISABLE KEYS */;
LOCK TABLES `DnD_Database`.`items` WRITE;

INSERT INTO `DnD_Database`.`items` (`armor_id`, `iname`, `itype`, `irarity`) VALUES 
  (21, 'Padded Armor', 'Armor', 'Common'),
  (22, 'Leather Armor', 'Armor', 'Common'),
  (23, 'Studded Leather Armor', 'Armor', 'Common'),
  (24, 'Hide Armor', 'Armor', 'Common'),
  (25, 'Chain Shirt', 'Armor', 'Common'),
  (26, 'Scale Mail', 'Armor', 'Common'),
  (27, 'Breastplate', 'Armor', 'Common'),
  (28, 'Half Plate Armor', 'Armor', 'Common'),
  (29, 'Ring Mail', 'Armor', 'Common'),
  (30, 'Chain Mail', 'Armor', 'Common');

UNLOCK TABLES;
/*!40000 ALTER TABLE `DnD_Database`.`items` ENABLE KEYS */;

-- dump spells into items
/*!40000 ALTER TABLE `DnD_Database`.`items` DISABLE KEYS */;
LOCK TABLES `DnD_Database`.`items` WRITE;

INSERT INTO `DnD_Database`.`items` (`spell_id`, `iname`, `itype`, `irarity`) VALUES 
  (31, 'Fireball', 'Spell', 'Common'),
  (32, 'Magic Missile', 'Spell', 'Common'),
  (33, 'Shield', 'Spell', 'Common'),
  (34, 'Mage Armor', 'Spell', 'Common'),
  (35, 'Cure Wounds', 'Spell', 'Common'),
  (36, 'Bless', 'Spell', 'Common'),
  (37, 'Detect Magic', 'Spell', 'Common'),
  (38, 'Dispel Magic', 'Spell', 'Common'),
  (39, 'Lightning Bolt', 'Spell', 'Common'),
  (40, 'Fly', 'Spell', 'Common'),
  (41, 'Invisibility', 'Spell', 'Common'),
  (42, 'Polymorph', 'Spell', 'Common'),
  (43, 'Counterspell', 'Spell', 'Common'),
  (44, 'Healing Word', 'Spell', 'Common'),
  (45, 'Silence', 'Spell', 'Common');

UNLOCK TABLES;
/*!40000 ALTER TABLE `DnD_Database`.`items` ENABLE KEYS */;



-- Create weapons table
DROP TABLE IF EXISTS `DnD_Database`.`weapons`;
CREATE TABLE `DnD_Database`.`weapons` (
  `item_id` bigint(20) unsigned NOT NULL,
  `weapon_id` bigint(20) unsigned NOT NULL auto_increment,
  `weapon_name` varchar(255) default NULL,
  `weapon_stat` varchar(255) default NULL,
  `weapon_type` varchar(255) default NULL,
  `weapon_properties` varchar(255) default NULL,
  `weapon_damage_die` varchar(255) default NULL,
  PRIMARY KEY (`weapon_id`),
  FOREIGN KEY (`item_id`) REFERENCES `DnD_Database`.`items` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Insert common weapons into the weapons table
/*!40000 ALTER TABLE `DnD_Database`.`weapons` DISABLE KEYS */;
LOCK TABLES `DnD_Database`.`weapons` WRITE;

-- dump data into weapons table

INSERT INTO `DnD_Database`.`weapons` (`item_id`, `weapon_name`, `weapon_stat`, `weapon_type`, `weapon_properties`, `weapon_damage_die`) VALUES 
  (1, 'Club', 'STR', 'Simple Melee', 'Light', '1d4 bludgeoning'),
  (2, 'Dagger', 'DEX', 'Simple Melee', 'Finesse, Light, Thrown (range 20/60)', '1d4 piercing'),
  (3, 'Greatclub', 'STR', 'Simple Melee', 'Two-handed', '1d8 bludgeoning'),
  (4, 'Handaxe', 'STR', 'Simple Melee', 'Light, Thrown (range 20/60)', '1d6 slashing'),
  (5, 'Javelin', 'STR', 'Simple Melee', 'Thrown (range 30/120)', '1d6 piercing'),
  (6, 'Light Hammer', 'STR', 'Simple Melee', 'Light, Thrown (range 20/60)', '1d4 bludgeoning'),
  (7, 'Mace', 'STR', 'Simple Melee', '', '1d6 bludgeoning'),
  (8, 'Quarterstaff', 'STR', 'Simple Melee', 'Versatile (1d8)', '1d6 bludgeoning'),
  (9, 'Sickle', 'STR', 'Simple Melee', 'Light', '1d4 slashing'),
  (10, 'Spear', 'STR', 'Simple Melee', 'Thrown (range 20/60), Versatile (1d8)', '1d6 piercing'),
  (11, 'Crossbow, Light', 'DEX', 'Simple Ranged', 'Ammunition (range 80/320), Loading, Two-handed', '1d8 piercing'),
  (12, 'Dart', 'DEX', 'Simple Ranged', 'Finesse, Thrown (range 20/60)', '1d4 piercing'),
  (13, 'Shortbow', 'DEX', 'Simple Ranged', 'Ammunition (range 80/320), Two-handed', '1d6 piercing'),
  (14, 'Sling', 'DEX', 'Simple Ranged', 'Ammunition (range 30/120)', '1d4 bludgeoning'),
  (15, 'Battleaxe', 'STR', 'Martial Melee', 'Versatile (1d10)', '1d8 slashing'),
  (16, 'Flail', 'STR', 'Martial Melee', '', '1d8 bludgeoning'),
  (17, 'Glaive', 'STR', 'Martial Melee', 'Heavy, Reach, Two-handed', '1d10 slashing'),
  (18, 'Greataxe', 'STR', 'Martial Melee', 'Heavy, Two-handed', '1d12 slashing'),
  (19, 'Greatsword', 'STR', 'Martial Melee', 'Heavy, Two-handed', '2d6 slashing'),
  (20, 'Halberd', 'STR', 'Martial Melee', 'Heavy, Reach, Two-handed', '1d10 slashing');

UNLOCK TABLES;
/*!40000 ALTER TABLE `DnD_Database`.`weapons` ENABLE KEYS */;


-- Create armor table
DROP TABLE IF EXISTS `DnD_Database`.`armor`;
CREATE TABLE `DnD_Database`.`armor` (
  `item_id` bigint(20) unsigned NOT NULL,
  `armor_id` bigint(20) unsigned NOT NULL auto_increment,
  `armor_name` varchar(255) default NULL,
  `armor_type` varchar(255) default NULL,
  `armor_stealth` varchar(255) default NULL,
  `armor_class` varchar(255) default NULL,
  PRIMARY KEY (`armor_id`),
  FOREIGN KEY (`item_id`) REFERENCES `DnD_Database`.`items` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- dump data into armor tables
/*!40000 ALTER TABLE `DnD_Database`.`armor` DISABLE KEYS */;
LOCK TABLES `DnD_Database`.`armor` WRITE;

INSERT INTO `DnD_Database`.`armor` (`item_id`, `armor_name`, `armor_type`, `armor_stealth`, `armor_class`) VALUES 
  (21, 'Padded Armor', 'Light', 'Disadvantage', '11 + DEX'),
  (22, 'Leather Armor', 'Light', 'None', '11 + DEX'),
  (23, 'Studded Leather Armor', 'Light', 'None', '12 + DEX'),
  (24, 'Hide Armor', 'Medium', 'None', '12 + DEX (max 2)'),
  (25, 'Chain Shirt', 'Medium', 'None', '13 + DEX (max 2)'),
  (26, 'Scale Mail', 'Medium', 'Disadvantage', '14 + DEX (max 2)'),
  (27, 'Breastplate', 'Medium', 'None', '14 + DEX (max 2)'),
  (28, 'Half Plate Armor', 'Medium', 'Disadvantage', '15 + DEX (max 2)'),
  (29, 'Ring Mail', 'Heavy', 'Disadvantage', '14'),
  (30, 'Chain Mail', 'Heavy', 'Disadvantage', '16');

UNLOCK TABLES;
/*!40000 ALTER TABLE `DnD_Database`.`armor` ENABLE KEYS */;


-- Create spells table
DROP TABLE IF EXISTS `DnD_Database`.`spells`;
CREATE TABLE `DnD_Database`.`spells` (
  `item_id` bigint(20) unsigned NOT NULL,
  `spell_id` bigint(20) unsigned NOT NULL auto_increment,
  `spell_name` varchar(255) default NULL,
  `spell_class` varchar(255) default NULL,
  `spell_damage` varchar(255) default NULL,
  `spell_length` varchar(255) default NULL,
  `spell_level` int(11) default NULL,
  PRIMARY KEY (`spell_id`),
  FOREIGN KEY (`item_id`) REFERENCES `DnD_Database`.`items` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- dump data into spells table
/*!40000 ALTER TABLE `DnD_Database`.`spells` DISABLE KEYS */;
LOCK TABLES `DnD_Database`.`spells` WRITE;

INSERT INTO `DnD_Database`.`spells` (`item_id`, `spell_name`, `spell_class`, `spell_damage`, `spell_length`, `spell_level`) VALUES 
  (31, 'Fireball', 'Evocation', '8d6 fire', 'Instantaneous', 3),
  (32, 'Magic Missile', 'Evocation', '1d4+1 force', 'Instantaneous', 1),
  (33, 'Shield', 'Abjuration', 'None', '1 round', 1),
  (34, 'Mage Armor', 'Abjuration', 'None', '8 hours', 1),
  (35, 'Cure Wounds', 'Evocation', '1d8+spellcasting modifier', 'Instantaneous', 1),
  (36, 'Bless', 'Enchantment', 'None', 'Concentration, up to 1 minute', 1),
  (37, 'Detect Magic', 'Divination', 'None', 'Concentration, up to 10 minutes', 1),
  (38, 'Dispel Magic', 'Abjuration', 'None', 'Instantaneous', 3),
  (39, 'Lightning Bolt', 'Evocation', '8d6 lightning', 'Instantaneous', 3),
  (40, 'Fly', 'Transmutation', 'None', 'Concentration, up to 10 minutes', 3),
  (41, 'Invisibility', 'Illusion', 'None', 'Concentration, up to 1 hour', 2),
  (42, 'Polymorph', 'Transmutation', 'None', 'Concentration, up to 1 hour', 4),
  (43, 'Counterspell', 'Abjuration', 'None', 'Instantaneous', 3),
  (44, 'Healing Word', 'Evocation', '1d4+spellcasting modifier', 'Instantaneous', 1),
  (45, 'Silence', 'Illusion', 'None', 'Concentration, up to 10 minutes', 2);

UNLOCK TABLES;
/*!40000 ALTER TABLE `DnD_Database`.`spells` ENABLE KEYS */;

DROP TABLE IF EXISTS `DnD_Database`.`characters`;
CREATE TABLE `DnD_Database`.`characters` (
  `character_id` bigint(20) unsigned NOT NULL auto_increment,
  `character_name` varchar(255) NOT NULL,
  `class_id` bigint(20) unsigned NOT NULL,
  `race_id` bigint(20) unsigned NOT NULL,
  `weapon_id` bigint(20) unsigned,
  `armor_id` bigint(20) unsigned,
  `spell_id` bigint(20) unsigned,
  PRIMARY KEY (`character_id`),
  FOREIGN KEY (`class_id`) REFERENCES `class`(`class_id`),
  FOREIGN KEY (`race_id`) REFERENCES `race`(`race_id`),
  FOREIGN KEY (`weapon_id`) REFERENCES `weapons`(`weapon_id`),
  FOREIGN KEY (`armor_id`) REFERENCES `armor`(`armor_id`),
  FOREIGN KEY (`spell_id`) REFERENCES `spells`(`spell_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- Alter items table to add foreign keys
ALTER TABLE `DnD_Database`.`items`
  ADD CONSTRAINT `fk_weapon_id` FOREIGN KEY (`weapon_id`) REFERENCES `DnD_Database`.`weapons` (`weapon_id`),
  ADD CONSTRAINT `fk_armor_id` FOREIGN KEY (`armor_id`) REFERENCES `DnD_Database`.`armor` (`armor_id`),
  ADD CONSTRAINT `fk_spell_id` FOREIGN KEY (`spell_id`) REFERENCES `DnD_Database`.`spells` (`spell_id`);



