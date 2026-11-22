import pandas as pd

def 정제(df):
    정제_df = df.copy()

    # 점수가 비어 있는 행을 삭제한다.
    정제_df = 정제_df.dropna(subset=["점수"])
    print(len(정제_df))

    # 모든 열의 값이 같은 중복 행을 삭제한다.
    정제_df = 정제_df.drop_duplicates()
    print(len(정제_df))

    # 반과 과목의 앞뒤 공백을 제거한다.
    정제_df["반"] = 정제_df["반"].str.strip()
    정제_df["과목"] = 정제_df["과목"].str.strip()
    print(len(정제_df))

    # 점수가 0 이상 100 이하인 행만 남긴다.
    정제_df = 정제_df[정제_df["점수"].between(0, 100)]
    print(len(정제_df))

    return 정제_df

def 반별평균(df):
    통계표 = df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]).round(2)
    통계표.columns = ["개수", "평균", "중앙값", "최댓값"]
    print(통계표)
    return 통계표["평균"]

if __name__ == "__main__":
    df = pd.read_csv("scores_2026.csv")
    정제된_df = 정제(df)
    print("\n정제")
    print(sorted(정제된_df["반"].unique()))
    print(sorted(정제된_df["과목"].unique()))

    print("\n필터링")
    수학_df = 정제된_df[정제된_df["과목"] == "수학"]
    print(len(수학_df))

    응용_df = 정제된_df[(정제된_df["반"] == "1반") & (정제된_df["점수"] >= 90)]
    print(len(응용_df))

    print("\n그룹화")
    반별_평균 = 정제된_df.groupby("반")["점수"].mean()
    print(반별_평균)

    과목_반별_평균 = 정제된_df.groupby(["과목", "반"])["점수"].mean()
    print(과목_반별_평균)

    print("\n통계")
    반별_평균값 = 반별평균(정제된_df)
    print(반별_평균값)

    print("\n검증")
    print(정제된_df.groupby("반")["점수"].sum().sum())
    print(정제된_df["점수"].sum())

    print(정제된_df.groupby("반")["점수"].count().sum())  # 100
    print(len(정제된_df))