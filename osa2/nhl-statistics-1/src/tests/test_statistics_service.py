import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_search_existing_player(self):
            player = self.stats.search("Semenko")
            self.assertEqual(player.name, "Semenko")

    def test_search_partial_name(self):
        player = self.stats.search("Seme")
        self.assertEqual(player.name, "Semenko")

    def test_search_non_existing_player(self):
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team_existing(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_team_non_existing(self):
        players = self.stats.team("XXX")
        self.assertEqual(players, [])

    def test_top_one(self):
        players = self.stats.top(1)
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name, "Gretzky")

    def test_top_all(self):
        players = self.stats.top(4)
        self.assertEqual(len(players), 5)

    def test_top_zero(self):
        players = self.stats.top(0)
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0].name, "Gretzky")
