from pathlib import Path

import pandas as pd

from analysis import 반별평균, 정제

폴더 = Path(__file__).parent
점수_df = pd.read_csv(폴더 / "scores_2026.csv")
미니_df = pd.read_csv(폴더 / "mini.csv")
정제된_점수_df = 정제(점수_df)
정제된_미니_df = 정제(미니_df)


def test_정제된_행수():
    assert len(정제된_점수_df) == 100


def test_반_종류():
    assert set(정제된_점수_df["반"]) == {"1반", "2반"}


def test_반별_점수_합계():
    반별_합계 = 정제된_점수_df.groupby("반")["점수"].sum().sum()
    assert 반별_합계 == 정제된_점수_df["점수"].sum()


def test_미니_1반_평균():
    assert 반별평균(정제된_미니_df)["1반"] == 80.0