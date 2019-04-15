# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd


def get_page(slug):
    page = requests.get('https://{}.fantasyclubcricket.co.uk/includes/playerlist.php'.format(slug))
    return json.loads(page.content)


if __name__ == "__main__":
    df_fantasy_clubs = pd.read_csv('fantasyclubs.csv')
    df = pd.DataFrame()
    for index, club in df_fantasy_clubs.iterrows():
        data = get_page(club['fantasyclubcricketslug'])
        df_club = pd.DataFrame(data)
        df_club.drop(columns=[
            'id', 'position_id',
            'total_points', 'week_points',
            'selected', 'transfer_selected',
            'club_name', 'percentage_selected_by',
            'selling_price', 'name'
        ], inplace=True)
        df_club['club_id'] = club['pc_id']
        df = pd.concat([df, df_club])

    df.to_csv('saved_players.csv', index=False)
