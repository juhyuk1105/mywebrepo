from tools import get_boxoffice

def get_movie_audience(date, title):

    movies = get_boxoffice(date)

    for movie in movies:
        if movie.get("movieNm") == title:
            audi_cnt = int(movie.get("audiCnt", 0))
            return f"{audi_cnt:,}명"

    return f"'{title}' 은(는) {date} 순위에 없습니다."

if __name__ == "__main__":
    print(get_movie_audience("20260824", "오디세이"))
    print(get_movie_audience("20260824", "호프"))
    print(get_movie_audience("20260824", "없는영화"))