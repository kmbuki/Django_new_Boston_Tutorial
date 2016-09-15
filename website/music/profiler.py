import cProfile
import pstats

from io import StringIO


def profile(func):
    def wrapper(*args, **kwargs):
        file_name = "/tmp/" + func.__name__ + ".profile"
        profiler = cProfile.Profile()
        profiler.enable()
        ret = func(*args, **kwargs)
        profiler.disable()
        s = StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
        ps.print_stats(20)
        stats = s.getvalue()
        with open(file_name, 'w') as f:
            f.write(stats)
        print(stats)
        s.close()
        return ret

    return wrapper
