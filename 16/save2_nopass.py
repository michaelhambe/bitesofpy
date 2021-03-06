from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    hundreds = [PYBITES_BORN + timedelta(days=x*100) for x+1 in range(20)]
    years = [PYBITES_BORN + timedelta(days=x*365) for x+1 in range(3)]
    for i, j in zip(hundreds, years):
        yield i
        yield j