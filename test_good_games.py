# test_goodgames.py

import unittest
from datetime import datetime
import csv
import os
from backend import Game, GameLibrary


class TestGoodGames(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        # Create test CSV if it doesn't exist
        if not os.path.exists('games.csv'):
            with open('games.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(
                    ['id', 'title', 'platform', 'status', 'rating', 'review', 'date_added', 'completion_date'])

        self.library = GameLibrary()
        self.test_game_data = {
            'title': 'Test Game',
            'platform': 'PC',
            'status': 'Playing'
        }

    def test_1_add_game(self):
        """Test adding a game to the library and CSV"""
        initial_rows = sum(1 for line in open('games.csv'))
        game = self.library.add_game(**self.test_game_data)

        # Check memory
        self.assertEqual(game['title'], self.test_game_data['title'])
        self.assertEqual(len(self.library.get_games()), initial_rows + 1)

        # Check CSV
        current_rows = sum(1 for line in open('games.csv'))
        self.assertEqual(current_rows, initial_rows + 1)

    def test_2_prevent_duplicate_games(self):
        """Test that identical games are not added twice"""
        initial_rows = sum(1 for line in open('games.csv'))

        # ignore that a ValueError is raised
        with self.assertRaises(ValueError) as context:
            self.library.add_game(**self.test_game_data)
        current_rows = sum(1 for line in open('games.csv'))
        self.assertEqual(current_rows, initial_rows)

    def test_3_load_existing_games(self):
        """Test loading existing games from CSV on startup"""
        # Add a game and verify it's in CSV
        self.library.add_game(**self.test_game_data)

        # Create new library instance (should load from CSV)
        new_library = GameLibrary()
        loaded_games = new_library.get_games()

        self.assertGreater(len(loaded_games), 0)
        found_game = False
        for game in loaded_games:
            if game['title'] == self.test_game_data['title']:
                found_game = True
                break

        # compare len of loaded games to the csv
        self.assertEqual(len(loaded_games), sum(1 for line in open('games.csv')))
        self.assertTrue(found_game)
