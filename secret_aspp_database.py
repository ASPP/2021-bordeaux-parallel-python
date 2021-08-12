import numpy as np
import time


secret_aspp_database = {
    42: "very funny",
    "42": "Answer to the Ultimate Question of Life, the Universe, and Everything",
    "pelita": ":)",
    3.1415: 2.7182,
    2.7182: 2.71828182845904523536028747135266249775724709369995,
}


def query_secret_aspp_database(x):
    if isinstance(x, str):
        n = len(x)
    elif isinstance(x, float):
        n = len(str(x))
    else:
        n = np.random.randint(20)
    time.sleep(n / 10)
    if x in secret_aspp_database:
        return secret_aspp_database[x]
    else:
        return np.random.randn()
