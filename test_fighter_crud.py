from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import unittest
import crud.fighter_crud
# from crud.fighter_crud import get_all_fighters, get_fighter, create_fighter, update_fighter, destroy_fighter
from models import db, app, Fighter_one, Fighter_two

# with app.app_context():
class TestCrud(unittest.TestCase):
    def test_get_one(self):
        self.assertEqual(crud.fighter_crud.get_fighter(1).universe,'Banjo-Kazooie')
        #     id: 'Banjo & Kazooie',
        #     universe: 'Banjo-Kazooie',
        #     availability: 'Downloadable',
        #     final_smash: 'The Mighty Jinjonator',
        #     quote: 'The missing piece of the puzzle is found as Banjo & Kazooie join Super Smash Bros. Ultimate as a playable fighter! With Banjo’s bare hands to bruise rivals up close and Kazooie’s egg-cellent shooting skills, your rivals will be singing the blues in no time. For their Final Smash, these perfect partners call upon a flock of Jinjos and the Mighty Jinjonator to deal the final blow to any “feeble jerk” that may stand in their way!',
        #     wiki_url: 'https://www.ssbwiki.com/Banjo & Kazooie_(SSBU)'
        # })
        # self.assertEqual(get_fighter(2), {
        #     id: 'Bayonetta',
        #     universe: 'Bayonetta',
        #     availability: 'Unlockable',
        #     final_smash: 'Infernal Climax',
        #     quote: 'An Umbra Witch who equips guns on her arms and legs, Bayonetta has mastered the beautiful but brutal Bullet Arts fighting style. She can even slow down her opponents with Witch Time!',
        #     wiki_url: 'https://www.ssbwiki.com/Bayonetta_(SSBU)'
        # })

if __name__ == '__main__':
    unittest.main()